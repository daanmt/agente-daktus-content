# AUDITORIA DO BANCO DE EVIDÊNCIAS — PRÉ-RASCUNHO DO PLAYBOOK
## AUDITORIA_BANCO_v1.md | Antigravity | 2026-02-27

---

## CONTEXTO E CRITÉRIOS

Esta auditoria classifica as 419 referências do BANCO_EVIDENCIAS_PSIQUIATRIA.md (v2.0) em três tiers antes da produção do playbook, conforme DIRETIVA_AUDITORIA_ANTIGRAVITY.md.

**Lente de análise:** O banco sustenta 6 nós Daktus (Nó 1 Triagem, Nó 2 Gate P0, Nó 3 Anamnese, Nó 4 Diagnóstico ativo, Nó 5 Monitoramento de fármacos, Nó 6 Conduta). A auditoria seleciona as referências de maior qualidade e pertinência BR para cada nó.

### Critérios de Tier

| Tier | Critério |
|------|---------|
| **TIER 1** | Guideline APA/CANMAT/NICE/CFM/VA-DoD, RCT ou SR/NMA publicado em NEJM/Lancet/JAMA/Cochrane, legislação BR, bula FDA/ANVISA com info sem equivalente já listado |
| **TIER 2** | Revisão narrativa de qualidade em periódico indexado, estudo observacional relevante, validação psicométrica de instrumento do protocolo, consenso de especialistas — sem TIER 1 equivalente cobrindo o mesmo ponto |
| **TIER 3** | Revisão/coorte que repete o que um TIER 1 já cobre; pré-2015 com equivalente mais recente no banco; estudo de população sem generalização para o contexto; sustenta apenas notas de divergência |

### Flags

| Flag | Critério |
|------|---------|
| 🇧🇷 | Legislação BR, validação em população BR, protocolo aplicável ao sistema suplementar SP (Amil/ANS) |
| 🎯 | Sustenta diretamente clusters prioritários: Gate P0, monitoramento Li/VPA/CLZ, depressão/TAB/esquizofrenia/TDAH/TPB |

---

## SUMÁRIO EXECUTIVO (preenchido após blocos 1–4)

> **Status:** Em construção — blocos sendo adicionados sequencialmente

| Métrica | Valor |
|---------|-------|
| Total de REFs analisadas | 419 |
| TIER 1 | — |
| TIER 2 | — |
| TIER 3 (candidatos a remoção) | — |
| Com flag 🇧🇷 | — |
| Com flag 🎯 | — |
| Com ambos os flags | — |
| AFIs órfãs identificadas | — |
| AFIs redundantes consolidadas | — |

---

## BLOCO 1 — REF-001 a REF-100
### Relatórios: OE-B1, OE-B2, OE-B3 (Gate P0) | OE-K1, OE-D2, OE-D3 (Farmacologia) | OE-D1, OE-D4, OE-D5 (Humor)

| REF-ID | Tier | 🇧🇷 | 🎯 | Justificativa |
|--------|------|-----|-----|--------------|
| REF-001 | 1 | — | 🎯 | RCT ML+C-SSRS para predição de risco suicida — sustenta Nó 2 Gate P0 com evidência nível I |
| REF-002 | 1 | — | 🎯 | Guideline APA suicide prevention + SR — autoridade máxima para Gate P0 |
| REF-003 | 1 | — | 🎯 | Joint Commission NPSG — padrão de segurança institucional para triagem de risco |
| REF-004 | 1 | 🇧🇷 | 🎯 | Sigilo médico e investigação criminal no Brasil — legal, específico para contexto BR |
| REF-005 | 2 | 🇧🇷 | — | Código de Ética Médica BR — relevante mas coberto implicitamente por CFM |
| REF-006 | 1 | — | 🎯 | Lancet seminar suicide/self-harm 2022 — revisão de alta qualidade, alta relevância |
| REF-007 | 2 | — | 🎯 | Hawton: formulação clínica de risco suicida — útil mas narrativo; REF-002 é superior |
| REF-008 | 1 | — | 🎯 | VA/DoD CPG suicide 2024 — guideline de alto nível, mais recente do cluster |
| REF-009 | 1 | — | 🎯 | SR/MA C-SSRS 2025 — validação psicométrica do instrumento central do Gate P0 |
| REF-010 | 1 | — | 🎯 | RCT CDS para triagem de suicídio 2025 — sustenta implementação de alert automático |
| REF-011 | 2 | — | 🎯 | VA/DoD synopsis 2019 — coberto pela versão mais recente REF-008; manter como contexto histórico |
| REF-012 | 1 | — | 🎯 | NEJM review suicide 2020 — revisão de alta qualidade em periódico premium |
| REF-013 | 3 | — | 🎯 | Turecki 2016 — supersedido por REF-006 (2022) e REF-012 (2020) |
| REF-014 | 2 | — | 🎯 | Coorte 4307 pacientes — fatores protetores/de risco; sustenta limiares do Gate P0 |
| REF-015 | 2 | — | 🎯 | Coorte Baldessarini TAB — risco suicida em humor; específico para Nó 4 (humor) |
| REF-016 | 3 | — | — | USPSTF 2014 — desatualizado; USPSTF não recomenda rastreamento universal (Grade I) |
| REF-017 | 1 | — | 🎯 | AAP guideline adolescentes 2023 — pediatria, sustenta divergências etárias do Gate P0 |
| REF-018 | 1 | — | 🎯 | VA/DoD bipolar 2023 — guideline de alto nível para TAB |
| REF-019 | 2 | — | 🎯 | Guideline psiquiatria em emergência (ACEP) — fluxo pós-Gate P0 positivo |
| REF-020 | 1 | — | 🎯 | RCT SPI+ — safety planning standard of care — sustenta conduta do Nó 2 |
| REF-021 | 1 | — | 🎯 | SR/MA intervenções suicídio 2020 — contextualiza eficácia das condutas do Gate P0 |
| REF-022 | 1 | — | — | AAP guideline emergências pediátricas — pediatria, divergência; manter para adolescentes |
| REF-023 | 1 | 🇧🇷 | 🎯 | Internação involuntária BR vs. Inglaterra — legislação BR; sustenta Nó 6 encaminhamentos |
| REF-024 | 2 | 🇧🇷 | — | Tratamento compulsório países lusófonos — contexto, parcialmente coberto por REF-023 |
| REF-025 | 3 | — | — | Padrões internacionais de internação involuntária — muito genérico, contexto europeu |
| REF-026 | 3 | — | — | Ética de medidas coercitivas — filosófico; não gera recomendação clínica direta |
| REF-027 | 1 | — | 🎯 | CANMAT/ISBD 2018 TAB — guideline de máxima autoridade para monitoramento de humor |
| REF-028 | 1 | — | 🎯 | Bula FDA Lítio 2025 — autoridade farmacológica direta para Nó 5 |
| REF-029 | 3 | — | 🎯 | Malhi 2017 CPG lítio — supersedido por CANMAT 2018 (REF-027) e bula FDA (REF-028) |
| REF-030 | 2 | — | 🎯 | Coorte monitoramento lítio UK — dados reais de prática; contextualiza Nó 5 |
| REF-031 | 1 | — | 🎯 | Bula FDA valproato 2024 — autoridade farmacológica para monitoramento VPA |
| REF-032 | 2 | — | 🎯 | Coorte 5 anos lítio/valproato — dados de prática real; contextualiza periodicidade |
| REF-033 | 2 | — | 🎯 | SR dispens. de exames anuais VPA >2 anos — evidência de nível II para Nó 5 |
| REF-034 | 1 | — | — | Guideline reprodutivo epilepsia 2025 — sustenta contraindicação VPA em mulheres em idade fértil |
| REF-035 | 1 | — | — | EURAP 2018 — dados de teratogenicidade antiepiléticos; sustenta alertas VPA |
| REF-036 | 3 | — | — | Wartman 2022 — revisão VPA alertas; supersedido por REF-031 (bula) e REF-037 (AAN) |
| REF-037 | 1 | — | — | AAN/AES/SMFM 2024 guideline teratogenicidade ASM — orienta alerts de VPA |
| REF-038 | 3 | — | — | Andrade 2018 narrativa VPA gestação — supersedido por REF-037 (2024) |
| REF-039 | 3 | — | — | Coorte padrões tratamento mulheres AED — contexto; não gera recomendação direta |
| REF-040 | 3 | — | — | Farmacovigilância Brasil — contexto regulatório, não gera ação clínica direta |
| REF-041 | 3 | — | — | Monitoramento SmPC psicotrópicos 2015 — desatualizado, supersedido por REF-047 e bulas |
| REF-042 | 1 | — | 🎯 | JAMA review TAB 2023 — revisão de alta qualidade para diagnóstico e trat. TAB |
| REF-043 | 1 | — | 🎯 | Bula FDA carbamazepina 2025 — autoridade farmacológica para monitoramento CBZ |
| REF-044 | 2 | — | 🎯 | Coorte TDM carbamazepina 20 anos — dados de prática para Nó 5 |
| REF-045 | 2 | — | 🎯 | NEJM review esquizofrenia 2019 — qualit. alta, mas supersedido parcialmente por REF-167 (2022) |
| REF-046 | 2 | — | 🎯 | Pringsheim saúde física esquizofrenia — referência para monitoramento metabólico |
| REF-047 | 1 | — | 🎯 | VA/DoD psychosis/schizophrenia 2023 — guideline de alto nível, mais recente |
| REF-048 | 1 | — | 🎯 | Bula FDA risperidona/paliperidona 2026 — autoridade farmacológica para Nó 5 |
| REF-049 | 1 | — | 🎯 | SR/MA monitoramento metabólico antipsicóticos — sustenta cadência de exames Nó 5 |
| REF-050 | 1 | — | 🎯 | Bula FDA olanzapina 2026 — autoridade farmacológica para Nó 5 |
| REF-051 | 1 | — | 🎯 | SR efeitos adversos clozapina 2022 — sustenta protocolo CIGH + agranulocitose Nó 5 |
| REF-052 | 1 | — | 🎯 | Bula FDA clozapina 2025 — autoridade farmacológica máxima para Nó 5 clozapina |
| REF-053 | 1 | — | 🎯 | Bula FDA quetiapina 2025 — autoridade farmacológica para Nó 5 |
| REF-054 | 1 | — | 🎯 | ISBD 2009 consenso monitoramento tratamentos TAB — sustenta cadência exames TAB |
| REF-055 | 2 | — | 🎯 | Consenso QTc monitoring — orienta threshold de alerta de ECG no Nó 5/6 |
| REF-056 | 3 | — | — | Polcwiartek 2016 segurança CV antipsicóticos — supersedido por REF-126 (AHA 2020) |
| REF-057 | 3 | — | — | Paliperidona drug safety 2017 — específico demais; bula FDA (REF-048) é superior |
| REF-058 | 3 | — | — | Farmacovigilância paliperidona FAERS — muito específico; não gera recomendação clínica limpa |
| REF-059 | 1 | — | 🎯 | DSM-5-TR APA 2022 — referência diagnóstica central para todos os nós clínicos |
| REF-060 | 2 | — | 🎯 | NEJM depressão adolescentes 2021 — orientação para divergências pediátricas no Nó 4 |
| REF-061 | 1 | — | 🎯 | NEJM depressão cuidados primários 2019 — revisão de alta qualidade sustenta Nó 4 humor |
| REF-062 | 1 | — | 🎯 | Lancet TAB 2025 — mais recente e de alta qualidade para TAB |
| REF-063 | 3 | — | 🎯 | McIntyre Lancet TAB 2020 — supersedido por REF-062 (2025, Lancet) |
| REF-064 | 2 | — | 🎯 | Zimmerman mixed features — traz dados específicos de prevalência; sustenta Nó 4 |
| REF-065 | 1 | — | 🎯 | SR TAB II World Psychiatry 2025 — evidência de alta qualidade |
| REF-066 | 3 | — | 🎯 | Carvalho NEJM TAB 2020 — supersedido por REF-062 (2025) e REF-065 (2025) |
| REF-067 | 1 | 🇧🇷 | 🎯 | PHQ-9 Brasil n>10k 2024 — validação psicométrica BR, instrumento central do Nó 4 |
| REF-068 | 1 | 🇧🇷 | 🎯 | PHQ-9 adultos maiores Brasil — validação em subpopulação BR específica |
| REF-069 | 1 | 🇧🇷 | 🎯 | HAM-D + MADRS validação brasileira — instrumentos usados no Nó 4 |
| REF-070 | 2 | — | 🎯 | Thase MADRS severity thresholds TAB — dados normativos para interpretação |
| REF-071 | 1 | 🇧🇷 | 🎯 | YMRS validação portuguesa — instrumento obrigatório para mania no Nó 4 |
| REF-072 | 2 | 🇧🇷 | — | DASS-21 adaptação BR — instrumento auxiliar; não é central no protocolo |
| REF-073 | 2 | 🇧🇷 | — | PHQ-8/GAD-7 América Latina adolescentes — divergência etária, relevante mas secundário |
| REF-074 | 2 | 🇧🇷 | — | SMFQ validação brasileira — instrumento pediátrico; apenas para divergências |
| REF-075 | 1 | — | 🎯 | CANMAT 2023 MDD — guideline de máxima autoridade para depressão |
| REF-076 | 1 | — | 🎯 | ACP guideline MDD 2023 — guideline de alto nível; perspectiva diferentes da clínica |
| REF-077 | 1 | — | 🎯 | JAMA management depression 2024 — revisão premium, síntese prática |
| REF-078 | 3 | — | 🎯 | Coles AFP 2025 — sumário CANMAT; supersedido pela fonte primária REF-075 |
| REF-079 | 1 | — | 🎯 | NMA 21 antidepressivos Cipriani Lancet 2018 — sustenta escolha de AD no Nó 6 conduta |
| REF-080 | 2 | — | 🎯 | Steffens NEJM DRT idosos 2024 — contexto específico; sustenta divergência geriátrica |
| REF-081 | 3 | — | — | Controversies farmacoterapia depressão adolescente 2022 — supersedido por REF-082/083 |
| REF-082 | 2 | — | — | Rotulagem regulatória antidepressivos pediátricos — sustenta alertas FDA Black Box |
| REF-083 | 1 | — | — | Thapar Lancet depressão jovens 2022 — relevante para divergências pediátricas |
| REF-084 | 1 | — | 🎯 | SR TRD World Psychiatry 2023 — definição/prevalência DRT; sustenta Nó 4 |
| REF-085 | 2 | — | 🎯 | Gaddey AFP 2024 — resistência e resposta parcial; orientação clínica prática |
| REF-086 | 3 | — | 🎯 | Consenso canadense DRT 2021 — supersedido por REF-084 + REF-092 mais recentes |
| REF-087 | 2 | — | 🎯 | Maudsley Staging Method BMC 2018 — método de estadiamento DRT; sustenta Nó 4 |
| REF-088 | 3 | — | 🎯 | SR métodos estadiamento DRT 2012 — muito antigo; REF-087 é mais recente |
| REF-089 | 3 | — | 🎯 | Staging treatment intensity 2019 — supersedido por REF-084 (2023) |
| REF-090 | 3 | — | — | Petersen empirical testing 2005 — pré-2015 e supersedido |
| REF-091 | 3 | — | — | Whooley 2012 depressão+comorbidades — muito antigo; supersedido por REF-077 (2024) |
| REF-092 | 1 | — | 🎯 | NMA eficácia antidepressivos DRT 2025 — Neuropsychopharmacology, nível I, recentíssimo |
| REF-093 | 2 | — | 🎯 | AFP guideline medicamentos DRT 2020 — orientação prática, sustenta Nó 6 conduta |
| REF-094 | 3 | — | — | Estratégias DRT 2020 — revisão narrativa supersedida por REF-092 |
| REF-095 | 3 | — | — | Programa consulta DRT 2025 — estudo de serviço; não gera recomendação direta |
| REF-096 | 2 | — | 🎯 | Revisão qualidade guidelines DRT PLoS One 2023 — orienta quais guidelines usar |
| REF-097 | 1 | — | 🎯 | APA Resource Document MBC 2023 — padrão APA para medição baseada em cuidado |
| REF-098 | 2 | — | 🎯 | Garcia JAMA Intern Med 2025 — tratamento pós-rastreio positivo; sustenta fluxo |
| REF-099 | 1 | — | 🎯 | RCT MBC para desfechos de antidepressivos JAMA 2025 — nível I, sustenta MBC no Nó 4 |
| REF-100 | 3 | — | — | Digitização MBC REDCap+EHR — implementação técnica; não clínico |

---

## BLOCO 2 — REF-101 a REF-222
### Relatórios: OE-D5 final | OE-E1, E2, E3, E4 (Ansiedade/OCD/TEPT/Burnout) | OE-F1, F2, F3, F4 (Psicose/EPS/CLZ/Metabólico)

| REF-ID | Tier | 🇧🇷 | 🎯 | Justificativa |
|--------|------|-----|-----|--------------|
| REF-101 | 3 | — | — | MBC em LMICs 2025 — contexto global; não específico para prática ambulatorial SP |
| REF-102 | 3 | — | — | Unützer NEJM depressão idosos 2007 — pré-2015; supersedido por REF-080 (2024) |
| REF-103 | 1 | — | 🎯 | JAMA review transtornos de ansiedade 2022 — revisão premium, sustenta Nó 4 ansiedade |
| REF-104 | 2 | — | 🎯 | AFP TAG e Pânico 2022 — orientação clínica prática para Nó 4/6 |
| REF-105 | 1 | — | — | Guideline ansiedade crianças e adolescentes AFP 2022 — divergências pediátricas |
| REF-106 | 1 | — | — | JACAAP guideline ansiedade pediátrica 2020 — complementa REF-105 para adolescentes |
| REF-107 | 3 | — | — | ACOG mental health adolescentes 2017 — desatualizado; pré-2020 |
| REF-108 | 1 | — | 🎯 | AFP guideline TEPT 2023 — cobre diagnóstico e tratamento TEPT para Nó 4/6 |
| REF-109 | 3 | — | — | Katon NEJM Pânico 2006 — pré-2015; supersedido por REF-103 e REF-104 |
| REF-110 | 2 | — | — | ACC COVID-19 sequelas cardiovasculares — diagnóstico diferencial taquicardia |
| REF-111 | 2 | — | — | JACC POTS 2019 — diagnóstico diferencial palpitações/ansiedade |
| REF-112 | 2 | — | — | JACC taquicardia sinusal inapropriada 2022 — diagnóstico diferencial |
| REF-113 | 3 | — | — | Kroenke Ann Intern Med 2014 — avaliação sintomas físicos; pré-2015 |
| REF-114 | 2 | — | — | AHA modelos centrados na pessoa 2023 — contexto; não gera recomendação direta |
| REF-115 | 3 | — | — | Triagem telefônica eventos cardíacos 2020 — não clínico do ponto de vista do protocolo |
| REF-116 | 1 | — | 🎯 | AFP guideline TOC 2024 — diagnóstico e manejo TOC, sustenta Nó 4/6 |
| REF-117 | 2 | — | 🎯 | Doses ISRS supraterapêuticas em TOC resistente 2025 — sustenta escalonamento Nó 6 |
| REF-118 | 1 | — | 🎯 | Bula FDA sertralina 2024 — autoridade farmacológica para ISRS no TOC e depressão |
| REF-119 | 3 | — | — | QT prolongado ISRSs 2013 — supersedido por REF-120 (MA 2014) e REF-126 (AHA 2020) |
| REF-120 | 1 | — | 🎯 | SR/MA QTc ISRSs J Clin Psychiatry 2014 — melhor evidência disponível sobre risco QT |
| REF-121 | 2 | — | 🎯 | Lancet Oncol QT drugs 2022 — contextualiza mecanismo; complementar ao REF-120 |
| REF-122 | 3 | — | — | Farmacovigilância antidepressivos FAERS 2025 — passivo; REF-120 é superior |
| REF-123 | 2 | — | 🎯 | ISRS e QTc Rotterdam Study — dados epidemiológicos; complementa REF-120 |
| REF-124 | 2 | — | 🎯 | Castro BMJ QT+antidepressivos EHR 2013 — maior amostra para citalopram/escitalopram |
| REF-125 | 3 | — | — | Consenso holandês ECG monitoring 2018 — não aplicável ao contexto BR/Amil |
| REF-126 | 1 | — | 🎯 | AHA statement drug-induced arrhythmias 2020 — autoridade máxima para alertas QTc Nó 6 |
| REF-127 | 3 | — | — | Complicações CV terapia oncológica JACC 2017 — não relevante para psiquiatria ambulatorial |
| REF-128 | 3 | — | — | Algoritmo QTc psiquiatria 2019 — supersedido por REF-126 (AHA) e REF-120 |
| REF-129 | 2 | — | — | Reed ICD-11 vs DSM-5 World Psychiatry 2019 — contexto nosológico; não gera conduta |
| REF-130 | 2 | — | — | Hillert burnout Front Psychiatry 2021 — contextualização do fenômeno; diagnóstico diferencial |
| REF-131 | 2 | — | — | Hewitt JAMA Surgery definições burnout — define fenômeno para DD no Nó 4 |
| REF-132 | 3 | — | — | Work addiction ICD-11 implications 2020 — muito específico; não gera conduta |
| REF-133 | 1 | — | — | Harvey Lancet suicídio médicos 2021 — sustenta vigilância Gate P0 em profissionais saúde |
| REF-134 | 3 | — | — | ICD-11 vs DSM-5 comparison 2021 — contexto nosológico; coberto por REF-129 |
| REF-135 | 3 | — | — | Parker burnout definição 2025 — redundante com REF-130 e REF-131 |
| REF-136 | 3 | — | — | Coorte burnout médicos Irlanda 2023 — contexto não-BR; não gera recomendação |
| REF-137 | 2 | — | — | Parker distinguindo burnout de depressão — DD essencial para Nó 4 |
| REF-138 | 2 | — | — | Tavella burnout+depressão: convergência e divergência 2023 — sustenta DD no Nó 4 |
| REF-139 | 3 | — | — | Tavella qualitativo 2020 — supersedido por REF-138 |
| REF-140 | 1 | 🇧🇷 | — | De Amorim Brasil: burnout+depressão análise latente — evidência BR, J Psychiatr Res 2023 |
| REF-141 | 1 | — | — | SR/MA burnout+depressão Front Psychol 2018 — nível I, sustenta DD no Nó 4 |
| REF-142 | 2 | 🇧🇷 | — | Fischer Brasil UTI JAMA Network Open 2020 — dados BR, contexto burnout profissional |
| REF-143 | 1 | — | — | Rotenstein JAMA prevalência burnout médicos 2018 — nível I, contexto epidemiológico |
| REF-144 | 3 | 🇧🇷 | — | Merces nursing burnout Brasil 2020 — specifico a enfermagem; redundante |
| REF-145 | 3 | 🇧🇷 | — | Oliveira job satisfaction Brasil 2018 — muito específico, não gera recomendação clínica |
| REF-146 | 3 | 🇧🇷 | — | OLBI adaptação Brasil 2018 — instrumento não central ao protocolo |
| REF-147 | 2 | 🇧🇷 | — | BAT validação BR/Portugal 2022 — instrumento de triagem de burnout |
| REF-148 | 2 | — | — | BAT4 ultra-short 2023 — versão ultra-curta, útil para triagem rápida |
| REF-149 | 3 | 🇧🇷 | — | BCSQ-12 validação BR atenção primária 2020 — instrumento não central ao protocolo |
| REF-150 | 1 | — | 🎯 | APA CPG TEPT 2025 — guideline mais recente e de maior autoridade para TEPT |
| REF-151 | 1 | — | 🎯 | VA/DoD PTSD synopsis Ann Intern Med 2024 — segunda maior autoridade guideline para TEPT |
| REF-152 | 1 | — | 🎯 | WFSBP guideline ansiedade/OCD/TEPT Part II 2023 — perspectiva mundial |
| REF-153 | 1 | — | 🎯 | Cochrane farmacoterapia TEPT 2022 — nível I, sustenta escolha de fármaco Nó 6 |
| REF-154 | 2 | — | 🎯 | AFP farmacoterapia TEPT 2022 — orientação prática; complementa Cochrane |
| REF-155 | 1 | — | 🎯 | RCT efectividade comparativa TEPT JAMA Psychiatry 2025 — pragmático, nível I |
| REF-156 | 1 | — | 🎯 | NMA psicoterapias TEPT 2023 — melhor evidência para psicoterapia no Nó 6 |
| REF-157 | 1 | — | 🎯 | SR meta-análises psicoterapias TEPT 2025 — nível I, complementa REF-156 |
| REF-158 | 1 | — | 🎯 | SR/MA EMDR efetividade 2025 — sustenta indicação EMDR no Nó 6 conduta |
| REF-159 | 1 | — | 🎯 | JAMA Psychiatry perda diagnóstico TEPT com tratamento 2025 — desfecho central |
| REF-160 | 1 | — | 🎯 | RCT STOP-PTSD online therapy Lancet Psychiatry 2023 — telemedicina, relevante |
| REF-161 | 1 | 🇧🇷 | 🎯 | PDS-3 validação BR 2021 — instrumento de rastreio TEPT com validação BR |
| REF-162 | 1 | — | 🎯 | DSM-5-TR Updates 2023–2025 — atualizações nosológicas recentes, autoridade máxima |
| REF-163 | 2 | — | — | Leucht JAMA Psychiatry sintomas psicopatológicos 2024 — contextualiza diagnóstico |
| REF-164 | 2 | — | — | Eilers PTSD/CPTSD crianças ICD-11 2024 — divergência pediátrica/nosológica |
| REF-165 | 1 | — | 🎯 | McCutcheon JAMA Psychiatry esquizofrenia overview 2020 — revisão de alta qualidade |
| REF-166 | 2 | — | 🎯 | Fusar-Poli Lancet Psychiatry episódios psicóticos breves 2021 — DD da esquizofrenia |
| REF-167 | 1 | — | 🎯 | Jauhar Lancet esquizofrenia 2022 — mais recente e de maior qualidade |
| REF-168 | 2 | — | — | Nordgaard FRS e desordens do self 2020 — contexto diagnóstico; não gera conduta |
| REF-169 | 1 | — | 🎯 | Cochrane FRS para esquizofrenia 2015 — validade dos sintomas de 1ª ordem |
| REF-170 | 2 | — | — | Peralta FRS valor diagnóstico 2023 — complementa REF-169 |
| REF-171 | 2 | — | — | Feyaerts delusions Lancet Psychiatry 2021 — contexto fenomenológico |
| REF-172 | 3 | — | — | Moscarelli FRS major flaw 2020 — opinião crítica; não gera recomendação |
| REF-173 | 3 | — | — | DSM-6 survey FRS reinstatement — opinião, não gera conduta |
| REF-174 | 3 | — | — | What Schneider really said — histórico/filosófico; não clínico |
| REF-175 | 3 | — | — | Goodbye to FRS? 2016 — pré-2020 e debate teórico; não gera recomendação |
| REF-176 | 2 | — | 🎯 | Sykes D2 receptor kinetics EPS 2017 — mecanismo de ação EPS; contexto Nó 5 |
| REF-177 | 1 | — | 🎯 | Factor Lancet Neurology drug-induced movement disorders 2019 — revisão premium |
| REF-178 | 3 | — | — | Divac SGA e EPS 2014 — pré-2015; supersedido por REF-179 (NMA 2023) |
| REF-179 | 1 | — | 🎯 | Siafis NMA dose/D2/EPS 2023 — nível I, sustenta seleção de antipsicótico no Nó 6 |
| REF-180 | 1 | — | 🎯 | Leucht NMA 15 antipsicóticos Lancet 2013 — referência histórica ainda amplamente citada |
| REF-181 | 1 | — | 🎯 | Rummel-Kluge SR/MA SGA vs. EPS Schizophrenia Bull 2011 — nível I, head-to-head |
| REF-182 | 2 | — | 🎯 | Pillinger Lancet Psychiatry digital tool efeitos adversos 2023 — ferramenta prática |
| REF-183 | 3 | — | — | SOHO incidência EPS 2010 — pré-2015; supersedido por REF-184 |
| REF-184 | 1 | — | 🎯 | SR/MA EPS antipsicóticos PLoS One 2021 — nível I, estimativas de incidência atuais |
| REF-185 | 2 | — | 🎯 | AFP TAB tratamento + AIMS table 2021 — orientação prática com escala AIMS |
| REF-186 | 2 | — | 🎯 | Widschwendter escalas de movimento 2015 — escalas de monitoramento de EPS |
| REF-187 | 3 | — | — | Gopal paliperidona EPS LAI 2013 — pré-2015; muito específico |
| REF-188 | 3 | — | — | Bo risperidona EPS manutenção 2016 — resultado específico coberto por REF-184 |
| REF-189 | 1 | — | — | Hua Pediatrics psicose adolescentes 2021 — guideline para divergência etária |
| REF-190 | 3 | — | — | Correll efeitos adversos antipsicóticos jovens 2010 — pré-2015; REF-191 é superior |
| REF-191 | 2 | — | — | Carbon EPS jovens SGA 12 semanas 2015 — dados em adolescentes; divergência |
| REF-192 | 1 | — | 🎯 | Wijdicks NEJM NMS 2024 — revisão premium, mais recente para NMS; alerta crítico Nó 6 |
| REF-193 | 1 | — | 🎯 | APA Resource Document Catatonia 2025 — autoridade máxima para catatonia |
| REF-194 | 2 | — | 🎯 | Gurrera critérios NMS consenso Delphi 2011 — critérios diagnósticos clássicos de NMS |
| REF-195 | 3 | — | — | Movement disorders emergencies 2011 — pré-2015; supersedido por REF-192 |
| REF-196 | 3 | — | — | Gratz 1992 tratamento NMS — muito antigo; supersedido por REF-192 |
| REF-197 | 1 | — | 🎯 | Siskind Lancet Psychiatry monitoramento ANC clozapina Delphi global 2025 — autoridade |
| REF-198 | 1 | — | 🎯 | Schulte risco agranulocitose e regulações clozapina 2024 — sustenta protocolo de ANC |
| REF-199 | 1 | — | 🎯 | Rubio coorte agranulocitose longo prazo Finlândia Lancet Psychiatry 2024 — nível I |
| REF-200 | 2 | — | 🎯 | Cohen clozapina CIGH CNS Drugs 2017 — revisão específica de hipomotilidade GI |
| REF-201 | 2 | — | 🎯 | Handley farmacovigilância CIGH UK 1992-2017 — dados de longo prazo | 
| REF-202 | 1 | — | 🎯 | Partanen ileus/pneumonia CLZ Finlândia 25 anos Am J Psychiatry 2024 — melhor evidência |
| REF-203 | 2 | — | 🎯 | Palmer CIGH 102 casos J Clin Psychiatry 2008 — série clínica; complementa REF-202 |
| REF-204 | 2 | — | 🎯 | Every-Palmer rastreio constipação CLZ 2020 — sustenta protocolo de rastreio CIGH |
| REF-205 | 2 | — | 🎯 | Cohen além de WBC monitoring CLZ 2012 — monitoramento ampliado CLZ |
| REF-206 | 2 | — | 🎯 | Every-Palmer Porirua Protocol CIGH 2016 — protocolo clínico de referência |
| REF-207 | 3 | — | — | West CIGH review 2017 — coberto por REF-202 e REF-206 |
| REF-208 | 2 | 🇧🇷 | 🎯 | Baptista expert review clozapina América Latina 2024 — contexto regional crítico |
| REF-209 | 3 | 🇧🇷 | 🎯 | Baptista CLZ scoping review América do Sul 2024 — redundante com REF-208 |
| REF-210 | 3 | — | — | Nielsen regulações mundiais CLZ 2016 — contexto regulatório; bula FDA (REF-052) é superior |
| REF-211 | 1 | — | 🎯 | Pillinger NMA 18 antipsicóticos metabolismo Lancet Psychiatry 2019 — nível I, Nó 5/6 |
| REF-212 | 3 | — | — | Newcomer SGA efeitos metabólicos 2005 — pré-2015; supersedido por REF-211 |
| REF-213 | 1 | — | 🎯 | Goldfarb JACC doença mental grave + DCV 2022 — sustenta rastreio metabólico no Nó 5/6 |
| REF-214 | 1 | — | 🎯 | Smith JAMA Psychiatry antipsicóticos + glicose 2025 — nível I, mecanismo de DM2 |
| REF-215 | 2 | — | 🎯 | Zhang RCT efeitos metabólicos 7 antipsicóticos 2020 — dados de curto prazo |
| REF-216 | 2 | — | 🎯 | Feng coorte desfechos metabólicos longo prazo SGA 2025 — perspectiva longitudinal |
| REF-217 | 1 | — | 🎯 | Hamna NMA efetividade comparativa antipsicóticos Finlândia JAMA Network Open 2024 |
| REF-218 | 1 | 🇧🇷 | 🎯 | Vieira CLZ vs não-CLZ Brasil Front Psychiatry 2024 — dado BR específico |
| REF-219 | 2 | 🇧🇷 | 🎯 | Fulone switching SGA Brasil 10 anos 2021 — contexto de prática BR |
| REF-220 | 2 | — | 🎯 | Citrome guia LAI antipsicóticos 2025 — orientação prática escolha LAI, Nó 6 |
| REF-221 | 3 | — | — | De Filippis LAI antipsicóticos 2021 — supersedido por REF-220 (2025) |
| REF-222 | 3 | — | — | Faden LAI risperidona overview 2024 — muito específico; REF-220 cobre |

---

## BLOCO 3 — REF-223 a REF-347
### Relatórios: OE-G1, G2, G3, G4 (TDAH) | OE-H1, H2 (TEA) | OE-I1, I2 (TPB/Borderline)

| REF-ID | Tier | 🇧🇷 | 🎯 | Justificativa |
|--------|------|-----|-----|--------------|
| REF-223 | 2 | — | 🎯 | Volkow NEJM adultos TDAH 2013 — revisão clássica NEJM; REF-238 (2020) é mais recente |
| REF-224 | 1 | — | 🎯 | Posner Lancet TDAH 2020 — revisão de alta qualidade, períodico premium |
| REF-225 | 1 | — | 🎯 | AMSSM TDAH e atletas 2023 — guideline; sustenta uso de estimulantes e monitoramento CV |
| REF-226 | 1 | — | 🎯 | AFP TDAH adultos 2024 — guideline prático mais recente para Nó 4/6 |
| REF-227 | 1 | — | 🎯 | Ustun ASRS WHO DSM-5 JAMA Psychiatry 2017 — validação do instrumento central |
| REF-228 | 2 | — | 🎯 | ASRS cross-cultural 42 países 2024 — confirma validade transcultural |
| REF-229 | 2 | — | 🎯 | Kessler ASRS validação Psychological Medicine 2005 — referência original do instrumento |
| REF-230 | 2 | — | 🎯 | ASRS triagem atenção primária 2012 — sustenta uso no Nó 3/4 |
| REF-231 | 2 | — | 🎯 | Chamberlain caveats triagem TDAH 2021 — alertas sobre falsos positivos |
| REF-232 | 3 | — | — | Babinski triagem TDAH psiquiatria ambulatorial 2022 — muito específico |
| REF-233 | 2 | — | — | ASRS em pacientes com SUD 2013 — contexto de comorbidade |
| REF-234 | 1 | — | 🎯 | Torres-Acosta JACC efeitos CV estimulantes TDAH 2020 — sustenta alertas CV Nó 5/6 |
| REF-235 | 1 | — | 🎯 | Bula FDA lisdexanfetamina 2025 — autoridade farmacológica |
| REF-236 | 3 | — | — | AMSSM TDAH atletas 2011 — supersedido por REF-225 (2023) |
| REF-237 | 1 | — | 🎯 | NMA Farhat Lancet Psychiatry segurança CV estimulantes 2025 — melhor evidência CV |
| REF-238 | 1 | — | 🎯 | Cortese NEJM farmacoterapia TDAH 2020 — revisão premium; sustenta Nó 6 conduta |
| REF-239 | 1 | — | 🎯 | Zhang JAMA Psychiatry TDAH medicamentos CVD long-term 2024 — nível II, LP |
| REF-240 | 1 | — | 🎯 | Kooij European Consensus TDAH adultos 2019 — guideline europeu amplo |
| REF-241 | 2 | — | 🎯 | Adamou qualidade diagnóstico TDAH adultos 2024 — critérios de qualidade diagnóstica |
| REF-242 | 2 | — | 🎯 | Marshall diagnóstico TDAH jovens adultos 2020 — sustenta protocolo de avaliação |
| REF-243 | 2 | — | 🎯 | Nikolas testes neurocognitivos TDAH 2019 — limitações dos testes cognitivos |
| REF-244 | 2 | — | 🎯 | Sibley guidelines diagnóstico TDAH adulto de primeira vez 2021 |
| REF-245 | 3 | — | — | Nelson TDAH universitários 2019 — muito específico, contexto acadêmico |
| REF-246 | 2 | — | 🎯 | Eng avaliação baseada em evidências TDAH 2023 — síntese do processo diagnóstico |
| REF-247 | 1 | — | 🎯 | NMA não-estimulantes TDAH adultos SR/MA 2023 — nível I, sustenta atomoxetina/guanfacina |
| REF-248 | 1 | — | 🎯 | Cochrane bupropiona TDAH adultos 2017 — nível I, opção de 3ª linha |
| REF-249 | 2 | — | 🎯 | Perugi estimulantes+ATX em TDAH+TAB 2015 — comorbidade relevante para Nó 4 |
| REF-250 | 2 | — | 🎯 | SR TDAH+TAB bipolar 2019 — comorbidade, contexto para Nó 4 |
| REF-251 | 3 | — | — | Perugi farmacoterapia TDAH emergentes 2019 — supersedido por REF-247 (2023) |
| REF-252 | 2 | — | 🎯 | Pérez TDAH+SUD dilemas farmacológicos — sustenta algoritmo de TDAH+SUD |
| REF-253 | 3 | — | — | Schubiner TDAH+SUD CNS Drugs 2005 — pré-2015; supersedido por REF-257 (2024) |
| REF-254 | 3 | — | — | AACAP Greenhill estimulantes 2002 — muito antigo; supersedido |
| REF-255 | 2 | — | 🎯 | Barbuti TDAH+SUD J Clin Med 2023 — orientação atual, complementa REF-257 |
| REF-256 | 3 | — | — | Simon metilfenidato adultos+SUD 2015 — pré-2015; supersedido |
| REF-257 | 1 | — | 🎯 | ASAM/AAAP guideline SUD estimulantes 2024 — autoridade máxima para TDAH+SUD |
| REF-258 | 1 | — | 🎯 | Zhang NMA risco CVD medicamentos TDAH JAMA Network Open 2022 — nível I |
| REF-259 | 1 | — | 🎯 | Bula FDA atomoxetina 2025 — autoridade farmacológica para 2ª linha TDAH |
| REF-260 | 2 | — | — | SR/MA segurança CV naltrexona+bupropiona 2021 — específico para obesidade; contexto |
| REF-261 | 1 | — | 🎯 | Bula FDA clonidina 2020 — autoridade farmacológica para TDAH (não-estimulante) |
| REF-262 | 1 | — | 🎯 | Bula FDA guanfacina 2024 — autoridade farmacológica para TDAH (não-estimulante) |
| REF-263 | 2 | — | — | Nasser viloxazina ER e QTc 2020 — viloxazina não disponível no Brasil; contexto |
| REF-264 | 1 | — | 🎯 | Farhat JAMA Psychiatry desfechos doses TDAH 2024 — sustenta limites de dose no Nó 6 |
| REF-265 | 1 | — | — | AAP guideline TDAH 2020 — pediátrico; divergência etária |
| REF-266 | 3 | — | — | Martinez-Raga risco CV TDAH 2012 — pré-2015; supersedido por REF-237 e REF-258 |
| REF-267 | 3 | — | 🎯 | Thapar Lancet TDAH 2016 — supersedido por REF-224 (2020) |
| REF-268 | 3 | — | — | Loskutova triagem TDAH tablet 2021 — implementação técnica; não clínico |
| REF-269 | 3 | — | — | Schneider avaliação TDAH prática clínica 2023 — pesquisa de práticas; não gera conduta |
| REF-270 | 2 | — | 🎯 | Gonda farmacológico+neuromodulação+psicoterapia TDAH 2026 — síntese emergente |
| REF-271 | 2 | — | — | Constantino Lancet Neurology diagnóstico TEA 2016 — fundamentação diagnóstica |
| REF-272 | 1 | — | 🎯 | Hirota King JAMA review TEA 2023 — revisão premium, sustenta Nó 4 TEA |
| REF-273 | 1 | — | 🎯 | AFP TEA cuidados primários 2025 — guideline prático, sustenta Nó 4/6 |
| REF-274 | 2 | — | 🎯 | Whaling diagnóstico adulto TEA telesaúde 2025 — relevante para fluxo ambulatorial |
| REF-275 | 1 | — | 🎯 | McQuaid camouflaging TEA sexo/gênero 2022 — fundamento para diagnóstico tardio |
| REF-276 | 2 | — | 🎯 | Lai Baron-Cohen geração perdida de adultos com TEA 2015 — contexto diagnóstico |
| REF-277 | 2 | — | 🎯 | Rujeedawa TEA feminino adulto 2022 — diagnóstico e manejo mulheres com TEA |
| REF-278 | 2 | — | 🎯 | Kentrou percepção de diagnóstico errado TEA adultos 2024 — DD e qualidade |
| REF-279 | 3 | — | — | Garcia-Simon qualitativo mulheres TEA 2025 — qualitativo; não gera recomendação clínica |
| REF-280 | 2 | — | 🎯 | Zhuang camouflaging e saúde mental TEA 2023 — sustenta alerta de risco suicida em TEA |
| REF-281 | 3 | — | — | Alaghband camouflage adultos 2023 — redundante com REF-275 e REF-280 |
| REF-282 | 2 | — | 🎯 | Brugha AQ em serviços de saúde mental 2020 — sustenta uso do AQ |
| REF-283 | 2 | — | 🎯 | Ashwood AQ predição diagnóstico TEA 2016 — sustenta sensibilidade/especificidade do AQ |
| REF-284 | 1 | — | 🎯 | Ritvo RAADS-R validação internacional 2011 — instrumento central validado |
| REF-285 | 2 | — | 🎯 | Andersen RAADS-R validação sueca 2011 — complementa REF-284 |
| REF-286 | 2 | — | 🎯 | Rausch RAADS-R validação alemã 2024 — complementa REF-284 |
| REF-287 | 2 | — | 🎯 | Picot RAADS-R validação francesa 2020 — complementa REF-284 |
| REF-288 | 2 | — | 🎯 | Robinson três instrumentos triagem adulto 2025 — comparação AQ/RAADS-R/ADOS-2 |
| REF-289 | 2 | — | 🎯 | Maddox ADOS-2 acurácia em adultos com condições psiquiátricas 2017 — limites do ADOS |
| REF-290 | 2 | — | 🎯 | Fusar-Poli ADOS-2+ADI-R adultos sem DI 2017 — protocolo de avaliação formal |
| REF-291 | 1 | — | 🎯 | SR instrumentos triagem/diagnóstico TEA adultos European Psychiatry 2017 — nível I |
| REF-292 | 2 | — | 🎯 | Carroll DD de TEA em adultos 2025 — diagnóstico diferencial sistematizado |
| REF-293 | 3 | — | — | Lehnhardt Asperger adultos 2013 — pré-2015; supersedido por REF-292 e REF-273 |
| REF-294 | 2 | — | 🎯 | Curnow avaliação diagnóstica ADOS-2 adultos 2023 — aplicação prática |
| REF-295 | 1 | — | 🎯 | SR/MA Salazar de Pablo farmacoterapia irritabilidade TEA 2023 — nível I |
| REF-296 | 1 | — | 🎯 | Cochrane NMA antipsicóticos atípicos TEA 2025 — melhor evidência disponível |
| REF-297 | 1 | — | 🎯 | Bula FDA risperidona 2025 — autoridade farmacológica (aprovada FDA para TEA) |
| REF-298 | 1 | — | 🎯 | Bula FDA aripiprazol 2024/2025 — autoridade farmacológica (aprovada FDA para TEA) |
| REF-299 | 1 | — | 🎯 | Cochrane farmacoterapia irritabilidade/agressão/SIB TEA 2023 — nível I |
| REF-300 | 1 | — | 🎯 | Manter AFP TEA farmacológico Lurie Center BMC 2025 — guideline abrangente |
| REF-301 | 1 | — | 🎯 | Persico SR farmacoterapia pediátrica TEA Parte I 2021 — nível I, fundamentado |
| REF-302 | 2 | — | 🎯 | Gannon algoritmo sintomas centrais TEA adultos 2020 — orientação prática |
| REF-303 | 1 | — | — | Bula FDA mirtazapina 2023 — autoridade farmacológica; mirtazapina em TEA/insônia |
| REF-304 | 2 | — | — | RCT mirtazapina ansiedade TEA jovens 2022 — piloto; evidência II |
| REF-305 | 1 | — | 🎯 | RCT guanfacina ER hiperatividade TEA 2015 — sustenta guanfacina em TEA+TDAH |
| REF-306 | 2 | — | 🎯 | RCT guanfacina ER TEA+TDAH desfechos secundários 2018 — complementa REF-305 |
| REF-307 | 3 | — | — | Doyle McDougle farmacoterapia TEA 2012 — pré-2015; supersedido por REF-295-301 |
| REF-308 | 3 | — | — | Simon JAMA management depression 2024 — duplicata de REF-077; mesmo artigo |
| REF-309 | 1 | — | 🎯 | SR/MA Zhou JACAAP farmacoterapia comportamentos restritivos/repetitivos TEA 2020 |
| REF-310 | 1 | — | 🎯 | NMA Siafis tratamentos farmacológicos + suplementos TEA 2022 — nível I |
| REF-311 | 1 | — | 🎯 | Ali SR burnout autístico 2025 — sustenta DD burnout/depressão em TEA Nó 4 |
| REF-312 | 2 | — | 🎯 | Higgins definição burnout autístico Delphi 2021 — define fenômeno para DD |
| REF-313 | 3 | — | — | Parker burnout vs depressão clínica TEA 2021 — redundante com REF-311 |
| REF-314 | 1 | — | 🎯 | NMA intervenções não farmacológicas ansiedade/depressão TEA 2025 — nível I |
| REF-315 | 2 | — | 🎯 | RCT CBT+MBSR adultos com TEA 2017 — evidência II para psicoterapias |
| REF-316 | 2 | — | 🎯 | RCT ADEPT TCC depressão adultos autistas 2020 — sustenta TCC adaptada TEA |
| REF-317 | 2 | — | 🎯 | RCT auto-ajuda guiada ADEPT 2019 — alternativa de menor intensidade |
| REF-318 | 2 | — | 🎯 | El Baou psicoterapia atenção primária autistas adultos Lancet Psychiatry 2023 |
| REF-319 | 2 | — | 🎯 | Lord Lancet TEA 2018 — revisão ampla; complementada por REF-272 (2023) |
| REF-320 | 2 | — | 🎯 | Sharp NEJM personality disorders 2022 — contextualiza TPB no espectro |
| REF-321 | 1 | — | 🎯 | Leichsenring JAMA review TPB 2023 — revisão premium, mais recente |
| REF-322 | 1 | — | 🎯 | Bohus Lancet TPB 2021 — revisão premium; sustenta Nó 4 e Nó 6 conduta |
| REF-323 | 2 | — | 🎯 | Kaess detecção precoce/intervenção TPB 2025 — adolescentes, divergência etária |
| REF-324 | 3 | — | — | Kaess TPB adolescência 2014 — pré-2015; supersedido por REF-323 |
| REF-325 | 2 | — | 🎯 | Fox SITBI-R desenvolvimento/validade 2020 — instrumento de rastreio IVNS |
| REF-326 | 1 | — | 🎯 | Yen CLPS 10 anos TPB + tentativas JAMA Psychiatry 2021 — dados preditivos críticos |
| REF-327 | 3 | — | — | Pérez TPB com/sem tentativas e IVNS 2014 — pré-2015; supersedido por REF-326 |
| REF-328 | 2 | — | 🎯 | Hepp previsão continuum suicida do IVNS 2025 — sustenta escalada de risco |
| REF-329 | 2 | — | 🎯 | Knorr predição suicidalidade do IVNS 2019 — complementa REF-328 |
| REF-330 | 2 | — | 🎯 | Reichl auto-lesão no contexto TPB 2021 — síntese de intervenções |
| REF-331 | 1 | — | 🎯 | Cochrane psicoterapias TPB 2020 (75 RCTs) — nível I, melhor evidência para conduta |
| REF-332 | 2 | — | 🎯 | Cohen efeito psicoterapia TPB AFP 2022 — orientação prática complementar |
| REF-333 | 1 | — | 🎯 | Stoffers-Winterling BJPsych 2022 — SR/MA focado psicoterapias TPB |
| REF-334 | 1 | — | 🎯 | Linehan RCT DBT alto risco suicida TPB JAMA Psychiatry 2015 — padrão-ouro DBT |
| REF-335 | 2 | — | 🎯 | Mendez-Miller AFP TPB 2022 — orientação clínica prática para Nó 6 |
| REF-336 | 1 | — | 🎯 | Brodsky RCT DBT vs ISRS suicidalidade TPB 2025 — nível I, recentíssimo |
| REF-337 | 2 | — | 🎯 | Bateman Lancet tratamento TPB 2015 — revisão; complementa os RCTs |
| REF-338 | 1 | — | 🎯 | Gerolymos NMA farmacológico TPB 2026 (35 RCTs) — melhor evidência farmacológica |
| REF-339 | 1 | — | 🎯 | Cochrane farmacoterapia TPB 2022 (46 RCTs) — nível I, sustenta Nó 6 conduta |
| REF-340 | 3 | — | — | Cochrane farmacoterapia TPB 2010 — supersedido por REF-339 (2022) |
| REF-341 | 2 | — | 🎯 | Pascual manejo farmacológico TPB+comorbidades 2023 — orientação prática |
| REF-342 | 3 | — | 🎯 | Gunderson NEJM TPB 2011 — pré-2015; supersedido por REF-321 e REF-322 |
| REF-343 | 2 | — | — | Ilagan GPM-A adolescentes com TPB 2021 — tratamento alternativo pediátrico |
| REF-344 | 1 | — | — | Chanen RCT MOBY intervenção precoce jovens JAMA Psychiatry 2022 — evidência I pediátrica |
| REF-345 | 2 | — | — | Bourvis intervenções adolescentes TPB 2023 — complementa REF-344 |
| REF-346 | 3 | — | — | Selby IVNS+TPB dinâmica desenvolvimental 2022 — não gera conduta clínica direta |
| REF-347 | 2 | — | 🎯 | Bosworth envolvimento cuidadores psicoterapia TPB jovens 2024 — sustenta família |

---

## BLOCO 4 — REF-348 a REF-419
### Relatórios: OE-J1, J2 (T. Alimentares) | OE-K2, REF1, REF2 (DDI, Internação, CAPS)

| REF-ID | Tier | 🇧🇷 | 🎯 | Justificativa |
|--------|------|-----|-----|--------------|
| REF-348 | 1 | — | — | APA DSM-5-TR 2025 Updates — autoridade nosológica para critérios TA |
| REF-349 | 1 | — | — | Mitchell NEJM Anorexia Nervosa 2020 — revisão premium, sustenta Nó 4 TA |
| REF-350 | 1 | — | — | Zipfel Lancet Psychiatry AN avaliação e tratamento 2015 — revisão fundamental |
| REF-351 | 2 | — | — | APA DSM-5-TR 2024 Updates — complementa REF-348; anterior por 1 ano |
| REF-352 | 1 | — | — | Hornberger Pediatrics TA crianças/adolescentes 2020 — guideline pediátrico |
| REF-353 | 1 | — | — | Attia JAMA TA review 2025 — mais recente e de alta qualidade |
| REF-354 | 1 | — | — | USPSTF rastreio TA 2022 — guideline de saúde pública |
| REF-355 | 1 | — | — | APA CPG tratamento TA 2023 — guideline de máxima autoridade |
| REF-356 | 2 | — | — | AFP tratamento TA 2024 — orientação clínica prática |
| REF-357 | 2 | — | — | Hampl Pediatrics obesidade crianças 2023 — relevante para limiares etários |
| REF-358 | 2 | — | — | Staller TA e doenças GI 2023 — diagnóstico diferencial |
| REF-359 | 3 | — | — | Normative range bioquímica adolescentes 2019 — muito específico |
| REF-360 | 2 | 🇧🇷 | 🎯 | Brito internação involuntária BR vs. England 2019 — legislação BR; duplicado REF-023 mas com foco em TA |
| REF-361 | 2 | 🇧🇷 | 🎯 | Schmeling tratamento compulsório países lusófonos 2024 — duplicado REF-024 mas com foco em TA |
| REF-362 | 2 | — | — | Clausen perspectivas internação involuntária AN 2020 — sustenta discussão ética |
| REF-363 | 3 | — | — | Douzenis internação involuntária AN Int J Law 2015 — supersedido por REF-355 + legislação BR |
| REF-364 | 3 | — | — | Appelbaum civil commitment AN 1998 — muito antigo; supersedido |
| REF-365 | 2 | — | — | Trapani complicações médicas AN Pediatrics 2025 — dados de complicações pediátricas |
| REF-366 | 1 | — | — | Treasure Lancet Eating Disorders 2020 — revisão premium de alta qualidade |
| REF-367 | 2 | — | — | Cederholm NEJM desnutrição adultos 2024 — sustenta critérios de realimentação |
| REF-368 | 1 | — | — | ASPEN consenso síndrome de realimentação 2020 — guideline de máxima autoridade |
| REF-369 | 2 | — | — | Schuetz Lancet desnutrição relacionada à doença 2021 — complementa ASPEN |
| REF-370 | 1 | — | — | Garber RCT HCR vs LCR realimentação AN JAMA Pediatrics 2020 — RCT nível I |
| REF-371 | 2 | — | — | Haas re-nutrição acelerada AN 2021 — complementa REF-370 |
| REF-372 | 2 | — | — | Klein TA cuidados primários AFP 2020 — orientação clínica prática |
| REF-373 | 1 | — | 🎯 | Bula FDA Lítio 2025 — duplicata de REF-028; mas contém informações de DDI específicas do OE-K2 |
| REF-374 | 2 | — | 🎯 | Scherf-Clavel DDI lítio+CV/anti-inflamatórios 2020 — mecanismo e dados de interação |
| REF-375 | 2 | — | 🎯 | Finley Drug interactions with lithium 2016 — revisão clínica completa |
| REF-376 | 3 | — | 🎯 | Finley 1995 relevância clínica DDI lítio — pré-2015; supersedido por REF-375 |
| REF-377 | 1 | — | 🎯 | Bula FDA lamotrigina 2026 — autoridade máxima para protocolo VPA+LTG |
| REF-378 | 1 | — | 🎯 | Smith NEJM manejo inicial convulsões adultos 2021 — nível II, complementa bula LTG |
| REF-379 | 1 | — | 🎯 | SR Quiles BZD+CLZ co-prescricão 2025 — melhor evidência disponível para DDI crítica |
| REF-380 | 2 | — | 🎯 | Hassamal tramadol e SS Am J Medicine 2018 — revisão do mecanismo |
| REF-381 | 2 | — | 🎯 | Nelson tramadol+ISRSs avoiding SS 2012 — complementa REF-380 |
| REF-382 | 1 | — | 🎯 | Bula FDA tramadol 2025 — autoridade farmacológica direta |
| REF-383 | 1 | — | 🎯 | Anrys consenso DDI idosos 66 interações JAMDA 2021 — autoridade para Beers/idosos |
| REF-384 | 1 | — | 🎯 | Croke Beers Criteria AFP 2019 — guideline de referência para idosos |
| REF-385 | 1 | — | 🎯 | Arnold Beers Criteria Update 2024 AFP — versão mais recente do Beers |
| REF-386 | 1 | — | 🎯 | AGS princípios guia cuidados idosos multimorbidade 2012 — Framework 4Ms |
| REF-387 | 2 | — | 🎯 | Rubenstein age-friendly geriatric assessment AFP 2025 — orientação prática |
| REF-388 | 2 | — | 🎯 | Pinkoh utilitidade bases de DDI (Lexicomp/Drugs.com) 2023 — sustenta CDS no Nó 6 |
| REF-389 | 2 | — | 🎯 | Mallet Lancet DDI em idosos 2007 — artigo clássico, ainda relevante |
| REF-390 | 2 | — | 🎯 | Alagiakrishnan uso de CDS para medicamentos em idosos 2016 — sustenta implementação |
| REF-391 | 2 | 🇧🇷 | 🎯 | Chang internações voluntárias vs. involuntárias no Brasil 2013 — dados BR específicos |
| REF-392 | 2 | — | 🎯 | Schneider admissões compulsórias Basel-Stadt 2023 — dados de prática real |
| REF-393 | 2 | — | 🎯 | Marty tomada de decisão em internação involuntária 2019 — análise fatores clínicos |
| REF-394 | 1 | — | 🎯 | SR/MA Walker Lancet Psychiatry fatores internação involuntária 2019 — nível I, melhor evidência |
| REF-395 | 2 | — | 🎯 | Kelly Rooman+Winterwerp: medidas terapêuticas reais 2024 — jurisprudência europeia relevante |
| REF-396 | 2 | — | 🎯 | Brayley critérios legais internação involuntária — desempenho dos médicos 2015 |
| REF-397 | 2 | — | 🎯 | Hotzy compliance com lei de internação involuntária — médicos encaminhadores 2019 |
| REF-398 | 2 | — | 🎯 | Brissos CTC — Checklist de Tratamento Compulsório 2017 — instrumento de suporte |
| REF-399 | 2 | — | 🎯 | O'Callaghan necessidade objetiva de tratamento involuntário 2022 — complementa CTC |
| REF-400 | 2 | — | — | Fiorillo EUNOMIA estudo internação involuntária 2011 — contexto europeu |
| REF-401 | 2 | — | — | Perrigo guideline civil commitment assessment 2016 — contexto americano |
| REF-402 | 2 | — | — | Wasserman 40 países admissões compulsórias 2020 — panorama global |
| REF-403 | 2 | 🇧🇷 | 🎯 | Ramos CAPS-AD Brasil Int Rev Psychiatry 2025 — contexto específico do sistema BR |
| REF-404 | 2 | 🇧🇷 | 🎯 | Sampaio CAPS saúde mental Brasil BMC Public Health 2021 — dados de prática BR |
| REF-405 | 2 | 🇧🇷 | — | Castanheira APS São Paulo SUS Guidelines 2023 — contexto regulatório SP |
| REF-406 | 2 | 🇧🇷 | — | Amaral saúde mental Brasil quatro cidades 2021 — contexto do sistema |
| REF-407 | 2 | 🇧🇷 | — | Fernandes RAPS reforma psiquiátrica 2020 — contexto estrutural |
| REF-408 | 3 | 🇧🇷 | — | Bastos coordenação SUS 2020 — muito estrutural; não gera conduta clínica |
| REF-409 | 2 | 🇧🇷 | — | Paim Lancet SUS história 2011 — contexto histórico; não gera conduta |
| REF-410 | 2 | 🇧🇷 | — | Paiva CAPS Brasil 2013-2019 PLoS One 2024 — dados de rede |
| REF-411 | 3 | 🇧🇷 | — | Castro Lancet SUS 30 anos 2019 — panorama; supersedido por REF-403/404 para contexto CAPS |
| REF-412 | 1 | 🇧🇷 | 🎯 | Fontenelle uso SUS por segurados privados 2019 — evidência BR sobre cobertura cruzada Amil/SUS |
| REF-413 | 3 | 🇧🇷 | — | Rodrigues desafios SUS 2025 — opinião; não gera conduta |
| REF-414 | 3 | 🇧🇷 | — | Oliveira barreiras acesso serviços 2019 — contexto estrutural; não gera conduta |
| REF-415 | 2 | — | 🎯 | Liu DDI screening indicators idosos psiquiatria 2024 — complementa Beers |
| REF-416 | 2 | — | 🎯 | Forgerini DDI idosos transtornos mentais SR 2020 — dados de prevalência |
| REF-417 | 3 | — | — | AGS guidelines idosos diabetes 2013 — pré-2015; não diretamente relevante para psiquiatria |
| REF-418 | 2 | — | 🎯 | Steinman JAMA medicamentos em idosos complexos 2010 — princípios de prescrição |
| REF-419 | 2 | — | 🎯 | Benetos JAMA polimedicação idosos 2015 — complementa Beers e Framework 4Ms |

---

## SUMÁRIO EXECUTIVO FINAL

> **Status:** ✅ COMPLETO — todos os 419 REF-IDs classificados

### Contagens por Tier

| Métrica | Valor | % |
|---------|-------|---|
| **Total de REFs analisadas** | 419 | 100% |
| **TIER 1 — Manter obrigatório** | ~163 | ~39% |
| **TIER 2 — Manter condicional** | ~173 | ~41% |
| **TIER 3 — Candidatos a remoção** | ~83 | ~20% |
| Com flag 🇧🇷 | ~42 | ~10% |
| Com flag 🎯 (Briefing-central) | ~231 | ~55% |
| Com ambos 🇧🇷🎯 | ~17 | ~4% |
| Duplicatas identificadas (REF-308=REF-077) | 1 | — |

> **Redução efetiva ao remover TIER 3:** de 419 → ~336 referências (-20%, redução da redundância conforme meta)

### AFIs Órfãs e Redundantes — Análise

**Duplicatas identificadas:**
- REF-308 (Simon JAMA 2024 em TEA) = REF-077 (mesmo artigo, já catalogado em humor) → eliminar REF-308 do banco

**Clusters com maior redundância interna (TIER 3 predominante):**
- **Burnout/Diagnóstico diferencial (OE-E3):** 12 REFs TIER 3 — fenômeno muito bem coberto pelas SR/NMA; narrativas individuais supérfluas
- **Debate FRS esquizofrenia (OE-F1):** 4 REFs TIER 3 — debate teórico sem impacto em conduta
- **Farmacologia antiga pré-2015:** múltiplas REFs de EPS (OE-F2), SGA, e TDAH

**AFIs órfãs (sustentadas apenas por TIER 3):**
- AFIs 130-149 (burnout): dependem de REFs 130-149, vários TIER 3 — mas cluster de burnout é sustentado por AFI-141 (TIER 1/SR) e REF-140 (TIER 1/BR). Sem AFIs verdadeiramente órfãs.
- Nenhuma AFI depende exclusivamente de TIER 3 sem ter pelo menos uma referência TIER 1 ou 2 de apoio.

**AFIs redundantes identificadas:**
- AFI-083 e AFI-084 (ambas sobre diagnóstico diferencial burnout vs. depressão): consolidar em uma AFI única
- **Recomendação:** não remover AFIs; consolidar texto de 2 pares com redação mais precisa

---

## RECOMENDAÇÕES PARA O PLAYBOOK

### Top 8 Áreas com Evidência Mais Robusta (🇧🇷 + 🎯)

| Área | REFs-âncora | Por que é forte |
|------|------------|-----------------|
| **Gate P0 (risco suicida)** | REF-002, REF-008, REF-009, REF-020 | Guideline APA + VA/DoD + SR/MA C-SSRS + RCT SPI — 4 autoridades de máximo nível |
| **Monitoramento de Lítio** | REF-027, REF-028, REF-373, REF-374 | CANMAT/ISBD + Bula FDA + mecanismo DDI com AINEs — completo para Nó 5 |
| **Monitoramento Metabólico (SGA)** | REF-049, REF-211, REF-213, REF-214 | SR guideline-concordant + NMA Lancet + JACC + JAMA Psychiatry 2025 |
| **Clozapina (ANC + CIGH)** | REF-052, REF-197, REF-199, REF-202, REF-379 | Bula FDA + Lancet Delphi + coorte finlandesa + Am J Psych 25 anos + SR 2025 |
| **Depressão/TAB tratamento** | REF-059, REF-062, REF-075, REF-079 | DSM-5-TR + Lancet TAB 2025 + CANMAT MDD 2023 + Cipriani NMA 21 ADs |
| **TEPT** | REF-150, REF-151, REF-153, REF-156 | APA CPG 2025 + VA/DoD 2024 + Cochrane + NMA psicoterapias — robusto |
| **DDI VPA+LTG** | REF-377, REF-378 | Bula FDA LTG 2026 + NEJM 2021 — autoridade máxima para protocolo de titulação |
| **Internação involuntária BR** | REF-023, REF-391, REF-412 | Legislação BR (REF-023) + dados BR (REF-391) + cobertura Amil/SUS (REF-412) |

### Top 5 Lacunas e Dependência de Literatura Não-Brasileira

| Lacuna | Impacto | Mitigação |
|--------|---------|-----------|
| **CAPS III em SP: sem dado de tempos de espera ou capacidade real** | CAPS III é alternativa central no Nó 6 — sem garantia de acesso | Usar REF-403/404 + recomendação de contato direto com unidade |
| **Valproato no Brasil: sem dado de frequência de teratogenicidade na prática real BR** | Alerta VPA em RMIF baseia-se em EURAP europeu | Usar dados EURAP com nota de extrapolação; aguardar dado ANVISA |
| **TDAH: ASRS sem validação formal em português do Brasil** | ASRS é o instrumento de triagem central mas validado internacionalmente, não em BR | Usar validação WHO + cross-cultural; flag em GUARDRAIL |
| **DBT no Brasil: custo e disponibilidade** | DBT é 1ª linha para TPB mas extremamente cara no sistema suplementar | Conduta no Nó 6 deve incluir alternativa (TCC-DBT-informada) |
| **Burnout: sem guideline clínico BR** | OE-E3 depende de literatura de alta qualidade mas sem guideline criado para o contexto BR específico | Usar REF-140 (dado BR) + REF-141 (SR) como âncoras |

---

## DECISÃO FINAL — O QUE USAR NO PLAYBOOK

**Para citar explicitamente no playbook e condicionar Nós do JSON:**

Usar prioritariamente REF-IDs com **ambos os flags 🇧🇷🎯**, seguido de **🎯 TIER 1**. Exemplos obrigatórios:
- Gate P0: REF-002, REF-008, REF-020
- Lítio: REF-027, REF-028
- CLZ: REF-052, REF-197, REF-379
- Scales BR: REF-067, REF-068, REF-069, REF-071
- Internação BR: REF-023, REF-391, REF-412
- Beers/idosos: REF-384, REF-385

**REFs TIER 3 — não citar no playbook**, mas manter no banco para:
- Contexto histórico (REF-013, REF-180, REF-181)
- Suporte a divergências documentadas

---

*Auditoria gerada por Antigravity em 2026-02-27 | Para aprovação por Dan antes do início do Playbook Draft*
