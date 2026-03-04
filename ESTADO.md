# ESTADO — agente-daktus-content
*Atualizado: 2026-03-04 (sessao 010) | Ferramenta: Claude Code (Opus 4.6)*

---

## O que e este projeto

**Pipeline agnostico de especialidade** para producao de fichas clinicas Daktus/Amil. Stage 1: gera playbook clinico + JSON da ficha. Stage 2 (validacao automatizada): repositorio `agente-daktus-qa`.

Especialidades entregues: Reumatologia, Cardiologia (em `referencia/`). Em desenvolvimento: Ginecologia (auditoria JSON), Psiquiatria (Fase 3). Especialidades em andamento ficam em `especialidades/{nome}/`.

---

## Fase atual

**Duas frentes paralelas:**

**[Ginecologia — Auditoria JSON]** Sessao 008 concluida | Status: Aguardando Dan aplicar correcoes
- Auditoria em `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md`
- 4 criticos pendentes (C1: formula espessamento OR quebrada; C2-C4: expressoes sem `is True`)
- 4 importantes pendentes (I1: LSIL; I2: citologia preselected; I3: hpv_resultado_nd; I4: diu_contraindicacao)
- 1 sugestao de nova pergunta: `historia_familiar_ca`

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
| Auditoria JSON | `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md` | Aguarda Dan aplicar C1-C4 |
| Playbook | `especialidades/ginecologia/playbooks/playbook_ginecologia_auditado.md` | v1.0 auditado |
| JSON | `especialidades/ginecologia/jsons/amil-ficha_ginecologia-vdraft.json` | vdraft1 no repo; vdraft2 nao versionado |

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

**2026-03-04 | Claude Code Opus (sessao 010):** Reestruturacao lean — centralizou history/ (10 sessions sequenciais), criou referencia/ (4 projetos entregues), removeu 520KB bloat (transcripts), consolidou INFRAESTRUTURA→SKILL.md e BRIEFING→AGENT_PROMPT, deletou 4 docs obsoletos (CLAUDECODE_KICKSTART, PROMPT_ALINHAMENTO, READMEs internos), limpou 5 pastas vazias. Repo: 51→42 arquivos.

**2026-03-03 | Claude Code Opus (sessao 009):** Consolidacao infra — diagnosticou divergencia worktree/main, resgatou audit_logic.py, criou especialidades/ginecologia/, criou session_008 retroativo.

**2026-03-03 | Claude Code Sonnet (sessao 008):** Auditoria vdraft2 — 8 resolucoes, 4 criticos novos (espessamento + is True), sugestao historia_familiar_ca. Refatoracao: psiquiatria em especialidades/, tools renomeados.

**2026-03-03 | Claude Code Sonnet (sessao 007):** Auditoria inicial vdraft1 — 6 criticos, 8 moderados.

---

## Proximos passos

**[Ginecologia JSON]**
1. **[Dan]** Aplicar C1: restaurar formula `espessamento_endometrial_significativo` com menopausa gate
2. **[Dan]** Aplicar C2-C4: adicionar `is True` em expressoes bare
3. **[Dan]** Decidir I1: LSIL → colposcopia imediata ou repetir citologia em 1 ano
4. **[Dan]** Adicionar pergunta `historia_familiar_ca`

**[Psiquiatria]**
5. **[Dan]** Revisar playbook em `especialidades/psiquiatria/playbooks/`
6. **[Agente]** Fase 4 — codificacao JSON: `tools/skills/codificacao-json/SKILL.md`

**[Infraestrutura]**
7. **[Dan]** Remover worktrees stale apos encerrar sessao:
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

---

## Para retomar: leia nesta ordem

1. **Este arquivo** (ESTADO.md) — onde estamos
2. `SKILL.md` — pipeline geral e regras
3. `tools/skills/{fase-atual}/SKILL.md` — instrucao da fase
4. Sessao mais recente: `history/session_010.md`
5. Auditoria ativa (se gine): `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md`
6. Banco evidencias (se psy): `especialidades/psiquiatria/research/BANCO_EVIDENCIAS_PSIQUIATRIA.md`

---

## Contexto do repositorio

```
GitHub: github.com/daanmt/agente-daktus-content   (Stage 1 — este repo)
Stage 2: github.com/daanmt/agente-daktus-qa        (validacao automatizada)
Local:   C:\Users\daanm\Daktus\agente-daktus-content
```

*Ao final de cada sessao: atualizar este arquivo e fazer commit.*
