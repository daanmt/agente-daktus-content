# AGENTE.md — BOOT DO AMBIENTE

Você está operando no ambiente daktus.

Este repositório é um ambiente de produção orientado por conhecimento, versionado em Git e projetado para ser portátil entre diferentes LLMs e interfaces. Seu trabalho não começa pela tarefa pedida; começa pela leitura correta do estado do ambiente.

---

## PRINCÍPIO CENTRAL

Assuma continuidade de projeto, não recomeço do zero.

Seu papel em cada sessão é:
1. localizar o estado atual;
2. confirmar a fase correta;
3. identificar o artefato-alvo da sessão;
4. ler apenas o necessário para esta fase;
5. executar um passo coerente no pipeline;
6. registrar a sessão e deixar o ambiente pronto para continuidade.

---

## ORDEM OBRIGATÓRIA DE LEITURA

Antes de qualquer ação:

1. Ler este arquivo por completo.
2. Ler `HANDOFF.md`, se existir.
3. Ler `ESTADO.md`.
4. Ler `SKILL.md` apenas para situar o pipeline e identificar a fase correta.
5. Ler apenas os arquivos da fase atual e da especialidade/tema em foco.
6. Ler `history/session_XXX.md` mais recente apenas se necessário para continuidade fina.

### Fallback
Se `HANDOFF.md` não existir, use `ESTADO.md` como fallback operacional e prossiga sem travar.

---

## ORDEM DE AUTORIDADE

Quando houver conflito entre fontes, siga esta ordem:

1. instrução explícita do usuário nesta sessão;
2. `HANDOFF.md`;
3. `ESTADO.md`;
4. `SKILL.md`;
5. documentos específicos da fase;
6. histórico em `history/`.

Nunca trate um snapshot potencialmente desatualizado como mais forte do que uma atualização explícita do usuário.

---

## O QUE VOCÊ PRECISA DESCOBRIR NO INÍCIO DE CADA SESSÃO

Antes de executar qualquer tarefa, responda internamente:

- Qual é a especialidade ou tema ativo?
- Em que fase do pipeline estamos?
- Qual é o artefato de entrada desta sessão?
- Qual é o artefato de saída desta sessão?
- Quais arquivos são fonte de verdade para esta fase?
- O que está proibido fazer agora?
- Qual é o critério de encerramento da sessão?
- Qual é o branch-base oficial para esta continuidade?

---

## REGRAS INVARIÁVEIS

- Não pular fase por inferência.
- Não abrir leitura indiscriminada do repositório.
- Não produzir artefato final sem confirmar que a fase está liberada.
- Não sobrescrever estado operacional sem atualizar os artefatos de continuidade.
- Não tratar histórico como fonte primária se o estado atual já estiver consolidado em `HANDOFF.md` ou `ESTADO.md`.
- Não avançar em mudanças clínicas novas sem respaldo documental ou autorização explícita do usuário.
- Sempre preferir leitura mínima com alta precisão.
- Toda sessão significativa deve terminar com atualização dos artefatos de continuidade.

---

## PROTOCOLO DE ABERTURA DE SESSÃO

1. Identificar especialidade ou tema ativo.
2. Confirmar fase atual.
3. Confirmar branch-base ou estado de integração vigente.
4. Identificar artefato de entrada e artefato de saída.
5. Ler apenas os arquivos necessários para a fase.
6. Declarar sucintamente o plano da sessão.
7. Executar.

---

## PROTOCOLO DE FECHAMENTO DE SESSÃO

Ao final de toda sessão significativa:

1. Resumir o que foi produzido.
2. Atualizar `HANDOFF.md`.
3. Atualizar `ESTADO.md` se o snapshot canônico mudou.
4. Registrar `history/session_NNN.md`.
5. Deixar explícito o próximo passo recomendado.
6. Realizar commit de sessão quando aplicável.

---

## REGRA DE PROGRESSIVE DISCLOSURE

Você nunca deve carregar todas as skills e todos os documentos do repositório de uma vez.

Leia o mínimo necessário para operar com precisão na fase atual.

- `AGENTE.md` resolve boot.
- `HANDOFF.md` resolve continuidade operacional.
- `ESTADO.md` resolve snapshot canônico.
- `SKILL.md` resolve arquitetura do pipeline.
- sub-skills resolvem execução específica da fase.

---

## REGRA DE OVERRIDE DO USUÁRIO

Se o usuário informar explicitamente que:
- uma fase mudou,
- um artefato foi aprovado,
- um gate foi liberado,
- uma decisão operacional recente ainda não foi refletida nos arquivos,

trate isso como atualização prioritária.

Nesses casos:
1. registre mentalmente a divergência;
2. prossiga com base na instrução mais recente do usuário;
3. recomende atualizar `HANDOFF.md` e `ESTADO.md` ao final.

---

## REGRA DE CONTINUIDADE MULTIAGENTE

Este ambiente pode ser operado por diferentes agentes e interfaces sobre a mesma pasta local.

Por isso:
- não assuma contexto conversacional prévio;
- assuma que o handoff deve estar no repositório;
- prefira decisões explícitas e rastreáveis;
- trate cada sessão como uma transação de conhecimento.

---

## SAÍDA ESPERADA DE UMA BOA SESSÃO

Uma boa sessão deixa o ambiente:
- mais claro do que estava no início;
- com menos ambiguidade operacional;
- com rastreabilidade preservada;
- pronto para o próximo agente continuar com o mínimo de atrito.