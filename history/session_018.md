# session_018.md — Correção condicional values + GUIA §5

**Data:** 2026-03-09
**Fase:** Fase 5 — QA iterativo (patches de design)
**Especialidade:** Psiquiatria
**Base:** `amil-ficha_psiquiatria-v0.1.2.json`

---

## Resumo da sessão

O usuário identificou que perguntas condicionais estavam com `"condicional": "condicional"` — valor inválido/depreciado no DSL Daktus. A regra correta: o campo `condicional` aceita apenas `"visivel"` (valor padrão, para perguntas exibidas com ou sem condição) ou `"oculto"` (campo verdadeiramente oculto, auto-preenchido pela plataforma — raramente necessário).

**12 perguntas corrigidas in-place** via Python inline. GUIA §5 atualizado com regra explícita.

---

## Regra codificada

| Valor | Quando usar |
|-------|-------------|
| `"visivel"` | **Valor padrão.** Pergunta exibida normalmente — sempre (sem `expressao`) ou condicionalmente (quando `expressao` for verdadeira) |
| `"oculto"` | Campo verdadeiramente oculto do formulário (preenchimento automático pela plataforma, ex.: `sex`, `age`) — raramente necessário |
| `"condicional"` | ❌ **NUNCA usar** — valor inválido/depreciado no DSL Daktus |

---

## Correções aplicadas (12 perguntas)

| Nó | UID | expressao presente? | Ação |
|----|-----|---------------------|------|
| node-psiq-03-anamnese | `gestante` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `tab_fase_diagnostica` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `ciclagem_rapida` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `audit_score` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `mdq_aplicado` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `phq9_score` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `ybocs_score` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `tept_psicoterapia_indicada` | sim | `"condicional"` → `"visivel"` |
| node-psiq-04-diagnostico | `burnout_criterios_tdm` | sim | `"condicional"` → `"visivel"` |
| node-psiq-05-farmacos | `ymrs_score` | sim | `"condicional"` → `"visivel"` |
| node-psiq-05-farmacos | `madrs_score` | sim | `"condicional"` → `"visivel"` |
| node-psiq-05-farmacos | `ap_tempo_uso` | sim | `"condicional"` → `"visivel"` |

*Nota: todas as 12 perguntas possuem `expressao` não-vazia — são perguntas condicionais que devem aparecer ao usuário quando a condição é satisfeita, portanto `"visivel"` é o valor correto.*

---

## Artefatos produzidos

| Arquivo | Ação |
|---------|------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json` | atualizado — 12 valores `"condicional"` corrigidos |
| `tools/GUIA_DESIGN_UX.md` | atualizado — §5 tabela de visibilidade corrigida, cascata corrigida, template boolean corrigido |
| `HANDOFF.md` | atualizado — session_018 documentada |
| `ESTADO.md` | atualizado — session_018 como última sessão integrada |
| `history/session_018.md` | criado — este arquivo |

---

## Verificação pós-patch

```
Instâncias "condicional": "condicional" restantes: 0  ✅
```

---

## Próxima sessão recomendada

1. QA clínico no preview Daktus — 3 perfis críticos:
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta gestante+VPA
   - Esquizofrenia refratária → indicação de clozapina
2. Avaliar 32 A3 residuais: manter, conectar ou remover
3. Promover para v1.0.0 após aprovação clínica completa
