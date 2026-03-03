# ESTADO — agente-daktus-content (Psiquiatria)
*Atualizado: 2026-03-03 (sessao 007) | Ferramenta: Claude Code (Sonnet 4.6)*

---

## O que é este projeto

Pipeline de produção de fichas clínicas Daktus/Amil. Stage 1 do pipeline: gera o playbook clínico e o JSON da ficha. Stage 2 (validação automatizada) é o repositório `agente-daktus-qa`. O projeto atual é a **Ficha de Psiquiatria** — o produto mais recente da série Reumato → Cardio → Gine → **Psiquiatria**.

---

## Fase atual

**Fase 3 — Revisão Clínica Humana** | Status: Aguardando

O playbook v1.0 está completo. Aguardando revisão de Dan antes de avançar para Fase 4 (codificacao-json).

Próxima ação após revisão: abrir `tools/skills/codificacao-json/SKILL.md` e usar `jsons/amil-ficha_ginecologia-vdraft.json` como referência UX para a ficha de psiquiatria.

---

## Artefatos existentes (mapa completo)

| Artefato | Arquivo | Status |
|----------|---------|--------|
| Banco de evidências | `research/BANCO_EVIDENCIAS_PSIQUIATRIA.md` | ✅ v3.0 — 412 REFs, 266 AFIs |
| Auditoria do banco | `research/AUDITORIA_MASTER.md` | ✅ consolidado (373 linhas) |
| Playbook | `playbooks/playbook_psiquiatria.md` | ✅ v1.0 — 645 linhas, aguarda revisão |
| JSON Psiquiatria | `jsons/` | ⏳ não iniciado |
| Sub-skills (7) | `tools/skills/*/SKILL.md` | ✅ no local canônico |
| Orchestrator | `SKILL.md` | ✅ inclui regras multi-agente |
| Relatórios OE | `research/OE_RELATORIO_01..10.md` | ✅ 10 relatórios ingeridos |
| JSON ref — Ginecologia | `jsons/amil-ficha_ginecologia-vdraft.json` | ✅ referencia UX ativa |
| Auditoria JSON Ginecologia | `research/AUDITORIA_JSON_GINECOLOGIA.md` | ✅ sessao 007 — 14 achados, aguarda feedback Dan |
| JSON ref — Cardiologia | `jsons/amil-ficha_cardiologia-v2.0.9.json` | ✅ referência |
| JSON ref — Reumatologia | `jsons/inclua-ficha_reumatologia-v1.1.0.json` | ✅ referência |
| Inteligência cross-projeto | `tools/INTELIGENCIA_CONSOLIDADA_REUMATO_CARDIO.md` | ✅ base para psiquiatria |

---

## Última sessão

**2026-03-03 | Claude Code (sessao 007):** Auditoria de qualidade do JSON da ficha de ginecologia (`amil-ficha_ginecologia-vdraft.json`) vs playbook. Extraiu estrutura completa (8 nos, 7 clinicalExpressions, 38 exames, 23 meds, 17 enc, 20 msgs). Identificou 6 achados criticos e 8 moderados/estruturais. Documento entregue: `research/AUDITORIA_JSON_GINECOLOGIA.md`. Aguardando feedback de Dan em cada achado.

**2026-03-01 | Claude Code (sessao 006):** Auditoria de infraestrutura — moveu 7 sub-skills do caminho errado para `tools/skills/`, limpou `tools/`, arquivou logs de chat em `history/`, criou `tools/CLAUDECODE_KICKSTART.md` e secao multi-agente em `SKILL.md`. Identificou 3 artefatos fantasma (nunca exportados do chat Antigravity) — confirmado que `AUDITORIA_MASTER.md` e a consolidacao oficial.

---

## Próximos passos (em ordem)

1. **[Dan]** Revisar `playbooks/playbook_psiquiatria.md` — aprovação clínica ou lista de correções
2. **[Agente]** Fase 4 — codificação JSON: abrir `tools/skills/codificacao-json/SKILL.md`
3. **[Agente]** Fase 5 — QA: `tools/skills/qa-entrega/SKILL.md` (28 checks)
4. **[Agente]** Após entrega: extrair inteligência psiquiatria → atualizar `INTELIGENCIA_CONSOLIDADA_*.md`

---

## Decisões críticas (não reverter sem contexto)

- **Playbook organizado por classe farmacológica**, não por síndrome — decisão deliberada para facilitar prescrição cruzada
- **AUDITORIA_MASTER.md é a consolidação oficial** dos relatórios de auditoria — não criar novos sem arquivar o master
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
