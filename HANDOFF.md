# HANDOFF.md — ESTADO OPERACIONAL CURTO
*Atualizado: 2026-03-07 — sessão de refatoração estrutural concluída*

---

## ESTADO OPERACIONAL ATUAL

- Branch-base: `main`
- Última sessão integrada: refatoração estrutural lean do ambiente daktus
- Especialidade/tema ativo: Psiquiatria
- Fase atual: **Fase 4 — codificação JSON** (pronta para início)
- Artefato em produção: nenhum — refatoração encerrada, JSON aguarda início

---

## O QUE JÁ ESTÁ INTEGRADO (esta sessão)

- `AGENTE.md` definido como ponto único de entrada — commitado e pushado
- `HANDOFF.md` instituído como estado operacional curto — commitado e pushado
- `ESTADO.md` reposicionado como snapshot canônico — commitado e pushado
- `CLAUDE.md` reduzido a bootstrap mínimo — commitado e pushado
- `SKILL.md` reposicionado como orchestrator, rotina de sessão lean — commitado e pushado
- `tools/AGENT_PROMPT_PROTOCOLO_DAKTUS.md` — linguagem de entrada removida, escopo correto
- 7 sub-skills — precondição de boot adicionada em todas
- Branch-base corrigido: `integration/agent` → `main`
- Commit: `8f0aa17` | Push: `origin/main` ✅

---

## O QUE ESTÁ ABERTO AGORA

- Nenhum bloqueio ativo.
- Próxima ação: iniciar **Fase 4 — codificação JSON de Psiquiatria**.

---

## PRÓXIMO PASSO RECOMENDADO

1. Abrir `tools/skills/codificacao-json/SKILL.md`
2. Iniciar com **paper design** — topologia de nós antes de qualquer JSON
3. Consultar benchmark: `especialidades/ginecologia/jsons/amil-ficha-ginecologia-v1.0.0.json`
4. Consultar playbook aprovado: `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md`

---

## ARQUIVOS A LER NA PRÓXIMA SESSÃO

1. `AGENTE.md`
2. `HANDOFF.md`
3. `ESTADO.md` (se precisar de contexto completo)
4. `SKILL.md`
5. `tools/skills/codificacao-json/SKILL.md`
6. `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md`
7. `especialidades/ginecologia/jsons/amil-ficha-ginecologia-v1.0.0.json` (referência UX)

---

## NÃO SOBRESCREVER SEM REVISAR

- fase atual de Psiquiatria (Fase 4 — JSON)
- branch-base: `main`
- papel de Ginecologia como benchmark estrutural (não copiar lógica clínica)
- separação entre `HANDOFF.md` e `ESTADO.md`
- centralidade de `AGENTE.md` como ponto de entrada

---

## DIVERGÊNCIAS / OVERRIDES

- `especialidades/psiquiatria/RELATORIO_PROCESSO.md` contém referência histórica a "Daktus/Amil" — mantida por contexto de relatório, não é arquivo operacional.
- Worktrees antigos em `.claude/worktrees/` são diretórios locais ignorados pelo Git (`.gitignore`). Não representam estado de trabalho ativo.
