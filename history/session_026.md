# session_026 — Onda 3: 7 gaps corrigidos + 2 bugs de segurança → v0.5.0

**Data:** 2026-03-11
**Branch:** main
**Input:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.4.0.json`
**Output:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.5.0.json`
**Script:** `scripts/patch_v040_to_v050.py`
**Resultado da auditoria:** ✅ 0 BLOQUEANTES

---

## Contexto

A auditoria clínica pós-Onda 2 (v0.4.0) identificou 7 gaps remanescentes com base em Kaplan & Sadock e Dalgalarrondo. Os gaps foram agrupados em 5 de cobertura e 2 bugs de segurança farmacológica:

| Gap | Categoria | Solução |
|-----|-----------|---------|
| G1 | Cobertura | `primeiro_episodio_psicotico` locked em diagnóstico rotulado — gate alargado |
| G2 | Cobertura | Urgência não suicida (mania grave, psicose florida) sem rota explícita |
| G3 | Cobertura | Agressividade sem gate de iminência para terceiros |
| G4 | Cobertura | TDAH sem proteção explícita contra falso-positivo TAB |
| G5 | Cobertura | TA fenotipagem apenas pós-diagnóstico rotulado |
| G6 | Cobertura | TEA adulto mascarado entra sem rastreio estruturado |
| G7a | Bug segurança | Bupropiona sugerida em bulimia/anorexia (contraindicação ignorada) |
| G7b | Bug segurança | Amônia sérica condicionada a `sintomas_toxicidade_litio` (campo de lítio) em contexto de VPA |

---

## Mudanças implementadas (14 total)

### GRUPO A — Modificar expressão de pergunta existente

#### A1 — `primeiro_episodio_psicotico` — gate alargado
- **Nodo:** `node-psiq-04-diagnostico`
- **Expressão anterior:** `'esquizofrenia' in diagnostico_ativo`
- **Nova expressão:** `'esquizofrenia' in diagnostico_ativo or 'sintomas_psicoticos' in motivo_consulta`
- **Impacto:** A investigação orgânica obrigatória (DD: TAB+psicose, TDM psicótico, substância, causa orgânica) agora dispara mesmo quando o médico ainda não rotulou o diagnóstico — justamente quando o suporte clínico é mais necessário.

---

### GRUPO B — 3 novas perguntas em node-psiq-04-diagnostico

#### B1 — `tea_suspeita_clinica` (multiChoice)
- **Posição:** 17 (após `tea_nivel_suporte`)
- **Condição:** `not('tea' in diagnostico_ativo) and selected_any(motivo_consulta, 'outra_queixa', 'deficit_atencao')`
- **Opções:**
  - `dificuldade_inferir_social`
  - `comunicacao_literal`
  - `rotinas_rigidas`
  - `interesses_restritos_intensos`
  - `sensibilidade_sensorial`
- **Impacto:** Neuropsicólogo recalibrado para incluir TEA suspeito (G3)

#### B2 — `ta_fenotipo` (choice)
- **Posição:** 22 (antes de `an_sinais_alarme`)
- **Condição:** `'comportamento_alimentar' in motivo_consulta or selected_any(diagnostico_ativo, 'ta_anorexia', 'ta_bulimia', 'ta_tcap')`
- **Opções:**
  - `restricao_medo_engordar`
  - `compulsao_purgacao`
  - `compulsao_sem_compensacao`
  - `inapetencia_sem_distorcao`
- **Impacto:** Ativa `an_sinais_alarme` via fenotipo (F1); mensagem E3 (BN+purgação)

#### B3 — `agressividade_iminencia` (multiChoice)
- **Posição:** 19 (após `contexto_agressividade`)
- **Condição:** `'agressividade' in diagnostico_ativo or 'agressividade_comportamento' in motivo_consulta`
- **Opções:**
  - `sem_risco_iminente` (preselected, exclusive)
  - `ameaca_atual`
  - `vitima_identificada`
  - `acesso_vitima`
  - `escalada_recente`
  - `agressao_fisica_recente`
- **Impacto:** Mensagem E2 (risco iminente para terceiros); SAMU expandido (G1)

---

### GRUPO C — Modificar opção existente

#### C1 — Nova opção em `tdah_discriminador`
- **Opção:** `curso_continuo_sem_episodios` — "Sintomas continuos desde a infancia, sem periodos de aceleracao, hipossonia e euforia/irritabilidade marcante intercalados"
- **Justificativa:** Proteção explícita contra falso-positivo TAB (mania tem curso episódico; TDAH tem curso persistente desde infância)

---

### GRUPO D — Nova pergunta em node-psiq-05-farmacos

#### D1 — `sintomas_toxicidade_vpa` (multiChoice)
- **Condição:** `'valproato' in medicamentos_em_uso`
- **Opções:**
  - `nenhum_vpa` (preselected, exclusive)
  - `confusao_vpa`
  - `nausea_vomito_vpa`
  - `tremor_vpa`
  - `sedacao_excessiva`
- **Impacto:** Corrige bug G7b — Amônia sérica agora referencia campo correto

---

### GRUPO E — 3 novas mensagens em node-psiq-06-conduta

| # | Nome | Condição |
|---|------|----------|
| E1 | URGÊNCIA — MANIA GRAVE COM AGITAÇÃO/PSICOSE | `selected_any(episodio_atual_humor, 'mania') and selected_any(contexto_agressividade, 'mania_agitacao', 'psicose_paranoia')` |
| E2 | AGRESSIVIDADE — RISCO IMINENTE PARA TERCEIROS | `selected_any(agressividade_iminencia, 'ameaca_atual', 'vitima_identificada', 'acesso_vitima', 'escalada_recente', 'agressao_fisica_recente')` |
| E3 | BULIMIA NERVOSA — Monitorar eletrólitos e risco de hipocalemia | `ta_fenotipo == 'compulsao_purgacao' or 'ta_bulimia' in diagnostico_ativo` |

---

### GRUPO F — Modificar gate de pergunta existente

#### F1 — `an_sinais_alarme` — gate ampliado
- **Expressão anterior:** `'ta_anorexia' in diagnostico_ativo`
- **Nova expressão:** `'ta_anorexia' in diagnostico_ativo or ta_fenotipo == 'restricao_medo_engordar'`

---

### GRUPO G — Recalibrações

| Item | Mudança |
|------|---------|
| SAMU 192 (G1) | + `selected_any(agressividade_iminencia, 'ameaca_atual', 'agressao_fisica_recente', 'vitima_identificada')` |
| Amônia sérica (G2) | `sintomas_toxicidade_litio` → `sintomas_toxicidade_vpa` + `confusao` → `confusao_vpa` |
| Neuropsicólogo (G3) | + `selected_any(tea_suspeita_clinica, 'dificuldade_inferir_social', ...)` |

---

### GRUPO H — Bug fixes farmacológicos

| Medicamento | Fix |
|-------------|-----|
| Bupropiona 150mg XL | + `and not selected_any(diagnostico_ativo, 'ta_bulimia', 'ta_anorexia')` |
| Bupropiona 300mg XL | + `and not selected_any(diagnostico_ativo, 'ta_bulimia', 'ta_anorexia')` |

---

## Ordem final das perguntas em node-psiq-04-diagnostico (v0.5.0)

| # | UID | Status |
|---|-----|--------|
| 1 | `internacao_indicada_p0` | existente |
| 2 | `episodio_atual_humor` | existente |
| 3 | `bipolar_rastreio` | existente |
| 4 | `burnout_tdm_discriminador` | existente (Onda 2) |
| 5 | `subtipo_ansioso` | existente |
| 6 | `audit_score` | existente |
| 7 | `substancia_relacao_quadro` | existente (Onda 2) |
| 8 | `primeiro_episodio_psicotico` | existente **[A1: gate alargado]** |
| 9 | `eps_presente` | existente |
| 10 | `esquizofrenia_refrataria` | existente |
| 11 | `comportamento_suicida_recorrente` | existente |
| 12 | `tpb_rastreio` | existente (Onda 2) |
| 13 | `tdah_abuso_substancias_ativo` | existente |
| 14 | `tdah_discriminador` | existente **[C1: +1 opção]** |
| 15 | `tea_irritabilidade_grave` | existente |
| 16 | `tea_nivel_suporte` | existente (Onda 2) |
| **17** | **`tea_suspeita_clinica`** | **NOVO (B1)** |
| 18 | `contexto_agressividade` | existente |
| **19** | **`agressividade_iminencia`** | **NOVO (B3)** |
| 20 | `perfil_sono` | existente |
| 21 | `sintomas_depressivos_presentes` | existente |
| **22** | **`ta_fenotipo`** | **NOVO (B2)** |
| 23 | `an_sinais_alarme` | existente **[F1: gate ampliado]** |
| 24 | `clozapina_semana` | existente |

---

## Métricas comparativas

| Métrica | v0.4.0 | v0.5.0 |
|---------|--------|--------|
| Perguntas (node-psiq-04-diagnostico) | 21 | **24** (+3) |
| Perguntas (node-psiq-05-farmacos) | 6 | **7** (+1) |
| Mensagens de conduta | 34 | **37** (+3) |
| Encaminhamentos recalibrados | — | **2** (SAMU, Neuropsicólogo) |
| Exames corrigidos | — | **1** (Amônia sérica) |
| Medicamentos corrigidos | — | **2** (Bupropionas) |
| Gates de pergunta recalibrados | — | **2** (primeiro_episodio_psicotico, an_sinais_alarme) |
| Eixos de discriminação sindrômica | 8 | **10** |
| Erros de validação | 0 | **0** ✅ |

---

## Artefatos produzidos

- `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.5.0.json`
- `scripts/patch_v040_to_v050.py`

---

## Próximo passo recomendado

QA clínico de v0.5.0 no preview Daktus — 10 perfis críticos:

1. Alto risco suicida com acesso a meios → restrição de meios letais
2. Mulher grávida em uso de valproato → alerta gestante+VPA
3. Esquizofrenia refratária → clozapina + hemograma
4. TDAH com TDM → Metilfenidato + Bupropiona (verificar bloqueio se TA presente)
5. Depressão com rastreio bipolar positivo → alerta BIPOLAR NÃO DESCARTADO
6. Agressividade com red flags orgânicos → Neurologia + alerta
7. Retorno medicamentoso → shortcut (sem internacao_psiq_previa e historico_familiar)
8. Autolesão sem diagnóstico de TPB → rastreio TPB + alerta TCD
9. **[novo Onda 3]** Sintomas psicóticos via motivo_consulta sem esquizofrenia → primeiro_episodio_psicotico aparece + investigação orgânica
10. **[novo Onda 3]** Mania grave com contexto psicótico → mensagem urgência E1 + SAMU ativado
