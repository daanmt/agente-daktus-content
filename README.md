# ambiente daktus

Pipeline lean de produção clínica estruturada, operado por estado, versionamento e continuidade entre agentes.

Este repositório foi desenhado para funcionar como um ambiente portátil de trabalho sobre a mesma pasta local, permitindo continuidade entre diferentes chats, diferentes modelos e diferentes sessões sem depender de memória conversacional.

---

## VISÃO GERAL

O ambiente daktus organiza a produção de artefatos clínicos estruturados por fases, com rastreabilidade documental e transições controladas entre etapas.

A lógica central do ambiente é simples:

- o estado do trabalho precisa viver no repositório;
- o agente não deve começar pela tarefa, e sim pelo estado;
- cada sessão deve executar apenas o próximo passo coerente;
- a continuidade precisa ser explícita, curta e legível.

---

## COMO ENTRAR NO AMBIENTE

Toda nova sessão deve começar por esta ordem:

1. `AGENTE.md`
2. `HANDOFF.md`
3. `ESTADO.md`
4. `SKILL.md`
5. sub-skill da fase atual

Não comece lendo o repositório inteiro.
Não comece pela tarefa pedida.
Comece localizando o estado atual.

---

## ARQUITETURA DOS ARQUIVOS-MESTRE

### `AGENTE.md`
Ponto único de entrada.

Define:
- ordem obrigatória de leitura;
- ordem de autoridade entre fontes;
- protocolo de abertura e fechamento de sessão;
- regras invariáveis do ambiente;
- lógica de continuidade multiagente.

### `HANDOFF.md`
Estado operacional curto.

Registra:
- frente ativa;
- fase atual;
- artefato em produção;
- próximo passo recomendado;
- pendências imediatas;
- overrides recentes do usuário.

### `ESTADO.md`
Snapshot canônico do ambiente.

Consolida:
- visão estável do estado atual;
- branch-base oficial;
- decisões críticas vigentes;
- frentes ativas;
- próximo passo macro.

### `CLAUDE.md`
Bootstrap mínimo.

Existe apenas para redirecionar corretamente o agente para `AGENTE.md` e reforçar as regras básicas de entrada e fechamento.

### `SKILL.md`
Orchestrator do pipeline.

Descreve:
- as fases do pipeline;
- as sub-skills disponíveis;
- quando cada uma deve ser ativada;
- as regras de gate entre fases.

---

## ESTRUTURA DO AMBIENTE

```text
/
├── AGENTE.md               # boot do ambiente
├── HANDOFF.md              # estado operacional curto
├── ESTADO.md               # snapshot canônico
├── CLAUDE.md               # bootstrap mínimo
├── SKILL.md                # orchestrator do pipeline
├── README.md               # visão geral estável
│
├── tools/
│   ├── skills/             # sub-skills por fase
│   └── *.md                # padrões, guardrails e documentos auxiliares
│
├── especialidades/         # frentes ativas em produção
├── referencia/             # artefatos maduros / read-only
├── history/                # registro de sessões
└── scripts/                # automações e validações
````

A estrutura exata pode evoluir, mas a separação de responsabilidades entre os arquivos-mestre deve permanecer estável.

---

## PIPELINE CANÔNICO

O ambiente opera sobre um pipeline por fases.

```text
briefing-arquitetura
→ ingestao-evidencias
→ auditoria-banco
→ redacao-playbook
→ auditoria-playbook
→ codificacao-json
→ qa-entrega
```

A regra principal é:

* não pular fase;
* não avançar sem gate liberado;
* não produzir artefato final sem base anterior consolidada.

Iteração é permitida dentro da fase.
Salto de fase não é.

---

## PRINCÍPIOS OPERACIONAIS

### 1. State-driven, não chat-driven

O estado real do trabalho deve estar documentado no repositório, não espalhado em memória de conversa.

### 2. Progressive disclosure

O agente deve ler o mínimo necessário para operar com precisão na fase atual.

### 3. Continuidade multiagente

O ambiente deve poder ser retomado por outro agente sem depender de contextualização longa.

### 4. Rastreabilidade

Toda decisão relevante deve ser ancorada em:

* instrução explícita do usuário,
* estado do ambiente,
* sub-skill ativa,
* documento técnico aplicável,
* artefato válido da especialidade.

### 5. Lean infrastructure

Arquivos estáveis não devem carregar estado volátil.
Estado operacional curto deve ficar em `HANDOFF.md`.
Snapshot canônico deve ficar em `ESTADO.md`.

---

## COMO O AGENTE DEVE OPERAR

Em cada sessão, o agente deve:

1. localizar a especialidade ou tema ativo;
2. identificar a fase atual;
3. confirmar o artefato de entrada;
4. confirmar o artefato de saída esperado;
5. abrir apenas a sub-skill da fase ativa;
6. executar o próximo passo coerente;
7. registrar continuidade ao final.

Sessões boas são sessões que deixam o ambiente:

* mais claro,
* menos ambíguo,
* mais fácil de retomar,
* melhor preparado para o próximo passo.

---

## REFERÊNCIAS E FRENTES ATIVAS

O ambiente pode conter dois tipos de material:

### Frentes ativas

Ficam em diretórios de trabalho, como `especialidades/`.

São materiais em produção, sujeitos a revisão, integração e evolução.

### Referências maduras

Ficam em `referencia/`.

Servem para:

* benchmark estrutural;
* padrões de arquitetura;
* exemplos de modelagem;
* histórico de decisões bem sucedidas.

Não devem ser tratadas como autorização automática para copiar lógica clínica entre especialidades.

---

## OPERAÇÃO MULTIAGENTE

Este ambiente foi pensado para funcionar com diferentes agentes e interfaces, desde que todos respeitem o mesmo boot e a mesma ordem de autoridade.

Isso inclui, por exemplo:

* Claude
* GPT
* interfaces de chat
* agentes acoplados ao repositório
* fluxos locais com Git

A memória compartilhada do trabalho não é a conversa anterior.
É o conjunto formado por:

* `AGENTE.md`
* `HANDOFF.md`
* `ESTADO.md`
* `SKILL.md`
* `history/`
* os artefatos da especialidade ativa

---

## FILOSOFIA DO AMBIENTE

Menos improviso.
Mais boot disciplinado.

Menos leitura indiscriminada.
Mais leitura orientada por fase.

Menos contexto bruto repetido a cada sessão.
Mais continuidade explícita no repositório.

Menos dependência do agente certo.
Mais previsibilidade do ambiente.

---

## REGRA PRÁTICA FINAL

Se você for um agente entrando neste repositório:

* não tente entender tudo de uma vez;
* não comece pela tarefa;
* não suponha a fase;
* não abra todas as skills;
* não use histórico como ponto de entrada principal.

Leia `AGENTE.md`.
Localize o estado.
Siga a fase correta.
Execute apenas o próximo passo coerente.