# HANDOFF.md — ESTADO OPERACIONAL CURTO
*Atualizado: 2026-03-11 — Onda 4: Quality & Precision Reform → v0.6.0 (session_027)*

---

## ESTADO OPERACIONAL ATUAL

- Branch-base: `main`
- Última sessão integrada: **Onda 4 — Quality & Precision Reform → v0.6.0** (session_027)
- Especialidade/tema ativo: Psiquiatria (Fase 5 — QA iterativo)
- Fase atual: **Fase 5 — QA iterativo** → próximo: QA clínico no preview Daktus
- Artefato ativo: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.6.0.json`

---

## VERSIONING — PSIQUIATRIA

| Versão | Status | Artefato | Observações |
|--------|--------|----------|-------------|
| v0.1.0 | legado publicado | `amil-ficha_psiquiatria-v0.1.0.json` | Primeira versão completa, com falhas estruturais de design |
| v0.1.1 | publicado | `amil-ficha_psiquiatria-v0.1.1.json` | Patch estrutural + conduta expandida — 0 BLOQUEANTES |
| v0.1.2 | legado (base de desenvolvimento) | `amil-ficha_psiquiatria-v0.1.2.json` | UX improvements + quality patch + DSL + condicional values fixes |
| v0.2 | publicado | `amil-ficha_psiquiatria-v0.2.json` | Primeira versão revisada conjuntamente — 42 perguntas, 79 conduta, 0 BLOQUEANTES |
| v0.2.1 | publicado | `amil-ficha_psiquiatria-v0.2.1.json` | Ajustes manuais do usuário + fixes session_021 — 37 perguntas, 79 conduta, TUSS 100%, MEVO 8/13 |
| v0.2.2 | histórico | `amil-ficha_psiquiatria-v0.2.2.json` | Correção estrutural (antipsicóticos) + 11 fármacos adicionados — 28 medicamentos, 0 BLOQUEANTES, MEVO 19/28 |
| v0.2.3 | histórico | `amil-ficha_psiquiatria-v0.2.3.json` | Fechamento de hiatos do briefing — 8 mudanças estruturais, 0 BLOQUEANTES, 105 IIDs |
| v0.3.0 | histórico | `amil-ficha_psiquiatria-v0.3.0.json` | Camada de dissecção sindrômica — 4 perguntas novas, 4 bugs corrigidos, 6 novas mensagens, 0 BLOQUEANTES, 111 IIDs |
| v0.4.0 | histórico | `amil-ficha_psiquiatria-v0.4.0.json` | Onda 2 — 6 perguntas novas (tipo_consulta + 4 eixos + TEA), 6 mensagens, shortcut retorno, 0 BLOQUEANTES, 117 IIDs |
| v0.5.0 | histórico | `amil-ficha_psiquiatria-v0.5.0.json` | Onda 3 — 3 perguntas novas (tea_suspeita, agressividade_iminencia, ta_fenotipo) + sintomas_toxicidade_vpa + 3 mensagens + 7 fixes, 0 BLOQUEANTES |
| **v0.6.0** | **ativo** | `amil-ficha_psiquiatria-v0.6.0.json` | Onda 4 — 3 fórmulas risco recalibradas + 4 bugs DSL + DEPRESSÃO LEVE corrigida + tdah_abuso removido + 19 TUSS + 6 orientações + 22 acentos, 0 BLOQUEANTES |

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

## O QUE FOI FEITO — session_018 (2026-03-09)

- **Correção condicional values**: 12 perguntas com `"condicional": "condicional"` corrigidas para `"condicional": "visivel"` em v0.1.2
  - Nó 3: `gestante`
  - Nó 4: `tab_fase_diagnostica`, `ciclagem_rapida`, `audit_score`, `mdq_aplicado`, `phq9_score`, `ybocs_score`, `tept_psicoterapia_indicada`, `burnout_criterios_tdm`
  - Nó 5: `ymrs_score`, `madrs_score`, `ap_tempo_uso`
- **Regra confirmada**: `"condicional"` aceita apenas `"visivel"` (padrão — pergunta condicional ou sempre exibida) ou `"oculto"` (campo auto-preenchido, nunca exibido — raramente necessário)
- **GUIA atualizado**: `tools/GUIA_DESIGN_UX.md` §5 — tabela de visibilidade corrigida, exemplo de cascata corrigido, template boolean (linha 56) corrigido

---

## O QUE FOI FEITO — session_019 (2026-03-09)

**Auditoria end-to-end + geração de v0.2:**

- **24 perguntas removidas** (66 → 42 perguntas):
  - Grupo A (6 re-adicionadas pelo agente): `spi_realizado`, `neuropsicologica_indicada`, `tept_psicoterapia_indicada`, `nutri_encaminhada`, `tpb_em_tcd`, `tea_comorbidades`
  - Grupo B (10 orphans diagnósticas): `tab_fase_diagnostica`, `mdq_aplicado`, `burnout_criterios_tdm`, `especificador_misto`, `tdah_apresentacao`, `sintomas_cardiacos_tdah`, `tea_nivel_suporte`, `tpb_autolesao_ativa`, `tpb_sintoma_alvo`, `ciclagem_rapida`
  - Grupo C (8 monitoramento farmacológico sem conduta): `litio_fase`, `litemia_valor`, `vpa_fase`, `vpa_nivel`, `vpa_labs_recentes`, `cbz_nivel`, `anc_valor`, `ap_tempo_uso`
- **12 condicionais de conduta corrigidas**:
  - 5 simplificações (gates de perguntas removidas)
  - 7 correções de UIDs não definidos (nunca disparavam)
- **v0.2 gerado**: `amil-ficha_psiquiatria-v0.2.json` — 0 BLOQUEANTES
- **Script**: `scripts/patch_v012_to_v02.py`

---

## O QUE FOI FEITO — session_021 (2026-03-09)

**Análise de melhorias v0.2.1 + fixes + TUSS/MEVO:**

**Contexto:** Usuário fez ajustes manuais em v0.2 (removeu 5 escores PHQ-9/YMRS/MADRS/YBOCS/PCL-5, corrigiu ECG com `selected_any`). Sessão auditou e corrigiu todos os problemas.

- **5 alertas bloqueantes corrigidos** (referenciavam escores removidos → substituídos por condições baseadas em `episodio_atual_humor` / `diagnostico_ativo`)
- **2 condições de medicamento** com `madrs_score` residual removidas (Quetiapina + Aripiprazol)
- **metadata.version**: "draft" → "0.2.1"
- **TUSS 100% populados**: HLA-B*1502 (40306887) + Troponina+PCR (40302571 + 40308391)
- **MEVO 8/13 populados**: Sertralina, Fluoxetina, Lítio, Lamotrigina, Quetiapina, Olanzapina, Risperidona, Aripiprazol
- **5 MEVOs ausentes** (não no catálogo Mevo/Amil atual): Escitalopram 10mg, Metilfenidato LP, Lisdexanfetamina, Biperideno, Propranolol — documentado, aguarda verificação
- **Scripts criados**: `scripts/patch_v021_fixes.py`, `scripts/patch_v021_to_v03_codigos.py`
- **Gap analysis completo** vs. playbook: maioria dos gaps previamente identificados já estavam em v0.2.1 (surpresa positiva); gaps reais documentados em roadmap v0.3

---

## PRÓXIMO PASSO RECOMENDADO

1. **QA clínico de v0.6.0** no ambiente de preview Daktus (10 perfis críticos):
   - Alto risco suicida com acesso a meios → restrição de meios letais + verificar fórmulas risco recalibradas
   - Mulher grávida em uso de valproato → alerta GESTANTE+VPA
   - Esquizofrenia refratária → clozapina + hemograma + orientação clozapina nova
   - TDAH com TDM comórbido → Metilfenidato (condição `'nenhum' in substancias_uso`) + Bupropiona
   - Depressão com rastreio bipolar positivo → alerta BIPOLAR NÃO DESCARTADO
   - Agressividade com red flags orgânicos → Neurologia + alerta
   - Retorno medicamentoso → shortcut (sem internacao_psiq_previa e historico_familiar)
   - Autolesão sem diagnóstico de TPB → rastreio TPB + alerta TCD
   - **[Onda 3]** Primeiro episódio psicótico via motivo_consulta → alerta investigação orgânica
   - **[Onda 3]** Mania grave com psicose/agitação → mensagem urgência + SAMU
2. **Confirmar MEVOs ausentes** com equipe Amil (ver `history/session_022_report_farmacologia.md` §1)
3. **Confirmar Escitalopram MEVO 20945** — código inserido manualmente, não verificado no Mevo..xlsx
4. **v0.7.0 / Onda 5** — fármacos de 2ª linha (Fluvoxamina, Clomipramina, Guanfacina XR, Prazosina, Buspirona) + limpeza de perguntas sem conduta (32 UIDs A3)
5. Promover para v1.0.0 após QA clínico completo

---

## ARQUIVOS A LER NA PRÓXIMA SESSÃO

1. `AGENTE.md`
2. `HANDOFF.md` (este)
3. `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.6.0.json`

---

## NÃO SOBRESCREVER SEM REVISAR

- v0.6.0 é o artefato ativo — não alterar sem novo patch documentado
- v0.5.0 mantido como marco histórico (session_026)
- v0.4.0 mantido como marco histórico (session_025)
- v0.3.0 mantido como marco histórico (session_024)
- v0.2.3 mantido como marco histórico (session_023)
- v0.2.2 mantido como marco histórico (session_022)
- v0.2.1 mantido como marco histórico (fixes session_021)
- v0.2 mantido como marco histórico (primeira revisão conjunta)
- v0.1.2 mantido como base histórica
- branch-base: `main`
- TUSS: 100% populados ✅
- MEVO pendentes (9): Metilfenidato LP, Lisdexanfetamina, Biperideno, Propranolol, Bupropiona, Mirtazapina, Carbamazepina, Clozapina, Atomoxetina — não no catálogo Mevo/Amil atual
- Escitalopram MEVO 20945 — inserido manualmente pelo usuário, pendente verificação com Amil

---

## O QUE FOI FEITO — session_020 (2026-03-09)

**Skillização piloto: criação de `skills/daktus-json-coding/`**

Objetivo: alinhar o projeto à infraestrutura de skills Anthropic com uma skill piloto exportável, sem romper a arquitetura state-driven existente.

**Arquivos criados (8):**
- `skills/daktus-json-coding/SKILL.md` — skill autocontida com frontmatter YAML, ~300 linhas
- `skills/daktus-json-coding/references/DSL_CONDICIONAL.md` — tabela de operadores, 14 anti-patterns, regras de visibilidade
- `skills/daktus-json-coding/references/PADROES_REUTILIZAVEIS.md` — 6 padrões arquiteturais extraídos de projetos anteriores
- `skills/daktus-json-coding/references/ERROS_DOCUMENTADOS.md` — 8 erros documentados + checklist QA ampliado
- `skills/daktus-json-coding/scripts/validate_json.py` — validação estrutural generalizada (CLI)
- `skills/daktus-json-coding/assets/template_form_node.json`
- `skills/daktus-json-coding/assets/template_conduta_node.json`
- `skills/daktus-json-coding/assets/template_edge.json`

**Arquivos modificados (2):**
- `tools/skills/codificacao-json/SKILL.md` — nota de shim adicionada (direciona para skill exportável)
- `SKILL.md` (root) — seção aditiva reconhecendo camada `/skills/`

**Validação:**
- `validate_json.py` executado contra `amil-ficha_psiquiatria-v0.2.0.json` → 0 erros, 9 nodes, 8 edges, 79 IIDs

**Arquitetura de duas camadas:**
- `tools/skills/` = pipeline interno (inalterado)
- `skills/` = skills exportáveis padrão Anthropic (nova camada)
- `tools/*.md` = fontes canônicas transversais (inalterados)

---

## O QUE FOI FEITO — session_022 (2026-03-10)

**Correção estrutural + fármacos faltantes → v0.2.2:**

**Contexto:** Usuário revisou manualmente o nó de conduta de v0.2.1 e gerou vdraft (2).json com antipsicóticos divididos por dose. Sessão identificou 4 grupos de bugs estruturais e adicionou 11 fármacos essenciais do playbook.

- **BUG 1 corrigido (6 itens)**: Schema inconsistente (`conteudo`/`observacao` → `posologia`/`mensagemMedico`/`via`) em Quetiapina 50/100mg, Olanzapina 5/10mg, Risperidona 1/2mg
- **BUG 2 corrigido**: Aripiprazol com 2 MEVOs → dividido em Aripiprazol 10mg (MEVO 35461) + Aripiprazol 15mg (MEVO 32613), cada um com `condicionalMedicamento: "domiciliar"` e schema completo
- **BUG 3 corrigido**: `nomeMed` adicionado a Quetiapina 50/100mg (coberto pelo BUG 1); todos os 28 itens têm `nomeMed` ✅
- **BUG 4 corrigido**: 3 IDs não-canônicos (`cf9ooj5a`, `5p6fdllf`, `0k5sfwqn`) substituídos por UUID v4 ✅
- **11 fármacos adicionados**: Venlafaxina XR 75mg, Duloxetina 60mg, Bupropiona 150mg, Mirtazapina 15mg, Paroxetina 20mg, Valproato de sódio 500mg, Carbamazepina 200mg, Haloperidol 5mg, Clozapina 25mg, Atomoxetina 40mg, Clonazepam 0,5mg
- **MEVO**: 19/28 populados (9 sem código — não no catálogo Mevo/Amil)
- **Script criado**: `scripts/patch_vdraft2_to_v022.py`
- **Relatório gerado**: `history/session_022_report_farmacologia.md` — 7 pontos em aberto documentados
- **Validação final**: 0 erros estruturais ✅ | 9 nodes | 8 edges | 94 IIDs

---

## O QUE FOI FEITO — session_023 (2026-03-10)

**Análise de hiatos + fechamento briefing → v0.2.3:**

**Contexto:** Usuário entregou vdraft(3) com melhorias significativas (37 meds, 25 exames, 13 encaminhamentos, novas clinical expressions, comorbidades_clinicas, outros_medicamentos_relevantes) e briefing dos psiquiatras. Sessão realizou análise rigorosa de hiatos entre o briefing e o que o sistema entregava.

**Análise de hiatos realizada:**
- 11 diagnósticos do briefing: 10/11 cobertos (Agressividade ausente) ✅ + gap identificado
- motivo_consulta: 11 opções existentes cobriam parcialmente; 8 itens do briefing ausentes/parciais
- Encaminhamentos: Neuropsicólogo restrito a TDAH (TEA + 1º psicótico não cobertos)
- Exames: 4/4 itens laboratoriais do briefing presentes; avaliação neuropsicológica coberta como encaminhamento
- Histórico familiar psiquiátrico: ausente do formulário

**8 mudanças aplicadas em v0.2.3:**
1. `motivo_consulta` +3 opções: `irritabilidade`, `agressividade_comportamento`, `sonolencia_hipersonia`
2. `diagnostico_ativo` +1 opção: `agressividade` (TEI / F63.8)
3. `node-psiq-03-anamnese` +1 pergunta: `historico_familiar_psiq` (6 opções multiChoice)
4. `node-psiq-04-diagnostico` +1 pergunta: `sintomas_depressivos_presentes` (anedonia, apatia, astenia, isolamento_social, choro_frequente, inapetencia) — condicional a TDM/distimia/burnout/TPB/TAB
5. Encaminhamento Neuropsicólogo: condição expandida para TDAH + TEA + `primeiro_episodio_psicotico`
6. Conduta +1 mensagem: alerta de risco para terceiros (Agressividade)
7. Conduta +1 orientação: atividade física / sedentarismo (condicional a transtornos de humor/ansiedade)
8. `metadata.version` → "0.2.3"

**Resultado:** 0 BLOQUEANTES ✅ | 9 nodes | 8 edges | 105 IIDs | 37 meds | 25 exames | 13 enc. | 22 mensagens | 5 orientações

**Script criado:** `scripts/patch_vdraft3_to_v023.py`

---

## O QUE FOI FEITO — session_024 (2026-03-10)

**Camada de dissecção sindrômica intermediária → v0.3.0:**

**Contexto:** Usuário compartilhou análise extensa realizada com GPT utilizando Kaplan & Sadock (Comprehensive Psychiatry) e Dalgalarrondo (Psicopatologia). Problema central identificado: protocolo forte em entradas e saídas, mas sem camada intermediária de dissecção sindrômica. Fluxo atual: queixa ampla → diagnóstico ativo (salto) → conduta. Fluxo desejado: queixa curta → discriminador sindrômico curto → hipótese dominante/red flags → conduta.

**Plano aprovado (Onda 1 — v0.3.0):**
- 4 perguntas discriminadoras novas (todas condicionais, 0 no tronco universal)
- 4 bugs corrigidos (alertas que nunca disparavam, perguntas ausentes para burnout/TPB)
- 6 novas mensagens de conduta ao médico
- 3 condições de encaminhamento recalibradas

**17 mudanças aplicadas em v0.3.0:**

GRUPO A — 4 perguntas novas em `node-psiq-04-diagnostico`:
1. `bipolar_rastreio` (multiChoice, 5 opções) — detector bipolar antes de prescrever AD; condicionado a TDM/distimia/burnout ou `humor_deprimido`
2. `subtipo_ansioso` (choice, 6 opções) — discrimina TAG/pânico/fobia_social/TOC/TEPT/secundário; condicionado a `ansiedade_panico` ou diagnósticos ansiosos
3. `contexto_agressividade` (multiChoice, 6 opções) — diferencia mania/psicose/substância/orgânico/TPB/TEI; condicionado a `agressividade` ou `agressividade_comportamento`
4. `perfil_sono` (choice, 6 opções) — sono como modificador sindrômico; condicionado a `insomnia_sono` ou `sonolencia_hipersonia`

GRUPO B — 2 bug fixes em perguntas existentes:
5. `comportamento_suicida_recorrente` expressão: `esquizofrenia` → `selected_any(diagnostico_ativo, 'esquizofrenia', 'tpb')` (TPB + comportamento suicida recorrente agora ativa alerta TCD)
6. `episodio_atual_humor` expressão expandida: adiciona `burnout`, `tpb` (episódios de humor em burnout e TPB agora capturáveis)

GRUPO C — 1 bug fix em conduta:
7. TAB + Antidepressivo: `'bupropiona_snri'` → `'bupropiona'` (alerta nunca disparava para usuários de bupropiona)

GRUPO D — 6 novas mensagens ao médico:
8. BIPOLAR NÃO DESCARTADO — Não iniciar antidepressivo sem estabilizador
9. SONO — Redução da necessidade sem fadiga: rastreio positivo para hipomania/mania
10. AGRESSIVIDADE — Red flags orgânicos/neurológicos: investigação obrigatória
11. AGRESSIVIDADE — Contexto psicótico: avaliar antipsicótico e segurança imediata
12. SUBTIPO ANSIOSO — TOC provável: avaliar ERP antes de fechar diagnóstico
13. SUBTIPO ANSIOSO — TEPT provável: avaliar TF-CBT/EMDR antes de fechar diagnóstico

GRUPO E — 3 recalibrações de encaminhamento:
14. Neuropsicólogo: remove `primeiro_episodio_psicotico` — só TDAH/TEA conforme playbook
15. Neurologia: adiciona `selected_any(contexto_agressividade, 'red_flag_organico')` — red flags na agressividade → neurológico obrigatório
16. CAPS II: adiciona `agressividade` em `diagnostico_ativo` + `psicose_paranoia` em `contexto_agressividade`

17. `metadata.version` → "0.3.0"

**Resultado:** 0 BLOQUEANTES ✅ | 9 nodes | 8 edges | 111 IIDs | 37 meds | 25 exames | 13 enc. | 28 mensagens (+6) | 5 orientações

**Script criado:** `scripts/patch_v023_to_v030.py`

---

## O QUE FOI FEITO — session_025 (2026-03-10)

**Onda 2 — 4 eixos adicionais de discriminação sindrômica + shortcut retorno → v0.4.0:**

**Contexto:** Plano da Onda 2 aprovado pelo usuário com base no roadmap das sessões anteriores (Kaplan & Sadock + Dalgalarrondo). 5 problemas resolvidos: TPB capturado tarde, TDAH sem critérios completos, burnout/TDM não discriminados, substância como causa vs. comorbidade, UX em retornos.

**17 mudanças aplicadas em v0.4.0:**

GRUPO A — 6 perguntas novas:
1. `tipo_consulta` (choice, 3 opções) — Triagem Enfermagem; shortcut de retorno medicamentoso
2. `substancia_relacao_quadro` (choice, 4 opções) — após `audit_score`; relação causal substância/quadro
3. `tpb_rastreio` (multiChoice, 6 opções) — após `comportamento_suicida_recorrente`; entrada via `autolesao`
4. `tdah_discriminador` (multiChoice, 4 opções) — após `tdah_abuso_substancias_ativo`; valida critérios
5. `burnout_tdm_discriminador` (multiChoice, 5 opções) — após `bipolar_rastreio`; feições de TDM sobreposto
6. `tea_nivel_suporte` (choice, 3 opções) — após `tea_irritabilidade_grave`; nível de suporte DSM-5

GRUPO B — 2 modificações de expressão (shortcut retorno):
7. `internacao_psiq_previa`: visível apenas em `primeira_consulta`
8. `historico_familiar_psiq`: visível apenas em `primeira_consulta`

GRUPO C+D — 6 novas mensagens:
9. SUBSTÂNCIA COMO CAUSA PRIMÁRIA — tratar dependência antes de psicofármaco
10. AUTOMEDICAÇÃO — identificar e tratar sintoma-alvo subjacente
11. RASTREIO POSITIVO PARA TPB — avaliar critérios completos antes de farmacoterapia
12. TDAH — Critérios diagnósticos incompletos: confirmar antes de prescrever estimulante
13. BURNOUT COM FEIÇÕES DE TDM — considerar TDM comórbido não diagnosticado
14. TEA Nível 2/3 — Suporte multidisciplinar substancial indicado

GRUPO E — 2 recalibrações de encaminhamento:
15. CAPS-AD: adiciona `substancia_relacao_quadro == 'causa_primaria'`
16. Psicólogo TCD: adiciona `selected_any(tpb_rastreio, 'autolesao_suicidio_recorrente')`
17. `metadata.version` → "0.4.0"

**Resultado:** 0 BLOQUEANTES ✅ | 9 nodes | 8 edges | 117 IIDs | 37 meds | 25 exames | 13 enc. | 34 mensagens (+6) | 5 orientações

**Script criado:** `scripts/patch_v030_to_v040.py`

---

## O QUE FOI FEITO — session_026 (2026-03-11)

**Onda 3 — 7 gaps clínicos corrigidos + 2 bugs de segurança → v0.5.0:**

**Contexto:** Auditoria clínica pós-Onda 2 identificou 7 gaps remanescentes: 5 de cobertura (psicose gate estreito, urgência não suicida sem rota, agressividade sem iminência, TA fenotipagem pós-diagnóstico, TEA mascarado) e 2 bugs de segurança farmacológica (bupropiona sem proteção em TA, amônia sérica usando campo de lítio em contexto de VPA).

**14 mudanças aplicadas em v0.5.0:**

GRUPO A — Modificar expressão de pergunta existente:
1. `primeiro_episodio_psicotico` gate alargado: + `'sintomas_psicoticos' in motivo_consulta`

GRUPO B — 3 novas perguntas em `node-psiq-04-diagnostico`:
2. `tea_suspeita_clinica` (multiChoice, 5 opções) — após `tea_nivel_suporte`; TEA adulto mascarado sem diagnóstico rotulado
3. `agressividade_iminencia` (multiChoice, 6 opções) — após `contexto_agressividade`; ameaça atual, vítima, escalada, agressão física
4. `ta_fenotipo` (choice, 4 opções) — antes de `an_sinais_alarme`; restricao/compulsao+purgacao/compulsao_sem_comp/inapetencia

GRUPO C — 1 nova opção em `tdah_discriminador`:
5. `curso_continuo_sem_episodios` — proteção explícita contra falso-positivo TAB

GRUPO D — 1 nova pergunta em `node-psiq-05-farmacos`:
6. `sintomas_toxicidade_vpa` (multiChoice, 5 opções) — gate: `'valproato' in medicamentos_em_uso`

GRUPO E — 3 novas mensagens em `node-psiq-06-conduta`:
7. URGÊNCIA — MANIA GRAVE COM AGITAÇÃO/PSICOSE
8. AGRESSIVIDADE — RISCO IMINENTE PARA TERCEIROS
9. BULIMIA NERVOSA — Monitorar eletrólitos e risco de hipocalemia

GRUPO F — Modificar gate de pergunta existente:
10. `an_sinais_alarme`: + `ta_fenotipo == 'restricao_medo_engordar'`

GRUPO G — Recalibrações:
11. SAMU: + `selected_any(agressividade_iminencia, 'ameaca_atual', 'agressao_fisica_recente', 'vitima_identificada')`
12. Amônia sérica: `sintomas_toxicidade_litio` → `sintomas_toxicidade_vpa` (bug fix G7b)
13. Neuropsicólogo: + `selected_any(tea_suspeita_clinica, ...)`

GRUPO H — Bug fixes farmacológicos:
14. Bupropiona 150mg + 300mg: + `not selected_any(diagnostico_ativo, 'ta_bulimia', 'ta_anorexia')`

**Resultado:** 0 BLOQUEANTES ✅ | 9 nodes | 8 edges | 24 perguntas em node-psiq-04 | 37 mensagens (+3) | 7 farmacos node-psiq-05 (+1)

**Script criado:** `scripts/patch_v040_to_v050.py`

---

## O QUE FOI FEITO — session_027 (2026-03-11)

**Onda 4 — Quality & Precision Reform → v0.6.0:**

**Contexto:** Revisão clínica aprofundada via GPT (Kaplan & Sadock + Dalgalarrondo) identificou 6 áreas de melhoria sistêmica: fórmulas de risco suicida incorretas, bugs DSL boolean, conteúdo invertido em DEPRESSÃO LEVE, pergunta redundante `tdah_abuso_substancias_ativo`, códigos TUSS incorretos e 6 orientações ao paciente clinicamente necessárias.

**63 mudanças aplicadas em v0.6.0:**

GRUPO A — 3 fórmulas de risco suicida recalibradas:
1. `risco_suicidio_baixo`: corrigido de `ideacao_ativa is True` (contradição) para `ideacao_passiva is True and ideacao_ativa is False`
2. `risco_suicidio_intermediario`: expandido com cláusula OR para cobrir (ativa-sem-plano-sem-acesso) OR (tentativa-sem-ideação-atual)
3. `risco_suicidio_alto`: restringido para exigir concorrência plano+intenção+acesso OU tentativa+ideação-ativa/plano/intenção

GRUPO B — 2 bug fixes:
4. `causa_organica_investigada`: 4 exames corrigidos de `!= 'sim'` para `is False` (boolean DSL correto)
5. DEPRESSÃO LEVE: nome e conteúdo corrigidos (era PHQ-9 ≥15, agora PHQ-9 < 10 + intervenções psicossociais)

GRUPO C — Eliminação de redundância `tdah_abuso_substancias_ativo`:
6. Pergunta `P51a70f03-...` removida de node-psiq-04-diagnostico (24 → 23 perguntas)
7. Expressão derivada `not('nenhum' in substancias_uso)` adicionada em `clinicalExpressions`
8–10. Condições de Metilfenidato 10mg, Concerta LP 18mg, Ritalina LA 10mg atualizadas para `'nenhum' in substancias_uso`

GRUPO D — 20 correções TUSS + 1 nome ECG:
11–30. 18 códigos TUSS corrigidos (Hemograma ×2, TSH, Cálcio, Uréia, Ácido valpróico, ALT, AST, Amônia, Carbamazepina, Sódio, Glicose, HbA1c, Lipidograma, Triglicerídeos, Prolactina, Beta-HCG, VDRL, HIV1+HIV2)
31. ECG: nome atualizado para `"ECG convencional de até 12 derivações"`

GRUPO E — 6 novas orientações ao paciente:
32–37. Lítio (segurança+monitoramento), TAB (sinais de episódio), Substâncias (impacto no tto), TDAH (estratégias práticas), Transtornos alimentares (recuperação), Clozapina (vigilância hematológica)

GRUPO F — 22 correções de acento em campos de display (titulo, nome, descricao, label, conteudo)

**Resultado:** 0 BLOQUEANTES ✅ | 9 nodes | 8 edges | 126 IIDs | 23 perguntas node-psiq-04 (-1) | 11 orientações (+6) | 5 clinicalExpressions (+1)

**Script criado:** `scripts/patch_v050_to_v060.py`

---

## DIVERGÊNCIAS / OVERRIDES

- HANDOFF atualizado em 2026-03-11 (session_027) — sobrescreve estado de session_026
- v0.6.0 agora é o artefato ativo (substituindo v0.5.0)
- v0.5.0 mantido como marco histórico (session_026)
- v0.4.0 mantido como marco histórico (session_025)
- v0.3.0 mantido como marco histórico (session_024)
- v0.2.3 mantido como marco histórico (session_023)
- v0.2.2 mantido como marco histórico (session_022)
- v0.2.1 mantido como marco histórico (fixes session_021)
- Versão local do usuário tem prioridade sobre commits anteriores (confirmado session_024)
- Skill exportável `skills/daktus-json-coding/` criada em session_020 — ativa
- Deprecação de `tools/skills/codificacao-json/` só quando skill exportável provar-se funcional em 2+ especialidades
- Neuropsicólogo: condição recalibrada (session_026) — inclui `tea_suspeita_clinica`
