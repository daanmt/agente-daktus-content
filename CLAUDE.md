# CLAUDE.md — agente-daktus-content

## INICIO OBRIGATORIO DE SESSAO

**Leia `ESTADO.md` antes de qualquer acao.** E a fonte de verdade do estado atual do projeto — fase, artefatos, proximos passos, decisoes criticas.

Apos ESTADO.md, siga a ordem de leitura indicada nele.

---

## Identidade dos agentes

| Agente | Foco |
|--------|------|
| **Antigravity** | Geracao de conteudo clinico, auditoria de evidencias, redacao de playbook, raciocinio longo |
| **Claude Code** | Git, scripts, validacao JSON, refatoracao estrutural, QA automatizado, operacoes de arquivo |

Para instrucoes detalhadas por agente:
- Claude Code: `tools/CLAUDECODE_KICKSTART.md`
- Antigravity: `tools/KICKSTART_PSIQUIATRIA.md`

---

## Protocolo de fim de sessao

Ao encerrar qualquer sessao (independente da ferramenta):

1. Atualizar `ESTADO.md` — fase atual, o que foi feito, proximo passo
2. Registrar `history/session_NNN.md` com log detalhado
3. Commit: `chore: atualiza ESTADO.md — YYYY-MM-DD [Claude Code / Antigravity]`
