# ESTADO — agente-daktus-content
*Atualizado: 2026-03-03 (sessao 007) | Ferramenta: Claude Code (Sonnet 4.6)*

---

## O que é este projeto

**Pipeline agnóstico de especialidade** para producao de fichas clinicas Daktus/Amil. Stage 1: gera playbook clinico + JSON da ficha. Stage 2 (validacao automatizada): repositorio `agente-daktus-qa`.

Especialidades entregues: Reumatologia, Cardiologia, Ginecologia. Em producao: Psiquiatria (Fase 3). Especialidades em andamento ficam em `especialidades/{nome}/`. O metodo (skills, scripts, padroes JSON) e agnóstico e reutilizavel.

---

## Fase atual

**Dois frentes paralelas:**

**[Psiquiatria]** Fase 3 — Revisao Clinica Humana | Status: Aguardando Dan
- Playbook v1.0 completo em `especialidades/psiquiatria/playbooks/`
- Proximo passo pos-revisao: `tools/skills/codificacao-json/SKILL.md`

**[Ginecologia — Auditoria JSON]** Sessao 008 concluida | Status: Aguardando Dan aplicar correcoes
- Auditoria do vdraft2 em `research/AUDITORIA_JSON_GINECOLOGIA.md`
- 4 criticos pendentes (C1-C4, todos sobre `is True` e formula espessamento)
- 1 sugestao de nova pergunta: `historia_familiar_ca` em N1

---

## Artefatos existentes (mapa completo)

| Artefato | Arquivo | Status |
|----------|---------|--------|
| Banco de evidencias (Psy) | `especialidades/psiquiatria/research/BANCO_EVIDENCIAS_PSIQUIATRIA.md` | ✅ v3.0 — 412 REFs, 266 AFIs |
| Playbook (Psy) | `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md` | ✅ v1.0 — aguarda revisao |
| JSON Psiquiatria | `especialidades/psiquiatria/jsons/` | ⏳ nao iniciado |
| Sub-skills (7) | `tools/skills/*/SKILL.md` | ✅ agnósticos |
| Orchestrator | `SKILL.md` | ✅ agnóstico |
| Padroes arquitetura JSON | `tools/PADROES_ARQUITETURA_JSON.md` | ✅ agnóstico (ex-Reumato/Cardio) |
| Kickstart template | `tools/KICKSTART_NOVA_ESPECIALIDADE.md` | ✅ agnóstico |
| Auditoria JSON Ginecologia | `research/AUDITORIA_JSON_GINECOLOGIA.md` | ✅ sessao 008 — aguarda Dan aplicar C1-C4 |
| JSON ref — Ginecologia | `jsons/amil-ficha_ginecologia-vdraft.json` | ✅ referencia ativa |
| JSON ref — Cardiologia | `jsons/amil-ficha_cardiologia-v2.0.9.json` | ✅ referencia |
| JSON ref — Reumatologia | `jsons/inclua-ficha_reumatologia-v1.1.0.json` | ✅ referencia |

---

## Última sessão

**2026-03-03 | Claude Code (sessao 008):** Auditoria atualizada para vdraft2 — marcou 8 resolucoes, adicionou 4 criticos novos (todos sobre `is True` sem booleano e formula espessamento OR quebrada), sugestao de nova pergunta `historia_familiar_ca` em N1. Refatoracao estrutural do repo: artefatos de psiquiatria movidos para `especialidades/psiquiatria/`, tools files renomeados para nomes agnosticos.

**2026-03-03 | Claude Code (sessao 007):** Auditoria inicial do vdraft1 — 6 criticos, 8 moderados/estruturais. Documento criado em `research/AUDITORIA_JSON_GINECOLOGIA.md`.

**2026-03-01 | Claude Code (sessao 006):** Auditoria de infraestrutura — moveu 7 sub-skills do caminho errado para `tools/skills/`, limpou `tools/`, arquivou logs de chat em `history/`, criou `tools/CLAUDECODE_KICKSTART.md` e secao multi-agente em `SKILL.md`. Identificou 3 artefatos fantasma (nunca exportados do chat Antigravity) — confirmado que `AUDITORIA_MASTER.md` e a consolidacao oficial.

---

## Próximos passos (em ordem)

**[Ginecologia JSON]**
1. **[Dan]** Aplicar C1: restaurar formula `espessamento_endometrial_significativo` com menopausa gate
2. **[Dan]** Aplicar C2-C4: adicionar `is True` em `espessamento`, `trh_indicada`, `alto_risco_mama` (todos os usos bare)
3. **[Dan]** Decidir I1: LSIL → colposcopia imediata ou repetir citologia em 1 ano
4. **[Dan]** Adicionar pergunta `historia_familiar_ca` em N1 (ver proposta na auditoria)

**[Psiquiatria]**
5. **[Dan]** Revisar `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md`
6. **[Agente]** Fase 4 — codificacao JSON: `tools/skills/codificacao-json/SKILL.md`

---

## Decisões críticas (não reverter sem contexto)

- **Playbook organizado por classe farmacológica**, não por síndrome — decisão deliberada para facilitar prescrição cruzada
- **AUDITORIA_MASTER_{ESPECIALIDADE}.md e a consolidacao oficial** dos relatorios de auditoria de cada especialidade — fica em `especialidades/{nome}/research/`
- **Fase 2* de auditoria do banco antecipada** (antes do playbook) — banco inflado contamina o playbook
- **Antigravity = conteúdo clínico; Claude Code = estrutura/scripts/git** — não misturar papéis
- **Nunca avançar de fase sem aprovação explícita do Dan**

---

## Para retomar: leia nesta ordem

1. **Este arquivo** (ESTADO.md) — onde estamos
2. `SKILL.md` — pipeline geral e regras de comportamento
3. `tools/skills/{fase-atual}/SKILL.md` — instrução da fase em execução
4. `history/session_007.md` — ultima sessao detalhada (Claude Code, auditoria ginecologia)
5. `research/AUDITORIA_JSON_GINECOLOGIA.md` — auditoria do JSON da ginecologia (com espacos para feedback)
6. `history/session_006.md` — sessao anterior (infraestrutura)
5. `research/BANCO_EVIDENCIAS_PSIQUIATRIA.md` — se a tarefa toca conteúdo clínico

---

## Contexto do repositório

```
GitHub: github.com/daanmt/agente-daktus-content   (Stage 1 — este repo)
Stage 2: github.com/daanmt/agente-daktus-qa        (validação automatizada)
Local:   C:\Users\daanm\Daktus\agente-daktus-content
```

*Ao final de cada sessão: atualizar este arquivo e fazer commit `chore: atualiza ESTADO.md — YYYY-MM-DD [ferramenta]`*
