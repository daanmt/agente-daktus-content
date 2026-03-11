# session_028 — Onda 5: Reforma Sindrômica → v0.7.0

**Data:** 2026-03-11
**Branch:** main
**Input:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.6.1.json`
**Output:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.7.0.json`
**Script:** `scripts/patch_v061_to_v070.py`
**Resultado da auditoria:** ✅ 0 BLOQUEANTES

---

## Contexto

O protocolo pensa sindromicamente (perguntas discriminadoras coletam fenótipo clínico antes do diagnóstico formal), mas a conduta (prescrição + exames) responde majoritariamente a `diagnostico_ativo`. Resultado: pacientes sem rótulo CID, mas com síndrome bem caracterizada, ficam sem conduta.

Solução (GPT, Kaplan & Sadock + Dalgalarrondo): inserir camada de **expressões derivadas de fenótipo** no summary node, e ampliar condições de medicamentos/exames com OR conservador — diagnóstico formal **OU** candidatura operacional por síndrome.

**Nota:** v0.6.1 foi gerado manualmente pelo usuário a partir de v0.6.0 (pasta de psiquiatria adicionada ao projeto). Os fixes de v0.6.0 (risco_baixo, causa_organica) já estavam presentes; apenas `tdah_abuso_substancias_ativo` derivado estava ausente.

---

## Mudanças implementadas (92 total)

### GRUPO X — Fixes residuais de v0.6.0 ausentes no v0.6.1

#### X2 — `tdah_abuso_substancias_ativo` derivado

Adicionado ao array `clinicalExpressions` do summary node:
```json
{
  "id": "expr-tdah-abuso-derivado-001",
  "name": "tdah_abuso_substancias_ativo",
  "expressao": "not('nenhum' in substancias_uso)"
}
```

> X1 (risco_suicidio_baixo) e X3 (causa_organica) já estavam corretos em v0.6.1 — dispensados.

---

### GRUPO A — 20 expressões derivadas de fenótipo e candidatura terapêutica

**Nó:** `summary-6e3e3703-1337-46f0-8b08-55e814f0f8ef` → `data.clinicalExpressions` (append)

#### A1 — 12 fenótipos base (sem dependência cruzada)

| `name` | `id` | `expressao` (resumida) |
|--------|------|------------------------|
| `bipolaridade_nao_descartada` | `expr-bipolar-nd-001` | `selected_any(bipolar_rastreio, 'elevacao_humor_previa', ...) or 'reducao_necessidade_sem_fadiga' in perfil_sono` |
| `burnout_com_tdm_provavel` | `expr-burnout-tdm-001` | `selected_any(burnout_tdm_discriminador, 'anedonia_universal', ..., 'duracao_criterio_tdm')` |
| `tag_provavel` | `expr-tag-provavel-001` | `'preocupacao_difusa_persistente' in subtipo_ansioso` |
| `panico_provavel` | `expr-panico-provavel-001` | `'crises_abruptas_esquiva' in subtipo_ansioso` |
| `toc_provavel` | `expr-toc-provavel-001` | `'obsessoes_compulsoes' in subtipo_ansioso` |
| `tept_provavel` | `expr-tept-provavel-001` | `'trauma_intrusao_evitacao' in subtipo_ansioso` |
| `fobia_social_provavel` | `expr-fobia-social-001` | `'medo_avaliacao_social' in subtipo_ansioso` |
| `tdah_confirmado_operacional` | `expr-tdah-confirmado-001` | `selected_any(tdah_discriminador, 'inicio_infancia_confirmado') and selected_any(..., 'curso_continuo_sem_episodios')` |
| `anorexia_provavel` | `expr-anorexia-provavel-001` | `'restricao_medo_engordar' in ta_fenotipo` |
| `bulimia_provavel` | `expr-bulimia-provavel-001` | `'compulsao_purgacao' in ta_fenotipo` |
| `tcap_provavel` | `expr-tcap-provavel-001` | `'compulsao_sem_compensacao' in ta_fenotipo` |
| `depressao_unipolar_provavel` | `expr-dep-unipolar-001` | `selected_any(episodio_atual_humor, 'depressao_leve', ...) and not(bipolaridade_nao_descartada is True) and not('causa_primaria' in substancia_relacao_quadro)` |

#### A2 — 7 candidatos terapêuticos (referenciam A1)

| `name` | `id` | `expressao` (resumida) |
|--------|------|------------------------|
| `candidato_isrs_depressao` | `expr-cand-isrs-dep-001` | `selected_any(diagnostico_ativo, 'tdm', 'distimia') or (depressao_unipolar_provavel is True) or (burnout_com_tdm_provavel is True)` |
| `candidato_isrs_ansiedade` | `expr-cand-isrs-ans-001` | `selected_any(diagnostico_ativo, 'tag', 'panico', ..., 'tept') or (tag_provavel is True) or ... or (tept_provavel is True)` |
| `candidato_estabilizador_mania` | `expr-cand-estab-001` | `('tab' in diagnostico_ativo) or selected_any(episodio_atual_humor, 'mania', 'hipomania')` |
| `candidato_estimulante` | `expr-cand-estimulante-001` | `(('tdah' in diagnostico_ativo) or (tdah_confirmado_operacional is True)) and ('nenhum' in substancias_uso) and not(bipolaridade_nao_descartada is True)` |
| `candidato_atomoxetina` | `expr-cand-atomoxetina-001` | `('tdah' in diagnostico_ativo) or (tdah_confirmado_operacional is True)` |
| `candidato_lisdex_tcap` | `expr-cand-lisdex-001` | `('ta_tcap' in diagnostico_ativo) or (tcap_provavel is True)` |
| `candidato_antipsicotico_psicose` | `expr-cand-ap-psicose-001` | `(primeiro_episodio_psicotico is True) or selected_any(contexto_agressividade, 'psicose_paranoia')` |

#### A3 — Agregador (último, múltiplas referências)

| `name` | `id` | `expressao` |
|--------|------|-------------|
| `sindrome_em_investigacao` | `expr-sind-invest-001` | `('sem_diagnostico' in diagnostico_ativo) and ((candidato_isrs_depressao is True) or (candidato_isrs_ansiedade is True) or (candidato_estimulante is True) or (candidato_estabilizador_mania is True) or (candidato_antipsicotico_psicose is True))` |

---

### GRUPO B — Expansão da condição node-04 → node-05

**Nó:** `node-psiq-04-diagnostico` → `data.condicionais[0]` (onde `linkId == "node-psiq-05-farmacos"`)

**Cláusulas OR adicionadas:**
```
or (candidato_isrs_depressao is True) or (candidato_isrs_ansiedade is True)
or (candidato_estimulante is True) or (candidato_estabilizador_mania is True)
or (candidato_antipsicotico_psicose is True)
```

---

### GRUPO C — Reforma OR conservador nos medicamentos (22 atualizações)

#### C1 — Antidepressivos ISRS/SNRI/outros (11 medicamentos, OR append)

| nomeMed | Cláusula OR adicionada |
|---------|------------------------|
| `Escitalopram 10mg` | `or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True)) or (tag_provavel is True) or (panico_provavel is True)` |
| `Sertralina 50mg` | `or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True)) or (candidato_isrs_ansiedade is True)` |
| `Fluoxetina 20mg` | `or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True)) or (bulimia_provavel is True) or (toc_provavel is True)` |
| `Venlafaxina XR 37,5mg` | `or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True)) or (tag_provavel is True) or (tept_provavel is True)` |
| `Venlafaxina XR 75mg` | idem |
| `Duloxetina 60mg` | `or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True)) or (tag_provavel is True)` |
| `Bupropiona 150mg` | `or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True) and not(anorexia_provavel is True) and not(bulimia_provavel is True))` |
| `Bupropiona 300mg` | idem |
| `Mirtazapina 15mg` | `or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))` |
| `Mirtazapina 30mg` | idem |
| `Paroxetina 20mg` | `or (tept_provavel is True) or (panico_provavel is True) or (fobia_social_provavel is True)` |

#### C2 — TDAH (7 medicamentos)

| nomeMed | Ação | Nova condição |
|---------|------|---------------|
| `Metilfenidato 10mg` | REPLACE | `('tdah' in diagnostico_ativo or tdah_confirmado_operacional is True) and 'nenhum' in substancias_uso and not(bipolaridade_nao_descartada is True)` |
| `Concerta LP 18mg` | REPLACE | idem |
| `Ritalina LA 10mg` | REPLACE | idem |
| `Lisdexanfetamina 30mg` (×2) | OR append | `or (tdah_confirmado_operacional is True) or (tcap_provavel is True)` |
| `Lisdexanfetamina 70mg` | OR append | idem |
| `Atomoxetina 40mg` | OR append | `or (tdah_confirmado_operacional is True)` |
| `Atomoxetina 80mg` | OR append | idem |

#### C3 — Estabilizadores e antipsicótico (3 medicamentos, OR append)

| nomeMed | Cláusula OR adicionada |
|---------|------------------------|
| `Lítio 300mg` | `or (candidato_estabilizador_mania is True)` |
| `Valproato de sódio 500mg` | `or (candidato_estabilizador_mania is True)` |
| `Haloperidol 5mg` | `or (candidato_antipsicotico_psicose is True)` |

---

### GRUPO D — Exames e perguntas (5 atualizações)

#### D1 — TSH (TUSS 40316521, condição litio/tdm)

- **Cláusula adicionada:** `or (depressao_unipolar_provavel is True) or (burnout_com_tdm_provavel is True)`
- (O segundo TSH — para primeiro episódio psicótico — não foi alterado)

#### D2 — Beta-HCG (TUSS 40305759)

- **Cláusula adicionada:** `or (candidato_estabilizador_mania is True)`
- Razão: candidato a lítio/valproato sem diagnóstico formal ainda precisa do baseline de gravidez

#### D3 — `ecg_indicado_psico` (pergunta node-psiq-05-farmacos)

- **Cláusula adicionada:** `or (candidato_estimulante is True) or (candidato_isrs_depressao is True) or (candidato_isrs_ansiedade is True)`

#### D4 — `sintomas_psicoticos_humor` (pergunta node-psiq-05-farmacos)

- **Cláusula adicionada:** `or (primeiro_episodio_psicotico is True) or selected_any(contexto_agressividade, 'psicose_paranoia')`

#### D5 — `causa_organica_investigada` (pergunta node-psiq-05-farmacos)

- **Cláusula adicionada:** `or (candidato_antipsicotico_psicose is True)`

---

### GRUPO E — Orientações ao paciente (4 atualizações)

#### E1 — "Sobre seu diagnóstico" (ID `047563fa-1333-45d9-9d95-173d5d6e8179`)

- **Condição anterior:** `not('sem_diagnostico' in diagnostico_ativo)`
- **Condição nova:** `not('sem_diagnostico' in diagnostico_ativo) or (sindrome_em_investigacao is True)`

#### E2 — "Sono e rotina" (ID `6912d79d-8b00-4283-8d63-a3759f91c734`)

- **Condição anterior:** `not('sem_diagnostico' in diagnostico_ativo)`
- **Condição nova:** `not('sem_diagnostico' in diagnostico_ativo) or (sindrome_em_investigacao is True)`

#### E3 — "Transtorno Bipolar — reconhecer sinais" (ID `orient-tab-episodio-001`)

- **Condição anterior:** `'tab' in diagnostico_ativo`
- **Condição nova:** `('tab' in diagnostico_ativo) or (bipolaridade_nao_descartada is True)`

#### E4 — NOVA — "Quadro em avaliação — o que esperar" (ID `orient-investigacao-001`)

- **Condição:** `sindrome_em_investigacao is True`
- Conteúdo: orientação para pacientes em investigação sindrômica pré-diagnóstico (o que esperar, quando buscar atendimento, sinais de alerta)

---

### GRUPO F — Correções de acento em campos de display

**38 correções** aplicadas recursivamente a campos `titulo`, `descricao`, `label`, `nome`, `conteudo`, `narrativa`. Campos técnicos (UIDs, expressões DSL, condições) inalterados.

Principais correções (além das já aplicadas na Onda 4):
- `feicoes` → `feições` | `relacao` → `relação` | `abstinencia` → `abstinência`
- `instaveis` → `instáveis` | `periodos` → `períodos` | `aceleracao` → `aceleração`
- `hipotese` → `hipótese` | `intencoes` → `intenções` | `emocoes` → `emoções`
- `comunicacao` → `comunicação` | `compulsao` → `compulsão` | `vomito` → `vômito`
- `inapetencia` → `inapetência` | `sonolencia` → `sonolência` | `sedacao` → `sedação`
- `Restricao` → `Restrição` | `Nivel ` → `Nível ` | `Nao ` → `Não `

---

## Notas de implementação

- **Estrutura das edges**: condições de roteamento armazenadas em `node["data"]["condicionais"][0]["condicao"]` do nó origem (não no array `edges`, que tem `data: {}`). GRUPO B atualiza `condicionais[0]` de `node-psiq-04-diagnostico`.
- **Dois TSH**: v0.6.1 tem dois exames TSH com TUSS `40316521` — um para litio/tdm (atualizado em D1), outro para `primeiro_episodio_psicotico` (inalterado).
- **Lisdexanfetamina 30mg ×2**: duas entradas distintas com mesmo nomeMed e mesma condição original — ambas atualizadas corretamente pelo loop.
- **Ordenação de expressões A1→A2→A3**: fundamental para que expressões derivadas que referenciam outras (ex: `candidato_isrs_depressao` referencia `depressao_unipolar_provavel`) sejam processadas após suas dependências.
- **OR conservador**: medicamentos não tiveram condições originais removidas — apenas cláusulas OR adicionadas ao final. Lamotrigina e Carbamazepina mantidas diagnosis-based conforme análise clínica.
- **X1 dispensado**: `risco_suicidio_baixo` já estava correto em v0.6.1 (`ideacao_passiva is True and ideacao_ativa is False`). Mesma para X3 (`causa_organica_investigada is False`).

---

## Métricas comparativas

| Métrica | v0.6.1 | v0.7.0 |
|---------|--------|--------|
| clinicalExpressions | 4 (3 risco + sexo_fem_ie) | **25** (+1 tdah_derivado + 20 novas) |
| Medicamentos com condição expandida | 0 | **22** (11 ISRS/SNRI + 7 TDAH + 3 estab/AP) |
| Exames com condição expandida | 0 | **2** (TSH litio + Beta-HCG) |
| Perguntas node-05 expandidas | 0 | **3** (ecg, sintomas_psicoticos, causa_organica) |
| Edge node-04→node-05 expandida | não | **sim** (+5 cláusulas OR) |
| Orientações ao paciente | 11 | **12** (+1: orient-investigacao-001) |
| Orientações com condição expandida | 0 | **3** (diagnóstico, sono/rotina, TAB) |
| Acentos corrigidos (Onda 5) | — | **38** instâncias |
| IIDs totais | 126 | **127** (+1 orientação) |
| Erros de validação | 0 | **0** ✅ |

---

## Artefatos produzidos

- `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.7.0.json`
- `scripts/patch_v061_to_v070.py`

---

## Próximo passo recomendado

1. **QA clínico de v0.7.0 no preview Daktus** — perfis críticos (expandidos dos 10 anteriores):
   - **[Novo — Onda 5]** Depressão provável sem diagnóstico formal → Escitalopram via `candidato_isrs_depressao`
   - **[Novo — Onda 5]** TAG provável sem diagnóstico → Escitalopram/Sertralina/Venlafaxina via `tag_provavel`
   - **[Novo — Onda 5]** TDAH confirmado operacionalmente sem CID → Metilfenidato via `tdah_confirmado_operacional`
   - **[Novo — Onda 5]** Síndrome em investigação → orient-investigacao-001 exibida
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta gestante+VPA
   - Esquizofrenia refratária → clozapina + hemograma + orientação clozapina
   - TDAH com TDM → Metilfenidato + Bupropiona
   - Depressão com rastreio bipolar positivo → alerta BIPOLAR NÃO DESCARTADO
   - **[Onda 3]** Primeiro episódio psicótico → alerta investigação orgânica
   - **[Onda 3]** Mania grave com psicose/agitação → mensagem urgência + SAMU
2. **Confirmar MEVOs** com equipe Amil (ver `history/session_022_report_farmacologia.md`)
3. **v0.8.0 / Onda 6** — fármacos de 2ª linha (Fluvoxamina, Clomipramina, Guanfacina XR, Prazosina, Buspirona) + limpeza de perguntas sem conduta (32 UIDs A3)
4. Promover para v1.0.0 após QA clínico completo
