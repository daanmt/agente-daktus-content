# HANDOFF.md — ESTADO OPERACIONAL CURTO
*Atualizado: 2026-03-08 — Patch v0.1.2 aplicado (v0.1.1 → v0.1.2)*

---

## ESTADO OPERACIONAL ATUAL

- Branch-base: `main`
- Última sessão integrada: **Fase 5 — Psiquiatria — Patch v0.1.1** (session_015)
- Especialidade/tema ativo: Psiquiatria
- Fase atual: **Fase 5 — QA iterativo (patches de design)**
- Artefato ativo: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json`

---

## VERSIONING — PSIQUIATRIA

| Versão | Status | Artefato | Observações |
|--------|--------|----------|-------------|
| v0.1.0 | legado publicado | `amil-ficha_psiquiatria-v0.1.0.json` (renomeado) | Primeira versão completa, com falhas estruturais de design |
| vdraft | base do usuário | `amil-ficha_psiquiatria-vdraft.json` | Modificações manuais do usuário (booleans Gate P0, novo nó summary, pausa enfermagem) |
| v0.1.1 | base | `amil-ficha_psiquiatria-v0.1.1.json` | Patch estrutural — todos os BLOQUEANTES zerados |
| **v0.1.2** | **ativo** | `amil-ficha_psiquiatria-v0.1.2.json` | Conduta expandida — 10 alertas + correções de expressões |

---

## O QUE FOI FEITO — PATCH v0.1.2 (session_015, continuação)

### Artefatos produzidos nesta sessão

- `tools/GUIA_DESIGN_UX.md` — guia de design UX consolidado ✅
- `scripts/audit_design_v01.py` — auditoria estrutural (não-destrutiva) ✅
- `scripts/patch_vdraft_to_v011.py` — script de patch (25 modificações) ✅
- `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.1.json` — artefato ativo ✅

### Modificações aplicadas no v0.1.1 (25 total)

**Grupo A — Fórmulas do nó summary corrigidas (3):**
- `risco_suicidio_alto`: critérios C-SSRS completos (plano, intenção, método, tentativa_previa, acesso_meios)
- `risco_suicidio_intermediario`: ideação ativa + tentativa prévia, sem plano/intenção
- `risco_suicidio_baixo`: ideação ativa sem fatores de risco, com fatores protetores

**Grupo B — Conduta: nivel_risco_p0 eliminado (3 condições reescritas):**
- Alertas e encaminhamento de SAMU agora usam `risco_suicidio_alto is True` / `risco_suicidio_intermediario is True`

**Grupo C — Perguntas movidas para Medicina (4 operações):**
- `spi_realizado` e `internacao_indicada_p0` removidos do nó de enfermagem (gate-p0)
- Inseridos como primeiras perguntas do nó de diagnóstico médico (nó 4)
- Expressões atualizadas para referenciar as novas variáveis booleanas do summary

**Grupo D — Referência inexistente corrigida (1):**
- `ideacao_com_plano.expressao`: `ideacao_suicida is True` → `ideacao_ativa is True`

**Grupo E — Boolean conversões iniciais Nó 4 (2):**
- `ciclagem_rapida` e `especificador_misto`: choice(sim/nao) → boolean

**Grupo F — Expressão de vpa_mie_consentimento (1):**
- `sexo_feminino_ie == 'sim'` → `sexo_feminino_ie is True`

**Grupo G — Boolean conversões residuais Nós 3 e 4 (10):**
- Nó 3: `sexo_feminino_ie`, `gestante`
- Nó 4: `burnout_criterios_tdm`, `primeiro_episodio_psicotico`, `esquizofrenia_refrataria`, `comportamento_suicida_recorrente`, `tdah_abuso_substancias_ativo`, `sintomas_cardiacos_tdah`, `tea_irritabilidade_grave`, `tpb_autolesao_ativa`

### Resultado da auditoria final v0.1.2

```
A1 choice→boolean BLOQUEANTE:  0  ✅
A2 labels enum BLOQUEANTE:      0  ✅
A4 conduta sem condicao BLOQ:   0  ✅
TOTAL BLOQUEANTES: 0

A1 revisão (choice 2-opções legítimas): 4
A3 uid sem impacto (revisão): 31  (eram 40 em v0.1.1)
Total conduta items: 66 (eram 56 em v0.1.1)
```

### Estrutura de nós v0.1.1

| ID | Tipo | Label | Questões |
|----|------|-------|----------|
| `node-psiq-01-triagem` | custom | Identificação — Prontuário | ~2q |
| `20e05d57-...` | custom | Triagem — Enfermagem | ~4q |
| `node-psiq-03-anamnese` | custom | Anamnese Psiquiátrica — Enfermagem | ~12q |
| `node-psiq-02-gate-p0` | custom | Triagem Suicídio — Enfermagem (C-SSRS) | 7q |
| `summary-6e3e...` | summary | Processamento Clínico | 3 clinicalExpressions |
| `conduta-a9cc...` | conduct | Conduta — Enfermagem (pausa) | handoff |
| `node-psiq-04-diagnostico` | custom | Fluxo de seguimento — Medicina | ~11q |
| `node-psiq-05-farmacos` | custom | Monitoramento Farmacológico — Medicina | ~10q |
| `node-psiq-06-conduta` | conduct | Conduta — Medicina | 9 alertas, 25 exames, 13 enc., 9 meds |

**Total:** 9 nodes, 8 edges, 75 questões | `nivel_risco_p0` e `ideacao_suicida`: ausentes ✅

---

## O QUE ESTÁ ABERTO AGORA

### A3 residual: 31 uids informativos (sem conduta direta)

Classificação dos uids A3 restantes:

**Contexto clínico legítimo (manter sem conduta):**
`tipo_consulta`, `motivo_consulta`, `exames_recentes`, `ideacao_passiva`,
`outros_medicamentos_relevantes`, `internacao_psiq_previa`, `phq9_score`,
`mdq_aplicado`, `audit_score`, `primeira_consulta_vida`

**Monitoramento farmacológico de referência (valores para o médico):**
`litio_fase`, `litemia_valor`, `litemia_dentro_faixa`, `vpa_fase`,
`vpa_nivel`, `vpa_labs_recentes`, `cbz_nivel`, `anc_valor`, `ap_tempo_uso`

**Nuances diagnósticas (potencial conduta futura):**
`tab_fase_diagnostica`, `ciclagem_rapida`, `especificador_misto`,
`ansiedade_subtipo`, `burnout_criterios_tdm`, `tdah_apresentacao`,
`sintomas_cardiacos_tdah`, `tea_nivel_suporte`, `tea_irritabilidade_grave`,
`tea_comorbidades`, `tpb_autolesao_ativa`, `tpb_sintoma_alvo`

### Próximo passo recomendado

**QA clínico no ambiente de preview Daktus com v0.1.2** — percorrer 3 perfis:
1. Alto risco suicida com acesso a meios → verificar lethal means counseling
2. Mulher grávida em uso de valproato → verificar alerta gestante+VPA
3. Esquizofrenia refratária → verificar indicação de clozapina

---

## PRÓXIMO PASSO RECOMENDADO

1. QA clínico do v0.1.2 no ambiente de preview Daktus (percorrer 3 perfis críticos)
2. Ajustar condicionais ou conteúdo clínico conforme feedback do QA
3. Avaliar 31 uids A3 residuais: manter, conectar ou remover
4. Promover para v1.0.0 após aprovação clínica completa

---

## ARQUIVOS A LER NA PRÓXIMA SESSÃO

1. `AGENTE.md`
2. `HANDOFF.md` (este)
3. `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json`

---

## NÃO SOBRESCREVER SEM REVISAR

- v0.1.1 é o artefato ativo — não alterar sem novo patch documentado
- `amil-ficha_psiquiatria-vdraft.json` mantido como referência de intenção do usuário
- branch-base: `main`
- TUSS pendentes: HLA-B*1502 e Troponina+PCR — `codigo: []` no JSON, sinalizado

---

## DIVERGÊNCIAS / OVERRIDES

- HANDOFF atualizado em 2026-03-08 (session_015) — sobrescreve estado de 2026-03-07
- v0.1.0 publicado como legado; vdraft como referência; v0.1.1 como artefato ativo
