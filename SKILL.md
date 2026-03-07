# SKILL.md — ORCHESTRATOR DO PIPELINE DO AMBIENTE DAKTUS

## PAPEL DESTE ARQUIVO

Este arquivo orquestra o pipeline de produção do ambiente daktus.

Ele não é o ponto de entrada do ambiente.
O ponto de entrada é `AGENTE.md`.

Este arquivo existe para:
- explicitar as fases do pipeline;
- mostrar quais sub-skills existem;
- indicar quando cada uma deve ser ativada;
- preservar a lógica de progressive disclosure;
- impedir que o agente misture fases ou salte gates.

---

## PRÉ-REQUISITO DE USO

Antes de usar este arquivo, o agente já deve ter lido:

1. `AGENTE.md`
2. `HANDOFF.md`, se existir
3. `ESTADO.md`

Este arquivo não substitui o boot operacional do ambiente.
Ele só deve ser usado depois que o estado atual já tiver sido identificado.

---

## PRINCÍPIO DE OPERAÇÃO

O agente conhece o pipeline completo por meio deste orchestrator, mas só deve abrir a sub-skill correspondente à fase ativa.

Regra:
- conhecer o todo;
- ler em profundidade apenas a fase atual;
- executar apenas o próximo passo coerente.

Isso preserva:
- foco;
- economia de contexto;
- continuidade entre sessões;
- portabilidade entre agentes.

---

## PIPELINE CANÔNICO

```text
Fase 1  briefing-arquitetura
Fase 2  ingestao-evidencias
Fase 3  auditoria-banco
Fase 4  redacao-playbook
Fase 5  auditoria-playbook
Fase 6  codificacao-json
Fase 7  qa-entrega
````

A numeração pode variar historicamente em discussões antigas ou em especialidades específicas, mas a lógica dos gates não muda.

O que importa é:

* não avançar sem artefato anterior consolidado;
* não executar fase posterior por inferência;
* não tratar benchmark como autorização para pular etapas.

---

## REGRA DE GATE

A sequência do pipeline é obrigatória.

Pode haver:

* refinamento interno dentro da mesma fase;
* retorno pontual à fase anterior para correção;
* iteração controlada entre artefatos próximos.

Não pode haver:

* salto direto de briefing para JSON;
* playbook sem auditoria correspondente;
* JSON sem playbook liberado;
* entrega final sem QA.

---

## SUB-SKILLS DISPONÍVEIS

### 1. `briefing-arquitetura`

**Pasta:** `tools/skills/briefing-arquitetura/`

Ativar quando:

* uma nova especialidade estiver começando;
* o problema ainda estiver sendo enquadrado;
* for necessário estruturar escopo, objetivos, arquitetura clínica e direção inicial.

Entrega esperada:

* mapa inicial da especialidade;
* enquadramento do problema;
* estrutura-base para as próximas fases.

---

### 2. `ingestao-evidencias`

**Pasta:** `tools/skills/ingestao-evidencias/`

Ativar quando:

* houver material bruto de evidência;
* relatórios, diretrizes, bancos ou documentos precisarem ser organizados;
* a base factual ainda não estiver pronta para redação.

Entrega esperada:

* evidências organizadas;
* material preparado para auditoria e uso posterior.

---

### 3. `auditoria-banco`

**Pasta:** `tools/skills/auditoria-banco/`

Ativar quando:

* as evidências já tiverem sido reunidas;
* for necessário depurar, validar ou classificar o banco;
* a base ainda não estiver segura para sustentar playbook.

Entrega esperada:

* banco auditado;
* evidências classificadas e depuradas;
* base apta para redação estruturada.

---

### 4. `redacao-playbook`

**Pasta:** `tools/skills/redacao-playbook/`

Ativar quando:

* a base de evidências já estiver suficiente;
* a especialidade precisar ser convertida em lógica clínica estruturada;
* o artefato alvo for o playbook.

Entrega esperada:

* playbook clínico estruturado;
* fluxo clínico legível e rastreável;
* base pronta para auditoria do playbook.

---

### 5. `auditoria-playbook`

**Pasta:** `tools/skills/auditoria-playbook/`

Ativar quando:

* o playbook já existir em draft ou versão inicial;
* for necessário revisar consistência clínica, rastreabilidade e completude;
* o objetivo for liberar o playbook para codificação.

Entrega esperada:

* playbook auditado;
* problemas críticos apontados ou corrigidos;
* gate clínico explícito para seguir ou não para JSON.

---

### 6. `codificacao-json`

**Pasta:** `tools/skills/codificacao-json/`

Ativar quando:

* o playbook tiver sido auditado e liberado;
* a fase clínica anterior estiver encerrada;
* o objetivo passar a ser arquitetura de nós, paper design, TUSS, clinicalExpressions e JSON.

Entrega esperada:

* paper design consolidado;
* estrutura de nós e condicionais;
* mapeamento técnico;
* JSON validável.

---

### 7. `qa-entrega`

**Pasta:** `tools/skills/qa-entrega/`

Ativar quando:

* o JSON já estiver consolidado;
* o artefato precisar de checagem final;
* a especialidade estiver próxima da entrega ou homologação.

Entrega esperada:

* checklist final;
* pendências residuais;
* artefato pronto para validação ou entrega.

---

## COMO ESCOLHER A SUB-SKILL CERTA

Depois de ler `AGENTE.md`, `HANDOFF.md` e `ESTADO.md`, o agente deve responder:

* Qual é a fase atual?
* Qual é o artefato de entrada?
* Qual é o artefato de saída esperado nesta sessão?
* O gate da fase atual já foi liberado?
* Existe algum bloqueio documental ou clínico?

Só depois disso a sub-skill correta deve ser aberta.

---

## REGRA DE LEITURA MÍNIMA

Este orchestrator não autoriza leitura indiscriminada do repositório.

O fluxo correto é:

1. identificar a fase;
2. abrir apenas a sub-skill da fase ativa;
3. consultar documentos auxiliares só quando necessários;
4. usar benchmarks apenas como referência estrutural.

---

## DOCUMENTOS AUXILIARES

Dependendo da fase, o agente pode consultar documentos de apoio, como:

* `tools/AGENT_PROMPT_PROTOCOLO_DAKTUS.md`
* `tools/PADROES_ARQUITETURA_JSON.md`
* `tools/GUARDRAIL_EVIDENCIAS.md`
* `tools/CONTEXTO_FERRAMENTAS_E_METODOS.md`
* `tools/KICKSTART_NOVA_ESPECIALIDADE.md`

Esses documentos não substituem a sub-skill da fase ativa.
Eles apenas complementam a execução quando necessário.

---

## REGRA DE BENCHMARK

Artefatos maduros podem ser usados como benchmark para:

* padrões de arquitetura;
* organização estrutural;
* estilo de modelagem;
* estratégias de auditoria;
* desenho de nós e conduta;
* decisões de QA.

Eles não podem ser usados para:

* copiar lógica clínica entre especialidades;
* presumir perguntas, mensagens ou condutas sem ancoragem documental;
* justificar salto de fase;
* importar decisões clínicas automaticamente.

---

## REGRA DE RASTREABILIDADE

Toda decisão relevante deve ser rastreável a pelo menos uma destas fontes:

* instrução explícita do usuário;
* estado atual do ambiente (`HANDOFF.md` / `ESTADO.md`);
* sub-skill da fase ativa;
* documento técnico auxiliar aplicável;
* artefato válido da especialidade em produção.

Quando houver conflito, vale a ordem de autoridade definida em `AGENTE.md`.

---

## ENTRADAS E SAÍDAS POR FASE

### briefing-arquitetura

**Entrada:** briefing inicial, escopo ou pedido de nova frente
**Saída:** enquadramento e arquitetura inicial da especialidade

### ingestao-evidencias

**Entrada:** materiais brutos de evidência
**Saída:** base organizada para auditoria

### auditoria-banco

**Entrada:** banco ou base de evidências
**Saída:** base auditada para sustentar playbook

### redacao-playbook

**Entrada:** base auditada
**Saída:** playbook clínico estruturado

### auditoria-playbook

**Entrada:** playbook draftado
**Saída:** playbook auditado e decisão de gate

### codificacao-json

**Entrada:** playbook liberado
**Saída:** paper design, mapeamento técnico e JSON

### qa-entrega

**Entrada:** JSON consolidado
**Saída:** artefato final revisado para entrega

---

## REGRAS TRANSVERSAIS DO AMBIENTE

* O agente nunca deve pular fase por conveniência.
* O agente nunca deve produzir artefato final sem gate explícito.
* O agente deve preferir leitura mínima com máxima precisão.
* O agente deve tratar `HANDOFF.md` como estado operacional curto.
* O agente deve tratar `ESTADO.md` como snapshot canônico.
* O agente deve tratar `history/` como registro arquivístico, não como ponto de entrada primário.
* Frentes ativas devem operar em seus diretórios próprios.
* Referências maduras devem ser tratadas como read-only, salvo instrução contrária.

---

## REGRA FINAL

Este orchestrator responde a três perguntas:

1. quais fases existem;
2. quando ativar cada fase;
3. como as fases se conectam.

Ele não responde sozinho:

* onde estamos agora;
* qual sessão está em curso;
* qual override recente o usuário forneceu.

Essas respostas vêm de:

* `AGENTE.md`
* `HANDOFF.md`
* `ESTADO.md`
* instrução explícita do usuário

Use este arquivo para navegar o pipeline.
Use o estado do ambiente para decidir o próximo passo real.