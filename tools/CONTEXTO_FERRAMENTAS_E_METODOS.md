# CONTEXTO DE FERRAMENTAS E METODOS — Pipeline Daktus

> **Documento complementar ao AGENT_PROMPT_PROTOCOLO_DAKTUS.md**
> Documenta ferramentas, padroes de codigo e metodologia aplicaveis a qualquer especialidade.
> Agnóstico de especialidade — exemplos usam ginecologia/reumatologia como referencia generica.

---

## PARTE I — FERRAMENTAS E MÉTODOS UTILIZADOS NA CONSTRUÇÃO DOS PROTOCOLOS

Esta seção documenta, com exemplos reais, as ferramentas, padrões de código e decisões de design que foram usadas na produção das fichas existentes. O agente deve internalizar esses padrões como sua forma padrão de trabalhar.

---

### 1.1 Bash Tool — Inspeção e Auditoria de Arquivos

O `bash_tool` foi a ferramenta mais usada no ciclo de auditoria. Ele roda comandos em Ubuntu 24 e é ideal para:

**Extração de citações com grep/regex:**

```bash
# Contar todas as citações numéricas no corpo do playbook
grep -oP '\[\d+\]' playbook_ginecologia_auditado.md | sort -t'[' -k2 -n | uniq -c

# Listar números únicos de citações no corpo (exclui seção de referências)
grep -oP '(?<=\[)\d+(?=\])' <(sed '/^## Referências/,$d' playbook.md) | sort -n | uniq

# Listar números das referências listadas
grep -oP '^\d+(?=\.)' <(sed -n '/^## Referências/,$p' playbook.md) | sort -n
```

**Validação estrutural do JSON:**

```bash
# Validar JSON (parse básico)
python3 -c "import json; json.load(open('ficha.json')); print('JSON válido')"

# Contar nodes e edges
python3 -c "
import json
d = json.load(open('ficha.json'))
print(f'Nodes: {len(d[\"nodes\"])}')
print(f'Edges: {len(d[\"edges\"])}')
"

# Listar IDs de todos os nodes
python3 -c "
import json
d = json.load(open('ficha.json'))
for n in d['nodes']:
    print(n['id'], '|', n['data']['label'])
"
```

**Busca de padrões específicos no JSON:**

```bash
# Encontrar todos os UIDs de perguntas
python3 -c "
import json
d = json.load(open('ficha.json'))
for node in d['nodes']:
    for q in node['data'].get('questions', []):
        print(node['data']['label'], '->', q.get('uid',''))
"

# Verificar se todos os linkIds existem como nodes
python3 -c "
import json
d = json.load(open('ficha.json'))
node_ids = {n['id'] for n in d['nodes']}
for node in d['nodes']:
    for cond in node['data'].get('condicionais', []):
        lid = cond['linkId']
        if lid not in node_ids:
            print(f'QUEBRADO: {node[\"id\"]} -> linkId {lid}')
"
```

---

### 1.2 Python Script Tool — Scripts de Auditoria Sistemática

Scripts Python foram usados para análises mais complexas que exigem cruzamento de dados.

**Script canônico de auditoria de referências (usado em ginecologia):**

```python
import re

def audit_references(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Separar corpo da seção de referências
    parts = re.split(r'^#{1,3}\s*Referências', text, flags=re.MULTILINE)
    body = parts[0]
    refs_section = parts[1] if len(parts) > 1 else ''
    
    # Citações no corpo: [N] onde N é número
    body_citations = set(int(x) for x in re.findall(r'\[(\d+)\]', body))
    
    # Entradas na lista de referências: linhas que começam com N.
    ref_entries = set(int(x) for x in re.findall(r'^(\d+)\.', refs_section, re.MULTILINE))
    
    phantom = body_citations - ref_entries  # citadas sem referência
    orphaned = ref_entries - body_citations  # listadas sem citação
    
    print(f"Citações no corpo: {sorted(body_citations)}")
    print(f"Referências listadas: {sorted(ref_entries)}")
    print(f"\nPHANTOM (citadas sem entrada): {sorted(phantom)}")
    print(f"ORPHANED (listadas sem citação): {sorted(orphaned)}")
    
    # Verificar sequência contínua
    if ref_entries:
        expected = set(range(1, max(ref_entries)+1))
        missing_seq = expected - ref_entries
        if missing_seq:
            print(f"\nNUMERAÇÃO COM BURACOS: {sorted(missing_seq)}")
    
    return phantom, orphaned

audit_references('playbook.md')
```

**Por que hole-filling e não renumeração:** durante a auditoria da ginecologia, tentamos renumerar em cascata uma vez e introduzimos 3 novas inconsistências. O pattern de "preencher o buraco" é mais seguro porque cada operação é atômica e verificável.

---

### 1.3 str_replace Tool — Edição Cirúrgica de Arquivos

Usado para correções pontuais no playbook e no JSON sem reescrever o arquivo inteiro.

**Padrão correto de uso:**

```
# NUNCA fazer:
str_replace(old="[47]", new="[42]")  # muito curto, pode ter false positives

# SEMPRE fazer (contexto suficiente para unicidade):
str_replace(
  old="Endocrine Society Guidelines. 2023. [47].",
  new="Endocrine Society Guidelines. 2023 [42]."
)
```

**Para correção de referências fantasma:** o padrão era sempre editar tanto a citação no corpo quanto a entrada na lista de referências na mesma operação, para manter a sincronia.

---

### 1.4 view Tool — Leitura de Arquivos do Projeto

Usada para ler os arquivos JSON de referência antes de escrever qualquer código novo.

```
view('/mnt/project/athena-rotinas_ginecologicas-v2.0.1.json')
view('/mnt/project/athena-Ficha_Clínica___Ginecologia-v344fbc14.json')
```

**Hábito crítico:** antes de criar qualquer node, ler pelo menos um JSON existente completo para extrair:
- Padrões de UIDs (`uid` das questions)
- Estrutura do node conduta (campos obrigatórios)
- Estrutura do node summary (clinicalExpressions)
- Padrão de posicionamento (x em múltiplos de 900)

---

### 1.5 project_knowledge_search — Recuperação de Contexto do Projeto

Usada extensamente para recuperar fragmentos de JSONs e playbooks sem precisar ler o arquivo inteiro.

**Padrões de query que funcionam bem:**

```
"conduta exames liberação condicional"     → retorna estrutura do nó conduta
"summary clinicalExpressions formula"      → retorna estrutura do nó summary
"condicionais linkId condicao"             → retorna exemplos de roteamento
"referências FEBRASGO INCA rastreamento"   → retorna seções do playbook
```

---

### 1.6 Padrões de Design JSON — O que Aprendemos com Ginecologia

#### O node summary tem um papel que não é óbvio

O `summary` não é apenas uma tela de "revisão". Ele contém **`clinicalExpressions`** — variáveis calculadas que são avaliadas antes de o médico ver a conduta. Essas variáveis funcionam como flags booleanas que outros condicionais referenciam.

Exemplo real da ginecologia:

```json
{
  "id": "expr-0a48e6d8-99ca-48c8-b3fb-7cd12d53cb60",
  "name": "aparece_mamografia",
  "formula": "selected_any(exames, \"mamografia\")",
  "description": "",
  "template": ""
}
```

Isso permite que, em nodes posteriores, você use `aparece_mamografia` como condição — ao invés de repetir `selected_any(exames, "mamografia")` em todo lugar.

**Regra derivada:** variáveis frequentemente reutilizadas devem virar `clinicalExpression` no node summary, não ficar inline nos condicionais.

#### O breakpoint não tem questions, mas tem papel de handoff

```json
{
  "id": "node-f6a6173f-14f1-4414-a761f",
  "type": "custom",
  "data": {
    "label": "breakpoint.resumo_enfermagem",
    "descricao": "{{resumo}}",
    "condicionais": [{ "linkId": "node-proximo", "condicao": "" }],
    "questions": []
  }
}
```

Ao aparecer `breakpoint.` no label, a plataforma trata aquele node como um ponto de pausa — a sessão de enfermagem termina ali e o médico assume no node seguinte.

#### As condições de saída de um node são avaliadas de cima para baixo

A última entrada em `condicionais` com `"condicao": ""` é o fallback. As anteriores são avaliadas em ordem e a primeira que satisfaz vence. Isso significa que a **ordem importa** — condições mais específicas devem vir antes das mais gerais.

#### O campo `expressao` nas questions controla visibilidade

```json
{
  "uid": "detalhe_valproato",
  "titulo": "Dose atual e data do último nível sérico de valproato:",
  "condicional": "visivel",
  "expressao": "'valproato' in medicamentos_em_uso",
  "select": "string"
}
```

Se `expressao` estiver vazio, a pergunta aparece sempre. Se preenchido, aparece condicionalmente. **`condicional` deve estar sempre como `"visivel"`** — é um campo legado que o sistema ainda exige mas não usa para esconder (quem esconde é a `expressao`).

---

### 1.7 Mapeamento TUSS — Processo Prático

A tabela TUSS do projeto (`conteúdo_Tabela_TUSS_compartilhada.xlsx`) e a planilha de depara (`Planilha_de_Depara_da_Mevo_UNIVERSAL_DAKTUS_.xlsx`) são o ponto de partida.

**Para psiquiatria, os códigos mais prováveis:**

| Exame | Código TUSS provável | Verificar |
|---|---|---|
| ECG / Eletrocardiograma | 40304361 | Confirmar na tabela |
| TGO (AST) | 40302279 | Confirmar |
| TGP (ALT) | 40302181 | Confirmar |
| Dosagem de ácido valproico | 40302733 | Confirmar |
| Litemia (lítio sérico) | 40302440 | Confirmar |
| Avaliação neuropsicológica | Código de procedimento | Verificar depara |
| Hemograma completo | 40302083 | Confirmar |
| TSH | 40302831 | Confirmar |
| Creatinina | 40302295 | Confirmar |
| Glicemia de jejum | 40302148 | Confirmar |
| Prolactina | 40302660 | Confirmar |

**Processo quando o código não é encontrado nas planilhas:**

1. Busca na tabela TUSS ANS (web, site ANS)
2. Se ainda não encontrado: `"codigo": []` e flag no relatório de QA como "pendente TUSS"
3. Nunca inventar código

---

---

## PARA NOVA ESPECIALIDADE

Ao iniciar um novo projeto, adicione aqui (ou em arquivo separado) o planejamento inicial de clusters da especialidade, analise do briefing e decisoes de design especificas. Consulte  como exemplo de referencia.
