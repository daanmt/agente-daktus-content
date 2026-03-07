# CLAUDE.md — BOOTSTRAP OPERACIONAL

Antes de qualquer ação, leia `AGENTE.md`.

Este arquivo não substitui `AGENTE.md`.
Ele existe apenas para garantir que qualquer agente entre no ambiente pelo ponto correto, com o menor atrito possível.

---

## SEQUÊNCIA OBRIGATÓRIA

1. Ler `AGENTE.md`.
2. Seguir a ordem de leitura definida nele.
3. Respeitar a ordem de autoridade definida nele.
4. Ler apenas os arquivos necessários para a fase atual.
5. Executar apenas o próximo passo coerente no pipeline.

---

## PREFLIGHT OPERACIONAL

Antes de executar a tarefa da sessão, confirmar:

- especialidade ou tema ativo;
- fase atual do pipeline;
- artefato de entrada;
- artefato de saída esperado;
- branch-base oficial ou estado de integração vigente;
- existência de override recente do usuário que tenha prioridade sobre snapshots antigos.

Se houver conflito entre documentação antiga e instrução explícita do usuário, siga a ordem de autoridade definida em `AGENTE.md`.

---

## INVARIANTES

- Não pular fase.
- Não produzir artefato final sem gate liberado.
- Não ler o repositório inteiro sem necessidade.
- Não ignorar `HANDOFF.md` e `ESTADO.md`.
- Não usar histórico como ponto de entrada principal quando o estado atual já estiver consolidado.
- Não encerrar a sessão sem registrar continuidade.

---

## REGRA DE EXECUÇÃO

Este ambiente é state-driven.

Isso significa:
- a tarefa não deve ser executada antes da leitura do estado;
- a fase não deve ser presumida;
- a leitura deve ser mínima, orientada pela fase atual;
- o agente deve operar como continuidade de projeto, não como recomeço do zero.

---

## FECHAMENTO DE SESSÃO

Ao final de toda sessão significativa:

1. Atualizar `HANDOFF.md`.
2. Atualizar `ESTADO.md` se o estado canônico tiver mudado.
3. Registrar `history/session_NNN.md`.
4. Deixar claro o próximo passo recomendado.
5. Commitar, quando aplicável.

---

## REGRA FINAL

Se você entrou neste repositório por `CLAUDE.md`, seu próximo passo é `AGENTE.md`.

Não improvise o boot.
Não comece pela tarefa.
Comece pelo estado.