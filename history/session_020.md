# session_020 — Skillização Piloto: daktus-json-coding

**Data:** 2026-03-09
**Tema:** Infraestrutura — Alinhamento com arquitetura de skills Anthropic
**Agente:** Claude Opus 4.6

---

## Objetivo

Criar a primeira skill exportável no padrão Anthropic (`daktus-json-coding`), preservando a arquitetura state-driven existente. Estabelecer modelo de duas camadas: pipeline interno (`tools/skills/`) + skills exportáveis (`skills/`).

---

## O que foi feito

### Fase 1 — Diagnóstico

Leitura completa do repositório para mapear:
- Boot sequence (AGENTE.md → HANDOFF.md → ESTADO.md → SKILL.md)
- 7 sub-skills em `tools/skills/` (nenhuma com YAML frontmatter)
- 4 docs de conhecimento fragmentado para codificação JSON
- Gap principal: ausência de frontmatter, autossuficiência e estrutura Anthropic

### Fase 2 — Planejamento

Plano aprovado com 7 etapas, arquitetura de duas camadas, mínima ruptura.

### Fase 3 — Criação da skill piloto

**Arquivos criados (8):**

| Arquivo | Linhas | Fonte |
|---------|--------|-------|
| `skills/daktus-json-coding/SKILL.md` | ~300 | Consolidação de `tools/skills/codificacao-json/SKILL.md` + `GUIA_DESIGN_UX.md` §2, §2.1 |
| `references/DSL_CONDICIONAL.md` | ~150 | `GUIA_DESIGN_UX.md` §2.1, §5, §7 |
| `references/PADROES_REUTILIZAVEIS.md` | ~120 | `PADROES_ARQUITETURA_JSON.md` Part I + `GUIA_DESIGN_UX.md` §4 |
| `references/ERROS_DOCUMENTADOS.md` | ~100 | `PADROES_ARQUITETURA_JSON.md` Parts II + IV |
| `scripts/validate_json.py` | ~60 | Generalização de `scripts/audit_design_v01.py` + template inline |
| `assets/template_form_node.json` | ~30 | Extraído de padrões inline |
| `assets/template_conduta_node.json` | ~25 | Extraído de padrões inline |
| `assets/template_edge.json` | ~5 | Extraído de padrões inline |

**Arquivos modificados (2):**

| Arquivo | Mudança |
|---------|---------|
| `tools/skills/codificacao-json/SKILL.md` | Nota de shim adicionada no topo (backward-compatible) |
| `SKILL.md` (root) | Seção aditiva "SKILLS EXPORTÁVEIS" no final |

### Fase 4 — Validação

- `validate_json.py` executado contra `amil-ficha_psiquiatria-v0.2.0.json`
- Resultado: 0 erros | 9 nodes | 8 edges | 79 IIDs

---

## Decisões tomadas

1. **Duas camadas**: `tools/skills/` (interno) permanece; `skills/` (exportável) nasce em paralelo
2. **Docs canônicos intocados**: `GUIA_DESIGN_UX.md`, `PADROES_ARQUITETURA_JSON.md`, `GUARDRAIL_EVIDENCIAS.md` continuam como fonte de verdade
3. **Shim, não migração**: `tools/skills/codificacao-json/SKILL.md` mantido intacto com nota de redirecionamento
4. **Deprecação gradual**: só quando skill exportável provar-se funcional em 2+ especialidades

---

## Próximo passo recomendado

1. Testar triggering da skill em sessão real de codificação JSON
2. Continuar QA clínico de v0.2 no preview Daktus (3 perfis — inalterado de session_019)
3. Avaliar criação de skills exportáveis para outras fases do pipeline após validação da piloto
