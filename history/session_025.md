# session_025 — Onda 2: 4 eixos discriminatórios + shortcut retorno → v0.4.0

**Data:** 2026-03-10
**Branch:** main
**Input:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.3.0.json`
**Output:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.4.0.json`
**Script:** `scripts/patch_v030_to_v040.py`
**Resultado da auditoria:** ✅ 0 BLOQUEANTES

---

## Contexto

A Onda 1 (v0.3.0) instalou a camada de dissecção sindrômica intermediária para 4 eixos:
- bipolar/unipolar (`bipolar_rastreio`)
- subtipo ansioso (`subtipo_ansioso`)
- agressividade (`contexto_agressividade`)
- sono (`perfil_sono`)

A Onda 2 estende essa lógica para 4 eixos adicionais e adiciona um shortcut de UX para retornos:

| Problema | Eixo |
|----------|------|
| TPB capturado tarde — só via diagnóstico, não via autolesão | `tpb_rastreio` |
| TDAH prescrito sem critérios obrigatórios | `tdah_discriminador` |
| Burnout e TDM compartilhando conduta sem discriminação | `burnout_tdm_discriminador` |
| Substância como causa vs. comorbidade (muda radicalmente o manejo) | `substancia_relacao_quadro` |
| Perguntas de intake único repetidas em todo retorno | `tipo_consulta` (shortcut) |

---

## Mudanças implementadas (17 total)

### GRUPO A — 6 novas perguntas

#### A1 — `tipo_consulta` (Triagem — Enfermagem)
- **Nodo:** `20e05d57-3dfa-43cb-b039-74279162a73a`
- **Inserção:** PRIMEIRA (antes de `motivo_consulta`)
- **Tipo:** `choice`
- **Condição:** sempre visível (`expressao: ""`)
- **Opções:**
  - `primeira_consulta` — Primeira consulta / avaliação inicial
  - `retorno_medicamentoso` — Retorno — Monitoramento medicamentoso
  - `retorno_clinico` — Retorno — Reavaliação clínica geral
- **Impacto:** gates os itens de intake único (GRUPO B)

#### A2 — `substancia_relacao_quadro` (node-psiq-04-diagnostico)
- **Inserção:** após `audit_score` (posição 7)
- **Tipo:** `choice`
- **Condição:** `not('nenhum' in substancias_uso)`
- **Opções:**
  - `causa_primaria` — Causa primária — sintomas surgem e melhoram com a abstinência
  - `agravante_descompensador` — Agravante — uso descompensa transtorno subjacente pré-existente
  - `automedicacao` — Automedicação — paciente usa a substância para aliviar sintomas psiquiátricos
  - `comorbidade_independente` — Comorbidade independente — coexistem sem relação causal clara
- **Impacto:** mensagens C1 (causa primária) e C2 (automedicação); recalibra CAPS-AD

#### A3 — `tpb_rastreio` (node-psiq-04-diagnostico)
- **Inserção:** após `comportamento_suicida_recorrente` (posição 12)
- **Tipo:** `multiChoice`
- **Condição:** `'autolesao' in motivo_consulta or 'tpb' in diagnostico_ativo`
- **Opções:**
  - `medo_abandono_frenetico`
  - `relacoes_instaveis_intensas`
  - `instabilidade_identidade`
  - `impulsividade_autoprejudicial`
  - `autolesao_suicidio_recorrente`
  - `afeto_instavel_reativo`
- **Impacto:** mensagem C3 (rastreio positivo); recalibra Psicólogo — TCD

#### A4 — `tdah_discriminador` (node-psiq-04-diagnostico)
- **Inserção:** após `tdah_abuso_substancias_ativo` (posição 14)
- **Tipo:** `multiChoice`
- **Condição:** `'deficit_atencao' in motivo_consulta or 'tdah' in diagnostico_ativo`
- **Opções:**
  - `inicio_infancia_confirmado`
  - `multiplos_contextos`
  - `prejuizo_funcional_claro`
  - `sem_explicacao_alternativa`
- **Impacto:** mensagem C4 (critérios incompletos — não prescrever estimulante)

#### A5 — `burnout_tdm_discriminador` (node-psiq-04-diagnostico)
- **Inserção:** após `bipolar_rastreio` (posição 4)
- **Tipo:** `multiChoice`
- **Condição:** `'esgotamento_burnout' in motivo_consulta or selected_any(diagnostico_ativo, 'burnout', 'tdm')`
- **Opções:**
  - `anedonia_universal`
  - `sem_melhora_fora_trabalho`
  - `culpa_desvalia`
  - `sem_contexto_ocupacional`
  - `duracao_criterio_tdm`
- **Impacto:** mensagem C5 (TDM comórbido não diagnosticado)

#### A6 — `tea_nivel_suporte` (node-psiq-04-diagnostico)
- **Inserção:** após `tea_irritabilidade_grave` (posição 16)
- **Tipo:** `choice`
- **Condição:** `'tea' in diagnostico_ativo`
- **Opções:**
  - `nivel_1_leve`
  - `nivel_2_moderado`
  - `nivel_3_grave`
- **Impacto:** mensagem D1 (suporte multidisciplinar urgente para nível 2/3)

---

### GRUPO B — Shortcut retorno: gateamento de perguntas de intake único

**Nodo:** `node-psiq-03-anamnese`

| UID | Expressão anterior | Nova expressão |
|-----|--------------------|----------------|
| `internacao_psiq_previa` | `""` | `tipo_consulta == 'primeira_consulta' or tipo_consulta == ''` |
| `historico_familiar_psiq` | `""` | `tipo_consulta == 'primeira_consulta' or tipo_consulta == ''` |

> `tipo_consulta == ''` garante backward compatibility para registros sem tipo_consulta.

---

### GRUPO C+D — 6 novas mensagens (node-psiq-06-conduta)

| # | Nome | Condição |
|---|------|----------|
| C1 | SUBSTÂNCIA COMO CAUSA PRIMÁRIA — tratar dependência antes de psicofármaco | `substancia_relacao_quadro == 'causa_primaria'` |
| C2 | AUTOMEDICAÇÃO — identificar e tratar sintoma-alvo subjacente | `substancia_relacao_quadro == 'automedicacao'` |
| C3 | RASTREIO POSITIVO PARA TPB — avaliar critérios completos antes de farmacoterapia | `selected_any(tpb_rastreio, ...) and not 'tpb' in diagnostico_ativo` |
| C4 | TDAH — Critérios diagnósticos incompletos: confirmar antes de prescrever estimulante | `('tdah' in diagnostico_ativo or 'deficit_atencao' in motivo_consulta) and not selected_any(tdah_discriminador, 'inicio_infancia_confirmado', 'multiplos_contextos')` |
| C5 | BURNOUT COM FEIÇÕES DE TDM — considerar TDM comórbido não diagnosticado | `selected_any(burnout_tdm_discriminador, ...) and not 'tdm' in diagnostico_ativo` |
| D1 | TEA Nível 2/3 — Suporte multidisciplinar substancial indicado | `selected_any(tea_nivel_suporte, 'nivel_2_moderado', 'nivel_3_grave')` |

---

### GRUPO E — Recalibrações de condições existentes

| Encaminhamento | Campo | Acréscimo |
|----------------|-------|-----------|
| CAPS-AD | `condicao` | `or substancia_relacao_quadro == 'causa_primaria'` |
| Psicólogo — TCD | `condicao` | `or selected_any(tpb_rastreio, 'autolesao_suicidio_recorrente')` |

---

## Ordem final das perguntas em node-psiq-04-diagnostico (v0.4.0)

| # | UID | Status |
|---|-----|--------|
| 1 | `internacao_indicada_p0` | existente |
| 2 | `episodio_atual_humor` | existente |
| 3 | `bipolar_rastreio` | existente |
| 4 | `burnout_tdm_discriminador` | **NOVO** |
| 5 | `subtipo_ansioso` | existente |
| 6 | `audit_score` | existente |
| 7 | `substancia_relacao_quadro` | **NOVO** |
| 8 | `primeiro_episodio_psicotico` | existente |
| 9 | `eps_presente` | existente |
| 10 | `esquizofrenia_refrataria` | existente |
| 11 | `comportamento_suicida_recorrente` | existente |
| 12 | `tpb_rastreio` | **NOVO** |
| 13 | `tdah_abuso_substancias_ativo` | existente |
| 14 | `tdah_discriminador` | **NOVO** |
| 15 | `tea_irritabilidade_grave` | existente |
| 16 | `tea_nivel_suporte` | **NOVO** |
| 17 | `contexto_agressividade` | existente |
| 18 | `perfil_sono` | existente |
| 19 | `sintomas_depressivos_presentes` | existente |
| 20 | `an_sinais_alarme` | existente |
| 21 | `clozapina_semana` | existente |

---

## Métricas comparativas

| Métrica | v0.3.0 | v0.4.0 |
|---------|--------|--------|
| IIDs totais | 111 | **117** (+6) |
| Perguntas (node-psiq-04-diagnostico) | 16 | **21** (+5) |
| Perguntas (Triagem Enfermagem) | N | **N+1** (`tipo_consulta`) |
| Mensagens de conduta | 28 | **34** (+6) |
| Encaminhamentos | 13 | 13 (condições recalibradas) |
| Perguntas no tronco universal | 0 novas | **0 novas** ✅ |
| Perguntas intake-only gateadas em retorno | 0 | **2** |
| Eixos de discriminação sindrômica | 4 | **8** |
| Erros de validação | 0 | **0** ✅ |

---

## Artefatos produzidos

- `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.4.0.json`
- `scripts/patch_v030_to_v040.py`

---

## Próximo passo recomendado

QA clínico de v0.4.0 no preview Daktus — 8 perfis críticos:

1. Alto risco suicida com acesso a meios → restrição de meios letais
2. Mulher grávida em uso de valproato → alerta gestante+VPA
3. Esquizofrenia refratária → clozapina + alerta hemograma
4. TDAH com TDM → prescrições simultâneas (Metilfenidato + Bupropiona)
5. Depressão com rastreio bipolar positivo → alerta BIPOLAR NÃO DESCARTADO
6. Agressividade com red flags orgânicos → Neurologia + alerta
7. **[novo]** Retorno medicamentoso → shortcut (sem internacao_psiq_previa e historico_familiar)
8. **[novo]** Autolesão sem TPB → rastreio TPB + alerta TCD
