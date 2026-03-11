# session_024.md — Dissecção sindrômica intermediária → v0.3.0

**Data:** 2026-03-10
**Fase:** Fase 5 — QA iterativo
**Especialidade:** Psiquiatria
**Base:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.3.json`
**Output:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.3.0.json`

---

## Resumo da sessão

O usuário compartilhou análise extensa realizada com GPT utilizando Kaplan & Sadock (Comprehensive Psychiatry) e Dalgalarrondo (Psicopatologia), identificando que o protocolo v0.2.3, embora forte em entradas e saídas clínicas, carecia de uma camada intermediária de dissecção sindrômica.

**Problema central diagnosticado:**
- Fluxo atual: `queixa ampla → diagnóstico ativo (salto) → detalhe → conduta`
- Fluxo desejado: `queixa curta → discriminador sindrômico curto → hipótese dominante/red flags → conduta`

A sessão planejou e implementou a **Onda 1** da reforma do protocolo (v0.3.0), incluindo 4 perguntas discriminadoras, 4 bugs corrigidos, 6 novas mensagens e 3 encaminhamentos recalibrados — totalizando 17 mudanças.

**Resultado:** 0 BLOQUEANTES ✅ | 9 nodes | 8 edges | 111 IIDs | 37 medicamentos | 25 exames | 13 encaminhamentos | 28 mensagens (+6) | 5 orientações | metadata.version = "0.3.0" ✅

---

## Diagnóstico estrutural — v0.2.3

### Problema central
O protocolo não tinha camada entre a entrada de queixa e a conduta. Um paciente com múltiplas queixas (ex.: comportamento agressivo + confusão) caía apenas em "agressividade + neurologia" porque o protocolo não tinha trilha para dissecar a síndrome antes de rotulá-la.

### Bugs confirmados na auditoria (Kaplan + Dalgalarrondo)

| # | Onde | Problema | Impacto |
|---|------|---------|---------|
| B1 | TAB + Antidepressivo (mensagem) | `bupropiona_snri` não existe em `medicamentos_em_uso`; deveria ser `bupropiona` | Alerta nunca disparava para usuários de bupropiona com TAB |
| B2 | `comportamento_suicida_recorrente` | Condicionado só a `esquizofrenia`; TPB com suicídio recorrente não ativava alerta TCD | Subdiagnóstico em TPB de alto risco |
| B3 | `episodio_atual_humor` | Ausente para `burnout` e `tpb`, que cursam com episódios de humor | Perda de informação clínica relevante |
| B4 | Neuropsicólogo | `primeiro_episodio_psicotico is True` incluído; playbook limita a TDAH/TEA (incerteza diagnóstica) | Encaminhamento inadequado em psicose aguda |

---

## Princípios de reforma (aprovados pelo usuário)

1. **Só pergunta o que muda conduta** — exame, encaminhamento, medicamento, retorno, urgência ou hipótese dominante
2. **Discriminador curto** — máximo 5–6 opções por questão discriminadora
3. **Gate P0 permanece condicionado à ideação passiva** — não redesenhar como universal
4. **Perguntas condicionadas por nodo prévio** — restrição técnica fixa do JSON
5. **Preservar conduta existente** — sem reescrever o que já funciona
6. **Síndrome antes do diagnóstico** — novas perguntas disparadas por `motivo_consulta`, não por `diagnostico_ativo`
7. **Progressão revelada** — menor número possível de perguntas para cada caso
8. **Substâncias e sono como modificadores transversais**

---

## Mudanças aplicadas — 17 total

### GRUPO A — 4 perguntas novas em node-psiq-04-diagnostico

| # | UID | Tipo | Condição | Inserção |
|---|-----|------|----------|---------|
| A1 | `bipolar_rastreio` | multiChoice (5 opções) | `selected_any(diagnostico_ativo, 'tdm', 'distimia', 'burnout') or 'humor_deprimido' in motivo_consulta` | após `episodio_atual_humor` |
| A2 | `subtipo_ansioso` | choice (6 opções) | `selected_any(motivo_consulta, 'ansiedade_panico') or selected_any(diagnostico_ativo, 'tag', 'panico', 'fobia_social', 'toc', 'tept')` | após `bipolar_rastreio` |
| A3 | `contexto_agressividade` | multiChoice (6 opções) | `'agressividade' in diagnostico_ativo or 'agressividade_comportamento' in motivo_consulta` | após `tea_irritabilidade_grave` |
| A4 | `perfil_sono` | choice (6 opções) | `selected_any(motivo_consulta, 'insomnia_sono', 'sonolencia_hipersonia')` | após `contexto_agressividade` |

**bipolar_rastreio — opções:**
- `sem_historico_bipolar` (exclusive) — Sem histórico de episódios maníacos ou hipomaníacos
- `elevacao_humor_previa` — Episódios prévios de euforia, expansividade ou irritabilidade marcante
- `reducao_sono_sem_fadiga` — Já ficou dias dormindo muito menos sem sentir cansaço
- `grandiosidade_episodica` — Episódios de autoconfiança exagerada, impulsividade ou decisões arriscadas
- `tab_documentado` — TAB já diagnosticado previamente

**subtipo_ansioso — opções:**
- `preocupacao_difusa_persistente` — Preocupação difusa, persistente, em múltiplos domínios (TAG)
- `crises_abruptas_esquiva` — Crises abruptas e intensas com medo de nova crise ou esquiva (Pânico)
- `medo_avaliacao_social` — Medo intenso de situações sociais ou de avaliação (Fobia social)
- `obsessoes_compulsoes` — Pensamentos intrusivos repetitivos + rituais/compulsões (TOC)
- `trauma_intrusao_evitacao` — Evento traumático com revivescência, evitação e hipervigilância (TEPT)
- `ansiedade_secundaria` — Ansiedade claramente relacionada a substância, estimulante ou condição clínica

**contexto_agressividade — opções:**
- `mania_agitacao` — Euforia/irritabilidade intensa + aceleração do pensamento + redução do sono
- `psicose_paranoia` — Delírios persecutórios ou alucinatórios associados ao comportamento
- `substancia_intoxicacao` — Comportamento claramente associado a intoxicação ou abstinência
- `red_flag_organico` — Red flags neuro: confusão, amnésia do episódio, aura, déficit focal ou início tardio
- `desregulacao_tpb` — Padrão de desregulação intensa com medo de abandono e impulsividade crônica (TPB)
- `episodico_tei` — Episódico, desproporcional, impulsivo, sem premeditação, com remorso após o ato (TEI)

**perfil_sono — opções:**
- `insonia_iniciacao` — Dificuldade para iniciar o sono (latência prolongada)
- `insonia_manutencao` — Despertares frequentes ou dificuldade para voltar a dormir
- `despertar_precoce` — Despertar muito cedo sem conseguir voltar a dormir (sugestivo de melancolia)
- `hipersonia_cansaco` — Sonolência excessiva com cansaço marcado (hipersonia)
- `reducao_necessidade_sem_fadiga` — Dormiu muito menos do habitual sem sentir cansaço (rastreio: hipomania/mania)
- `pesadelos_trauma` — Pesadelos recorrentes ou sono perturbado relacionado a evento traumático (TEPT)

### GRUPO B — 2 correções de expressão em perguntas existentes

| # | UID | De | Para |
|---|-----|-----|------|
| B2 | `comportamento_suicida_recorrente` | `'esquizofrenia' in diagnostico_ativo` | `selected_any(diagnostico_ativo, 'esquizofrenia', 'tpb')` |
| B3 | `episodio_atual_humor` | `('tdm' in diagnostico_ativo) or ('distimia' in diagnostico_ativo) or ('tab' in diagnostico_ativo)` | `selected_any(diagnostico_ativo, 'tdm', 'distimia', 'tab', 'burnout', 'tpb')` |

### GRUPO C — 1 bug fix em mensagem de conduta

| # | Mensagem | De | Para |
|---|---------|-----|------|
| C1 | TAB + Antidepressivo | `'bupropiona_snri'` | `'bupropiona'` |

### GRUPO D — 6 novas mensagens ao médico

| # | Nome | Condição |
|---|------|---------|
| D1 | BIPOLAR NÃO DESCARTADO — Não iniciar antidepressivo sem estabilizador | `selected_any(bipolar_rastreio, 'elevacao_humor_previa', 'reducao_sono_sem_fadiga', 'grandiosidade_episodica', 'tab_documentado') and not 'tab' in diagnostico_ativo` |
| D2 | SONO — Redução da necessidade sem fadiga: rastreio positivo para hipomania/mania | `perfil_sono == 'reducao_necessidade_sem_fadiga'` |
| D3 | AGRESSIVIDADE — Red flags orgânicos/neurológicos: investigação obrigatória | `selected_any(contexto_agressividade, 'red_flag_organico')` |
| D4 | AGRESSIVIDADE — Contexto psicótico: avaliar antipsicótico e segurança imediata | `selected_any(contexto_agressividade, 'psicose_paranoia')` |
| D5 | SUBTIPO ANSIOSO — TOC provável: avaliar ERP antes de fechar diagnóstico | `subtipo_ansioso == 'obsessoes_compulsoes' and not 'toc' in diagnostico_ativo` |
| D6 | SUBTIPO ANSIOSO — TEPT provável: avaliar TF-CBT/EMDR antes de fechar diagnóstico | `subtipo_ansioso == 'trauma_intrusao_evitacao' and not 'tept' in diagnostico_ativo` |

### GRUPO E — 3 recalibrações de encaminhamento

| # | Encaminhamento | De | Para | Por quê |
|---|--------------|-----|------|---------|
| E1 | Neuropsicólogo | `selected_any(diagnostico_ativo, 'tdah', 'tea') or primeiro_episodio_psicotico is True` | `selected_any(diagnostico_ativo, 'tdah', 'tea')` | Playbook: neuropsicologia apenas para incerteza diagnóstica neurodesenvolvimento |
| E2 | Neurologia | `primeiro_episodio_psicotico is True or selected_any(comorbidades_clinicas, 'epilepsia')` | `... or selected_any(contexto_agressividade, 'red_flag_organico')` | Red flags na agressividade → neurológico obrigatório |
| E3 | CAPS II | `('esquizofrenia' in diagnostico_ativo) or (comportamento_suicida_recorrente is True)` | `selected_any(diagnostico_ativo, 'esquizofrenia', 'agressividade') or (comportamento_suicida_recorrente is True) or selected_any(contexto_agressividade, 'psicose_paranoia')` | Psicose na agressividade e diagnóstico de agressividade também indicam CAPS II |

---

## Ordem das perguntas em node-psiq-04-diagnostico após v0.3.0

| # | UID | Condicional |
|---|-----|-------------|
| 1 | `internacao_indicada_p0` | `risco_suicidio_alto is True` |
| 2 | `episodio_atual_humor` | `selected_any(diagnostico_ativo, 'tdm', 'distimia', 'tab', 'burnout', 'tpb')` **[B3]** |
| 3 | `bipolar_rastreio` | `selected_any(diagnostico_ativo, 'tdm', 'distimia', 'burnout') or 'humor_deprimido' in motivo_consulta` **[NOVO]** |
| 4 | `subtipo_ansioso` | `selected_any(motivo_consulta, 'ansiedade_panico') or selected_any(diagnostico_ativo, 'tag', 'panico', 'fobia_social', 'toc', 'tept')` **[NOVO]** |
| 5 | `audit_score` | `'alcool_uso_problematico' in substancias_uso` |
| 6 | `primeiro_episodio_psicotico` | `'esquizofrenia' in diagnostico_ativo` |
| 7 | `eps_presente` | `'esquizofrenia' in diagnostico_ativo` |
| 8 | `esquizofrenia_refrataria` | `'esquizofrenia' in diagnostico_ativo` |
| 9 | `comportamento_suicida_recorrente` | `selected_any(diagnostico_ativo, 'esquizofrenia', 'tpb')` **[B2]** |
| 10 | `tdah_abuso_substancias_ativo` | `'tdah' in diagnostico_ativo` |
| 11 | `tea_irritabilidade_grave` | `'tea' in diagnostico_ativo` |
| 12 | `contexto_agressividade` | `'agressividade' in diagnostico_ativo or 'agressividade_comportamento' in motivo_consulta` **[NOVO]** |
| 13 | `perfil_sono` | `selected_any(motivo_consulta, 'insomnia_sono', 'sonolencia_hipersonia')` **[NOVO]** |
| 14 | `sintomas_depressivos_presentes` | `selected_any(diagnostico_ativo, 'tdm', 'distimia', 'burnout', 'tpb', 'tab') or 'humor_deprimido' in motivo_consulta` |
| 15 | `an_sinais_alarme` | `'ta_anorexia' in diagnostico_ativo` |
| 16 | `clozapina_semana` | `'clozapina' in medicamentos_em_uso` |

---

## Impacto clínico por eixo

### Eixo bipolar/unipolar
- `bipolar_rastreio` detecta histórico de mania/hipomania antes do rótulo diagnóstico formal
- Qualquer opção positiva (exceto `sem_historico_bipolar`) + ausência de `tab` em `diagnostico_ativo` → alerta BIPOLAR NÃO DESCARTADO
- `reducao_sono_sem_fadiga` também dispara alerta SONO específico (sinal cardinal de hipomania)
- Bug B1 corrigido: alerta TAB + Antidepressivo agora dispara corretamente para bupropiona

### Eixo ansioso
- `subtipo_ansioso` converte "ansiedade" em categoria acionável para encaminhamento
- `obsessoes_compulsoes` → alerta ERP (mesmo sem diagnóstico de TOC fechado)
- `trauma_intrusao_evitacao` → alerta TF-CBT/EMDR (mesmo sem diagnóstico de TEPT fechado)
- Médico recebe orientação de terapia específica antes de formalizar o diagnóstico

### Eixo agressividade
- `contexto_agressividade` transforma o alerta genérico em uma trilha sindrômica com 6 subtipos
- `red_flag_organico` → alerta + Neurologia obrigatória (E2)
- `psicose_paranoia` → alerta + CAPS II (E3)
- Bug B2 corrigido: `comportamento_suicida_recorrente` agora aparece também para TPB

### Eixo sono
- `perfil_sono` torna sono um modificador sindrômico ativo (antes: só orientação de saída)
- `reducao_necessidade_sem_fadiga` → alerta de hipomania/mania (combinado com `bipolar_rastreio`)
- `pesadelos_trauma` → reforço de TEPT (combinado com `subtipo_ansioso`)
- `despertar_precoce` → suporte diagnóstico para TDM melancólico

---

## Artefatos produzidos

| Arquivo | Ação |
|---------|------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.3.0.json` | criado — v0.3.0 final |
| `scripts/patch_v023_to_v030.py` | criado — script de patch |
| `HANDOFF.md` | atualizado — session_024 documentada, artefato ativo = v0.3.0 |
| `ESTADO.md` | atualizado — session_024 como última sessão integrada |
| `history/session_024.md` | criado — este arquivo |

---

## Roadmap aprovado — Ondas 2 e 3

### Onda 2 — v0.4.0 (sessão futura)

| O que entra | Justificativa |
|-------------|--------------|
| `tipo_consulta` → shortcut "retorno medicamentoso" | Reduz perguntas em retornos puros de monitorização |
| `substancia_relacao_quadro` — relação substância/quadro (causa, agravante, comorbidade) | Substâncias como modificador transversal, não só listagem |
| TPB mini-discriminador (critérios básicos na entrada) | Detectar TPB antes do rótulo fechado |
| TDAH/TEA separação granular (início precoce, múltiplos contextos) | Distinguir TDAH real de imitadores depressivos/ansiosos |
| Burnout vs. TDM discriminador | Vínculo ocupacional + melhora fora do trabalho |
| Fármacos 2ª linha: Fluvoxamina, Clomipramina, Guanfacina XR, Prazosina, Buspirona | Completar arsenal terapêutico |

### Onda 3 — v1.0.0 prep (sessão futura)

| O que entra | Justificativa |
|-------------|--------------|
| Transtornos alimentares: fenótipo (restrição/compulsão/purgação/imagem corporal) | Falta fenótipo inicial além de sinais de alarme |
| Psicose: subtipo provável (primária/afetiva/substância/orgânica) | Subtipagem geral além de 1º episódio |
| Limpeza de perguntas sem impacto na conduta | Auditoria final |
| Calibração fina de todas as condições | Revisão antes de v1.0 |

---

## Próxima sessão recomendada

1. **QA clínico de v0.3.0** no preview Daktus (6 perfis críticos):
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta GESTANTE+VPA + Valproato como prescrição
   - Esquizofrenia refratária → indicação clozapina + alerta hemograma
   - TDAH com TDM comórbido → prescrições simultâneas (Metilfenidato + Bupropiona)
   - **[novo]** Depressão com rastreio bipolar positivo → alerta BIPOLAR NÃO DESCARTADO
   - **[novo]** Agressividade com red flags orgânicos → alerta + encaminhamento Neurologia
2. **Confirmar MEVOs** com equipe Amil (ver `history/session_022_report_farmacologia.md`)
3. **v0.4.0** — Onda 2 conforme roadmap acima
