# ESTADO — agente-daktus-content
*Atualizado: 2026-03-04 (sessao 011) | Ferramenta: Claude Code (Opus 4.6)*

---

## O que e este projeto

**Pipeline agnostico de especialidade** para producao de fichas clinicas Daktus/Amil. Stage 1: gera playbook clinico + JSON da ficha. Stage 2 (validacao automatizada): repositorio `agente-daktus-qa`.

Especialidades entregues: Reumatologia, Cardiologia (em `referencia/`). Em desenvolvimento: Ginecologia (auditoria v1.0.0), Psiquiatria (Fase 3). Especialidades em andamento ficam em `especialidades/{nome}/`.

---

## Fase atual

**Duas frentes paralelas:**

**[Ginecologia — Auditoria v1.0.0]** Sessao 011 concluida | Status: 8 correcoes criticas pendentes
- Auditoria atualizada em `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md`
- JSON v1.0.0 versionado em `especialidades/ginecologia/jsons/amil-ficha-ginecologia-v1.0.0.json`
- **Resolvidos (v1.0.0):** C1 (espessamento formula), I1 (LSIL conservador), I2 (preselected removido), hemograma ampliado, creatinina adicionada
- **Criticos pendentes:** 7 usos bare de clinicalExpressions (is True), 1 typo `seletec_any` na DXA
- **Moderados pendentes:** 3 bare na orientacao cervical, CID creatinina incorreto
- **Feedback Gabriel:** ficha aprovada no geral; teste final pendente

**[Psiquiatria]** Fase 3 — Revisao Clinica Humana | Status: Aguardando Dan
- Playbook v1.0 em `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md`
- Proximo passo pos-revisao: `tools/skills/codificacao-json/SKILL.md`

---

## Artefatos existentes

### Metodo (agnostico)
| Artefato | Arquivo |
|----------|---------|
| Orchestrator | `SKILL.md` |
| Sub-skills (7) | `tools/skills/*/SKILL.md` |
| Instrucoes JSON | `tools/AGENT_PROMPT_PROTOCOLO_DAKTUS.md` |
| Padroes arquitetura | `tools/PADROES_ARQUITETURA_JSON.md` |
| Template kickstart | `tools/KICKSTART_NOVA_ESPECIALIDADE.md` |
| Guardrail evidencias | `tools/GUARDRAIL_EVIDENCIAS.md` |
| Contexto ferramentas | `tools/CONTEXTO_FERRAMENTAS_E_METODOS.md` |
| Scripts QA | `scripts/validate_json.py, audit_references.py, audit_logic.py, versionar.py` |

### Ginecologia
| Artefato | Arquivo | Status |
|----------|---------|--------|
| Auditoria JSON | `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md` | v1.0.0 — 8 criticos + 3 moderados pendentes |
| Playbook | `especialidades/ginecologia/playbooks/playbook_ginecologia_auditado.md` | v1.0 auditado |
| JSON v1.0.0 | `especialidades/ginecologia/jsons/amil-ficha-ginecologia-v1.0.0.json` | Atualizado por Gabriel + Dan |
| JSON vdraft | `especialidades/ginecologia/jsons/amil-ficha_ginecologia-vdraft.json` | Versao anterior (referencia) |

### Psiquiatria
| Artefato | Arquivo | Status |
|----------|---------|--------|
| Banco evidencias | `especialidades/psiquiatria/research/BANCO_EVIDENCIAS_PSIQUIATRIA.md` | v3.0 — 412 REFs, 266 AFIs |
| Auditoria master | `especialidades/psiquiatria/research/AUDITORIA_MASTER.md` | TIER 1/2/3 completo |
| OE Relatorios | `especialidades/psiquiatria/research/OE_RELATORIO_01..10.md` | 10 relatorios |
| Playbook | `especialidades/psiquiatria/playbooks/playbook_psiquiatria.md` | v1.0 — aguarda revisao |
| Relatorio processo | `especialidades/psiquiatria/RELATORIO_PROCESSO.md` | Para Gabriel (head de conteudo) |

### Referencia (entregues)
| Artefato | Arquivo |
|----------|---------|
| JSON Cardiologia | `referencia/amil-ficha_cardiologia-v2.0.9.json` |
| JSON Reumatologia | `referencia/inclua-ficha_reumatologia-v1.1.0.json` |
| Playbook Cardiologia | `referencia/playbook_cardiologia.md` |
| Playbook Reumatologia | `referencia/playbook_reumatologia.md` |

---

## Ultimas sessoes

**2026-03-04 | Claude Code Opus (sessao 011):** Auditoria v1.0.0 ginecologia — analisou JSON atualizado pelo Gabriel, extraiu feedback da 1:1, encontrou typo `seletec_any` e bare clinicalExpressions residuais. 5 achados resolvidos na v1.0.0 (C1 formula, I1 LSIL, I2 preselected, hemograma, creatinina). 8 criticos + 3 moderados pendentes. Scripts QA corrigidos (validate_json.py + audit_logic.py).

**2026-03-04 | Claude Code Opus (sessao 010):** Reestruturacao lean — centralizou history/ (10 sessions sequenciais), criou referencia/ (4 projetos entregues), removeu 520KB bloat (transcripts), consolidou INFRAESTRUTURA→SKILL.md e BRIEFING→AGENT_PROMPT, deletou 4 docs obsoletos.

**2026-03-03 | Claude Code Opus (sessao 009):** Consolidacao infra — diagnosticou divergencia worktree/main, resgatou audit_logic.py, criou especialidades/ginecologia/, criou session_008 retroativo.

**2026-03-03 | Claude Code Sonnet (sessao 008):** Auditoria vdraft2 — 8 resolucoes, 4 criticos novos (espessamento + is True), sugestao historia_familiar_ca.

---

## Proximos passos

**[Ginecologia — Correcoes v1.0.1]**
1. **[Gabriel]** Ultima rodada de testes → salvar rascunho → avisar Dan
2. **[Dan]** Aplicar 8 correcoes criticas no Spider (7x `is True` + 1x `seletec_any → selected_any`)
3. **[Dan]** Aplicar 3 correcoes moderadas (orientacao cervical bare + CID creatinina)
4. **[Dan/Gabriel]** Gravar Loom videos (cenarios clinicos) para modelador Paulo
5. **[Dan]** Decidir I3 (`hpv_resultado_nd`) e I4 (`diu_contraindicacao`)
6. **[Futuro]** Adicionar `historia_familiar_ca` em N1 + expandir `alto_risco_mama`

**[Psiquiatria]**
7. **[Dan]** Revisar playbook em `especialidades/psiquiatria/playbooks/`
8. **[Agente]** Fase 4 — codificacao JSON: `tools/skills/codificacao-json/SKILL.md`

**[Skills Environment]**
9. **[Dan]** Reunir com Humberto para alinhar adocao do skills environment
10. **[Dan/Gabriel/Humberto]** Deadline: fim de Abril para empresa usar
11. **[Dan]** Avaliar Antigravity + Claude Code vs Adapta

**[Infraestrutura]**
12. **[Dan]** Remover worktrees stale apos encerrar sessao:
   ```bash
   cd C:\Users\daanm\Daktus\agente-daktus-content
   git worktree remove .claude/worktrees/thirsty-chatelet --force
   git branch -d claude/thirsty-chatelet
   ```

---

## Decisoes criticas (nao reverter sem contexto)

- **Playbook organizado por classe farmacologica**, nao por sindrome
- **AUDITORIA_MASTER e consolidacao oficial** de cada especialidade
- **Fase 2 de auditoria do banco antecipada** (antes do playbook)
- **Nunca avancar de fase sem aprovacao explicita do Dan**
- **Sessions numeradas globalmente** em `history/` (sequenciais, 001+)
- **Expressoes do summary sempre com `is True`** nas condicionais de conduta
- **referencia/** para projetos entregues (read-only), **especialidades/** para ativos
- **LSIL → colposcopia imediata** — abordagem conservadora (decisao Gabriel+Dan, sessao 011)
- **Hemograma amplo** — rastreamento universal sem restricao de queixa (decisao Gabriel, sessao 011)

---

## Para retomar: leia nesta ordem

1. **Este arquivo** (ESTADO.md) — onde estamos
2. `SKILL.md` — pipeline geral e regras
3. `tools/skills/{fase-atual}/SKILL.md` — instrucao da fase
4. Sessao mais recente: `history/session_011.md`
5. Auditoria ativa (gineco): `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md`
6. Banco evidencias (psy): `especialidades/psiquiatria/research/BANCO_EVIDENCIAS_PSIQUIATRIA.md`

---

## Contexto do repositorio

```
GitHub: github.com/daanmt/agente-daktus-content   (Stage 1 — este repo)
Stage 2: github.com/daanmt/agente-daktus-qa        (validacao automatizada)
Local:   C:\Users\daanm\Daktus\agente-daktus-content
```

*Ao final de cada sessao: atualizar este arquivo e fazer commit.*
