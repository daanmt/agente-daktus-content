# ESTADO — agente-daktus-content
*Atualizado: 2026-03-03 (sessao 009) | Ferramenta: Claude Code (Opus 4.6)*

---

## O que e este projeto

**Pipeline agnostico de especialidade** para producao de fichas clinicas Daktus/Amil. Stage 1: gera playbook clinico + JSON da ficha. Stage 2 (validacao automatizada): repositorio `agente-daktus-qa`.

Especialidades entregues: Reumatologia, Cardiologia. Em desenvolvimento: Ginecologia (auditoria JSON), Psiquiatria (Fase 3). Especialidades em andamento ficam em `especialidades/{nome}/`. O metodo (skills, scripts, padroes JSON) e agnostico e reutilizavel.

---

## Fase atual

**Duas frentes paralelas:**

**[Ginecologia — Auditoria JSON]** Sessao 008 concluida | Status: Aguardando Dan aplicar correcoes
- Auditoria do vdraft2 em `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md`
- 4 criticos pendentes (C1: formula espessamento OR quebrada; C2-C4: expressoes sem `is True`)
- 4 importantes pendentes (I1: LSIL; I2: citologia preselected; I3: hpv_resultado_nd; I4: diu_contraindicacao)
- 1 sugestao de nova pergunta: `historia_familiar_ca` em N1

**[Psiquiatria]** Fase 3 — Revisao Clinica Humana | Status: Aguardando Dan
- Playbook v1.0 completo em `especialidades/psiquiatria/playbooks/`
- Proximo passo pos-revisao: `tools/skills/codificacao-json/SKILL.md`

---

## Artefatos existentes (mapa completo)

| Artefato | Arquivo | Status |
|----------|---------|--------|
| **Ginecologia** | | |
| Auditoria JSON Gine | `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md` | Sessao 008 — aguarda Dan aplicar C1-C4 |
| Playbook Gine | `especialidades/ginecologia/playbooks/playbook_ginecologia_auditado.md` | v1.0 auditado |
| JSON Gine (vdraft) | `especialidades/ginecologia/jsons/amil-ficha_ginecologia-vdraft.json` | vdraft1 — vdraft2 nao esta no repo |
| Sessions Gine | `especialidades/ginecologia/history/session_007.md, session_008.md` | completos |
| **Psiquiatria** | | |
| Banco de evidencias | `especialidades/psiquiatria/research/BANCO_EVIDENCIAS_PSIQUIATRIA.md` | v3.0 — 412 REFs, 266 AFIs |
| Playbook Psy | `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md` | v1.0 — aguarda revisao |
| JSON Psiquiatria | `especialidades/psiquiatria/jsons/` | nao iniciado |
| Sessions Psy | `especialidades/psiquiatria/history/session_001..006.md` | completos |
| **Metodo (agnostico)** | | |
| Orchestrator | `SKILL.md` | agnostico |
| Sub-skills (7) | `tools/skills/*/SKILL.md` | agnosticos |
| Padroes arquitetura JSON | `tools/PADROES_ARQUITETURA_JSON.md` | agnostico |
| Kickstart template | `tools/KICKSTART_NOVA_ESPECIALIDADE.md` | agnostico |
| Scripts | `scripts/validate_json.py, audit_references.py, audit_logic.py, versionar.py` | agnosticos |
| **Referencia (fichas entregues)** | | |
| JSON Cardiologia | `jsons/amil-ficha_cardiologia-v2.0.9.json` | referencia |
| JSON Reumatologia | `jsons/inclua-ficha_reumatologia-v1.1.0.json` | referencia |
| Playbook Cardiologia | `playbooks/Playbook Clinico — Ficha de Cardiologia...` | referencia |
| Playbook Reumatologia | `playbooks/playbook_reumatologia.md` | referencia |

---

## Ultimas sessoes

**2026-03-03 | Claude Code Opus (sessao 009):** Consolidacao de infraestrutura — diagnosticou divergencia worktree/main, resgatou `audit_logic.py`, criou `especialidades/ginecologia/` e moveu 4 artefatos para la, criou session_008 (retroativo) e session_009, atualizou ESTADO.md e READMEs. Worktrees stale identificados para remocao manual.

**2026-03-03 | Claude Code Sonnet (sessao 008):** Auditoria atualizada para vdraft2 — marcou 8 resolucoes, adicionou 4 criticos novos (formula espessamento OR quebrada + 3 expressoes sem `is True`), sugestao de nova pergunta `historia_familiar_ca`. Refatoracao: psiquiatria movida para `especialidades/`, tools files renomeados para nomes agnosticos.

**2026-03-03 | Claude Code Sonnet (sessao 007):** Auditoria inicial do vdraft1 — 6 criticos, 8 moderados/estruturais.

**2026-03-01 | Claude Code Sonnet (sessao 006):** Auditoria de infraestrutura — skills movidos, tools limpos, logs arquivados.

---

## Proximos passos (em ordem)

**[Ginecologia JSON]**
1. **[Dan]** Aplicar C1: restaurar formula `espessamento_endometrial_significativo` com menopausa gate e parenteses corretos
2. **[Dan]** Aplicar C2-C4: adicionar `is True` em `espessamento`, `trh_indicada`, `alto_risco_mama` (todos os usos bare)
3. **[Dan]** Decidir I1: LSIL → colposcopia imediata ou repetir citologia em 1 ano
4. **[Dan]** Adicionar pergunta `historia_familiar_ca` em N1 (ver proposta na auditoria)

**[Psiquiatria]**
5. **[Dan]** Revisar `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md`
6. **[Agente]** Fase 4 — codificacao JSON: `tools/skills/codificacao-json/SKILL.md`

**[Infraestrutura]**
7. **[Dan]** Remover worktrees stale apos encerrar sessao Claude Code:
   ```bash
   cd C:\Users\daanm\Daktus\agente-daktus-content
   git worktree remove .claude/worktrees/thirsty-chatelet --force
   git worktree remove .claude/worktrees/suspicious-zhukovsky --force
   git branch -d claude/thirsty-chatelet
   ```

---

## Decisoes criticas (nao reverter sem contexto)

- **Playbook organizado por classe farmacologica**, nao por sindrome — facilita prescricao cruzada
- **AUDITORIA_MASTER_{ESP}.md e consolidacao oficial** de cada especialidade — em `especialidades/{nome}/research/`
- **Fase 2 de auditoria do banco antecipada** (antes do playbook) — banco inflado contamina playbook
- **Antigravity = conteudo clinico; Claude Code = estrutura/scripts/git** — nao misturar papeis
- **Nunca avancar de fase sem aprovacao explicita do Dan**
- **Sessions numeradas globalmente** — nao por especialidade. Sessions de especialidade ficam em `especialidades/{nome}/history/`, sessions transversais em `history/`
- **Expressoes do summary sempre com `is True`** nas condicionais de conduta (nao bare)

---

## Para retomar: leia nesta ordem

1. **Este arquivo** (ESTADO.md) — onde estamos
2. `SKILL.md` — pipeline geral e regras de comportamento
3. `tools/skills/{fase-atual}/SKILL.md` — instrucao da fase em execucao
4. Sessao mais recente da especialidade em foco:
   - Ginecologia: `especialidades/ginecologia/history/session_008.md`
   - Psiquiatria: `especialidades/psiquiatria/history/session_006.md`
5. Auditoria ativa (se aplicavel): `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md`
6. Banco de evidencias (se a tarefa toca conteudo clinico): `especialidades/{nome}/research/BANCO_EVIDENCIAS_*.md`

---

## Contexto do repositorio

```
GitHub: github.com/daanmt/agente-daktus-content   (Stage 1 — este repo)
Stage 2: github.com/daanmt/agente-daktus-qa        (validacao automatizada)
Local:   C:\Users\daanm\Daktus\agente-daktus-content
```

*Ao final de cada sessao: atualizar este arquivo e fazer commit `chore: atualiza ESTADO.md — YYYY-MM-DD [ferramenta]`*
