# session_016.md — Fase 5 Psiquiatria: Quality Patch v0.1.2

**Data:** 2026-03-08
**Fase:** Fase 5 — QA iterativo (patches de design)
**Especialidade:** Psiquiatria
**Base:** `amil-ficha_psiquiatria-v0.1.2.json` (UX draft do usuário + patch v0.1.2 de session_015)

---

## Resumo da sessão

Sessão de quality improvement profundo sobre o JSON de psiquiatria v0.1.2. O usuário entregou uma versão
revisada com melhorias de UX próprias (sex/age como `oculto`, roteamento por `ideacao_passiva`,
`especificador_misto` movido para Nó 5) e solicitou análise de qualidade para reduzir redundância,
corrigir violações estruturais, remover emojis e melhorar coesão clínica.

Resultado: 46 modificações em 9 grupos, 0 BLOQUEANTES na auditoria final.

---

## Melhorias do usuário incorporadas (base do draft)

- `sex` e `age` configurados como `"condicional": "oculto"` (preenchimento automático pela plataforma)
- `ideacao_passiva` usado como gate de roteamento de nó (condicional de nó, não de pergunta)
- `especificador_misto` movido para Nó 5 (Fármacos) — correto, pois referencia `episodio_atual_humor` do Nó 4

---

## Artefatos entregues pelo usuário no início da sessão

- `amil-ficha_psiquiatria-v0.1.2.json` (draft) — versão com modificações manuais de UX do usuário

---

## Sequência de ações

### 1. Análise de qualidade do draft v0.1.2

Exploração sistemática para identificar:
- 5 violações same-node (perguntas condicionadas por UIDs do mesmo nó)
- `ansiedade_subtipo` redundante com `diagnostico_ativo`
- `phq9_score` e `audit_score` como A3 órfãos (sem conduta)
- 19 emojis em nomes de alertas + 2 em labels de opções
- `categorias: []` em todos os 25 exames
- Nó de pausa de enfermagem sem conteúdo (`condutaDataNode` ausente)
- Orientações ausentes (seção `orientacao` vazia)
- 4 antipsicóticos ausentes da conduta médica
- Falhas de coesão: typo, anglicismo, nodeId mismatch, metadata.version = "draft"

### 2. Script de patch: `patch_v012_improvements.py`

46 modificações em 9 grupos — aplicado in-place sobre `v0.1.2.json`:

| Grupo | Descrição | Modificações |
|-------|-----------|-------------|
| A | Same-node fix: mover perguntas entre nós | 5 (+1 bug fix de condicional) |
| B | Remover `ansiedade_subtipo` (redundante) | 1 |
| C | Conectar escores órfãos à conduta | 3 |
| D | Remover emojis de alertas e labels | 21 |
| E | Adicionar categorias a todos os exames | 25 |
| F | Handoff messages no nó de pausa de enfermagem | 3 |
| G | 4 antipsicóticos na conduta médica | 4 |
| H | 4 orientações ao paciente (voz 2ª pessoa) | 4 |
| I | Correções de coesão | 6 |

### 3. Grupo A — Violações same-node corrigidas

Regra violada: expressão de pergunta só pode referenciar UIDs de nós **anteriores**.

| Pergunta | Nó original | Referência | Problema | Solução |
|----------|------------|------------|---------|---------|
| `phq9_score` | Nó 3 | `diagnostico_ativo` (Nó 3) | mesmo nó | → Nó 4 |
| `mdq_aplicado` | Nó 3 | `diagnostico_ativo` (Nó 3) | mesmo nó | → Nó 4 |
| `audit_score` | Nó 3 | `substancias_uso` (Nó 3) | mesmo nó | → Nó 4 |
| `madrs_score` | Nó 4 | `episodio_atual_humor` (Nó 4) | mesmo nó | → Nó 5 |
| `ymrs_score` | Nó 4 | `episodio_atual_humor` (Nó 4) | mesmo nó | → Nó 5 |

Bug adicional: `madrs_score` tinha `"condicional": "visivel"` com `expressao` ativa → corrigido para `"condicional"`.

### 4. Grupos C — Escores conectados à conduta

- **PHQ-9 ≥15**: alerta de depressão moderada-grave (complementar ao MADRS, condição excludente)
- **AUDIT ≥8**: alerta de uso problemático de álcool com orientação de intervenção breve
- **CAPS-AD**: condição expandida para incluir `audit_score >= 16` (dependência de álcool)

### 5. Grupos D/E — Emojis e categorias

**Emojis removidos:**
- 19 nomes de alertas (⛔/⚠️/ℹ️ removidos)
- 2 labels de `sintomas_miocardite` (⛔/⚠️ removidos)

**Categorias de exames** (padrão ginecologia):
- "Monitoramento Farmacológico": litemia, creatinina, VPA, HLA-B*, CBZ, ANC, troponina+PCR (7)
- "Investigação Orgânica": TSH, cálcio, VDRL, HIV, neuroimagem (5)
- "Cardiometabólico": glicemia, HbA1c, colesterol, ECG (4)
- "Avaliação Laboratorial": hemograma e demais (9)

### 6. Grupo F — Handoff no nó de pausa de enfermagem

Nó `conduta-a9ccd9ee-4962-4bf2-ae6a-a0f4fef7d7d9` (tipo: pausa) recebu `condutaDataNode.mensagem` com:
- Handoff risco ALTO: chamar médico imediatamente / não deixar desacompanhado
- Handoff risco INTERMEDIÁRIO: comunicar médico antes de prosseguir / SPI nesta consulta
- Handoff risco BAIXO: triagem concluída / aguardar avaliação médica

### 7. Grupo G/H — Conduta médica expandida

**Antipsicóticos adicionados:**
- Quetiapina 25/50/100 mg — humor/psicose/potencialização
- Olanzapina 5/10 mg — psicose/TAB
- Risperidona 1/2 mg — psicose/TEA irritabilidade grave
- Aripiprazol 10/15 mg — baixo risco metabólico / potencialização

**Orientações ao paciente (voz 2ª pessoa):**
- "Sobre seu diagnóstico" — psicoeducação acessível
- "Sobre seus medicamentos" — adesão e expectativas
- "Plano de segurança em crise" — passos e contatos em crise
- "Sono e rotina" — higiene do sono e rotina saudável

### 8. Grupo I — Coesão

- Typo "EPÍSODIO" → "EPISÓDIO" (no nome de alerta)
- Anglicismo "Lethal means counseling" → "Restrição de meios letais" (no `nome`)
- NodeId corrigido em 3 perguntas: `tipo_consulta`, `motivo_consulta`, `exames_recentes`
- `metadata.version`: "draft" → "0.1.2"

### 9. Resultado da auditoria final v0.1.2

Executado via `audit_design_v01.py` (com override do filepath):

```
A1 choice→boolean BLOQUEANTE:  0  ✅
A2 labels enum BLOQUEANTE:      0  ✅
A4 conduta sem condicao BLOQ:   0  ✅
TOTAL BLOQUEANTES: 0

A1 revisão (choice 2-opções legítimas): 2
A3 uid sem impacto (revisão): 32  (contexto clínico + monitoramento farmacológico)
Total itens de conduta: 77 (no6) + 3 (pausa)
```

**Nota:** 3 BLOQUEANTES foram encontrados após a primeira execução (orientações com `condicao` vazia).
Corrigidos com condições significativas antes da auditoria final.

---

## Inventário final da conduta médica (node-psiq-06-conduta)

| Seção | Antes (v0.1.1) | Depois (v0.1.2) |
|-------|----------------|-----------------|
| mensagem (alertas) | 19 | 21 (+PHQ-9 ≥15, +AUDIT ≥8) |
| exame | 25 | 25 (categorizados) |
| encaminhamento | 14 | 14 (CAPS-AD condição expandida) |
| medicamento | 9 | 13 (+quetiapina, +olanzapina, +risperidona, +aripiprazol) |
| orientacao | 0 | 4 (novo) |
| **total** | **67** | **77** |

---

## Artefatos produzidos

| Arquivo | Status |
|---------|--------|
| `scripts/patch_v012_improvements.py` | ✅ criado |
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json` | ✅ atualizado in-place |
| `HANDOFF.md` | ✅ atualizado |
| `ESTADO.md` | ✅ atualizado |
| `history/session_016.md` | ✅ este arquivo |

---

## A3 residuais (32) — classificação pós-patch

**Contexto clínico legítimo (manter sem conduta):**
`tipo_consulta`, `motivo_consulta`, `exames_recentes`, `ideacao_passiva`,
`outros_medicamentos_relevantes`, `internacao_psiq_previa`, `mdq_aplicado`, `primeira_consulta_vida`

**Monitoramento farmacológico de referência:**
`litio_fase`, `litemia_valor`, `litemia_dentro_faixa`, `vpa_fase`,
`vpa_nivel`, `vpa_labs_recentes`, `cbz_nivel`, `anc_valor`, `ap_tempo_uso`

**Nuances diagnósticas (potencial conduta futura):**
`tab_fase_diagnostica`, `ciclagem_rapida`, `especificador_misto`,
`burnout_criterios_tdm`, `tdah_apresentacao`, `sintomas_cardiacos_tdah`,
`tea_nivel_suporte`, `tea_irritabilidade_grave`, `tea_comorbidades`,
`tpb_autolesao_ativa`, `tpb_sintoma_alvo`

---

## TUSS pendentes (histórico)

- HLA-B*1502: `codigo: []` — pendente codificação ANS
- Troponina+PCR: `codigo: []` — pendente codificação institucional

---

## Próxima sessão recomendada

1. QA clínico no preview Daktus — percorrer 3 perfis críticos:
   - Alto risco suicida com acesso a meios → verificar restrição de meios letais
   - Mulher grávida em uso de valproato → verificar alerta gestante+VPA
   - Esquizofrenia refratária → verificar indicação de clozapina
2. Ajustar condicionais ou conteúdo conforme feedback do QA clínico
3. Avaliar 32 uids A3 residuais: manter, conectar ou remover
4. Promover para v1.0.0 após aprovação clínica completa
