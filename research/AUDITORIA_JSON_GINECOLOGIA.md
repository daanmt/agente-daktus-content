# Auditoria de Qualidade — Ficha de Ginecologia (Amil)
**Arquivo:** `amil-ficha_ginecologia-vdraft.json`
**Playbook de referencia:** `playbooks/playbook_ginecologia_auditado.md`
**Data:** 2026-03-03
**Ferramenta:** Claude Code (Sonnet 4.6)
**Status:** Aguardando revisao e feedback de Dan

---

## Estrutura do JSON (8 nos)

| No | ID (prefixo) | Tipo | Questoes |
|----|-------------|------|----------|
| N1 | `node-bb461b9b` | custom | 9 — triagem + rastreio historico |
| N2 | `node-23cfdf6d` | custom | 6 — anamnese clinica |
| N3 | `node-9c3fbfda` | custom | 13 — entrada de exames anteriores |
| C-ENF | `conduta-a9b1a09a` | conduct | 1 mensagem (breakpoint enfermeiro) |
| N4 | `node-860d135b` | custom | 22 — fluxo sintomatic |
| N5 | `node-30532994` | custom | 17 — fluxo seguimento (resultados) |
| Summary | `summary-ginecoamil-v1` | summary | 7 clinicalExpressions |
| C-MED | `conduta-07915c23` | conduct | 38 exames / 23 meds / 17 enc / 20 msgs |

**Roteamento C-ENF:** Pacientes com queixa (nao `nenhuma_queixa`) cursam N4 E N5. Pacientes sem queixa pulo N4 e vao direto a N5.

---

## Summary — clinicalExpressions

| Nome | Formula |
|------|---------|
| `alto_risco_mama` | `selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama')` |
| `rastreio_cervical_habitual` | `(age >= 25) and (age <= 64) and ('hpv_nunca' in hpv or 'hpv_mais_5a' in hpv) and (histerectomia_previa is False)` |
| `rastreio_cervical_intensificado` | `(age >= 25) and (not 'hpv_menos_1a' in hpv) and ((imunocomprometimento is True) or ('nic2_mais' in hist_oncologico)) and (histerectomia_previa is False)` |
| `co_teste_papanicolau` | `((imunocomprometimento is True) and (age >= 25) and (not 'papa_menos_1a' in papa)) or (('nic2_mais' in hist_oncologico) and (histerectomia_previa is True) and (not 'papa_menos_1a' in papa))` |
| `trh_indicada` | `('svm_moderado' in svm_intensidade or 'svm_grave' in svm_intensidade) and ('sem_ci_trh' in contraindicacao_trh)` |
| `espessamento_endometrial_significativo` | `(('trouxe_usgtv' in exames_recentes) and ('usgtv_espessamento' in usgtv_achados)) or (((espessura_endometrial > 4 and not 'trh' in muc) or (espessura_endometrial > 8 and 'trh' in muc)) and ('menopausa' in status_menstrual))` |
| `poi_suspeita` | `('trouxe_lab' in exames_recentes) and (fsh_resultado > 25) and (age < 45)` |

---

## Achados da Auditoria

### CRITICOS — afetam conduta clinica diretamente

---

#### C1 — Biopsia e Coizacao com condicao identica

**Campos:** `Biopsia do colo uterino` / `Traquelectomia (CAF/conizacao)`
**Condicao atual (ambas):** `('colpo_nic2' in colposcopia_resultado) or ('colpo_nic3' in colposcopia_resultado)`

**Problema:** As duas condutas aparecem simultaneamente para qualquer NIC2 ou NIC3. Clinicamente incorreto:
- NIC2 → biopsia (confirmacao histologica) pode ser necessaria antes da CAF
- NIC3 → conizacao e o tratamento; biopsia pode ser dispensavel
- Ambas simultaneas geram confusao clinica (procedimento diagnostico + terapeutico como se fossem equivalentes)

**Correcao sugerida:**
- Biopsia: `'colpo_nic2' in colposcopia_resultado` (confirmacao antes de tratar)
- CAF/Conizacao: `'colpo_nic2' in colposcopia_resultado or 'colpo_nic3' in colposcopia_resultado` (ou bifurcar por grau)

**Feedback Dan:** ___

---

#### C2 — `pos_coital` dispara colposcopia direta

**Campo:** Colposcopia (cérvice uterina e vagina)
**Condicao:** `('hpv_16_18' in hpv_resultado) or ('pos_coital' in sua_padrao) or (selected_any(citologia_reflexa_resultado, 'cito_asc_us', 'cito_lsil', 'cito_hsil_mais'))`

**Problema:** Sangramento pos-coital nao e indicacao direta de colposcopia pelo protocolo ASCCP/FEBRASGO. O fluxo correto seria investigar com HPV/citologia primeiro. Colposcopia direta sem HPV pre-coleta pode antecipar desnecessariamente o procedimento e sair do caminho clinico do protocolo.

**Correcao sugerida:** Remover `'pos_coital' in sua_padrao` da condicao de colposcopia. Garantir que `pos_coital` dispare USGTV + HPV como investigacao inicial.

**Feedback Dan:** ___

---

#### C3 — BI-RADS 3 dispara encaminhamento para Mastologia

**Campo:** `Mastologia — BI-RADS 3 (seguimento semestral)`
**Condicao:** `'birads_3' in mamo_resultado`

**Problema:** O playbook especifica BI-RADS 3 = "seguimento semestral com USG" — achado provavelmente benigno, sem indicacao de encaminhamento obrigatorio para mastologia. O encaminhamento e mandatorio apenas a partir de BI-RADS 4. Gerar referencia para BI-RADS 3 e sobrereferenciamento.

**Correcao sugerida:** Converter o encaminhamento BI-RADS 3 em orientacao/mensagem ("Repetir mamografia + USG em 6 meses, sem urgencia") e manter encaminhamento mastologia apenas para BI-RADS >= 4.

**Feedback Dan:** ___

---

#### C4 — Vitamina D acionada para toda mulher em menopausa

**Campo:** `Vitamina D 25-HIDROXI`
**Condicao atual:** `('osteoporose' in comorbidades) or (t_score <= -1.0) or ('menopausa' in status_menstrual or histerectomia_previa is True) or ('drc' in comorbidades) or ('cirurgia_bariatrica' in comorbidades) or (poi_suspeita is True)`

**Problema:** O trecho `'menopausa' in status_menstrual or histerectomia_previa is True` nao tem nenhum criterio adicional — dispara VitD para TODA mulher em menopausa. O playbook restringe explicitamente: "nao e rastreamento universal — indicada apenas para DXA alterada, POI, fratura por fragilidade, DRC, sindrome disabsortiva/bariatrica e corticoterapia cronica."

**Correcao sugerida:** Remover `'menopausa' in status_menstrual` como criterio isolado. Manter: `(t_score <= -1.0) or (poi_suspeita is True) or ('osteoporose' in comorbidades) or ('drc' in comorbidades) or ('cirurgia_bariatrica' in comorbidades)`.

**Feedback Dan:** ___

---

#### C5 — `diu_contraindicacao` coletado mas nunca usado

**Campo:** `diu_contraindicacao` (N5)
**Expressao:** `'deseja_inserir' in diu_situacao`
**Opcoes:** `['sem_ci_diu', 'ca_mama_atual', 'sangramento_nao_investigado_diu', 'dip_ativa', 'distorcao_cavidade', 'gestacao']`

**Problema:** A questao captura contraindiacoes absolutas ao DIU (inclusive gestacao e DIP ativa), mas nenhuma condicao de conduta e gateada por ela. O sistema pode apresentar dipirona para insercao, HIV/Chlamydia pre-DIU, e USGTV para insercao mesmo quando ha contraindicacao absoluta — sem alerta ou bloqueio.

**Correcao sugerida:** Adicionar mensagem de alerta condicional: `'dip_ativa' in diu_contraindicacao or 'gestacao' in diu_contraindicacao` → "Insercao contraindicada neste momento".

**Feedback Dan:** ___

---

#### C6 — DXA acionada para toda menopausa <65 sem FR adicionais

**Campo:** Densitometria ossea
**Trecho da condicao:** `(age < 65) and ('menopausa' in status_menstrual)`

**Problema:** O playbook exige para pos-menopausa <65 anos: risco aumentado avaliado por FRAX ou presenca de FR clinicos (IMC <21, fratura previa, corticoide cronicos, tabagismo, etilismo, artrite reumatoide, historia familiar de fratura de quadril). A condicao atual dispara DXA para qualquer mulher menopausada <65, independentemente de risco.

**Correcao sugerida:** Para `age < 65 and menopausa`, adicionar pelo menos um FR: `('corticoide_cronico' in muc) or ('tabagismo' in historia_social) or ('etilismo_pesado' in historia_social)`.

**Feedback Dan:** ___

---

### MODERADOS — impactam rastreio ou UX

---

#### M1 — HIV e HCV sem trigger de "uma vez na vida"

**Condicoes atuais:**
- HIV: `(not 'sem_FR_ist_med' in fr_ist_med) or ('deseja_inserir' in diu_situacao)`
- HCV: `(not 'sem_FR_ist_med' in fr_ist_med)`

**Problema:** O playbook recomenda HIV ao menos uma vez entre 15-65 anos e HCV ao menos uma vez entre 18-79 anos, independentemente de fatores de risco. A condicao atual exige que a paciente declare FR — pacientes sem FR declarado nunca recebem a recomendacao de rastreio unico.

**Correcao sugerida (opcional):** Adicionar `or (age >= 15 and age <= 65)` para HIV e `or (age >= 18 and age <= 79)` para HCV — ou adicionar mensagem orientando rastreio unico mesmo sem FR, se a plataforma suportar logica de "nunca rastreado".

**Feedback Dan:** ___

---

#### M2 — Lipidograma sem trigger por idade

**Campo:** Perfil lipidico
**Condicao:** `('climaterio' in queixa_principal) or ('dm' in comorbidades) or ('has' in comorbidades) or ('sop' in comorbidades) or ('obesidade' in comorbidades) or ('doenca_autoimune' in comorbidades)`

**Problema:** O playbook indica perfil lipidico "a partir dos 40 anos ou qualquer idade com FR cardiovascular." A condicao nao inclui `age >= 40` como trigger isolado. Mulher de 45 anos em consulta de rotina sem as comorbidades listadas — mas dentro da faixa etaria recomendada — nao receberia a solicitacao.

**Correcao sugerida:** Adicionar `or (age >= 40)` como trigger standalone, ou restringir com `age >= 40 and nenhuma_queixa` para evitar redundancia.

**Feedback Dan:** ___

---

#### M3 — `galactorreia` sem entry point como queixa isolada

**Campo:** `galactorreia` (N4)
**Expressao de visibilidade:** `'amenorreia_irregularidade' in queixa_principal`

**Problema:** Galactorreia pode ocorrer com ciclos regulares (prolactinoma, uso de medicamentos). Paciente com galactorreia isolada sem amenorreia nao seria capturada pelo fluxo. A queixa_principal nao tem opcao "galactorreia" e nenhuma outra queixa a expoe.

**Correcao sugerida:** Adicionar `or 'queixa_mamaria' in queixa_principal` na expressao de `galactorreia` (ja que descarga papilar e queixa mamaria). Ou criar opcao de queixa_principal para "amenorreia / galactorreia".

**Feedback Dan:** ___

---

#### M4 — `alto_risco_mama` incompleto

**Formula:** `selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama')`

**Problema:** O playbook lista como alto risco tambem lesoes proliferativas (HLA, HDA, CLIS, CDIS) e familiar de 1o grau com CA mama/ovario. Nenhuma dessas situacoes esta capturada no `hist_oncologico` atual. Mulheres com essas historias nao teriam RM anual solicitada.

**Observacao:** Expandir `hist_oncologico` para incluir `'lesao_proliferativa'` e `'familiar_ca_mama'` e depois incluir no `alto_risco_mama`.

**Feedback Dan:** ___

---

#### M5 — `mastalgia_aciclica` dispara USG mamas

**Campo:** US Mamas
**Trecho:** `or ('mastalgia_aciclica' in dor_mamaria_tipo)`

**Problema:** Mastalgia aciclica isolada nao e indicacao estabelecida de USG mamas no playbook. E causa benigna frequente; o playbook lista USG para nodulo palpavel, BI-RADS 0, BI-RADS 3, descarga suspeita, alto risco e mamas densas. Mastalgia gera potencial de exames sem indicacao.

**Feedback Dan:** ___

---

### ESTRUTURAIS — modularidade e robustez

---

#### E1 — T4L usa valor numerico de TSH sem guard para nulo

**Condicao T4L:** `(tsh > 4.5 or tsh < 0.3)`
**Condicao de visibilidade de `tsh` (N3):** `'trouxe_lab' in exames_recentes`

**Problema:** Se a paciente nao trouxe labs, `tsh` nunca e preenchido. A expressao `tsh > 4.5` com `tsh` nulo pode causar comportamento imprevisivel na engine Daktus (erro silencioso ou sempre False — depende da implementacao).

**Correcao sugerida:** Adicionar guard: `('trouxe_lab' in exames_recentes) and (tsh > 4.5 or tsh < 0.3)`.

**Feedback Dan:** ___

---

#### E2 — Summary nao tem `anemia_laboratorial` nem `alt_tsh`

**Problema:** As condicoes de ferritina, ferro serico e T4L usam `hemoglobina < 12` e `tsh > 4.5` diretamente nas condicoes de conduta, sem passar por expressoes derivadas no summary. Isso reduz a modularidade — mudancas em limiares precisam ser feitas em multiplos lugares.

**Sugestao:** Criar expressions `anemia_laboratorial = ('trouxe_lab' in exames_recentes) and (hemoglobina < 12)` e `alt_tsh = ('trouxe_lab' in exames_recentes) and (tsh > 4.5 or tsh < 0.3)` no summary.

**Feedback Dan:** ___

---

#### E3 — `histerectomia_previa` como proxy de menopausa cirurgica

**Trecho DXA:** `or (histerectomia_previa is True)` (sem exigir menopausa)

**Problema:** Histerectomia com ovarios preservados nao causa menopausa. A condicao atual dispara DXA para qualquer histerectomizada independentemente de status ovariano. E clinicamente conservador (safe side), mas pode gerar exames desnecessarios em histerectomizadas jovens com ovarios funcionantes.

**Feedback Dan:** ___

---

## Verificacoes que PASSARAM (conforme esperado pelo protocolo)

| Topico | Verificacao | Resultado |
|--------|------------|-----------|
| Rastreio cervical primario | HPV como metodo primario, 25-64 anos, intervalo 5 anos | OK |
| Imunossuprimidas | `rastreio_cervical_intensificado` sem limite de idade (>64 continua) | OK |
| HPV 16/18 → colposcopia direta | Condicao separada sem citologia intermediaria | OK |
| hrHPV outros → citologia reflexa | `'hpv_outros_hr' in hpv_resultado` dispara Papanicolau | OK |
| Imunocomprometida + NIC2+ → co-teste anual | `co_teste_papanicolau` cobre ambos | OK |
| NIC2+ com histerectomia → citologia de cupula | `co_teste_papanicolau` segunda clausula | OK |
| LSIL + hrHPV → colposcopia | `selected_any(citologia_reflexa_resultado, 'cito_asc_us', 'cito_lsil', 'cito_hsil_mais')` | OK |
| Mamografia risco habitual 40-74 anos bienal | `age >= 40 and age <= 74 and (mamo_nunca ou mamo_mais_2a)` | OK |
| BI-RADS 0 → USG mamas | Condicao presente | OK |
| Alto risco mama → RM anual | `alto_risco_mama` dispara RM | OK |
| USGTV nao como rastreio de rotina | Sem trigger universal; apenas sintomas/indicacoes especificas | OK |
| Histeroscopia por espessamento endometrial | `espessamento_endometrial_significativo is True` | OK |
| Histeroscopia em SUA refrataria | `sua_refrataria is True and usgtv_polipos/espessamento` | OK |
| TSH so com indicacao clinica | Nao e universal; exige queixa/comorbidade especifica | OK |
| T4L so quando TSH alterado | `tsh > 4.5 or tsh < 0.3` | OK (ver E1) |
| Testosterona so com sinais de hiperandrogenismo | `not 'sem_sinais' in hiperandrogenismo_sinais` | OK |
| TRH = SVM moderado/grave + sem contraindicacao | `trh_indicada` formula | OK |
| Estradiol vaginal: atrofia + sem CI sistemica | Condicao separada de TRH sistemica | OK |
| POI: FSH > 25 + idade < 45 | `poi_suspeita` formula | OK |
| DIP: alerta imediato | `suspeita_dip is True` dispara mensagem urgente | OK |
| Chlamydia + gonorreia pre-DIU | `'deseja_inserir' in diu_situacao` incluso | OK |
| Alendronato: T-score <= -2.5 | Condicao presente | OK |
| Encaminhamento GO Oncologico: lesao alto grau | NIC2+/NIC3/carcinoma → GO Oncologico | OK |
| Lynch → encaminhamento especifico | `'lynch' in hist_oncologico` | OK |
| Endometriose profunda → encaminhamento GO Cirurgico | `aine_refrataria or rm_endometriose ou endo_dor_refrataria` | OK |
| Perda de peso intensa → nutricao | `perda_peso_intensa is True` usado em encaminhamento Nutricao | OK |
| SUA refrataria → histeroscopia | `sua_refrataria` usado em condicao de histeroscopia | OK |

---

## Resumo de Prioridades para Correcao

| # | Achado | Impacto | Correcao |
|---|--------|---------|---------|
| C1 | Biopsia + CAF condicoes identicas | Alto | Bifurcar por grau NIC |
| C2 | `pos_coital` → colposcopia direta | Alto | Remover da condicao colposcopia |
| C3 | BI-RADS 3 → encaminhamento mastologia | Alto | Converter em mensagem/orientacao |
| C4 | VitD para toda menopausa | Medio-alto | Remover trigger generico menopausa |
| C5 | `diu_contraindicacao` sem uso em conduta | Medio | Adicionar alerta condicional |
| C6 | DXA <65 sem FR especificos | Medio | Adicionar pelo menos 1 FR como gate |
| M1 | HIV/HCV sem trigger universal de uma vez | Medio | Adicionar trigger etario |
| M2 | Lipidograma sem trigger por idade | Medio | Adicionar `age >= 40` |
| M3 | Galactorreia sem entry point isolado | Baixo-medio | Expandir expressao da questao |
| M4 | `alto_risco_mama` incompleto | Medio | Adicionar lesoes proliferativas |
| M5 | Mastalgia aciclica → USG mamas | Baixo | Revisar indicacao clinica |
| E1 | T4L sem guard para TSH nulo | Baixo | Adicionar guard `trouxe_lab` |
| E2 | Sem expressions derivadas de anemia/TSH | Baixo | Refatorar em summary |
| E3 | Histerectomia como proxy menopausa cirurgica | Baixo | Documentar decisao ou refinar |

---

## Log de Feedback do Dan

*A ser preenchido durante revisao. Cada achado acima tem campo `Feedback Dan:` para registro inline.*

**Data revisao:** ___
**Ferramenta de revisao:** ___

### Decisoes ja registradas em sessoes anteriores (escopo excluido desta auditoria)
- `trouxe_exames` / `age` como campos base: decisao ja tomada, nao revisitar
- Formato geral de queixa_principal com opcao `nenhuma_queixa`: design intencional

---

*Auditoria gerada por Claude Code — 2026-03-03*
*Proxima acao: Dan revisa e registra feedback nos campos acima. Antigravity pode continuar a partir deste arquivo.*
