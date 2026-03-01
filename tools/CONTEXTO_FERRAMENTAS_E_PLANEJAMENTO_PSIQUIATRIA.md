# CONTEXTO DE FERRAMENTAS, MÉTODOS E PLANEJAMENTO — PSIQUIATRIA

> **Documento complementar ao AGENT_PROMPT_PROTOCOLO_DAKTUS.md**  
> Serve como memória técnica do que foi construído e como plano de execução para a ficha de Psiquiatria.

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

## PARTE II — PLANEJAMENTO DA FICHA DE PSIQUIATRIA

### 2.1 Análise do Briefing

O briefing traz informações suficientes para estruturar as Fases 0 e 1. Vamos decompô-lo:

**O que o briefing nos diz:**
- Contexto de uso: ambulatorial, Pinheiros
- Problema: ficha geral prolonga atendimento, não cobre hipóteses da especialidade, é abandonada
- Consequências mensuráveis: baixa adesão, perda de rastreabilidade, dificuldade em KPIs
- Comorbidades alvo: 11 condições listadas (ver abaixo)
- Sintomas alvo: 19 sintomas/fatores listados
- Encaminhamentos frequentes: Neuropsicologia e Psicologia
- Exames listados pelos psiquiatras: ECG, TGO, TGP, dosagem de ácido valproico, litemia, avaliação neuropsicológica

**O que o briefing NÃO traz (pendências da Fase 0):**
- Dados de volume e custo do Metabase (não recebidos — solicitar)
- Taxa de exames fora de protocolo
- Escopo etário: adultos apenas ou também adolescentes?
- Existe ficha de Neurologia separada ou compartilhada? (mencionado junto)
- CIDs de entrada que a Amil/Daktus já usa para psiquiatria

---

### 2.2 Mapeamento de Clusters

Com base no briefing + conhecimento clínico, proposta de organização em clusters:

#### Cluster A — Anamnese Psiquiátrica Estruturada

Coletado pela enfermagem. Deve ser rápido e capturar o mínimo necessário para o médico saber o contexto sem reler do zero.

Perguntas candidatas:
- Motivo da consulta (primeiro atendimento / retorno / urgência)
- Diagnóstico(s) psiquiátrico(s) já estabelecido(s) — com campo de texto livre para detalhamento
- Medicamentos psiquiátricos em uso (lista com checkboxes: lítio, valproato, carbamazepina, antipsicóticos, antidepressivos, benzodiazepínicos, estimulantes)
- Histórico de internação psiquiátrica (sim/não)
- Sintomas atuais presentes (lista dos 19 do briefing + extras clínicos relevantes)
- Uso de substâncias (álcool, tabaco, SPA — com campo de detalhamento)
- Sedentarismo (sim/não)

#### Cluster B — Triagem de Risco Imediato (Gate de Segurança)

**Isso é mandatório em psiquiatria.** Ideação suicida/homicida deve ser um gate explícito.

Perguntas candidatas:
- Ideação suicida atual? (sim/não — se sim, aciona fluxo de segurança)
- Comportamento autolesivo recente?
- Ideação heteroagressiva?

**Conduta se positivo:** protocolo de crise / encaminhamento imediato — não avança no fluxo normal.

#### Cluster C — Exame do Estado Mental (Médico)

Capturado pelo médico após o breakpoint. Diferente da anamnese de enfermagem, aqui o médico registra achados do EEM:

- Aparência e comportamento
- Humor e afeto
- Pensamento (forma e conteúdo)
- Sensopercepção (alucinações?)
- Cognição (orientação, memória, atenção)
- Insight e julgamento

Na prática do Daktus, isso pode ser um campo de texto livre estruturado + checkboxes para achados que acionam exames.

#### Cluster D — Módulo de Humor / Depressão / TAB

Acionado quando: diagnóstico de depressão, TAB, ou sintomas de humor presentes.

Perguntas candidatas:
- Episódio atual: depressivo / maníaco / misto / hipomaníaco / eutímico
- Gravidade estimada (leve / moderada / grave)
- Em uso de lítio? → aciona monitoramento de litemia
- Em uso de valproato? → aciona monitoramento de ácido valproico + TGO/TGP
- Em uso de antipsicótico atípico? → aciona glicemia, perfil lipídico, prolactina, ECG (QTc)
- Primeiro episódio? → aciona triagem laboratorial inicial (TSH, hemograma, glicemia, creatinina)

#### Cluster E — Módulo de Ansiedade / TOC / TEPT

Acionado quando: diagnóstico ou sintomas compatíveis.

Perguntas candidatas:
- Tipo principal: TAG / TPA / fobia / TOC / TEPT
- Sintomas físicos de ansiedade presentes (taquicardia, insônia, etc.)
- Em uso de ISRS/ISRSN? → ECG se dose alta de citalopram/escitalopram
- Burnout como diagnóstico principal? (dado o briefing)

#### Cluster F — Módulo de Psicose

Acionado quando: diagnóstico de esquizofrenia, psicose NOS, ou sintomas psicóticos presentes.

Perguntas candidatas:
- Diagnóstico: esquizofrenia / transtorno esquizoafetivo / psicose breve / outros
- Antipsicótico em uso (típico / atípico / clozapina)
- Clozapina? → hemograma com diferencial obrigatório
- Antipsicótico atípico? → glicemia, lipídios, HbA1c, prolactina, ECG
- Sintomas extrapiramidais presentes?

#### Cluster G — Módulo de TDAH

Acionado quando: diagnóstico de TDAH.

Perguntas candidatas:
- Tipo: desatento / hiperativo-impulsivo / combinado
- Estimulante em uso? (metilfenidato, lisdexanfetamina)
- ECG pré-tratamento realizado? (obrigatório antes de estimulantes)
- PA e FC (pode ser capturado pelo exame físico de enfermagem)
- Avaliação neuropsicológica solicitada/realizada?

#### Cluster H — Módulo de TEA

Acionado quando: diagnóstico de TEA.

Perguntas candidatas:
- Diagnóstico confirmado? Se sim, por quem e quando
- Comorbidades associadas (TDAH, ansiedade, epilepsia)
- Medicação atual
- Avaliação neuropsicológica/fonoaudiologia realizada?
- Encaminhamento para neuropsicologia necessário?

#### Cluster I — Módulo de Transtorno de Personalidade

Acionado quando: TPB (Borderline) ou outros TP.

Perguntas candidatas:
- Tipo de TP (Borderline / outros)
- Comportamento autolesivo (gate de segurança — já capturado no Cluster B)
- Em psicoterapia? (DBT, outros)
- Medicação de suporte

#### Cluster J — Módulo de Transtornos Alimentares

Acionado quando: anorexia, bulimia, TCAP.

Perguntas candidatas:
- Tipo: anorexia nervosa / bulimia / TCAP / outros
- IMC atual (capturado pelo exame físico)
- Critérios de gravidade (IMC <17, bradicardia, hipotensão)
- Eletrólitos indicados? (hipocalemia na bulimia)
- Encaminhamento para nutrição/psicoterapia

#### Cluster K — Monitoramento de Fármacos (transversal)

Este cluster é acionado por qualquer módulo que envolva medicamento que requer monitoramento laboratorial. É o núcleo dos exames mais frequentes.

| Fármaco | Exames de monitoramento | Frequência |
|---|---|---|
| Lítio | Litemia, creatinina, TSH, ECG | Inicial: mensal. Estável: a cada 6 meses |
| Valproato / Valproato ER | Ácido valproico, TGO, TGP, hemograma | Inicial: 1–3 meses. Estável: anual |
| Carbamazepina | Nível sérico, hemograma, TGO, TGP, sódio | Inicial: 1–3 meses |
| Antipsicóticos atípicos | Glicemia, HbA1c, lipídios, prolactina, ECG, peso/IMC | Inicial: 3 meses. Estável: anual |
| Clozapina | Hemograma (neutrófilos obrigatório) | Semanal no início, mensal após 1 ano |
| ISRS em dose alta | ECG (QTc) | Antes de titular e quando alterado |
| Estimulantes | ECG, PA, FC | Pré-tratamento e periódico |

---

### 2.3 Fluxo Principal Proposto

```
[Node 1] Nodo padrão
  → Idade (number)
  → Sexo

[Node 2] Termo de Ciência (CFM 1.638/2002)

[Node 3] Anamnese — Enfermagem (Cluster A)
  → Motivo da consulta
  → Diagnósticos conhecidos
  → Medicamentos em uso
  → Sintomas presentes
  → Uso de substâncias / tabagismo / sedentarismo
  → Histórico de internação

[Node 4] Triagem de Risco (Cluster B) — GATE DE SEGURANÇA
  → Ideação suicida?
  → Comportamento autolesivo?
  → Condição: se POSITIVO → breakpoint especial de crise
              se NEGATIVO → continua

[Node 5] Exame Físico — Enfermagem
  → PA, FC, FR
  → Peso, altura, IMC (calculado)
  → Temperatura

[Node 6] breakpoint.resumo_enfermagem  ← PAUSA

[Node 7] Resumo do Atendimento — Médico
  → Confirmação/atualização de diagnósticos
  → EEM (texto estruturado)
  → Hipótese diagnóstica principal
  → Módulo ativo: Humor / Ansiedade / Psicose / TDAH / TEA / TP / TA
    (condicional de roteamento por módulo)

[Node 8A] Módulo de Humor (Cluster D)
  — liberado por: 'depressao' ou 'tab' in diagnostico_principal
[Node 8B] Módulo de Ansiedade (Cluster E)
  — liberado por: 'ansiedade' ou 'toc' ou 'tept' in diagnostico_principal
[Node 8C] Módulo de Psicose (Cluster F)
  — liberado por: 'esquizofrenia' ou 'psicose' in diagnostico_principal
[Node 8D] Módulo de TDAH (Cluster G)
  — liberado por: 'tdah' in diagnostico_principal
[Node 8E] Módulo de TEA (Cluster H)
  — liberado por: 'tea' in diagnostico_principal
[Node 8F] Módulo de TP/Burnout (Cluster I)
  — liberado por: 'tp' ou 'burnout' in diagnostico_principal
[Node 8G] Módulo de TA (Cluster J)
  — liberado por: 'transtorno_alimentar' in diagnostico_principal

[Node 9] Monitoramento de Fármacos (Cluster K) — transversal a todos os módulos

[summary-N] Summary / Processamento

[conduta-N] Conduta
  → Exames condicionais (libera apenas o que foi habilitado pela clínica)
  → Encaminhamentos (Neuropsicologia, Psicologia, CAPS, Internação)
  → Orientações
```

**Decisão de design crítica:** Os módulos 8A–8G não são nodes exclusivos — um paciente pode ter múltiplos diagnósticos. O design deve usar checkboxes no Node 7 (hipóteses múltiplas selecionáveis), e todos os módulos relevantes aparecem sequencialmente ou em questões condicionais dentro de um único node de detalhamento.

**Alternativa mais pragmática** (preferida pela equipe da ginecologia): em vez de 7 nodes separados por módulo, usar um único "Node de Detalhamento Clínico" com perguntas condicionais por `expressao`. Isso reduz o número de nodes e simplifica o grafo. Discutir com o usuário qual estratégia preferir.

---

### 2.4 Exames da Conduta — Mapeamento Inicial

Todos os exames abaixo devem constar no node conduta com condicionais explícitas:

| Exame | Condição de Liberação (rascunho) |
|---|---|
| ECG | `'lítio' in med_em_uso or 'antipsicótico' in med_em_uso or 'estimulante' in med_em_uso or 'isrs_altadose' in med_em_uso or 'primeiro_atendimento' in motivo_consulta and selected_any(...)` |
| TGO + TGP | `'valproato' in med_em_uso or 'carbamazepina' in med_em_uso` |
| Dosagem ácido valproico | `'valproato' in med_em_uso` |
| Litemia | `'lítio' in med_em_uso` |
| Hemograma | `'clozapina' in med_em_uso or 'carbamazepina' in med_em_uso or primeiro_atendimento` |
| TSH | `primeiro_atendimento or 'lítio' in med_em_uso` |
| Glicemia / HbA1c | `'antipsicótico_atípico' in med_em_uso or FR metabólico` |
| Perfil lipídico | `'antipsicótico_atípico' in med_em_uso` |
| Prolactina | `'antipsicótico' in med_em_uso and (sintoma_galactorreia or sintoma_amenorreia)` |
| Creatinina + TFG | `'lítio' in med_em_uso` |
| Avaliação neuropsicológica | `encaminhamento_neuropsicologia is True` |
| Natremia | `'carbamazepina' in med_em_uso` |
| Nível sérico carbamazepina | `'carbamazepina' in med_em_uso` |

---

### 2.5 Encaminhamentos — Condições de Ativação

| Encaminhamento | Condição |
|---|---|
| Neuropsicologia | TDAH com necessidade de avaliação formal, TEA (diagnóstico), declínio cognitivo |
| Psicologia / Psicoterapia | TPB (DBT indicada), transtornos alimentares, luto complicado, TEPT |
| CAPS | Paciente em crise aguda com suporte familiar inadequado |
| Internação (indicação) | Risco suicida alto, psicose aguda grave, anorexia grave (IMC <15) |
| Neurologista | Epilepsia associada, TEA com suspeita de causa orgânica, cefaleia crônica |

---

### 2.6 CIDs de Saída Esperados

| CID | Descrição |
|---|---|
| F20.x | Esquizofrenia |
| F25.x | Transtorno esquizoafetivo |
| F31.x | Transtorno bipolar |
| F32.x | Episódio depressivo |
| F33.x | Transtorno depressivo recorrente |
| F40.x | Transtornos fóbico-ansiosos |
| F41.x | Outros transtornos ansiosos (TAG, TPA) |
| F42.x | TOC |
| F43.x | TEPT, transtornos de adaptação |
| F50.x | Transtornos alimentares |
| F60.3 | TPB (Borderline) |
| F84.0 | Autismo (TEA) |
| F90.x | TDAH |
| F43.8 | Burnout (esgotamento relacionado ao trabalho — Z73.0 também usado) |
| F10–F19 | Transtornos por uso de substâncias |

---

### 2.7 Pendências da Fase 0 a Resolver com o Usuário

Antes de iniciar a Fase 1, preciso das respostas para:

1. **Dados Metabase:** existe relatório de volume/custo de consultas e exames de psiquiatria da Amil similar ao que existe para ginecologia? (total de consultas, top exames por frequência, custo médio por consulta, % fora de protocolo)

2. **Escopo etário:** a ficha cobre apenas adultos ou também adolescentes? (TEA e TDAH têm muito paciente adolescente/jovem adulto)

3. **Estratégia de módulos:** nodes separados por módulo clínico (mais granular, mais fácil de manter, grafo maior) OU perguntas condicionais em poucos nodes (mais compacto, mais difícil de ler o grafo)?

4. **Retorno com resultados:** o padrão das outras fichas tem um node de "retorno" que captura resultados de exames. Quer incluir isso em psiquiatria? (litemia alterada, valproato fora da janela terapêutica têm condutas específicas)

5. **Gate de suicídio:** quando ideação suicida é positiva, qual é o fluxo esperado dentro da plataforma Daktus? Existe um protocolo de crise já definido que a ficha deve ativar, ou precisa criar esse fluxo do zero?

6. **Documentos adicionais:** você mencionou que usará OpenEvidence, DSM-5, Kaplan e possíveis resumos/apostilas. Esses documentos serão injetados como contexto de projeto ou enviados pontualmente durante a Fase 1?

---

### 2.8 Cronograma Proposto (resposta ao briefing)

Com base no ritmo das especialidades anteriores:

| Fase | Estimativa | Dependência |
|---|---|---|
| Fase 0 — Briefing completo | 1–2 sessões | Dados Metabase + definições de escopo |
| Fase 1 — Playbook draft | 3–5 sessões | Documentos OpenEvidence + DSM-5/Kaplan |
| Fase 2 — Auditoria referências | 1 sessão (automatizada) | Fase 1 aprovada |
| Fase 3 — Revisão clínica | 2–4 sessões | Feedback dos psiquiatras |
| Fase 4 — Implementação JSON | 3–4 sessões | Fase 3 aprovada + TUSS mapeado |
| Fase 5 — QA final | 1 sessão | Fase 4 completa |
| **Total estimado** | **11–16 sessões de trabalho** | — |

---

## PARTE III — INSTRUÇÕES PARA O AGENTE LOCAL

### O que este documento adiciona ao prompt principal

O `AGENT_PROMPT_PROTOCOLO_DAKTUS.md` contém as regras. Este documento contém a **memória técnica operacional** — como as regras foram descobertas na prática. O agente deve usar ambos.

### Prioridade de leitura ao iniciar uma sessão

1. Ler `AGENT_PROMPT_PROTOCOLO_DAKTUS.md` (regras e arquitetura)
2. Ler este documento (ferramentas e planejamento)
3. Ler os JSONs de referência no projeto (`view /mnt/project/`)
4. Verificar se há documentos adicionais injetados pelo usuário (OpenEvidence, apostilas)

### O que fazer com documentos externos (OpenEvidence, DSM-5, Kaplan)

Quando o usuário fornecer um relatório OpenEvidence ou trecho de livro:
1. Extrair as afirmações clínicas com suas referências bibliográficas
2. Verificar se a referência está citada de forma verificável (autor, publicação, ano)
3. Incorporar ao playbook com numeração sequencial a partir do último número usado
4. Executar `audit_references` após cada incorporação

**Não incorporar afirmações sem fonte identificável.** Se o OpenEvidence não citar a origem, marcar como `[FONTE PENDENTE]` e sinalizar para o usuário.

---

*Fim do documento. Versão 1.0 — 2026-02-27*
