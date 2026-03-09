# DSL de Condicionais — Referência Completa

> Consolidado de `tools/GUIA_DESIGN_UX.md` §2.1, §5, §7.
> Tabela de operadores, anti-patterns, regras de visibilidade e exemplos do corpus real.

---

## Operadores válidos por tipo de campo

| Tipo de campo | Verificar 1 valor | Verificar N valores | Negação | Comparação |
|---------------|-------------------|---------------------|---------|------------|
| `boolean` | `campo is True` | — | `campo is False` | — |
| `choice` (multiChoice) | `'v1' in campo` | `selected_any(campo, 'v1', 'v2', ...)` | `not ('v1' in campo)` | — |
| `choice` com `exclusive: true` | `'v1' in campo` | `selected_any(campo, 'v1', 'v2', ...)` | `not ('v1' in campo)` | — |
| `single` (radio puro) | `campo == 'v1'` | — | `campo != 'v1'` | — |
| `number` | `campo >= N` | — | `campo != N` | `>=`, `<=`, `>`, `<`, `==` |

**Nota critica sobre `choice` com `exclusive: true`:**
Campos `select=choice` com todas as opções `exclusive: True` são radios que PARECEM ser `single`, mas seu tipo declarado é `choice`. O DSL avalia expressões pelo tipo declarado (`choice`), então use **sempre** `'v1' in campo` ou `selected_any()`, NUNCA `campo == 'v1'`.

---

## Composição de expressões

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

---

## Anti-patterns — NUNCA usar

| # | Anti-pattern | Problema | Correto |
|---|-------------|----------|---------|
| 1 | `campo in ('v1', 'v2')` | **MAIS COMUM** — inverte operandos: tenta encontrar o campo dentro de uma tupla. Sempre silenciosamente falso. | `selected_any(campo, 'v1', 'v2')` |
| 2 | `campo in ('v1')` | Mesmo erro com valor único | `'v1' in campo` |
| 3 | `selected_any('v1', campo)` | Argumentos invertidos — primeiro arg deve ser o CAMPO | `selected_any(campo, 'v1')` |
| 4 | `campo != 'valor'` para `choice` | Para `choice`, o operador `!=` não funciona como esperado | `not ('valor' in campo)` |
| 5 | `campo == 'valor'` para `choice` | `==` é para `single`, não `choice` | `'valor' in campo` |
| 6 | `is true` / `is false` (minúsculo) | Python exige maiúscula | `is True` / `is False` |
| 7 | `seçected_any(...)` ou `selected_any (...)` | Typo ou espaço indevido | `selected_any(...)` |
| 8 | `not 'v1' in campo` (sem parênteses) | Precedência ambígua | `not ('v1' in campo)` |

---

## Regras de visibilidade

| `condicional` | Quando usar |
|--------------|-------------|
| `"visivel"` | **Valor padrão.** Pergunta exibida normalmente — sempre (sem `expressao`) ou condicionalmente (quando `expressao` for verdadeira) |
| `"oculto"` | Campo auto-preenchido pela plataforma (ex.: `sex`, `age`) — raramente necessário |
| `"condicional"` | **NUNCA usar** — valor invalido/depreciado no DSL Daktus |

Se `condicional: "visivel"` sem condição → deixar `expressao: ""` (string vazia).

---

## Regras de conduta

Todo item de conduta (exame, alerta, encaminhamento, medicamento) **deve ter `condicao` não-vazia**.

```json
{ "condicao": "'litio' in medicamentos_em_uso" }   // condicional específica
{ "condicao": "" }                                  // ANTI-PATTERN: genérica
```

Alertas devem usar formato imperativo:
- `"Acionar SAMU 192 / encaminhar UPA imediatamente."`
- `"Suspender clozapina imediatamente."`
- NUNCA texto acadêmico: `"O lítio pode causar toxicidade renal quando..."`

---

## Exemplos corretos (corpus real psiquiatria)

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

## Anti-patterns de design consolidados

| # | Anti-pattern | Severidade | Solução |
|---|---|---|---|
| 1 | `choice` com exatamente 2 opções sim/nao | **Bloqueante** | Converter para `boolean` |
| 2 | Label "Q1:", "Q2:", "Item N" | **Bloqueante** | Label clínico descritivo |
| 3 | uid sem referência em nenhuma `expressao` nem `condicao` | **Revisão** | Remover ou mapear uso |
| 4 | `string` onde `choice`/`single` resolve | **Recomendado** | Migrar para opções estruturadas |
| 5 | Conduta sem `condicao` (genérica) | **Bloqueante** | Adicionar condicional específica |
| 6 | Alerta com texto acadêmico | **Recomendado** | Reescrever em imperativo |
| 7 | `multiChoice` sem opção "nenhum" preselected | **Recomendado** | Adicionar opção neutra |
| 8 | Campos mutuamente dependentes sem cascata | **Recomendado** | Criar cascata boolean → campo condicional |
