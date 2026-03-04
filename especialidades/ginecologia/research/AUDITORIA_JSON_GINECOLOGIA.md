# Auditoria de Qualidade — Ficha de Ginecologia (Amil)
**Versao analisada:** `amil-ficha_ginecologia-vdraft (2).json` (vdraft2)
**Versao anterior:** `amil-ficha_ginecologia-vdraft.json` (vdraft1)
**Playbook de referencia:** `playbooks/playbook_ginecologia_auditado.md`
**Sessao 007:** 2026-03-03 — analise inicial (vdraft1) por Claude Code
**Sessao 008:** 2026-03-03 — atualizacao (vdraft2) + DOCX + feedback Dan
**Status:** Aguardando aplicacao das correcoes pendentes na plataforma Daktus

---

## Estrutura do JSON (8 nos — identica entre vdraft1 e vdraft2)

| No | Tipo | Questoes | Descricao |
|----|------|----------|-----------|
| N1 | custom | 9 | Triagem + rastreio historico |
| N2 | custom | 6 | Anamnese clinica |
| N3 | custom | 13 | Entrada de exames anteriores |
| C-ENF | conduct | 1 msg | Breakpoint enfermeiro |
| N4 | custom | 22 | Fluxo sintomatic |
| N5 | custom | 17 | Fluxo seguimento (resultados) |
| Summary | summary | 7 exprs | Processamento silencioso |
| C-MED | conduct | 38 ex / 23 med / 17 enc / 20 msg | Conduta medica |

**Roteamento:** pacientes com queixa cursam N4 E N5; sem queixa vao direto a N5.

---

## Summary — clinicalExpressions (vdraft2)

| Nome | Formula |
|------|---------|
| `alto_risco_mama` | `selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama')` |
| `rastreio_cervical_habitual` | `(age >= 25) and (age <= 64) and ('hpv_nunca' in hpv or 'hpv_mais_5a' in hpv) and (histerectomia_previa is False)` |
| `rastreio_cervical_intensificado` | `(age >= 25) and (not 'hpv_menos_1a' in hpv) and ((imunocomprometimento is True) or ('nic2_mais' in hist_oncologico)) and (histerectomia_previa is False)` |
| `co_teste_papanicolau` | `((imunocomprometimento is True) and (age >= 25) and (not 'papa_menos_1a' in papa)) or (('nic2_mais' in hist_oncologico) and (histerectomia_previa is True) and (not 'papa_menos_1a' in papa))` |
| `trh_indicada` | `('svm_moderado' in svm_intensidade or 'svm_grave' in svm_intensidade) and ('sem_ci_trh' in contraindicacao_trh)` |
| `espessamento_endometrial_significativo` | `('trouxe_usgtv' in exames_recentes) and ('usgtv_espessamento' in usgtv_achados) and ((espessura_endometrial > 4) and (not 'trh' in muc)) or ((espessura_endometrial > 8) and ('trh' in muc))` — **VER C1** |
| `poi_suspeita` | `('trouxe_lab' in exames_recentes) and (fsh_resultado > 25) and (age < 45)` |

---

## Resolucoes de vdraft1 → vdraft2

Os achados abaixo foram corrigidos entre versoes. Confirmados por comparacao direta dos JSONs.

| Achado (sessao 007) | Status | O que mudou |
|--------------------|--------|------------|
| C2: `pos_coital` → colposcopia direta | **RESOLVIDO** | `pos_coital` removido da condicao de colposcopia; agora aciona citopatologia (fluxo correto: citologia → se ASC-US+ → colpo) |
| C3: BI-RADS 3 → encaminhamento mastologia | **RESOLVIDO** | Encaminhamento mastologia BI-RADS 3 removido; BI-RADS 3 tratado so por USG + orientacao |
| C4: VitD para toda menopausa | **RESOLVIDO** | `'menopausa' in status_menstrual` removido da condicao de VitD |
| C6: DXA sem FR adicionais para menopausada <65 | **RESOLVIDO (parcial)** | `tabagismo` e `etilismo_pesado` adicionados ao gate <65; parenteses corrigidos |
| M1: HIV/HCV sem trigger de uma vez na vida | **RESOLVIDO** | HIV: `age >= 15 and age <= 65`; HCV: `age >= 18 and age <= 79` adicionados |
| M2: Lipidograma sem trigger por idade | **RESOLVIDO** | `age >= 40` adicionado como criterio standalone |
| M3: Galactorreia sem entry point isolado | **RESOLVIDO** | Expressao de galactorreia inclui agora `queixa_mamaria` |
| C1: Biopsia + CAF condicoes identicas | **PARCIALMENTE RESOLVIDO** | CAF/Conizacao agora so para NIC3; biopsia ainda NIC2 + NIC3 — aceitavel (biopsia confirma NIC2 antes de tratar) |

---

## Achados Pendentes — CRITICOS

---

### C1 — `espessamento_endometrial_significativo`: regressao de parenteses

**Formula atual (vdraft2):**
```
('trouxe_usgtv' in exames_recentes) and ('usgtv_espessamento' in usgtv_achados)
and ((espessura_endometrial > 4) and (not 'trh' in muc))
or ((espessura_endometrial > 8) and ('trh' in muc))
```

**Problema:** Devido a precedencia de operadores (AND > OR), o segundo branch avalia sem o gate de menopausa e sem o gate de USGTV. A expressao efetiva e:
```
(trouxe_usgtv AND usgtv_espessamento AND espessura>4 AND not_trh)
OR
(espessura>8 AND trh)   ← dispara para QUALQUER paciente com TRH e espessura>8, mesmo pre-menopausada
```

O gate `('menopausa' in status_menstrual)` presente no vdraft1 foi perdido.

**Impacto clinico:** Qualquer paciente usando TRH (incluindo pre-menopausada com SOP em uso de TRH ou ACO) com espessura > 8mm dispararia "espessamento significativo" → encaminhamento GO Oncologico + alerta de sangramento pos-menopausa.

**Formula correta:**
```
(('trouxe_usgtv' in exames_recentes) and ('usgtv_espessamento' in usgtv_achados))
or
(('menopausa' in status_menstrual) and
 (((espessura_endometrial > 4) and (not 'trh' in muc))
  or ((espessura_endometrial > 8) and ('trh' in muc))))
```

**Feedback Dan:** ___

---

### C2 — `espessamento_endometrial_significativo`: usos sem `is True`

**Contexto:** `espessamento_endometrial_significativo` e uma clinicalExpression (variavel booleana derivada do summary). Deve ser referenciada como `espessamento_endometrial_significativo is True` nas condicionais de conduta.

**Usos bare (sem `is True`) no vdraft2:**
- Encaminhamento "GO Oncologico — sangramento pos-menopausa": `... and espessamento_endometrial_significativo`
- Mensagem "Alerta: espessura endometrial aumentada": `espessamento_endometrial_significativo`

**Usos corretos (`is True`) — ja corretos:**
- Histeroscopia: `espessamento_endometrial_significativo is True` ✓

**Correcao:** substituir `espessamento_endometrial_significativo` por `espessamento_endometrial_significativo is True` em todos os usos bare.

**Feedback Dan:** ___

---

### C3 — `trh_indicada`: usos sem `is True`

**Usos bare (sem `is True`) no vdraft2:**
- Estradiol 1mg: `trh_indicada`
- Estradiol adesivo transdermico: `trh_indicada and (...)`
- Tibolona 2,5mg: `trh_indicada and (...)`
- Mensagem "TRH: janela de oportunidade": `trh_indicada`

**Nenhum uso usa `is True`.** Todos devem ser `trh_indicada is True`.

**Feedback Dan:** ___

---

### C4 — `alto_risco_mama`: usos sem `is True`

**Usos bare no vdraft2:**
- Mamografia: `... or alto_risco_mama` (no final da condicao)
- RM Mama: `alto_risco_mama or ('birads_4_5' in mamo_resultado)`

**Correcao:** `alto_risco_mama is True`.

**Feedback Dan:** ___

---

## Achados Pendentes — IMPORTANTES

---

### I1 — LSIL dispara colposcopia imediata

**Condicao colposcopia (vdraft2):**
```
('hpv_16_18' in hpv_resultado) or
(selected_any(citologia_reflexa_resultado, 'cito_asc_us', 'cito_lsil', 'cito_hsil_mais'))
```

**Problema:** `cito_lsil` aciona colposcopia imediata. O protocolo ASCCP/FEBRASGO 2024 para hrHPV nao-16/18 + LSIL na **primeira ocorrencia**: seguimento com DNA-HPV em 1 ano, nao colposcopia direta. Colposcopia imediata por LSIL so se persistente (≥2 resultados LSIL) em ≥30 anos com HPV positivo.

**Limitacao da ficha:** O campo unico `citologia_reflexa_resultado` nao diferencia "primeiro LSIL" de "LSIL persistente". Ha dois caminhos:
1. **Manter como esta** — opcao conservadora (nao perde lesao); gera alguma sobrerreferencia
2. **Separar por colpo imediata vs seguimento** — mais preciso, mais complexo

**Decisao do usuario (Dan):** Manter ou bifurcar?

**Feedback Dan:** ___

---

### I2 — `citologia_reflexa_resultado`: opcao padrao pode disparar falsos alertas

**Questao em N5:** `citologia_reflexa_resultado` com opcoes `['cito_negativa', 'cito_asc_us', 'cito_lsil', 'cito_hsil_mais', 'cito_nao_realizada']`.

Se `cito_nao_realizada` e a opcao preselected (padrao), toda paciente com hrHPV nao-16/18 que nao responder ativamente a questao tera a mensagem "citologia reflexa nao realizada — pendente" disparada automaticamente.

**Verificar:** qual e o `preselected` atual desta questao no JSON? O correto e que nao haja preselected, ou que seja uma opcao neutra.

**Citopatologia tambem dispara**: `or ('cito_nao_realizada' in citologia_reflexa_resultado)` — isso significa que o exame de Papanicolau vai aparecer na conduta quando a citologia nao foi realizada, que e intencional (lembrar o medico de pedila). Esse comportamento e correto.

**Ponto de atencao apenas:** confirmar que `preselected` da questao nao e `cito_nao_realizada`.

**Feedback Dan:** ___

---

### I3 — `hpv_resultado_nd` sem conduta definida

**Cenario:** paciente traz resultado de HPV mas o laudo nao especifica tipo ("resultado nao discriminado").

**Opcao:** `hpv_resultado_nd` existe em `hpv_resultado` mas nao ha mensagem, conduta ou encaminhamento para este caso. O medico fica sem orientacao.

**Sugestao:** adicionar mensagem: "HPV positivo — resultado nao discrimina subtipo. Solicitar novo exame com genotipagem parcial para conduta especifica."

**Feedback Dan:** ___

---

### I4 — `diu_contraindicacao` coletado mas sem uso em conduta

Da sessao 007, ainda pendente. A questao coleta contraindicacoes ao DIU (gestacao, DIP ativa, distorcao cavitaria...) mas nenhum item de conduta e gateado por ela. O sistema pode orientar insercao mesmo com gestacao ou DIP ativa declarada.

**Sugestao:** mensagem de alerta condicional: `selected_any(diu_contraindicacao, 'gestacao', 'dip_ativa') → "Insercao contraindicada no momento presente."`.

**Feedback Dan:** ___

---

## Achados Informacionais

---

### F1 — `alto_risco_mama` incompleto (lesoes proliferativas)

**Formula atual:** `selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama')`

**Playbook lista como alto risco tambem:** lesoes proliferativas (HLA, HDA, CLIS, CDIS) e familiar de 1o grau com CA mama/ovario.

Esses criterios nao estao capturados. Mulheres com essas historias nao teriam RM mama anual solicitada.

Ver tambem **Sugestao de Nova Pergunta (historia_familiar_ca)** abaixo — a adicao de `historia_familiar_ca` permite expandir `alto_risco_mama`.

**Feedback Dan:** ___

---

### F2 — Testosterona / DHEA / 17-OHP: comportamento esperado mas nao documentado

Os tres exames disparam com `not 'sem_sinais' in hiperandrogenismo_sinais`. A questao `hiperandrogenismo_sinais` so aparece em N4 quando ha `amenorreia_irregularidade` ou `sop` em comorbidades. Fora do N4, a variavel e nula e os exames nao disparam — comportamento correto.

**Ponto:** nao e um bug; e um padrao intencional. Apenas documentar para referencia futura.

---

## Sugestao de Nova Pergunta — `historia_familiar_ca`

**Justificativa (usuario Dan):** Canceres tem padroes hereditarios distintos. A ausencia de historia familiar na triagem de enfermagem e uma lacuna real:
- CA mama/ovario: BRCA1/2, familiar 1o grau
- CA endometrio/coloretal: Sindrome de Lynch
- CA colo do utero: HPV-dependente, pouca hereditariedade direta

**Localizacao sugerida:** N1 (triagem/enfermagem), sempre visivel

**Proposta:**
```
uid: historia_familiar_ca
label: Historia familiar de cancer
type: multiChoice
options:
  - sem_historia_familiar   [Sem historia familiar — preselected, exclusive]
  - fam_ca_mama             [Cancer de mama (familiar 1o grau)]
  - fam_ca_ovario           [Cancer de ovario (familiar 1o grau)]
  - fam_ca_endometrio       [Cancer de endometrio / suspeita de Lynch]
  - fam_ca_coloretal        [Cancer colorretal (Lynch)]
  - fam_brca_conhecido      [Mutacao BRCA confirmada na familia]
expressao: (nenhuma — sempre visivel)
```

**Impacto nas clinicalExpressions:**

`alto_risco_mama` deve expandir para:
```
(selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama'))
or (selected_any(historia_familiar_ca, 'fam_ca_mama', 'fam_ca_ovario', 'fam_brca_conhecido'))
```

Nova expression `lynch_suspeita` (para USGTV anual e encaminhamento Lynch):
```
selected_any(historia_familiar_ca, 'fam_ca_endometrio', 'fam_ca_coloretal')
```

`lynch_suspeita` permitiria: ativar USGTV anual para vigilancia endometrial, criar encaminhamento GO Oncologico para Lynch, sem depender apenas de `hist_oncologico` (que e a historia da propria paciente, nao familiar).

**Feedback Dan:** ___

---

## Achados que PASSARAM — verificados como conformes ao protocolo

| Topico | Verificacao | vdraft2 |
|--------|------------|---------|
| HPV primario, 25-64 anos | `rastreio_cervical_habitual is True` | OK ✓ |
| Imunossuprimida sem limite 64 | `rastreio_cervical_intensificado is True` sem age <= 64 | OK ✓ |
| HPV 16/18 → colposcopia direta | Sem citologia intermediaria | OK ✓ |
| pos_coital → citologia (nao colposcopia) | Movido da colposcopia para citopatologia | OK ✓ |
| hrHPV outros → citologia reflexa | `'hpv_outros_hr' in hpv_resultado` | OK ✓ |
| co_teste_papanicolau | `is True` + cobre imuno e NIC2+histerectomia | OK ✓ |
| LSIL + cito_lsil → colpo | ver I1 (adaptacao conservadora, discutivel) | ± |
| Mamografia 40-74 bienal | `age >= 40 and age <= 74 and mamo_nunca/mais_2a` | OK ✓ |
| BI-RADS 3 → USG + seguimento (sem mastologia) | Encaminhamento BI-RADS 3 removido | OK ✓ |
| USGTV nao universal | Sem trigger universal; apenas sintomas/indicacoes | OK ✓ |
| Histeroscopia por espessamento | `espessamento_endometrial_significativo is True` | OK ✓ |
| SUA refrataria → histeroscopia | `sua_refrataria is True and usgtv_polipos/espessamento` | OK ✓ |
| TSH so com indicacao clinica | Nao universal; exige queixa/comorbidade | OK ✓ |
| T4L so com TSH alterado | `tsh > 4.5 or tsh < 0.3` | OK ✓ |
| TRH com SVM + sem CI | `trh_indicada is True` nos cervicais; bare nas meds (ver C3) | ± |
| TRH: progesterona + histerectomia | `histerectomia_previa is False` na progesterona | OK ✓ |
| Estradiol vaginal: atrofia + sem CI | Condicao separada de TRH sistemica | OK ✓ |
| POI: FSH>25 + idade<45 | `poi_suspeita is True` | OK ✓ |
| DIP: alerta imediato | `suspeita_dip is True` | OK ✓ |
| HIV age 15-65 | Adicionado no vdraft2 | OK ✓ |
| HCV age 18-79 | Adicionado no vdraft2 | OK ✓ |
| Lipidograma age >= 40 | Adicionado no vdraft2 | OK ✓ |
| Alendronato T-score <= -2.5 | Condicao presente | OK ✓ |
| Encaminhamento GO Oncologico: NIC2+/NIC3/carcinoma | Presente | OK ✓ |
| Endometriose profunda → GO Cirurgico | `aine_refrataria or rm_endometriose ou endo_dor_refrataria` | OK ✓ |
| Lynch → encaminhamento especifico | `'lynch' in hist_oncologico` | OK ✓ |
| Perda de peso → encaminhamento Nutricao | `perda_peso_intensa is True` | OK ✓ |

---

## Resumo de Prioridades para Correcao (vdraft2 → vdraft3)

| # | Achado | Severidade | Acao necessaria |
|---|--------|-----------|-----------------|
| C1 | `espessamento_endometrial_significativo` formula OR quebrada (menopausa gate perdido) | CRITICO | Restaurar formula com parenteses e menopausa gate |
| C2 | `espessamento_endometrial_significativo` bare (sem `is True`) em encaminhamento e mensagem | CRITICO | Adicionar `is True` |
| C3 | `trh_indicada` bare em 4 condutas | CRITICO | Adicionar `is True` |
| C4 | `alto_risco_mama` bare em 2 condutas | CRITICO | Adicionar `is True` |
| I1 | LSIL → colposcopia imediata vs repetir citologia | IMPORTANTE | Decisao clinica de Dan |
| I2 | `citologia_reflexa_resultado`: verificar preselected | IMPORTANTE | Verificar na plataforma |
| I3 | `hpv_resultado_nd` sem conduta | IMPORTANTE | Adicionar mensagem fallback |
| I4 | `diu_contraindicacao` sem uso em conduta | MODERADO | Adicionar alerta de CI absoluta |
| F1 | `alto_risco_mama` sem lesoes proliferativas | INFORMACIONAL | Expandir com `historia_familiar_ca` |
| — | Adicionar questao `historia_familiar_ca` em N1 | SUGESTAO | Implementar em N1; expandir summary |

---

## Log de Feedback do Dan

*Preencher os campos `Feedback Dan:` inline em cada achado acima.*

**Data revisao:** ___
**Ferramenta de revisao:** ___

### Escopo excluido desta auditoria (decisoes ja tomadas)
- `trouxe_exames` / `age` como campos base
- Formato geral de queixa_principal com `nenhuma_queixa`
- Histerectomia_previa como proxy de menopausa cirurgica (conservador, intencional)
- Biópsia para NIC2 + NIC3 (biopsia confirma antes de CAF) — aceitavel como esta

---

*Sessao 007: analise inicial vdraft1 — Claude Code 2026-03-03*
*Sessao 008: atualizacao vdraft2 + DOCX + feedback usuario — Claude Code 2026-03-03*
*Proxima acao: Dan aplica C1-C4 na plataforma; decide I1; adiciona historia_familiar_ca em N1*
