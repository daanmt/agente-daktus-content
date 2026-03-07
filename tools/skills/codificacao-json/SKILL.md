# SKILL — CODIFICAÇÃO JSON DAKTUS
## `codificacao-json` | Fase 4

> **Pré-condição de boot:** esta skill é invocada após boot completo via `AGENTE.md`.
> `HANDOFF.md` deve ter sido lido e a fase atual confirmada antes de executar qualquer ação aqui.


---

## O QUE ESTA SKILL FAZ

Traduz o playbook aprovado clinicamente em JSON Daktus válido — um grafo de nós e arestas com exames mapeados em TUSS, condicionais corretos e validação estrutural automatizada.

---

## ARQUIVOS DE ENTRADA

```
playbooks/playbook_{esp}_vFINAL.md     ← playbook aprovado clinicamente
research/BANCO_EVIDENCIAS_{ESP}.md     ← para confirmar condicionais de exames
jsons/referencia/                      ← JSONs de outras especialidades como referência UX
```

## ARQUIVO DE SAÍDA

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

**Fontes de lookup TUSS (em ordem de confiabilidade):**
1. Tabela TUSS compartilhada do projeto (xlsx em `/jsons/referencia/` ou equivalente)
2. Planilha Depara Mevo/Daktus
3. Tabela TUSS oficial ANS

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

## 4. PADRÕES DE ESTRUTURA JSON

### Nó de formulário (form)

```json
{
  "id": "node-UUID",
  "type": "customNode",
  "position": { "x": 900, "y": 100 },
  "data": {
    "label": "Nome do nó",
    "questions": [
      {
        "uid": "q_nome_variavel",
        "label": "Texto da pergunta para o médico",
        "type": "multiChoice",
        "options": [
          { "value": "opcao_1", "label": "Rótulo da opção 1", "preselected": false },
          { "value": "opcao_2", "label": "Estado mais comum", "preselected": true }
        ],
        "condicional": "condicional",
        "expressao": "uid_variavel_anterior == 'valor'"
      }
    ],
    "condicionais": [
      { "linkId": "node-TARGET-UUID", "expressao": "q_variavel == 'valor_de_rota'" }
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
    "conduta": {
      "exames": [
        {
          "iid": "iid-UUID",
          "nome": "Nome do exame",
          "codigo": ["XXXXXXXX"],
          "condicional": "condicional",
          "expressao": "q_diagnostico == 'condicao_x'",
          "periodicidade": "anual",
          "cid": ["ZXX.X"]
        }
      ],
      "orientacao": [],
      "encaminhamentos": []
    }
  }
}
```

### Aresta (edge)

```json
{ "id": "e-{source}-{target}", "source": "node-UUID", "target": "node-UUID2" }
```

---

## 5. REGRAS CRÍTICAS DE DESIGN

| Regra | Detalhe |
|-------|---------|
| Gate de segurança = Nó 2 | Incontornável. `exclusive: false` nas opções de risco alto. Alerta de risco alto = PRIMEIRO item na conduta |
| Primeiro nó em x=900 | Espaçamento de 900 por nó subsequente |
| `iid` únicos | Sem repetição em todo o catálogo de condutas |
| Breakpoint de resumo | Presente na sequência de nós quando aplicável |
| Termo de ciência | No nó correspondente conforme exigência da especialidade |

---

## 6. VALIDAÇÃO ESTRUTURAL AUTOMATIZADA

```python
import json
from collections import Counter

def validate(filepath):
    d = json.load(open(filepath))
    nodes = {n['id'] for n in d['nodes']}
    errors = []

    for e in d['edges']:
        if e['source'] not in nodes:
            errors.append(f"Edge source inexistente: {e['source']}")
        if e['target'] not in nodes:
            errors.append(f"Edge target inexistente: {e['target']}")
        if e['id'] != f"e-{e['source']}-{e['target']}":
            errors.append(f"Edge ID inválido: {e['id']}")

    for node in d['nodes']:
        for cond in node['data'].get('condicionais', []):
            if cond['linkId'] not in nodes:
                errors.append(f"linkId inexistente: {cond['linkId']} em {node['id']}")

    iids = []
    for node in d['nodes']:
        if node['id'].startswith('conduta-'):
            for section in ['exames', 'orientacao', 'encaminhamentos']:
                for item in node['data'].get('conduta', {}).get(section, []):
                    iid = item.get('iid') or item.get('id', '')
                    if iid: iids.append(iid)
    dups = {i: c for i, c in Counter(iids).items() if c > 1}
    if dups: errors.append(f"IIDs duplicados: {dups}")

    if errors:
        for e in errors: print(f"  ✗ {e}")
    else:
        print(f"✓ JSON válido — {len(d['nodes'])} nodes, {len(d['edges'])} edges")
```

---

## ENTREGA DA FASE 4

```
RELATÓRIO DE ESTADO — FASE 4
- Nodes criados: N
- Edges criadas: N
- Exames mapeados com TUSS: N/N_total
- Exames sem TUSS (pendentes): [lista]
- Validação estrutural: PASSOU / FALHOU [detalhes]
- Arquivo: jsons/ficha_{esp}_v{versao}.json
- AGUARDANDO AUTORIZAÇÃO PARA FASE 5 (QA final)
```
