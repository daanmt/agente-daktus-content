# GUIA DE DESIGN UX — Fichas Clínicas Daktus

> **Versão:** 1.0 | **Data:** 2026-03-08
> Referência rápida de design para Fase 4 (Codificação JSON).
> Leia junto com `AGENT_PROMPT_PROTOCOLO_DAKTUS.md` e `PADROES_ARQUITETURA_JSON.md`.
> Benchmark de UX: `especialidades/ginecologia/jsons/amil-ficha-ginecologia-v1.0.0.json`

---

## §1 — Princípio Central

> **Toda pergunta deve fazer algo.**

Cada pergunta deve cumprir ao menos uma função:

- **(a) Liberar ou bloquear** um item na conduta (exame, alerta, encaminhamento, medicamento), OU
- **(b) Controlar a visibilidade** de outra pergunta downstream

Pergunta que não cumpre nenhuma das duas funções é candidata a remoção.
Antes de remover, verificar se o `uid` aparece em alguma `expressao` ou `condicao` do JSON inteiro.

---

## §2 — Tipos de `select` (tabela completa e corrigida)

| Tipo | Quando usar | Avaliado em expressão como |
|------|-------------|---------------------------|
| `boolean` | Sim/Não puro. Nenhuma opção intermediária. | `uid is True` / `uid is False` |
| `choice` | Múltipla seleção (checkboxes). Mais de 2 opções não-exclusivas. | `'op' in uid` / `selected_any(uid, ...)` |
| `single` | Escolha única (radio). Opções mutuamente exclusivas, não-binárias. | `uid == 'op'` |
| `number` | Valor numérico (age, IMC, litemia, score). | `uid >= 40` / `uid < 15` |
| `string` | Texto livre. Usar com parcimônia. | Raramente referenciado em condicionais |
| `date` | Data (ex: data de cirurgia, última menstruação). | Raramente referenciado em condicionais |

### Regra de decisão para perguntas Sim/Não

```
A pergunta é puramente binária?
  ├── SIM → vai ser avaliada com `is True` / `is False`?
  │     └── SIM → use `boolean` (sem options, sem iids, com `defaultValue: "false"`)
  └── NÃO → as opções têm labels clínicos distintos?
            └── SIM → use `choice` com `exclusive: true` em todas + 1 preselected
```

**Exemplos:**
- "Paciente gestante?" → `boolean` ✅
- "Litemia dentro da faixa?" → `choice` (sim / baixo / alto_risco / nao_coletada) ✅
- "Sim / Não" como opções de `choice` → ❌ anti-pattern, use `boolean`

### Template boolean (padrão ginecologia)

```json
{
  "uid": "gestante",
  "titulo": "<p><strong>Paciente gestante?</strong></p>",
  "condicional": "visivel",
  "expressao": "sexo_feminino_ie is True",
  "select": "boolean",
  "options": [],
  "defaultValue": "false"
}
```

---

## §2.1 — DSL de condicionais: operadores, regras e anti-patterns

### Tabela de operadores válidos por tipo de campo

| Tipo de campo | Verificar 1 valor | Verificar N valores | Negação | Comparação |
|---------------|-------------------|---------------------|---------|------------|
| `boolean` | `campo is True` | — | `campo is False` | — |
| `choice` (multiChoice) | `'v1' in campo` | `selected_any(campo, 'v1', 'v2', ...)` | `not ('v1' in campo)` | — |
| `choice` com `exclusive: true` | `'v1' in campo` | `selected_any(campo, 'v1', 'v2', ...)` | `not ('v1' in campo)` | — |
| `single` (radio puro) | `campo == 'v1'` | — | `campo != 'v1'` | — |
| `number` | `campo >= N` | — | `campo != N` | `>=`, `<=`, `>`, `<`, `==` |

**Nota crítica sobre `choice` com `exclusive: true`:**
Campos `select=choice` com todas as opções `exclusive: True` são radios que PARECEM ser `single`, mas seu tipo declarado é `choice`. O DSL avalia expressões pelo tipo declarado (`choice`), então use **sempre** `'v1' in campo` ou `selected_any()`, NUNCA `campo == 'v1'`.

### Composição de expressões

```
# Conjunção
expr1 and expr2

# Disjunção
expr1 or expr2

# Negação — SEMPRE com parênteses
not ('v1' in campo)
not (campo is True)

# Múltiplas verificações — preferir selected_any()
selected_any(campo, 'v1', 'v2', 'v3')     # preferido
'v1' in campo or 'v2' in campo or ...     # verboso mas válido

# Precedência com parênteses
(expr1 and expr2) or expr3
campo >= 40 and campo <= 74
```

### Anti-patterns críticos — NUNCA usar

| ❌ Anti-pattern | Problema | ✅ Correto |
|----------------|----------|-----------|
| `campo in ('v1', 'v2')` | **MAIS COMUM** — inverte operandos: tenta encontrar o campo dentro de uma tupla. Sempre silenciosamente falso. | `selected_any(campo, 'v1', 'v2')` |
| `campo in ('v1')` | Mesmo erro com valor único | `'v1' in campo` |
| `selected_any('v1', campo)` | Argumentos invertidos — primeiro arg deve ser o CAMPO | `selected_any(campo, 'v1')` |
| `campo != 'valor'` para `choice` | Para `choice`, o operador `!=` não funciona como esperado | `not ('valor' in campo)` |
| `campo == 'valor'` para `choice` | `==` é para `single`, não `choice` | `'valor' in campo` |
| `is true` / `is false` (minúsculo) | Python exige maiúscula | `is True` / `is False` |
| `seçected_any(...)` ou `selected_any (...)` | Typo ou espaço indevido | `selected_any(...)` |
| `not 'v1' in campo` (sem parênteses) | Precedência ambígua | `not ('v1' in campo)` |

### Exemplos corretos (corpus real)

```
# Booleanos
gestante is True
ideacao_passiva is False
primeiro_episodio_psicotico is True

# Campos choice — verificação única
'litio' in medicamentos_em_uso
'tdm' in diagnostico_ativo
'tept' in diagnostico_ativo

# Campos choice — múltiplos valores (selected_any)
selected_any(medicamentos_em_uso, 'litio', 'valproato', 'carbamazepina')
selected_any(diagnostico_ativo, 'tdm', 'tag', 'panico')
selected_any(episodio_atual_humor, 'mania', 'hipomania')
selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada', 'depressao_grave')

# Campos choice — negação
not ('nenhum' in sintomas_miocardite)
not ('sem_diagnostico' in diagnostico_ativo)

# Composições
selected_any(diagnostico_ativo, 'tdm', 'tag') and selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada')
'litio' in medicamentos_em_uso and gestante is True
(risco_suicidio_alto is True) or (risco_suicidio_intermediario is True)

# Numéricos
phq9_score >= 15
madrs_score >= 20
age >= 40 and age <= 74
```

---

## §3 — Labels de perguntas (`titulo`)

### Regra

- **NUNCA** usar enumeração genérica: `"Q1:"`, `"Q2:"`, `"Item 1"`, `"Pergunta 3"`
- **SEMPRE** usar label clínico descritivo, mesmo que curto

### Exemplos corretos vs. errados

| ❌ Anti-pattern | ✅ Correto |
|----------------|-----------|
| `"Q1 — Ideação:"` | `"Ideação suicida passiva — pensamentos de morte ou desejo de morrer?"` |
| `"Q3 — Plano:"` | `"Plano suicida formulado?"` |
| `"Q6 — Acesso:"` | `"Acesso a meios letais na residência ou facilmente disponíveis?"` |
| `"Item 2"` | `"Ciclagem rápida (≥4 episódios/ano)?"` |

### Formato HTML

```html
<p><strong>Label clínico descritivo aqui?</strong></p>
```

Critérios clínicos ou contexto relevante podem ser adicionados após o label principal:

```html
<p><strong>Paciente imunocomprometida?</strong></p>
<p>HIV+, transplantada, imunossupressão crônica</p>
```

---

## §4 — Preselection e exclusividade

### multiChoice (`choice` com seleções múltiplas)

```json
{ "id": "nenhuma_queixa", "label": "Nenhuma / rotina", "preselected": true,  "exclusive": true  },
{ "id": "queixa_a",       "label": "Queixa A",          "preselected": false, "exclusive": false },
{ "id": "queixa_b",       "label": "Queixa B",          "preselected": false, "exclusive": false }
```

- **Primeiro item:** sempre o estado neutro/nenhum — `preselected: true, exclusive: true`
- **Demais itens:** `preselected: false, exclusive: false`
- Selecionar qualquer item clínico desmarca automaticamente o "nenhum" (por ser exclusive)

### choice / single (seleção única)

```json
{ "id": "sem_risco",      "label": "Sem risco",      "preselected": true,  "exclusive": true },
{ "id": "baixo",          "label": "Baixo",          "preselected": false, "exclusive": true },
{ "id": "intermediario",  "label": "Intermediário",  "preselected": false, "exclusive": true },
{ "id": "alto",           "label": "Alto",           "preselected": false, "exclusive": true }
```

- **Todos os itens:** `exclusive: true`
- **Um item:** `preselected: true` (o estado mais comum ou o mais seguro)

---

## §5 — Economia de perguntas e condicionais

### Princípio de tela

> **Poucas telas, muitas perguntas por tela quando necessário.**
> Um nó = uma tela de formulário. Não criar nós temáticos por diagnóstico.

### Visibilidade padrão

| `condicional` | Quando usar |
|--------------|-------------|
| `"visivel"` | **Valor padrão.** Pergunta exibida normalmente — sempre (sem `expressao`) ou condicionalmente (quando `expressao` for verdadeira) |
| `"oculto"` | Campo verdadeiramente oculto do formulário (preenchimento automático pela plataforma, ex.: `sex`, `age`) — **raramente necessário** |
| `"condicional"` | ❌ **NUNCA usar** — valor inválido/depreciado no DSL Daktus |

> **Regra:** Use `"visivel"` para qualquer pergunta que deva aparecer na tela (com ou sem condição). Use `"oculto"` apenas para campos auto-preenchidos pela plataforma que nunca devem ser exibidos ao usuário.

### Cascata válida (exemplo)

```
queixa_principal (visivel, sem expressao)
  → sua_padrao (visivel, expressao: "'sua' in queixa_principal")
      → sua_refrataria (visivel, expressao: "'sua' in queixa_principal and (age >= 35 or ...)")
```

### Expressão vazia

Se `condicional: "visivel"` sem condição → deixar `expressao: ""` (string vazia)

---

## §6 — Regras de conduta

### Condicionais de itens de conduta

Todo item de conduta (exame, alerta, encaminhamento, medicamento) **deve ter `condicao` não-vazia**.
Conduta sem `condicao` = conduta genérica = mostrada para todos = anti-pattern.

```json
{ "condicao": "'litio' in medicamentos_em_uso" }   // ✅ condicional específica
{ "condicao": "" }                                  // ❌ genérica, aparece sempre
```

### Alertas: formato imperativo

```
✅ "Acionar SAMU 192 / encaminhar UPA imediatamente."
✅ "Suspender clozapina imediatamente."
❌ "O lítio pode causar toxicidade renal quando..."  (texto acadêmico)
```

---

## §7 — Anti-patterns consolidados

| # | Anti-pattern | Severidade | Solução |
|---|---|---|---|
| 1 | `choice` com exatamente 2 opções sim/nao | **Bloqueante** | Converter para `boolean` |
| 2 | Label "Q1:", "Q2:", "Item N" | **Bloqueante** | Label clínico descritivo |
| 3 | Pergunta cujo `uid` não aparece em nenhuma `expressao` nem `condicao` | **Revisão** | Remover ou mapear uso |
| 4 | `string` onde `choice`/`single` resolve | **Recomendado** | Migrar para opções estruturadas |
| 5 | Conduta sem `condicao` (genérica) | **Bloqueante** | Adicionar condicional específica |
| 6 | Alerta com texto acadêmico | **Recomendado** | Reescrever em imperativo |
| 7 | `multiChoice` sem opção "nenhum" preselected | **Recomendado** | Adicionar opção neutra |
| 8 | Dois campos com informação mutuamente dependente (ex: "sim/não" + "detalhe") usados separadamente sem cascata | **Recomendado** | Criar cascata boolean → campo condicional |

---

## §8 — Referências de implementação

| Regra | Fonte canônica |
|-------|---------------|
| Filosofia de mínimo de perguntas | `AGENT_PROMPT_PROTOCOLO_DAKTUS.md` §1.1 + Apêndice A |
| Alias de classe farmacológica | `PADROES_ARQUITETURA_JSON.md` §1.1 |
| Contexto obrigatório no mesmo nó | `PADROES_ARQUITETURA_JSON.md` §1.4 |
| Boolean gate → campo condicional | `PADROES_ARQUITETURA_JSON.md` §1.5 |
| Gate de negação composta | `PADROES_ARQUITETURA_JSON.md` §1.3 |
| Benchmark UX completo | `especialidades/ginecologia/jsons/amil-ficha-ginecologia-v1.0.0.json` |
