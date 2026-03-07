# HANDOFF.md — ESTADO OPERACIONAL CURTO
*Atualizado: 2026-03-07 — Fase 4 (JSON Psiquiatria) concluída*

---

## ESTADO OPERACIONAL ATUAL

- Branch-base: `main`
- Última sessão integrada: **Fase 4 — Psiquiatria — JSON completo** (sessions 009–014)
- Especialidade/tema ativo: Psiquiatria
- Fase atual: **Fase 4 CONCLUÍDA** → pronta para Fase 5 (QA final com usuário)
- Artefato produzido: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json`

---

## O QUE JÁ ESTÁ INTEGRADO (Fase 4 — sessions 009–014)

| Sessão | Conteúdo | Commit | Status |
|--------|----------|--------|--------|
| A | Nós 1 + 2 (Triagem + Gate P0 C-SSRS, 21q) | ✅ commitado | ok |
| B | Nó 3 (Anamnese Psiquiátrica, 15q) | ✅ commitado | ok |
| C–F | Nós 4 + 5 (Diagnóstico 30q + Farmacológico 17q) | `9d33d01` ✅ | ok |
| G–H | Nó 6 (Conduta: 9 alertas, 25 exames, 13 encam., 9 meds) + clinicalExpressions | `459b6b4` ✅ | ok |

**Validação estrutural:** PASSOU — 6 nodes, 5 edges, 83 questões, 260 iids únicos, 0 erros
**QA clínico:** 3 perfis simulados — alto risco suicida, TDM leve, TAB+lítio+VPA — todos corretos

---

## ARTEFATO DE SAÍDA — PSIQUIATRIA

```
especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json
```

| Nó | ID | Questões | Conteúdo |
|----|----|----------|---------|
| 1 | node-psiq-01-triagem | 10q | Triagem Enfermagem + 5 clinicalExpressions |
| 2 | node-psiq-02-gate-p0 | 11q | Gate C-SSRS (breakpoint) |
| 3 | node-psiq-03-anamnese | 15q | Anamnese completa |
| 4 | node-psiq-04-diagnostico | 30q | 6 blocos diagnósticos |
| 5 | node-psiq-05-farmacos | 17q | Monitoramento farmacológico |
| 6 | node-psiq-06-conduta | conduta | 9 alertas, 25 exames TUSS, 13 encam., 9 meds |

---

## O QUE ESTÁ ABERTO AGORA

- **Fase 5 — QA final** aguarda revisão do usuário (Dan):
  - Revisar condicionais e expressões do JSON
  - Validar conteúdo clínico das condutas
  - Confirmar TUSS de itens pendentes (HLA-B*1502, troponina+PCR)
  - Ajustar versão: `1.0.0-draft` → `1.0.0` quando aprovado

---

## PRÓXIMO PASSO RECOMENDADO

1. Revisar `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json`
2. Executar QA clínico completo no ambiente de preview Daktus
3. Corrigir eventuais ajustes pontuais de condicionais ou conteúdo
4. Atualizar metadata.version para `1.0.0` e registrar entrega

---

## ARQUIVOS A LER NA PRÓXIMA SESSÃO

1. `AGENTE.md`
2. `HANDOFF.md` (este)
3. `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json`
4. `history/session_014.md`

---

## NÃO SOBRESCREVER SEM REVISAR

- versão `1.0.0-draft` do JSON — não alterar para `1.0.0` sem aprovação explícita
- branch-base: `main`
- separação entre `HANDOFF.md` e `ESTADO.md`
- centralidade de `AGENTE.md` como ponto de entrada

---

## DIVERGÊNCIAS / OVERRIDES

- `especialidades/psiquiatria/RELATORIO_PROCESSO.md` contém referência histórica — arquivo operacional inativo.
- Worktrees antigos em `.claude/worktrees/` são ignorados pelo Git. Não representam estado ativo.
- TUSS pendentes: HLA-B*1502 e Troponina+PCR — `codigo: []` no JSON, sinalizado.
