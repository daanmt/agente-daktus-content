# HANDOFF.md — ESTADO OPERACIONAL CURTO
*Atualizado: 2026-03-09 — Validação DSL + GUIA atualizado (session_017)*

---

## ESTADO OPERACIONAL ATUAL

- Branch-base: `main`
- Última sessão integrada: **Fase 5 — Psiquiatria — Quality Patch v0.1.2** (session_016)
- Especialidade/tema ativo: Psiquiatria
- Fase atual: **Fase 5 — QA iterativo (patches de design)**
- Artefato ativo: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json`

---

## VERSIONING — PSIQUIATRIA

| Versão | Status | Artefato | Observações |
|--------|--------|----------|-------------|
| v0.1.0 | legado publicado | `amil-ficha_psiquiatria-v0.1.0.json` | Primeira versão completa, com falhas estruturais de design |
| v0.1.1 | publicado | `amil-ficha_psiquiatria-v0.1.1.json` | Patch estrutural + conduta expandida — 0 BLOQUEANTES |
| **v0.1.2** | **ativo (draft)** | `amil-ficha_psiquiatria-v0.1.2.json` | UX improvements (usuário) + quality patch (46 mod.) — 0 BLOQUEANTES |

---

## O QUE FOI FEITO — QUALITY PATCH v0.1.2 (session_016)

### Script produzido

- `scripts/patch_v012_improvements.py` — 46 modificações ✅

### Modificações aplicadas (46 total)

**Grupo A — Correção de violações same-node (5 movimentações):**
- `phq9_score`, `mdq_aplicado`, `audit_score`: Nó 3 → Nó 4 (expressões referenciam Nó 3 como nó anterior → válido)
- `madrs_score`, `ymrs_score`: Nó 4 → Nó 5 (expressões referenciam `episodio_atual_humor` do Nó 4 como anterior → válido)
- `madrs_score`: condicional corrigido de "visivel" para "condicional" (bug)

**Grupo B — Redundância removida (1):**
- `ansiedade_subtipo` removido do Nó 4 (duplicava opções já presentes em `diagnostico_ativo`)

**Grupo C — Escores conectados à conduta (3 operações):**
- Alerta PHQ-9 ≥15 adicionado (complementar ao MADRS, sem duplicata)
- Alerta AUDIT ≥8 adicionado (intervenção breve / CAPS-AD)
- Encaminhamento CAPS-AD: condição expandida com `audit_score >= 16`

**Grupo D — Emojis removidos (21):**
- 19 nomes de alertas: prefixos ⛔/⚠️/ℹ️ removidos
- 2 labels de opções de `sintomas_miocardite`: prefixos ⛔/⚠️ removidos

**Grupo E — Categorias adicionadas a todos os exames (25):**
- "Monitoramento Farmacológico": litemia, creatinina, VPA, HLA-B*, CBZ, ANC, troponina+PCR
- "Investigação Orgânica": TSH, cálcio, VDRL, HIV, neuroimagem
- "Cardiometabólico": glicemia, HbA1c, colesterol, ECG
- "Avaliação Laboratorial": hemograma, ureia, transaminases, sódio, prolactina, beta-HCG, etc.

**Grupo F — Mensagem de handoff na pausa de enfermagem (3 mensagens):**
- `condutaDataNode` adicionado ao nó `conduta-a9ccd9ee-...` com 3 mensagens de handoff por nível de risco

**Grupo G — 4 antipsicóticos adicionados à conduta médica (4):**
- Quetiapina 25/50/100 mg, Olanzapina 5/10 mg, Risperidona 1/2 mg, Aripiprazol 10/15 mg

**Grupo H — 4 orientações ao paciente adicionadas (4):**
- "Sobre seu diagnóstico", "Sobre seus medicamentos", "Plano de segurança em crise", "Sono e rotina"
- Escritas em 2ª pessoa (voz do paciente)

**Grupo I — Correções de coesão (6):**
- Typo: "EPÍSODIO" → "EPISÓDIO"
- Anglicismo: "Lethal means counseling" → "Restrição de meios letais" (no nome)
- NodeId: 3 perguntas com nodeId errado corrigidas (`tipo_consulta`, `motivo_consulta`, `exames_recentes`)
- `metadata.version`: "draft" → "0.1.2"

### Resultado da auditoria final v0.1.2 (quality patch)

```
A1 choice→boolean BLOQUEANTE:  0  ✅
A2 labels enum BLOQUEANTE:      0  ✅
A4 conduta sem condicao BLOQ:   0  ✅
TOTAL BLOQUEANTES: 0

A1 revisão (choice 2-opções legítimas): 2
A3 uid sem impacto (revisão): 32  (contexto clínico + monitoramento farmacológico)
Total itens de conduta: 79
```

### Inventário da conduta médica (node-psiq-06-conduta)

| Seção | Antes | Depois |
|-------|-------|--------|
| mensagem (alertas) | 19 | 21 (+PHQ-9 ≥15, +AUDIT ≥8) |
| exame | 25 | 25 (categorizados) |
| encaminhamento | 14 | 14 (CAPS-AD condição expandida) |
| medicamento | 9 | 13 (+quetiapina, +olanzapina, +risperidona, +aripiprazol) |
| orientacao | 0 | 4 (novo) |
| **total** | **67** | **77** |

---

## O QUE ESTÁ ABERTO AGORA

### A3 residual: 32 uids informativos (sem conduta direta)

Classificação dos uids A3 restantes:

**Contexto clínico legítimo (manter sem conduta):**
`tipo_consulta`, `motivo_consulta`, `exames_recentes`, `ideacao_passiva`,
`outros_medicamentos_relevantes`, `internacao_psiq_previa`, `mdq_aplicado`,
`primeira_consulta_vida`

**Monitoramento farmacológico de referência (valores para o médico):**
`litio_fase`, `litemia_valor`, `litemia_dentro_faixa`, `vpa_fase`,
`vpa_nivel`, `vpa_labs_recentes`, `cbz_nivel`, `anc_valor`, `ap_tempo_uso`

**Nuances diagnósticas (potencial conduta futura):**
`tab_fase_diagnostica`, `ciclagem_rapida`, `especificador_misto`,
`burnout_criterios_tdm`, `tdah_apresentacao`,
`sintomas_cardiacos_tdah`, `tea_nivel_suporte`, `tea_irritabilidade_grave`,
`tea_comorbidades`, `tpb_autolesao_ativa`, `tpb_sintoma_alvo`

*(Nota: `ansiedade_subtipo` removido do JSON. `phq9_score` e `audit_score` conectados à conduta — não são mais A3.)*

### Próximo passo recomendado

**QA clínico no ambiente de preview Daktus com v0.1.2** — percorrer 3 perfis:
1. Alto risco suicida com acesso a meios → verificar restrição de meios letais
2. Mulher grávida em uso de valproato → verificar alerta gestante+VPA
3. Esquizofrenia refratária → verificar indicação de clozapina

---

## O QUE FOI FEITO — session_017 (2026-03-09)

- **Correção DSL**: 13 padrões `campo in ('v1', 'v2')` corrigidos para `selected_any(campo, 'v1', 'v2')` em v0.1.2 (3 em `expressao`, 10 em `condicao`)
- **Diagnóstico confirmado**: `select=choice` com `exclusive: True` usa DSL de `choice` (`selected_any`), não de `single` (`==`)
- **Script criado**: `scripts/patch_v012_conditional_fix.py` — utilidade de validação e correção DSL futura (13 substituições catalogadas)
- **GUIA atualizado**: `tools/GUIA_DESIGN_UX.md` §2.1 — nova seção com tabela de operadores, anti-patterns e exemplos reais
- **Auditoria reconfirmada**: 0 BLOQUEANTES | 32 A3 (legítimos)

---

## PRÓXIMO PASSO RECOMENDADO

1. QA clínico do v0.1.2 no ambiente de preview Daktus (percorrer 3 perfis críticos)
2. Ajustar condicionais ou conteúdo clínico conforme feedback do QA
3. Avaliar 32 uids A3 residuais: manter, conectar ou remover
4. Promover para v1.0.0 após aprovação clínica completa

---

## ARQUIVOS A LER NA PRÓXIMA SESSÃO

1. `AGENTE.md`
2. `HANDOFF.md` (este)
3. `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json`

---

## NÃO SOBRESCREVER SEM REVISAR

- v0.1.2 é o artefato ativo — não alterar sem novo patch documentado
- v0.1.1 mantido como versão publicada estável
- branch-base: `main`
- TUSS pendentes: HLA-B*1502 e Troponina+PCR — `codigo: []` no JSON, sinalizado

---

## DIVERGÊNCIAS / OVERRIDES

- HANDOFF atualizado em 2026-03-09 (session_017) — sobrescreve estado de session_016
- v0.1.0 publicado como legado; v0.1.1 como versão estável; v0.1.2 como artefato ativo (draft)
- vdraft do usuário incorporado ao v0.1.2 (UX improvements: sex/age ocultos, roteamento por `ideacao_passiva`, `especificador_misto` movido para Nó 5)
- DSL confirmado correto em v0.1.2 — patterns `campo in ('v1')` reportados pelo usuário não existiam no artefato (apenas no vdraft dele)
