---
name: daktus-json-coding
description: |
  Compila playbooks clínicos auditados em JSON Daktus executável.
  Usar quando o playbook estiver liberado e o objetivo for gerar
  o grafo de nós, arestas, condutas e condicionais em JSON.
  Gatilhos: "codificar JSON", "gerar ficha", "paper design",
  "mapear TUSS", "nó de conduta", "validar JSON estrutural".
version: 0.1.0
triggers:
  - codificar JSON a partir de playbook
  - gerar ficha Daktus
  - paper design de nós
  - mapear exames para TUSS
  - construir nó de conduta
  - validar JSON estrutural
inputs:
  - playbook clínico auditado (vFINAL)
  - banco de evidências da especialidade
  - tabelas TUSS e MEVO
outputs:
  - JSON Daktus válido (jsons/ficha_{esp}_v{versao}.json)
---

# SKILL — CODIFICAÇÃO JSON DAKTUS

## O QUE ESTA SKILL FAZ

Traduz um playbook clínico aprovado em JSON Daktus válido — um grafo de nós e arestas com exames mapeados em TUSS, condicionais DSL corretos e validação estrutural automatizada.

### Fronteira

- **Começa quando**: playbook auditado e liberado (gate da fase anterior passado)
- **Termina quando**: JSON validado estruturalmente, pronto para QA final
- **Não faz**: auditoria clínica do playbook, QA final de entrega, gestão de evidências

### Arquivos de entrada

```
playbooks/playbook_{esp}_vFINAL.md     ← playbook aprovado
research/BANCO_EVIDENCIAS_{ESP}.md     ← para confirmar condicionais de exames
referencia/TUSS.xlsx                   ← códigos de exames ANS
referencia/Mevo.xlsx                   ← códigos de medicamentos MEVO
```

### Arquivo de saída

```
jsons/ficha_{esp}_v{versao}.json
```

---

## SEQUÊNCIA INTERNA — NESTA ORDEM

```
1. Paper design        ← topologia de nós em texto antes de qualquer JSON
2. Mapeamento TUSS     ← todos os exames mapeados antes de qualquer nó de conduta
3. Geração de IDs      ← UUIDs e edge IDs gerados de forma consistente
4. JSON nó por nó      ← construção incremental
5. JSON integrado      ← montagem do grafo completo
6. Validação           ← script automatizado de verificação estrutural
```

**Nunca pular o paper design.** Definir a topologia antes de escrever JSON evita refatorações custosas.

---

## 1. PAPER DESIGN — MAPA DE NÓS

Antes de escrever uma linha de JSON, definir em texto:

```markdown
## Topologia proposta — {Especialidade}

| Posição | ID (placeholder) | Label | Tipo | Clusters atendidos |
|---------|-----------------|-------|------|-------------------|
| x=900   | nó-1 | [Label] | form | [Clusters] |
| x=1800  | nó-2 | [Gate de segurança] | form | [Cluster gate] |
| x=2700  | nó-3 | [Label] | form | [Clusters] |
| ...     | ... | ... | ... | ... |
| x=N*900 | conduta-1 | Conduta | conduta | Todos |

## Variáveis críticas
| Variável (uid) | Tipo | Nó de origem | Usada como condicional em |
|---------------|------|-------------|--------------------------|
```

---

## 2. MAPEAMENTO TUSS

Criar tabela antes de codificar qualquer nó de conduta:

```python
exam_map = {
  "nome_exame": {
    "tuss": "XXXXXXXX",
    "nome_tuss": "Nome oficial tabela ANS",
    "cid_principal": "ZXX.X",
    "categoria": "Exames"
  }
}
```

**Fontes de lookup:** `referencia/TUSS.xlsx` para exames e `referencia/Mevo.xlsx` para medicamentos MEVO.

**Sem código TUSS identificado:** manter `"codigo": []`, sinalizar para o usuário e **não bloquear a produção**.

---

## 3. GERAÇÃO DE IDs

```python
import uuid

def new_uuid():      return str(uuid.uuid4())
def new_node_id():   return f"node-{new_uuid()}"
def new_conduta_id(): return f"conduta-{new_uuid()}"
def new_edge_id(src, tgt): return f"e-{src}-{tgt}"

# Posicionamento horizontal — todos com y=100
x_positions = [900, 1800, 2700, 3600, 4500, 5400, 6300, ...]
```

---

## 4. ESTRUTURA JSON — PADRÕES OBRIGATÓRIOS

### Metadata

```json
{
  "id": "amil-Ficha Clínica | {Especialidade}",
  "company": "amil",
  "name": "Ficha Clínica | {Especialidade}",
  "version": "{uuid-v4}",
  "createdAt": "{ISO8601}",
  "description": "Descrição sucinta da versão"
}
```

### Nó de formulário (form)

```json
{
  "id": "node-UUID",
  "type": "custom",
  "position": { "x": 900, "y": 100 },
  "data": {
    "label": "Nome do nó",
    "descricao": "<p>Contexto opcional</p>",
    "condicionais": [
      { "linkId": "node-TARGET-UUID", "condicao": "q_variavel == 'valor_de_rota'" }
    ],
    "questions": [
      {
        "uid": "q_nome_variavel",
        "titulo": "<p><strong>Texto da pergunta para o médico</strong></p>",
        "descricao": null,
        "condicional": "visivel",
        "expressao": "uid_variavel_anterior == 'valor'",
        "select": "choice",
        "options": [
          { "id": "opcao_1", "label": "Rótulo da opção 1", "preselected": false, "exclusive": false },
          { "id": "opcao_2", "label": "Estado mais comum", "preselected": true, "exclusive": true }
        ]
      }
    ]
  }
}
```

### Nó de conduta

```json
{
  "id": "conduta-UUID",
  "type": "condutaNode",
  "position": { "x": 5400, "y": 100 },
  "data": {
    "condutaDataNode": {
      "exame": [
        {
          "iid": "iid-UUID",
          "nome": "Nome do exame",
          "codigo": ["XXXXXXXX"],
          "condicao": "'diagnostico_x' in diagnostico_ativo",
          "periodicidade": "anual",
          "cid": ["ZXX.X"]
        }
      ],
      "orientacao": [],
      "encaminhamento": [],
      "medicamento": [],
      "mensagem": []
    }
  }
}
```

### Aresta (edge)

```json
{ "id": "e-{source}-{target}", "source": "node-UUID", "target": "node-UUID2", "data": {} }
```

---

## 5. TIPOS DE CAMPO — TABELA DE DECISÃO

| Tipo | Quando usar | Avaliado em expressão como |
|------|-------------|---------------------------|
| `boolean` | Sim/Não puro. Nenhuma opção intermediária. | `uid is True` / `uid is False` |
| `choice` | Múltipla seleção (checkboxes). Mais de 2 opções não-exclusivas. | `'op' in uid` / `selected_any(uid, ...)` |
| `single` | Escolha única (radio). Opções mutuamente exclusivas, não-binárias. | `uid == 'op'` |
| `number` | Valor numérico (age, IMC, score). | `uid >= 40` |
| `string` | Texto livre. Usar com parcimônia. | Raramente referenciado |
| `date` | Data. | Raramente referenciado |

### Regra de decisão Sim/Não

```
A pergunta é puramente binária?
  ├── SIM → use `boolean` (sem options, com defaultValue: "false")
  └── NÃO → as opções têm labels clínicos distintos?
            └── SIM → use `choice` com exclusive: true em todas + 1 preselected
```

### Preselection e exclusividade

**multiChoice** (seleção múltipla):
- Primeiro item = estado neutro → `preselected: true, exclusive: true`
- Demais itens → `preselected: false, exclusive: false`

**choice/single** (seleção única):
- Todos os itens → `exclusive: true`
- Um item (mais comum/seguro) → `preselected: true`

---

## 6. DSL DE CONDICIONAIS — RESUMO EXECUTIVO

### Operadores por tipo de campo

| Tipo | 1 valor | N valores | Negação |
|------|---------|-----------|---------|
| `boolean` | `campo is True` | — | `campo is False` |
| `choice` | `'v1' in campo` | `selected_any(campo, 'v1', 'v2')` | `not ('v1' in campo)` |
| `single` | `campo == 'v1'` | — | `campo != 'v1'` |
| `number` | `campo >= N` | — | `campo != N` |

### 5 regras invioláveis

1. **`choice` com `exclusive: true` continua sendo `choice`** — usar `'v1' in campo`, NUNCA `campo == 'v1'`
2. **`condicional` aceita apenas `"visivel"` ou `"oculto"`** — `"condicional"` como valor e INVALIDO
3. **Negação SEMPRE com parênteses** — `not ('v1' in campo)`, nunca `not 'v1' in campo`
4. **`selected_any()` — primeiro arg é o CAMPO** — `selected_any(campo, 'v1', 'v2')`, nunca invertido
5. **Toda conduta deve ter `condicao` não-vazia** — conduta sem condicao = genérica = anti-pattern

> Para tabela completa de anti-patterns e exemplos do corpus real, ver `references/DSL_CONDICIONAL.md`.

---

## 7. REGRAS CRITICAS DE DESIGN

| Regra | Detalhe |
|-------|---------|
| Gate de segurança = Nó 2 | Incontornável. `exclusive: false` nas opções de risco alto. Alerta de risco alto = PRIMEIRO item na conduta |
| Primeiro nó em x=900 | Espaçamento de 900 por nó subsequente. Todos y=100 |
| `iid` únicos | Sem repetição em todo o catálogo de condutas |
| Breakpoint de resumo | Presente na sequência quando aplicável |
| Labels clínicos | NUNCA "Q1:", "Item N" — sempre descritivo |
| Alertas em imperativo | "Suspender imediatamente", não texto acadêmico |
| Princípio central | Toda pergunta deve liberar/bloquear conduta OU controlar visibilidade de outra pergunta |

---

## 8. VALIDAÇÃO ESTRUTURAL

Usar o script `scripts/validate_json.py` desta skill:

```bash
python skills/daktus-json-coding/scripts/validate_json.py <caminho_do_json>
```

Checks realizados:
- Edges com source/target existentes
- Edge IDs no formato `e-{source}-{target}`
- linkIds em condicionais apontam para nós existentes
- iids únicos em todo o catálogo de condutas
- Posicionamento sequencial (x múltiplo de 900)

---

## 9. ENTREGA DA FASE

```
RELATÓRIO DE ESTADO — CODIFICAÇÃO JSON
- Nodes criados: N
- Edges criadas: N
- Exames mapeados com TUSS: N/N_total
- Exames sem TUSS (pendentes): [lista]
- Validação estrutural: PASSOU / FALHOU [detalhes]
- Arquivo: jsons/ficha_{esp}_v{versao}.json
- AGUARDANDO AUTORIZAÇÃO PARA QA FINAL
```

---

## REFERÊNCIAS INTERNAS

| Tópico | Arquivo |
|--------|---------|
| DSL completo + anti-patterns | `references/DSL_CONDICIONAL.md` |
| Padrões arquiteturais reutilizáveis | `references/PADROES_REUTILIZAVEIS.md` |
| Erros documentados + checklist QA | `references/ERROS_DOCUMENTADOS.md` |
| Templates JSON | `assets/template_form_node.json`, `assets/template_conduta_node.json`, `assets/template_edge.json` |
| Script de validação | `scripts/validate_json.py` |

### Fontes canônicas externas (consultar quando necessário)

| Tópico | Arquivo |
|--------|---------|
| Protocolo de evidências | `tools/GUARDRAIL_EVIDENCIAS.md` |
| Schema JSON detalhado | `tools/AGENT_PROMPT_PROTOCOLO_DAKTUS.md` §2 |
| UX transversal ao pipeline | `tools/GUIA_DESIGN_UX.md` |
