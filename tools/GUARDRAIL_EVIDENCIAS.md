# PROTOCOLO DE GESTÃO DE EVIDÊNCIAS — GUARDRAIL DO AGENTE

> **Documento complementar ao AGENT_PROMPT_PROTOCOLO_DAKTUS.md e ao CONTEXTO_FERRAMENTAS_E_PLANEJAMENTO.md**  
> Define o comportamento mandatório do agente ao encontrar incerteza clínica, conflito entre fontes ou gaps de evidência durante o desenvolvimento de qualquer artefato.

---

## PRINCÍPIO FUNDAMENTAL

**O agente não toma decisões clínicas por conta própria quando a evidência é insuficiente, conflitante ou desatualizada.**

Protocolos clínicos têm valor médico-legal. Uma afirmação incorreta sobre uma indicação de exame, intervalo de rastreamento ou conduta pode causar dano real ao paciente e expor a operadora a risco regulatório. Por isso, o manejo rigoroso de evidências não é uma preferência de qualidade — é um requisito de segurança.

A ferramenta OpenEvidence (e equivalentes: UpToDate, PubMed, diretrizes de sociedades) é o oráculo de consulta. O agente não resolve incertezas por inferência quando a consulta é possível. **Ele formula a pergunta certa e para.**

---

## GATILHOS DE INTERRUPÇÃO

O agente deve pausar o desenvolvimento do artefato corrente e emitir uma **Solicitação de Evidência** sempre que identificar qualquer uma das situações abaixo:

### G1 — Conflito entre Fontes

Duas ou mais diretrizes consultadas divergem sobre a mesma conduta.

*Exemplos:*
- FEBRASGO recomenda conduta A, mas CANMAT recomenda conduta B para o mesmo cenário
- DSM-5-TR usa critério diferente do CID-11 para o mesmo diagnóstico, e isso afeta a indicação de exame
- Guideline de 2022 diz X, guideline de 2024 diz Y sobre o mesmo ponto

### G2 — Ausência de Diretriz Nacional

A conduta em questão não tem guideline brasileiro publicado, e a extrapolação de diretrizes internacionais exige confirmação.

*Exemplos:*
- Intervalo de litemia em manutenção — ABP tem recomendação? Ou só CANMAT/BAP?
- Rastreamento cognitivo em psiquiatria ambulatorial — existe recomendação formal no Brasil?

### G3 — Evidência Desatualizada

A fonte disponível é anterior a 2022 e o tema é de evolução rápida (psicofarmacologia, critérios diagnósticos, rastreamento).

*Exemplos:*
- Referência sobre QTc e antipsicóticos de 2018 — existe meta-análise mais recente?
- Recomendação de dosagem de valproato de livro-texto de 2015 — o guideline atual confirma?

### G4 — Afirmação de Alto Impacto sem Fonte Identificável

O agente está prestes a escrever uma conduta com impacto clínico significativo (gate de segurança, critério de internação, contraindicação absoluta) e não tem referência verificável para ancora-la.

*Exemplos:*
- "Litemia acima de 1,5 mEq/L é tóxica" — qual a fonte exata? Faixa terapêutica e janela de toxicidade precisam de referência primária.
- "ECG obrigatório antes de iniciar antipsicótico atípico" — qual guideline faz essa recomendação com esse grau?

### G5 — Atrito entre Prática Clínica Relatada e Evidência

O briefing clínico (o que os médicos fazem) diverge do que a evidência formal recomenda.

*Exemplos:*
- Médicos solicitam avaliação neuropsicológica de rotina para TDAH, mas guideline diz que é reservada para casos complexos
- Psiquiatras monitoram valproato mensalmente, mas guideline diz que semestral é suficiente em paciente estável

### G6 — Grau de Recomendação Relevante para Decisão de Design

O agente precisa decidir se um exame entra como **obrigatório** (sempre liberado na condição clínica) ou **opcional** (liberado apenas se o médico marcar), e isso depende do nível de evidência/grau de recomendação.

*Exemplos:*
- TSH em primeiro atendimento psiquiátrico — grau A, B ou C? Muda se for obrigatório ou opcional
- Prolactina de rotina em antipsicótico — recomendação baseada em sintomas ou de rastreamento cego?

---

## FORMATO DA SOLICITAÇÃO DE EVIDÊNCIA

Quando um gatilho é ativado, o agente para o desenvolvimento e emite:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 SOLICITAÇÃO DE EVIDÊNCIA #[N]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GATILHO: [G1 / G2 / G3 / G4 / G5 / G6]
ARTEFATO EM DESENVOLVIMENTO: [playbook seção X / node Y do JSON]
PONTO DE PARADA: [trecho exato onde o desenvolvimento travou]

CONTEXTO CLÍNICO:
[2–4 frases descrevendo o cenário clínico específico que gerou a dúvida.
Inclui: condição do paciente, fármaco/exame/conduta em questão, o que
já se sabe e o que está incerto.]

CONFLITO / GAP IDENTIFICADO:
[Descrição objetiva da incerteza. Se for conflito entre fontes, citar
ambas. Se for ausência de diretriz, dizer o que foi buscado e não
encontrado. Se for prática vs. evidência, descrever ambos.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERGUNTA PARA OPENEVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A pergunta, pronta para ser colada no OpenEvidence ou similar.
Formulada segundo os princípios abaixo.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O QUE PRECISO DA RESPOSTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Grau de recomendação / nível de evidência
□ Fonte primária (guideline / RCT / meta-análise + ano)
□ Posição da diretriz brasileira (se aplicável)
□ Resolução do conflito entre [Fonte A] e [Fonte B]
□ [Outro específico desta pergunta]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMPACTO NO ARTEFATO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Se resposta for [A]: [o que muda no protocolo]
Se resposta for [B]: [o que muda no protocolo]

DESENVOLVIMENTO PAUSADO — aguardando resposta.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## PRINCÍPIOS DE FORMULAÇÃO DA PERGUNTA

A qualidade da resposta do OpenEvidence depende diretamente da qualidade da pergunta. O agente deve seguir estes princípios:

### P1 — Especificidade Clínica Máxima

Nunca perguntar em abstrato. Sempre ancorar no paciente/cenário concreto.

```
❌ RUIM:
"Qual o monitoramento laboratorial para pacientes em uso de lítio?"

✅ BOM:
"Em paciente adulto com transtorno bipolar tipo I em uso de lítio 900mg/dia
há 18 meses, clinicamente estável e com litemia de 0,7 mEq/L no último
controle, qual é o intervalo recomendado para nova aferição de litemia,
creatinina e TSH? Existe diretriz brasileira (ABP) ou guideline internacional
(CANMAT 2023 / BAP 2023) com grau de recomendação explícito para este
cenário de manutenção estável?"
```

### P2 — Solicitar Grau de Recomendação Explicitamente

```
✅ SEMPRE incluir:
"Qual o grau de recomendação (A/B/C) e nível de evidência (I/II/III)
desta conduta segundo [guideline específico]?"
```

### P3 — Solicitar a Fonte Primária, não a Síntese

```
❌ RUIM:
"O OpenEvidence recomenda monitorar prolactina em uso de antipsicóticos?"

✅ BOM:
"Qual guideline (nome, ano, organização emissora) fundamenta a
recomendação de dosagem de prolactina em pacientes em uso de antipsicóticos
de segunda geração sem sintomas de hiperprolactinemia? É rastreamento
de rotina ou condicional a sintomas? Citar a referência exata."
```

### P4 — Enquadrar o Conflito quando Houver

```
✅ QUANDO HÁ CONFLITO:
"O CANMAT 2023 recomenda X para [condição], enquanto o DSM-5-TR / APA
2022 orienta Y para o mesmo cenário. Existe evidência recente (2023–2026)
que resolva essa divergência? Qual a posição mais conservadora do ponto
de vista de segurança do paciente?"
```

### P5 — Pedir Nível de Certeza quando Relevante

Para condutas de gate de segurança (suicídio, internação, contraindicação):

```
✅ INCLUIR:
"Esta recomendação tem suporte de ensaio clínico randomizado, ou é
baseada em consenso de especialistas / opinião de guideline sem
evidência primária robusta? Isso é relevante para a decisão de torná-la
obrigatória vs. opcional no protocolo."
```

### P6 — Preguntar sobre Contexto Brasileiro quando Aplicável

```
✅ INCLUIR quando relevante:
"Existe adaptação desta diretriz para o contexto brasileiro (ABP,
CFM, MS)? Ou a prática brasileira segue diretamente o guideline
internacional sem adaptação publicada?"
```

---

## COMPORTAMENTO APÓS RECEBER A RESPOSTA

Quando o usuário retornar com a resposta do OpenEvidence (ou outra fonte):

### Passo 1 — Verificação de Completude

```
VERIFICAÇÃO DA RESPOSTA #[N]

□ Grau de recomendação recebido? [sim / parcial / não]
□ Fonte primária identificável? [sim / parcial / não]
□ Conflito resolvido? [sim / parcial / não]
□ Posição brasileira clara? [sim / parcial / não]

→ Se algum item é "não" ou "parcial": emitir pergunta de seguimento
  antes de retomar o desenvolvimento.
→ Se todos "sim": registrar a evidência e retomar.
```

### Passo 2 — Registro Estruturado da Evidência

Antes de incorporar ao playbook, o agente registra internamente:

```
EVIDÊNCIA REGISTRADA #[N]
Afirmação: [a conduta/critério que será incorporado]
Fonte: [Autor/Organização. Título. Publicação. Ano. Páginas/Seção.]
Grau: [A/B/C/D ou equivalente do sistema usado]
Nível: [I/II/III ou equivalente]
Número da referência no playbook: [N]
Contexto de uso: [em qual seção/node será aplicada]
```

### Passo 3 — Incorporação com Citação Imediata

A afirmação vai para o playbook **já com a citação** na mesma operação. Nunca escrever texto sem citar e "deixar para adicionar a referência depois" — isso é a principal fonte de phantoms.

```markdown
# ERRADO (gera phantom):
A litemia deve ser monitorada mensalmente no primeiro ano de tratamento.

# CORRETO:
A litemia deve ser monitorada mensalmente durante o primeiro ano de
tratamento e a cada 3–6 meses em pacientes estáveis [N].
```

---

## CASOS ESPECIAIS

### Quando a resposta do OpenEvidence é "não há evidência robusta"

Esta é uma resposta válida e deve ser documentada como tal no playbook:

```markdown
Não existe ensaio clínico randomizado ou meta-análise de alta qualidade
que defina o intervalo ideal de monitoramento de [X] em [cenário Y].
A recomendação abaixo baseia-se em consenso de especialistas
[Referência do consenso, ano] e na prática clínica predominante. [N]
```

No JSON, condutas baseadas em consenso fraco **não devem ser obrigatórias** — devem ser opcionais (sem condição de liberação automática, deixando a critério do médico).

### Quando há conflito irresolvível entre fontes de igual peso

Documentar a divergência explicitamente no playbook e adotar a posição **mais conservadora em termos de segurança do paciente**:

```markdown
Existe divergência entre [Fonte A, ano] e [Fonte B, ano] sobre [ponto].
[Fonte A] recomenda X [N], enquanto [Fonte B] recomenda Y [N]. Este
protocolo adota Y por ser a conduta mais conservadora [ou: por ser a
diretriz mais recente / por ser a diretriz da sociedade brasileira],
com nota de que a prática pode variar conforme o julgamento clínico.
```

### Quando o usuário fornece uma apostila ou resumo sem referências primárias

O agente aceita o conteúdo como **orientação clínica não-citável**. Ele usa o conteúdo para entender a prática e identificar o que deve ser buscado, mas nunca o cita diretamente no playbook. Para cada afirmação relevante da apostila, deve emitir uma Solicitação de Evidência buscando a fonte primária correspondente.

```
ℹ️ NOTA SOBRE FONTE SECUNDÁRIA
O documento "[nome da apostila]" fornecido afirma que [X].
Esta afirmação não tem referência primária identificável no documento.
Emitindo Solicitação de Evidência #[N] para localizar a fonte original
antes de incorporar ao playbook.
```

---

## EXEMPLO COMPLETO — CENÁRIO REAL DE PSIQUIATRIA

**Situação:** O agente está escrevendo a seção de monitoramento de lítio no playbook e precisa definir o intervalo de dosagem de creatinina. Encontra divergência entre fontes.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 SOLICITAÇÃO DE EVIDÊNCIA #1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GATILHO: G1 (conflito entre fontes) + G6 (grau de recomendação
         relevante para decisão de design)
ARTEFATO: Playbook Psiquiatria — Seção "Monitoramento de Lítio"
PONTO DE PARADA: Definição do intervalo de monitoramento de função
                 renal (creatinina/TFG) em uso crônico de lítio

CONTEXTO CLÍNICO:
Paciente adulto em uso de lítio para TAB tipo I, em manutenção estável.
Preciso definir com que frequência o protocolo deve liberar/solicitar
creatinina + TFG. A nefrotoxicidade do lítio é dose-dependente e
cumulativa. O intervalo impacta diretamente no design da conduta: se
for semestral, vai no check periódico; se for anual, vai no check anual;
se depender do tempo de uso, preciso de lógica condicional no JSON.

CONFLITO / GAP IDENTIFICADO:
- CANMAT 2023 (Bipolar Disorder Guidelines) menciona monitoramento
  renal a cada 6 meses de forma genérica, sem estratificar por tempo
  de uso ou TFG basal.
- BAP 2023 (British Association for Psychopharmacology) recomenda
  anual para pacientes estáveis com função renal normal, mas semestral
  se TFG < 60 ou se uso > 10 anos.
- Não localizei recomendação explícita da ABP com grau de evidência.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERGUNTA PARA OPENEVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Em paciente adulto com transtorno bipolar tipo I em uso de lítio
há mais de 2 anos, clinicamente estável, com TFG basal > 60 mL/min,
qual é o intervalo recomendado para monitoramento de função renal
(creatinina sérica e/ou TFG estimada)?

Especificamente:
1. O CANMAT 2023 ou BAP 2023 estratificam esse intervalo por tempo
   de uso (< 5 anos vs. > 10 anos) ou por TFG basal?
2. Existe grau de recomendação (A/B/C) explícito para este intervalo
   em algum dos dois guidelines?
3. A ABP (Associação Brasileira de Psiquiatria) tem diretriz publicada
   (2020–2025) sobre monitoramento renal no uso crônico de lítio?
4. Em caso de divergência entre CANMAT e BAP, qual a justificativa
   de cada um para o intervalo escolhido?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O QUE PRECISO DA RESPOSTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Intervalo específico com grau de recomendação
□ Se o intervalo é estratificado por TFG ou por tempo de uso
□ Fonte primária com ano (não síntese)
□ Posição da ABP se existir

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMPACTO NO ARTEFATO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Se intervalo anual para TFG normal: conduta liberada no check anual,
  sem lógica condicional complexa.
Se intervalo estratificado por TFG: preciso de pergunta adicional no
  node de monitoramento capturando TFG mais recente, e dois caminhos
  condicionais no JSON.
Se ABP tem diretriz: adotar como referência primária brasileira,
  sobrepondo CANMAT/BAP.

DESENVOLVIMENTO PAUSADO — aguardando resposta.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## INTEGRAÇÃO COM O FLUXO DE FASES

As Solicitações de Evidência podem ocorrer em qualquer fase, mas têm padrões típicos:

| Fase | Tipo de SE mais comum |
|---|---|
| Fase 1 (Playbook) | G1, G2, G3 — conflito e gaps durante pesquisa |
| Fase 2 (Auditoria) | G4 — afirmações sem fonte identificável |
| Fase 3 (Revisão) | G5 — prática clínica do médico vs. evidência |
| Fase 4 (JSON) | G6 — grau para decidir obrigatório vs. opcional |

**Limite razoável por sessão:** se o agente identificar mais de 3 SEs pendentes simultaneamente, ele agrupa todas antes de pausar, para que o usuário possa levar um lote ao OpenEvidence de uma vez.

---

*Fim do documento. Versão 1.0 — 2026-02-27*
