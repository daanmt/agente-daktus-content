# BRIEFING DE ARQUITETURA — O QUE É UM NÓ NO DAKTUS
## Para: Antigravity | De: Claude Sonnet 4.6 | Data: 2026-02-27
## Leitura obrigatória ANTES de qualquer trabalho em playbook ou JSON

---

## ⚠️ CORREÇÃO CONCEITUAL CRÍTICA

Você (e eu) usamos a palavra "nó" de forma imprecisa até agora. Precisamos alinhar o conceito antes de produzir qualquer linha de playbook ou JSON.

**Um nó NÃO é um módulo clínico temático** (ex: "módulo de humor", "módulo de psicose").  
**Um nó É uma tela** — uma única tela de formulário que um profissional de saúde preenche na plataforma Daktus.

Cada tela tem perguntas. As respostas geram variáveis. As variáveis controlam o que aparece na tela de saída. Isso é o produto inteiro.

---

## 1. O QUE É UM NÓ — DEFINIÇÃO TÉCNICA

Lendo os JSONs de cardiologia e ginecologia, um nó tem esta estrutura:

```json
{
  "id": "node-XXXX",
  "type": "custom",
  "data": {
    "label": "Nome da tela",
    "descricao": "",
    "condicionais": [
      { "linkId": "node-YYYY", "condicao": "expressão ou vazio" }
    ],
    "questions": [ ... ]
  }
}
```

### Tipos de questão dentro de um nó

| `select` | O que é | Quando usar |
|----------|---------|-------------|
| `choice` | Seleção única | Sexo, sim/não |
| `multiChoice` | Seleção múltipla | Queixas, comorbidades, sintomas |
| `number` | Campo numérico | Idade, IMC, litemia, dose |
| `string` | Texto livre | Complemento da queixa, observações |

### O que são `condicionais`

É o roteamento entre telas. Define **qual nó vem a seguir** e com qual condição:
```json
"condicionais": [
  { "linkId": "node-GATE-P0", "condicao": "'ideacao_com_plano' in risco_suicida" },
  { "linkId": "node-anamnese-medico", "condicao": "" }
]
```
A primeira condição que for verdadeira direciona o fluxo. A sem condição é o fallback.

### O que são variáveis

Cada questão tem um `uid` — esse é o nome da variável que fica disponível em todo o grafo:
```json
{ "uid": "risco_suicida", "select": "multiChoice" }
```
Depois disso, `'ideacao_com_plano' in risco_suicida` é uma expressão válida em qualquer nó.

---

## 2. OS TIPOS DE NÓ EXISTENTES NO SISTEMA

### Tipo A — Nó de Coleta (input)
A maioria dos nós. Contém perguntas, gera variáveis.  
**Exemplos:** Triagem de Enfermagem, Anamnese Médico, Gate P0.

### Tipo B — Nó de Conduta (output)
Nó especial que contém as recomendações clínicas.  
**Não tem perguntas.** Tem listas de exames, medicamentos, alertas e encaminhamentos — cada item com uma condição de exibição.  
**É onde a inteligência clínica vive.**

Estrutura típica de item de exame na conduta:
```json
{
  "nome": "Litemia (lítio sérico)",
  "condicao": "('litio' in medicamentos_em_uso) and (tempo_uso_litio == 'iniciando')",
  "periodicidade": "Coleta 5–7 dias após ajuste de dose",
  "codigo": [{ "sistema": "TUSS", "codigo": "40302440" }]
}
```

Estrutura típica de alerta na conduta:
```json
{
  "nome": "GATE P0 — Ideação com plano: NÃO deixar paciente sozinho",
  "condicao": "'ideacao_com_plano' in risco_suicida",
  "conteudo": "<p>Acionar SAMU/UPA imediatamente. Não deixar o paciente desacompanhado. Iniciar SPI. Completar laudo médico para transferência. Notificar família (CFM Art. 46).</p>"
}
```

---

## 3. O FLUXO TÍPICO DE UMA FICHA — REFERÊNCIA: GINECOLOGIA

A ficha de ginecologia tem **~5 nós** no total. Não tem 11 módulos.

```
Nó 1: Enfermeiro — Triagem
  → coleta: idade, queixa principal, exames trazidos
  → roteia para: Nó 2

Nó 2: Anamnese Médico — inicial
  → coleta: histórico, comorbidades, medicamentos, histórico reprodutivo
  → roteia para: Nó 3 (se trouxe exames) OU Nó 4

Nó 3: Revisão de Exames (condicional)
  → coleta: resultados de HPV, citologia, mamografia, labs
  → roteia para: Nó 4

Nó 4: Anamnese Médico — detalhe de queixa
  → coleta: sintomas específicos condicionados pela queixa (ex: se SUA → perguntas de SUA)
  → roteia para: Nó 5 (Conduta)

Nó 5 (Conduta): Exames + Medicamentos + Alertas + Encaminhamentos
  → sem perguntas
  → mostra apenas o que é relevante para cada paciente, baseado em todas as variáveis coletadas
```

**Conclusão:** O produto inteiro é uma sequência de 4–6 telas de formulário, culminando em uma tela de saída inteligente.

---

## 4. COMO OS CLUSTERS A–K DO BRIEFING SE TRADUZEM EM NÓS

O briefing identificou 11 clusters temáticos. Isso **não significa 11 nós**. Significa 11 áreas de conteúdo clínico, que serão distribuídos assim:

| Nó | Label | Clusters atendidos |
|----|-------|-------------------|
| **Nó 1** | Enfermeiro — Triagem | A parcial (motivo da consulta, sinais vitais, medicamentos) |
| **Nó 2** | Gate P0 — Risco Suicida | **B** (OBRIGATÓRIO — segundo nó, logo após triagem) |
| **Nó 3** | Anamnese Psiquiátrica | A completo + histórico pessoal relevante + substâncias |
| **Nó 4** | Módulo de Diagnóstico Ativo | D, E, F, G, H, I, J (condicional por diagnóstico) |
| **Nó 5** | Monitoramento de Fármacos | K (condicional por medicamento em uso) |
| **Nó 6 (Conduta)** | Saída: Exames + Alertas + Encaminhamentos | Todos os clusters |

**O Nó 4 é o nó crítico de design:** ele deve mostrar perguntas específicas de acordo com o diagnóstico ativo. Se o paciente tem TAB → aparece YMRS + perguntas de humor. Se tem TDAH → aparecem perguntas de TDAH. Se tem esquizofrenia → aparecem perguntas de EPS + clozapina. As perguntas se condicionam pelo que foi marcado no Nó 3.

**O Nó 2 (Gate P0) é INCONTORNÁVEL:** toda consulta passa por ele, sem exceção. A questão de ideação suicida com plano deve ter `exclusive: false` nas opções de risco e o item de alerta na conduta deve ser o PRIMEIRO item, com a condição mais prioritária.

---

## 5. PRINCÍPIOS DE DESIGN — O QUE O FEEDBACK DOS OUTROS PROJETOS ENSINA

Com base nos feedbacks de ginecologia, cardiologia e outros:

**✅ Fazer:**
- Poucas telas, muitas perguntas por tela quando necessário
- Perguntas condicionais dentro da mesma tela (`"condicional": "condicional"` + `"expressao"`) para evitar telas extras
- Opção com `"preselected": true` para o estado mais comum (ex: "sem risco suicida ativo")
- Alertas na conduta curtos, acionáveis, com conduta específica
- Exames na conduta com código TUSS e periodicidade explícita
- Lógica de conduta conservadora: melhor mostrar algo extra do que esconder algo necessário

**❌ Não fazer:**
- Um nó por diagnóstico (seria 11+ telas — inviável na prática)
- Perguntas abertas (`string`) onde multiChoice funciona
- Conduta genérica sem condicional (mostra o mesmo para todos)
- Ausência de Gate P0 ou Gate P0 como último nó
- Exames sem código TUSS
- Alertas com texto académico — deve ser texto de conduta, imperativo, com verbo no infinitivo

---

## 6. O QUE O PLAYBOOK É — E O QUE NÃO É

O playbook **não é o JSON**. O playbook é a **documentação clínica** que justifica cada decisão do JSON. Ele documenta:

1. O raciocínio clínico por trás de cada pergunta do formulário
2. A lógica de cada expressão condicional
3. As referências que sustentam cada indicação de exame
4. Os limiares de alerta e sua fonte de evidência
5. Os critérios de encaminhamento e internação

O playbook de ginecologia (referência mais atual) tem estas seções:
- Introdução e mudanças de paradigma
- Panorama epidemiológico
- Dados da operadora e aderência (Metabase)
- Objetivos do protocolo
- Cobertura e estratégias de rastreio (por condição)
- Exames e suas indicações clínicas (tabelas com nível de evidência)
- Exames proscritos
- Terapêuticas (quando aplicável)
- Calculadoras e escores
- Metas auditáveis e KPIs
- Referências

**O playbook de psiquiatria seguirá a mesma estrutura**, adaptada para:
- Rastreamento de risco (Gate P0) em vez de rastreamento oncológico
- Monitoramento farmacológico em vez de rastreamento preventivo
- Escalas de avaliação em vez de calculadoras de risco

---

## 7. SEQUÊNCIA CORRETA DE TRABALHO — ORDEM INVIOLÁVEL

```
[FASE 0 ✅]  Briefing + banco de evidências completo

[FASE 2 🔄]  PRÉ-AUDITORIA do banco (você está aqui)
             → Classificar 419 refs em TIER 1/2/3
             → Consolidar AFIs redundantes
             → Gerar AUDITORIA_BANCO_v1.md
             → Aguardar aprovação de Dan

[FASE 1]     PLAYBOOK DRAFT — por cluster, na ordem:
             → Cluster B (Gate P0) — primeiro porque é bloqueante
             → Cluster A (Anamnese Enfermagem)
             → Cluster K (Monitoramento fármacos — transversal)
             → Clusters D, E, F, G, H, I, J (por diagnóstico)
             → Encaminhamentos e internação
             Cada seção do playbook cita AFI-IDs do banco como fonte

[FASE 2]     AUDITORIA DO PLAYBOOK
             → Verificar rastreabilidade de cada afirmação
             → Confirmar códigos TUSS
             → Identificar lacunas

[FASE 3]     REVISÃO CLÍNICA com psiquiatras da Amil

[FASE 4]     IMPLEMENTAÇÃO JSON
             → Primeiro: mapa de nós e variáveis (paper design)
             → Segundo: JSON de cada nó
             → Terceiro: JSON completo integrado

[FASE 5]     QA FINAL + homologação
```

**Regra de ouro:** Nenhuma fase começa antes da anterior ser aprovada por Dan. Não há atalhos.

---

## 8. DÚVIDAS SOBRE O PROJETO — ONDE BUSCAR RESPOSTA

Antes de assumir qualquer coisa, leia nesta ordem:
1. `/tools` — documentos de instrução do agente
2. Os playbooks de referência (ginecologia + cardiologia) — estrutura e nível de detalhe esperados
3. Os JSONs de referência (ginecologia + cardiologia) — padrões técnicos de implementação
4. `BANCO_EVIDENCIAS_PSIQUIATRIA.md` — autoridade clínica do projeto
5. Os relatórios OE individuais (REL-01 a REL-10) — se precisar de contexto completo de uma seção

Se ainda houver dúvida após consultar essas fontes, registre a dúvida no arquivo de sessão e aguarde Dan.

---

*Este documento deve ser lido no início de toda nova sessão. Versão 1.0 — 2026-02-27.*
