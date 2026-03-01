# BANCO DE EVIDÊNCIAS — PSIQUIATRIA AMBULATORIAL
## Amil / Daktus | Fase 1 — Alimentado pelo OpenEvidence

> **Instrução de uso:** Cada relatório recebido do OpenEvidence deve ser consolidado aqui seguindo o template de entrada abaixo. Nunca sobrescrever — apenas acrescentar. O Antigravity deve ler este arquivo inteiro antes de iniciar qualquer nó do playbook.
> 
> **Legenda de Auditoria:**
> - Referências marcadas com `*(T3)*` = TIER 3 auditado — **não citar no playbook**; presentes no banco apenas como contexto histórico.
> - Referências com tachado `~~REF-XXX~~` = duplicatas removidas — usar a referência substituta indicada.
> - Para o playbook, usar apenas referências **sem** marcador `*(T3)*` e **sem** tachado.
>
> **Versão:** 3.0 | **Última atualização:** 2026-02-27 | **Relatórios consolidados:** 10/10 (REL-01 a REL-10) ✅ COMPLETO | **Auditoria:** AUDITORIA_BANCO_v1.md + AUDITORIA_BANCO_v1_REVISAO.md + AUDITORIA_BANCO_v2.md ✅ — 7 duplicatas removidas, 10 Tiers reclassificados, ~83 TIER 3 marcados, 9 AFIs órfãs corrigidas | **Status:** PRONTO PARA PLAYBOOK

---

## ÍNDICE DE PERGUNTAS RESPONDIDAS

| Código | Tema | Status | Relatório |
|--------|------|--------|-----------|
| OE-B1 | Gate P0 — itens mínimos triagem suicida | ✅ Consolidado | REL-01 |
| OE-B2 | Gate P0 — fatores de risco por diagnóstico | ✅ Consolidado | REL-01 |
| OE-B3 | Gate P0 — conduta após ideação com plano | ✅ Consolidado | REL-01 |
| OE-K1 | Monitoramento laboratorial transversal | ✅ Consolidado | REL-02 |
| OE-D2 | Lítio — faixa e monitoramento | ✅ Consolidado | REL-02 |
| OE-D3 | Valproato — faixa e monitoramento | ✅ Consolidado | REL-02 |
| OE-D1 | Critérios — Humor | ✅ Consolidado | REL-03 |
| OE-D4 | Escalas — Depressão e Mania | ✅ Consolidado | REL-03 |
| OE-D5 | Antidepressivos e depressão resistente | ✅ Consolidado | REL-03 |
| OE-E1 | Critérios — Ansiedade, TOC, TEPT | ✅ Consolidado | REL-04 |
| OE-E2 | ISRS doses altas e QTc | ✅ Consolidado | REL-04 |
| OE-E3 | Burnout — diagnóstico e rastreio | ✅ Consolidado | REL-04 |
| OE-E4 | TEPT — tratamento e encaminhamento | ✅ Consolidado | REL-04 |
| OE-F1 | Critérios — Psicose | ✅ Consolidado | REL-05 |
| OE-F2 | Efeitos extrapiramidais e escalas | ✅ Consolidado | REL-05 |
| OE-F3 | Clozapina — monitoramento | ✅ Consolidado | REL-05 |
| OE-F4 | Antipsicóticos atípicos — risco metabólico | ✅ Consolidado | REL-05 |
| OE-G1 | Critérios — TDAH adulto | ✅ Consolidado | REL-06 |
| OE-G2 | TDAH — ECG pré-estimulantes | ✅ Consolidado | REL-06 |
| OE-G3 | TDAH — neuropsicológica formal | ✅ Consolidado | REL-06 |
| OE-G4 | TDAH — alternativas ao metilfenidato | ✅ Consolidado | REL-06 |
| OE-H1 | Critérios — TEA adulto | ✅ Consolidado | REL-07 |
| OE-H2 | TEA — farmacoterapia sintomas-alvo | ✅ Consolidado | REL-07 |
| OE-I1 | Critérios — TPB e autolesão | ✅ Consolidado | REL-08 |
| OE-I2 | TPB — DBT e adjuvantes | ✅ Consolidado | REL-08 |
| OE-J1 | Critérios — Transtornos Alimentares | ✅ Consolidado | REL-09 |
| OE-J2 | Anorexia — internação e complicações | ✅ Consolidado | REL-09 |
| OE-K2 | Interações medicamentosas | ✅ Consolidado | REL-10 |
| OE-REF1 | Internação — critérios e documentação | ✅ Consolidado | REL-10 |
| OE-REF2 | CAPS vs. internação | ✅ Consolidado | REL-10 |

---

## TABELA MESTRE DE REFERÊNCIAS

> Todas as fontes citadas em qualquer relatório entram aqui. Evita duplicatas e permite rastreabilidade cruzada entre clusters.

| REF-ID | Tipo | Autores / Organização | Título resumido | Ano | Nível evidência | Usado em |
|--------|------|----------------------|-----------------|-----|-----------------|----------|
| REF-001 | RCT/ML | Wilimitis D et al. | C-SSRS + ML para predição de risco suicida | 2022 | I | OE-B1 |
| REF-002 | Guideline/SR | Mann JJ, Michel CA, Auerbach RP (APA) | Suicide prevention — systematic review | 2021 | I | OE-B1, OE-B2 |
| REF-003 | Guideline | The Joint Commission | R3 Report Issue 18: NPSG Suicide Prevention | 2018 | III *(Consenso institucional — reclassificado de I→II pela auditoria v1; REF-002/REF-008 são âncoras superiores)* | OE-B1 |
| REF-004 | Revisão | Zarpellon HM et al. | Sigilo médico e investigação criminal — Brasil | 2025 | IV | OE-B1, OE-B3 |
| REF-005 | Revisão | Gracindo GCL et al. | Bioethical principles, Brazil Medical Ethics Code | 2018 | IV | OE-B1, OE-B3 |
| REF-006 | Revisão | Knipe D et al. | Suicide and self-harm (Lancet seminar) | 2022 | II | OE-B1, OE-B2, OE-B3 |
| REF-007 | Revisão | Hawton K et al. | Assessment of suicide risk — para formulação clínica | 2022 | III | OE-B1 |
| REF-008 | Guideline | Bahraini N et al. (VA/DoD) | Assessment and Management at Risk for Suicide 2024 | 2024 | Consenso | OE-B1, OE-B2, OE-B3 |
| REF-009 | SR/MA | Daray FM et al. | C-SSRS: systematic review and meta-analysis | 2025 | I | OE-B1 |
| REF-010 | RCT | Walsh CG et al. | Risk model–guided CDS for suicide screening | 2025 | I | OE-B1 |
| REF-011 | Guideline | Sall J et al. | VA/DoD guidelines synopsis — suicide risk | 2019 | Consenso | OE-B1, OE-B3 |
| REF-012 | Revisão | Fazel S, Runeson B | Suicide (NEJM review) | 2020 | II | OE-B2, OE-B3 |
| REF-013 | Revisão | Turecki G, Brent DA | Suicide and suicidal behaviour | 2016 | II *(T3)* | OE-B2 |
| REF-014 | Coorte | Miola A et al. | Suicidal risk/protective factors — coorte 4307 pacientes | 2023 | II | OE-B2 |
| REF-015 | Coorte | Baldessarini RJ et al. | Suicidal risk factors in major affective disorders | 2019 | II | OE-B2 |
| REF-016 | Guideline | LeFevre ML (USPSTF) | Suicide screening recommendation | 2014 | Consenso *(T3)* | OE-B1 |
| REF-017 | Guideline | Hua LL et al. (AAP) | Suicide and suicide risk in adolescents | 2023 | Consenso | OE-B1, OE-B2, OE-B3 |
| REF-018 | Guideline | Abrams T et al. (VA/DoD) | Management of Bipolar Disorder 2023 | 2023 | Consenso | OE-B2 |
| REF-019 | Guideline | Nazarian DJ et al. | Clinical policy: psychiatric patient in ED | 2017 | Consenso | OE-B3 |
| REF-020 | RCT | Stanley B et al. | SPI+ vs. usual care | 2018 | I | OE-B3 |
| REF-021 | SR/MA | Doupnik SK et al. | Suicide prevention interventions — meta-analysis | 2020 | I | OE-B3 |
| REF-022 | Guideline | Saidinejad M et al. (AAP) | Pediatric mental health emergencies | 2023 | Consenso | OE-B3 |
| REF-023 | Revisão | Brito ES, Ventura CAA | Internação involuntária — Brasil vs. Inglaterra | 2019 | IV | OE-B3 |
| REF-024 | Revisão | Schmeling J et al. | Compulsory treatment — países lusófonos | 2024 | IV | OE-B3 |
| REF-025 | Revisão | Sheridan Rains L et al. | Padrões de internação involuntária — internacional | 2019 | III *(T3)* | OE-B3 |
| REF-026 | Revisão | Chieze M et al. | Medidas coercitivas em psiquiatria — revisão ética | 2021 | IV *(T3)* | OE-B3 |
| REF-027 | Guideline | Yatham LN et al. (CANMAT/ISBD) | CANMAT/ISBD 2018 Guidelines — Bipolar Disorder | 2018 | I/Consenso | OE-K1, OE-D2, OE-D3 |
| REF-028 | Bula (FDA) | FDA | Lithium Carbonate/Lithium Drug Labels (2022–2025) | 2025 | — | OE-D2 |
| REF-029 | Revisão | Malhi GS, Gessler D, Outhred T | Lithium for BD: recommendations from CPGs | 2017 | III *(T3)* | OE-D2 |
| REF-030 | Coorte | Nikolova VL et al. | Lithium monitoring in UK secondary care | 2018 | III | OE-D2 |
| REF-031 | Bula (FDA) | FDA | Valproic Acid Drug Label | 2024 | — | OE-D3 |
| REF-032 | Coorte | Carli M et al. | 5-year lithium/valproate monitoring — Italian center | 2022 | III | OE-D2, OE-D3 |
| REF-033 | SR | Meijboom RW, Grootens KP | Dispensability of annual lab follow-up after >2y valproate | 2017 | II | OE-D3 |
| REF-034 | Revisão | Bjørk MH et al. | Management of reproductive risks in epilepsy | 2025 | II | OE-D3 |
| REF-035 | Coorte/SR | Tomson T et al. (EURAP) | Comparative risk of malformations — antiepileptics | 2018 | II | OE-D3 |
| REF-036 | Revisão | Wartman C, VandenBerg A | Valproate: not all boxed warnings equal | 2022 | IV *(T3)* | OE-D3 |
| REF-037 | Guideline | Pack AM et al. (AAN/AES/SMFM) | Teratogenesis after in utero exposure to ASM | 2024 | Consenso | OE-D3 |
| REF-038 | Revisão | Andrade C | Valproate in pregnancy: research and regulatory responses | 2018 | IV *(T3)* | OE-D3 |
| REF-039 | Coorte | Kim H et al. | AED treatment patterns in women of childbearing age | 2019 | III *(T3)* | OE-D3 |
| REF-040 | Revisão | Varallo FR et al. | Harmonization of pharmacovigilance in Brazil | 2019 | IV *(T3)* | OE-K1 |
| REF-041 | Revisão | Nederlof M et al. | Clinical/biomarker monitoring in SmPC psychotropics | 2015 | IV *(T3)* | OE-K1 |
| REF-042 | Revisão | Nierenberg AA et al. | Diagnosis and treatment of BD — JAMA review | 2023 | II | OE-D2, OE-D3 |
| REF-043 | Bula (FDA) | FDA | Carbamazepine Drug Labels (2025) | 2025 | — | OE-K1 |
| REF-044 | Coorte | Grześk G et al. | Therapeutic drug monitoring of carbamazepine — 20 years | 2021 | III | OE-K1 |
| REF-045 | Revisão | Marder SR, Cannon TD | Schizophrenia (NEJM) | 2019 | II | OE-K1 |
| REF-046 | Revisão | Pringsheim T et al. | Physical health and drug safety in schizophrenia | 2017 | III | OE-K1 |
| REF-047 | Guideline | VA/DoD (Arias-Reynoso M et al.) | Management of First-Episode Psychosis/Schizophrenia 2023 | 2023 | Consenso | OE-K1 |
| REF-048 | Bula (FDA) | FDA | Risperidone/Paliperidone Drug Labels (2025–2026) | 2026 | — | OE-K1 |
| REF-049 | SR/MA | Mitchell AJ et al. | Guideline-concordant metabolic monitoring — SR/MA | 2011 | I | OE-K1 |
| REF-050 | Bula (FDA) | FDA | Olanzapine Drug Labels (2025–2026) | 2026 | — | OE-K1 |
| REF-051 | SR | Gurrera RJ et al. | Recognition and management of clozapine adverse effects | 2022 | II | OE-K1 |
| REF-052 | Bula (FDA) | FDA | Clozapine Drug Label (2025) | 2025 | — | OE-K1 |
| REF-053 | Bula (FDA) | FDA | Quetiapine Fumarate Drug Labels (2025) | 2025 | — | OE-K1 |
| REF-054 | Guideline | Ng F et al. (ISBD) | ISBD consensus guidelines — safety monitoring BD treatments | 2009 | III *(pré-2015; supersedido por CANMAT 2018 — REF-027; reclassificado pela auditoria)* | OE-K1 |
| REF-055 | Consenso | Xiong GL et al. | QTc monitoring — expert consensus | 2020 | III | OE-K1 |
| REF-056 | Revisão | Polcwiartek C et al. | Cardiovascular safety of antipsychotics | 2016 | III *(T3)* | OE-K1 |
| REF-057 | Revisão | Mauri MC et al. | Paliperidone drug safety evaluation | 2017 | III *(T3)* | OE-K1 |
| REF-058 | Farmacovigil. | Lou S et al. | Adverse events paliperidone — pharmacovigilance FAERS/JADER | 2025 | III *(T3)* | OE-K1 |
| REF-059 | Guideline | APA | DSM-5-TR (Diagnostic and Statistical Manual, 5th ed., Text Revision) | 2022 | Consenso | OE-D1 |
| REF-060 | Revisão | Miller L, Campo JV | Depression in Adolescents | NEJM | 2021 | II | OE-D1, OE-D5 |
| REF-061 | Revisão | Park LT, Zarate CA | Depression in the Primary Care Setting | NEJM | 2019 | II | OE-D1, OE-D5 |
| REF-062 | Revisão | Singh B et al. | Bipolar Disorder (Lancet 2025) | Lancet | 2025 | II | OE-D1 |
| REF-063 | Revisão | McIntyre RS et al. | Bipolar Disorders (Lancet 2020) | Lancet | 2020 | II *(T3)* | OE-D1 |
| REF-064 | Original | Zimmerman M, Mackin D | Mixed features specifier — how many criteria? | J Clin Psychiatry | 2026 | II | OE-D1 |
| REF-065 | SR | Berk M et al. | Bipolar II Disorder: state-of-the-art review | World Psychiatry | 2025 | I | OE-D1 |
| REF-066 | Revisão | Carvalho AF, Firth J, Vieta E | Bipolar Disorder (NEJM 2020) | NEJM | 2020 | II *(T3)* | OE-D1 |
| REF-067 | Psicometria | Faro A et al. | PHQ-9 in Brazil — psychometric analysis (n>10k) | Front Psychol | 2024 | II | OE-D4 |
| REF-068 | Psicometria | Moreno-Agostino D et al. | PHQ-9 psychometric properties — older adults Brazil | Aging Mental Health | 2022 | II | OE-D4 |
| REF-069 | Psicometria | Carneiro AM et al. | HAM-D and MADRS — Brazilian validation | Health QoL Outcomes | 2015 | II | OE-D4 |
| REF-070 | Original | Thase ME et al. | MADRS severity thresholds in bipolar depression | J Affect Disord | 2021 | II | OE-D4 |
| REF-071 | Psicometria | Vilela JA et al. | YMRS — Portuguese validation | Braz J Med Biol Res | 2005 | II | OE-D4 |
| REF-072 | Psicometria | Vignola RC, Tucci AM | DASS-21 — Brazilian Portuguese adaptation | J Affect Disord | 2014 | III | OE-D4 |
| REF-073 | Psicometria | Vilela-Estrada AL et al. | PHQ-8/GAD-7 — Latin American adolescents | J Affect Disord | 2025 | II | OE-D4 |
| REF-074 | Psicometria | Jobim GDS et al. | SMFQ — Brazilian validation | J Psychiatr Res | 2025 | II | OE-D4 |
| REF-075 | Guideline | Lam RW et al. (CANMAT) | CANMAT 2023 Update — MDD | Can J Psychiatry | 2024 | I/Consenso | OE-D1, OE-D5 |
| REF-076 | Guideline | Qaseem A et al. (ACP) | ACP Living Guideline — MDD (2023) | Ann Intern Med | 2023 | Consenso | OE-D5 |
| REF-077 | Revisão | Simon GE, Moise N, Mohr DC | Management of Depression in Adults | JAMA | 2024 | II | OE-D5 |
| REF-078 | Revisão | Coles S, Wise D | Management of MDD — CANMAT guidelines summary | Am Fam Physician | 2025 | III *(T3)* | OE-D5 |
| REF-079 | SR/NMA | Cipriani A et al. | 21 antidepressants — comparative efficacy NMA | Lancet | 2018 | I | OE-D5 |
| REF-080 | Revisão | Steffens DC | Treatment-Resistant Depression in Older Adults | NEJM | 2024 | II | OE-D5 |
| REF-081 | Revisão | Masi G | Controversies pharmacotherapy adolescent depression | Curr Pharm Design | 2022 | III *(T3)* | OE-D5 |
| REF-082 | Revisão | Tanana L et al. | Regulatory labeling pediatric depression — international | J Child Adolesc Psychopharmacol | 2021 | III | OE-D5 |
| REF-083 | Revisão | Thapar A et al. | Depression in young people | Lancet | 2022 | II | OE-D5 |
| REF-084 | SR | McIntyre RS et al. | TRD — definition, prevalence, detection | World Psychiatry | 2023 | I | OE-D5 |
| REF-085 | Revisão | Gaddey HL et al. | Depression managing resistance and partial response | Am Fam Physician | 2024 | III | OE-D5 |
| REF-086 | Consenso | Rybak YE et al. | TRD — Canadian expert consensus on definition | Depression and Anxiety | 2021 | III *(T3)* | OE-D5 |
| REF-087 | Revisão | Fekadu A et al. | Maudsley Staging Method — standardisation framework | BMC Psychiatry | 2018 | III | OE-D5 |
| REF-088 | SR | Ruhé HG et al. | Staging methods for TRD | J Affect Disord | 2012 | II *(T3)* | OE-D5 |
| REF-089 | Revisão | Salloum NC, Papakostas GI | Staging treatment intensity — defining TRD | J Clin Psychiatry | 2019 | III *(T3)* | OE-D5 |
| REF-090 | Original | Petersen T et al. | Empirical testing staging models for TRD | J Clin Psychopharmacol | 2005 | II *(T3)* | OE-D5 |
| REF-091 | Revisão | Whooley MA | Diagnosis and treatment depression + comorbid conditions | JAMA | 2012 | III *(T3)* | OE-D5 |
| REF-092 | SR/NMA | Saelens J et al. | Relative effectiveness of antidepressants in TRD | Neuropsychopharmacology | 2025 | I | OE-D5 |
| REF-093 | Guideline | Arnold MJ et al. | Medications for Treatment-Resistant Depression | Am Fam Physician | 2020 | Consenso | OE-D5 |
| REF-094 | Revisão | Goh KK et al. | Therapeutic strategies for TRD | Curr Pharm Design | 2020 | III *(T3)* | OE-D5 |
| REF-095 | Original | Fournier JC et al. | TRD consultation program | J Clin Psychiatry | 2025 | III *(T3)* | OE-D5 |
| REF-096 | SR | Gabriel FC et al. | Guidelines for TRD — quality review | PLoS One | 2023 | II | OE-D5 |
| REF-097 | Guideline | Ridout K et al. (APA) | Resource Document on MBC | APA | 2023 | Consenso | OE-D5 |
| REF-098 | Original | Garcia ME et al. | Depression treatment after positive screen | JAMA Intern Med | 2025 | II | OE-D5 |
| REF-099 | RCT | Husain MI et al. | MBC to enhance antidepressant outcomes | JAMA Network Open | 2025 | I | OE-D5 |
| REF-100 | Original | Hawley S et al. | Digitization of MBC — REDCap + EHR | J Med Internet Res | 2021 | III *(T3)* | OE-D5 |
| REF-101 | Original | Kumar M et al. | Mental health systems in LMICs — routine MBC | JAMA Psychiatry | 2025 | III *(T3)* | OE-D5 |
| REF-102 | Revisão | Unützer J | Late-Life Depression | NEJM | 2007 | II *(T3)* | OE-D5 |
| REF-103 | Revisão | Szuhany KL, Simon NM | Anxiety Disorders: A Review | JAMA | 2022 | II | OE-E1 |
| REF-104 | Revisão | DeGeorge KC et al. | GAD and Panic Disorder in Adults | Am Fam Physician | 2022 | III | OE-E1 |
| REF-105 | Guideline | Kowalchuk A et al. | Anxiety Disorders in Children and Adolescents | Am Fam Physician | 2022 | Consenso | OE-E1 |
| REF-106 | Guideline | Walter HJ et al. | Clinical PG anxiety disorders children — JACAAP | JACAAP | 2020 | Consenso | OE-E1 |
| REF-107 | Guideline | ACOG | Mental Health Disorders in Adolescents | ACOG | 2017 | Consenso *(T3)* | OE-E1 |
| REF-108 | Guideline | Sartor Z et al. | PTSD Evaluation and Treatment | Am Fam Physician | 2023 | Consenso | OE-E1, OE-E4 |
| REF-109 | Revisão | Katon WJ | Panic Disorder | NEJM | 2006 | II *(T3)* | OE-E1 |
| REF-110 | Guideline | Gluckman TJ et al. (ACC) | COVID-19 cardiovascular sequelae — ACC Expert Consensus | JACC | 2022 | Consenso | OE-E1 |
| REF-111 | Revisão | Bryarly M et al. | POTS — JACC Focus Seminar | JACC | 2019 | II | OE-E1 |
| REF-112 | Revisão | Ahmed A et al. | Inappropriate Sinus Tachycardia — JACC Review | JACC | 2022 | II | OE-E1 |
| REF-113 | Revisão | Kroenke K | Practical evidence-based approach to common symptoms | Ann Intern Med | 2014 | III *(T3)* | OE-E1 |
| REF-114 | Guideline | Rossi LP et al. (AHA) | Person-Centered Models for CV Care | Circulation | 2023 | Consenso | OE-E1 |
| REF-115 | Original | Wouters LT et al. | Telephone triage nurses — acute cardiac event | J Clin Nursing | 2020 | III *(T3)* | OE-E1 |
| REF-116 | Guideline | Semenya AM, Bhatnagar P | Diagnosis and Management of OCD in primary care | Am Fam Physician | 2024 | Consenso | OE-E1, OE-E2 |
| REF-117 | Revisão | Gualtieri G et al. | Supratherapeutic SSRI doses in resistant OCD | J Clin Med | 2025 | III | OE-E2 |
| REF-118 | Bula (FDA) | FDA | Sertraline Hydrochloride Drug Labels 2024 (consolidated) | FDA | 2024 | — | OE-E2 |
| REF-119 | Revisão | Funk KA, Bostwick JR | Comparison of QT prolongation among SSRIs | Ann Pharmacother | 2013 | III *(T3)* | OE-E2 |
| REF-120 | SR/MA | Beach SR et al. | Meta-analysis SSRI-associated QTc prolongation | J Clin Psychiatry | 2014 | I | OE-E2 |
| REF-121 | Revisão | Giraud EL et al. | QT interval prolongation potential — drugs | Lancet Oncol | 2022 | II | OE-E2 |
| REF-122 | Farmacovigil. | Cao S et al. | Arrhythmic events antidepressants — FAERS | Front Psychiatry | 2025 | III *(T3)* | OE-E2 |
| REF-123 | Coorte | Maljuric NM et al. | SSRI and QTc — Rotterdam Study | Br J Clin Pharmacol | 2015 | II | OE-E2 |
| REF-124 | Coorte | Castro VM et al. | QT interval and antidepressants — EHR cross-sectional | BMJ | 2013 | II | OE-E2 |
| REF-125 | Consenso | Simoons M et al. | Dutch consensus ECG monitoring antidepressants | Drug Safety | 2018 | III *(T3)* | OE-E2 |
| REF-126 | Guideline | Tisdale JE et al. (AHA) | Drug-Induced Arrhythmias — AHA Scientific Statement | Circulation | 2020 | Consenso | OE-E2 |
| REF-127 | Revisão | Chang HM et al. | Cardiovascular complications cancer therapy — JACC | JACC | 2017 | III *(T3)* | OE-E2 |
| REF-128 | Revisão | Zolezzi M, Cheung L | Algorithm QTc prolongation — psychiatric population | Neuropsychiatr Dis Treat | 2019 | IV *(T3)* | OE-E2 |
| REF-129 | Revisão | Reed GM et al. | ICD-11 classification changes — World Psychiatry | World Psychiatry | 2019 | IV | OE-E3 |
| REF-130 | Revisão | Hillert A et al. | Burnout phenomenon — 15,000+ publications | Front Psychiatry | 2021 | IV | OE-E3 |
| REF-131 | Original | Hewitt DB et al. | Burnout definitions and prevalence — JAMA Surgery | JAMA Surgery | 2020 | III | OE-E3 |
| REF-132 | Revisão | Atroszko PA et al. | Work addiction and burnout — ICD-11 implications | Int J Environ Res PH | 2020 | IV *(T3)* | OE-E3 |
| REF-133 | Revisão | Harvey SB et al. | Mental illness and suicide among physicians | Lancet | 2021 | II | OE-E3 |
| ~~REF-134~~ | ~~Revisão~~ | ~~First MB et al.~~ | ~~ICD-11 vs DSM-5 comparison~~ | ~~2021~~ | ~~IV~~ | ~~OE-E3~~ | ⚠️ **REMOVIDA — DUPLICATA FUNCIONAL de REF-129** (Reed 2019, mesmo tema/cluster; manter REF-129) |
| REF-135 | Revisão | Parker G, Russo N | Burnout definition and measurement — review | Psychiatry Research | 2025 | IV *(T3)* | OE-E3 |
| REF-136 | Original | Crudden G et al. | Physician burnout anxiety and depression — Ireland | PLoS One | 2023 | III *(T3)* | OE-E3 |
| REF-137 | Original | Parker G, Tavella G | Distinguishing burnout from depression — theoretical | J Affect Disord | 2021 | IV | OE-E3 |
| REF-138 | Original | Tavella G et al. | Burnout and depression — convergence and divergence | J Affect Disord | 2023 | III | OE-E3 |
| REF-139 | Original | Tavella G, Parker G | Distinguishing burnout from depression — qualitative | Psychiatry Research | 2020 | IV *(T3)* | OE-E3 |
| REF-140 | Original | de Amorim Macedo MJ et al. | Burnout depression anxiety — latent and network analysis (Brazil) | J Psychiatr Res | 2023 | II | OE-E3 |
| REF-141 | SR/MA | Koutsimani P et al. | Burnout depression anxiety relationship — SR/MA | Front Psychol | 2018 | I | OE-E3 |
| REF-142 | Original | Fischer R et al. | Burnout depression anxiety Brazil (critical care) — JAMA Netw Open | JAMA Network Open | 2020 | III | OE-E3 |
| REF-143 | SR | Rotenstein LS et al. | Prevalence burnout among physicians — systematic review | JAMA | 2018 | I | OE-E3 |
| REF-144 | Original | Merces MCD et al. | Burnout nursing Brazil — prevalence and factors | Int J Environ Res PH | 2020 | III *(T3)* | OE-E3 |
| REF-145 | Original | Oliveira AM et al. | Job satisfaction burnout depression — Brazilian teaching hospital | Medicine | 2018 | III *(T3)* | OE-E3 |
| REF-146 | Psicometria | Sinval J et al. | OLBI transcultural adaptation — Brazil and Portugal | Front Psychol | 2018 | III *(T3)* | OE-E3 |
| REF-147 | Psicometria | Sinval J et al. | BAT — validity evidence from Brazil and Portugal | Int J Environ Res PH | 2022 | II | OE-E3 |
| REF-148 | Psicometria | Hadžibajramović E et al. | BAT4 ultra-short — validation and measurement invariance | PLoS One | 2023 | II | OE-E3 |
| REF-149 | Psicometria | Demarzo M et al. | BCSQ-12 validation — Brazilian primary care | Int J Environ Res PH | 2020 | II *(T3)* | OE-E3 |
| REF-150 | Guideline | Zoellner LA et al. (APA) | CPG PTSD adults 2025 | APA | 2025 | Consenso | OE-E4 |
| REF-151 | Guideline | Schnurr PP et al. | VA/DoD PTSD guideline synopsis — Ann Intern Med | Ann Intern Med | 2024 | Consenso | OE-E4 |
| REF-152 | Guideline | Bandelow B et al. (WFSBP) | Guidelines anxiety OCD PTSD — Part II | World J Biol Psychiatry | 2023 | Consenso | OE-E4 |
| REF-153 | SR/MA | Williams T et al. | Pharmacotherapy for PTSD — Cochrane 2022 | Cochrane Database | 2022 | I | OE-E4 |
| REF-154 | Guideline | Seales S, Seales P | Pharmacotherapy for PTSD — Am Fam Physician | Am Fam Physician | 2022 | Consenso | OE-E4 |
| REF-155 | RCT | Fortney JC et al. | Pragmatic comparative effectiveness PTSD — primary care | JAMA Psychiatry | 2025 | I | OE-E4 |
| REF-156 | NMA | Hoppen TH et al. | Psychological interventions adult PTSD — network MA | J Consult Clin Psychol | 2023 | I | OE-E4 |
| REF-157 | SR | Kip A et al. | Psychological interventions PTSD — SR of meta-analyses | J Anxiety Disord | 2025 | I | OE-E4 |
| REF-158 | SR/MA | Simpson E et al. | EMDR effectiveness and cost-effectiveness — SR/MA | Br J Psychol | 2025 | I | OE-E4 |
| REF-159 | SR/MA | Milligan T et al. | Loss of PTSD diagnosis in response to evidence-based treatments | JAMA Psychiatry | 2025 | I | OE-E4 |
| REF-160 | RCT | Ehlers A et al. | STOP-PTSD — therapist-assisted online therapy RCT | Lancet Psychiatry | 2023 | I | OE-E4 |
| REF-161 | Psicometria | de Faria Cardoso C et al. | PDS-3 short version — Brazilian Portuguese validation | Front Psychol | 2021 | II | OE-E4 |
| REF-162 | Guideline | APA | DSM-5-TR Updates 2023–2025 (consolidated) | APA | 2025 | Consenso | OE-E1 |
| REF-163 | Revisão | Leucht S et al. | Psychopathological symptoms in psychiatric diagnoses | JAMA Psychiatry | 2024 | II | OE-E1 |
| REF-164 | Original | Eilers R et al. | PTSD and CPTSD children/adolescents — ICD-11 effects | Bundesgesundheitsbl | 2024 | II | OE-E1, OE-E4 |
| REF-165 | Revisão | McCutcheon RA et al. | Schizophrenia — An Overview | JAMA Psychiatry | 2020 | II | OE-F1, OE-F2 |
| REF-166 | Revisão | Fusar-Poli P et al. | Brief psychotic episodes — review and research agenda | Lancet Psychiatry | 2021 | II | OE-F1 |
| REF-167 | Revisão | Jauhar S et al. | Schizophrenia | Lancet | 2022 | II | OE-F1 |
| REF-168 | Original | Nordgaard J et al. | Associations between self-disorders and FRS | Psychopathology | 2020 | III | OE-F1 |
| REF-169 | SR | Soares-Weiser K et al. | First rank symptoms for schizophrenia — Cochrane | Cochrane Database | 2015 | II *(reclassificado de I→II pela auditoria: debate FRS superado clinicamente; não citar em seções de conduta)* | OE-F1 |
| REF-170 | Original | Peralta V, Cuesta MJ | Schneider's FRS — diagnostic value | Psychological Medicine | 2023 | II | OE-F1 |
| REF-171 | Revisão | Feyaerts J et al. | Delusions beyond beliefs — Lancet Psychiatry | Lancet Psychiatry | 2021 | II | OE-F1 |
| REF-172 | Original | Moscarelli M | FRS — major flaw in diagnosis of schizophrenia | Psychological Medicine | 2020 | IV *(T3)* | OE-F1 |
| REF-173 | Original | Moritz S et al. | DSM-6 survey — FRS reinstatement as core criteria | Schizophrenia Bulletin | 2024 | III *(T3)* | OE-F1 |
| REF-174 | Original | Moritz S et al. | What Kurt Schneider really said | Schizophrenia Bulletin | 2023 | IV *(T3)* | OE-F1 |
| REF-175 | Revisão | Heinz A et al. | Shall we say goodbye to FRS? | European Psychiatry | 2016 | IV *(T3)* | OE-F1 |
| REF-176 | Original | Sykes DA et al. | EPS linked to association kinetics at D2 receptors | Nature Communications | 2017 | II | OE-F2 |
| REF-177 | Revisão | Factor SA et al. | Drug-induced movement disorders | Lancet Neurology | 2019 | II | OE-F2 |
| REF-178 | Revisão | Divac N et al. | SGA and extrapyramidal adverse effects | Biomed Research International | 2014 | III *(T3)* | OE-F2 |
| REF-179 | SR/NMA | Siafis S et al. | Antipsychotic dose, D2 occupancy and EPS | Molecular Psychiatry | 2023 | I | OE-F2 |
| REF-180 | NMA | Leucht S et al. | Comparative efficacy and tolerability 15 antipsychotics | Lancet | 2013 | II *(pré-2015; reclassificado de I→II pela auditoria — REF-211 e REF-217 são superiores; manter como clássico histórico)* | OE-F2, OE-F4 |
| REF-181 | SR/MA | Rummel-Kluge C et al. | SGA and EPS — head-to-head comparisons | Schizophrenia Bulletin | 2011 | II *(pré-2015; reclassificado de I→II pela auditoria — REF-184 e REF-179 são superiores)* | OE-F2 |
| REF-182 | Revisão | Pillinger T et al. | Antidepressant/antipsychotic side-effects digital tool | Lancet Psychiatry | 2023 | II | OE-F2, OE-F4 |
| REF-183 | Coorte | Novick D et al. | EPS incidence SOHO 36-month | J Clin Psychopharmacol | 2010 | II *(T3)* | OE-F2 |
| REF-184 | SR/MA | Ali T et al. | Antipsychotic-induced EPS — observational SR/MA | PLoS One | 2021 | I | OE-F2 |
| REF-185 | Guideline | Marzani G, Price Neff A | Bipolar Disorders evaluation and treatment — AIMS table | Am Fam Physician | 2021 | Consenso | OE-F2 |
| REF-186 | Original | Widschwendter CG et al. | EPS adverse events and movement disorder rating scales | Int J Neuropsychopharmacol | 2015 | II | OE-F2 |
| REF-187 | Original | Gopal S et al. | Paliperidone EPS incidence — LAI pooled analysis | Neuropsychiatr Dis Treat | 2013 | II *(T3)* | OE-F2 |
| REF-188 | Coorte | Bo QJ et al. | EPS during risperidone maintenance — multicenter | J Clin Psychopharmacol | 2016 | II *(T3)* | OE-F2 |
| REF-189 | Guideline | Hua LL | Collaborative care psychosis adolescents | Pediatrics | 2021 | Consenso | OE-F2 |
| REF-190 | Revisão | Correll CU | Adverse effects antipsychotic young patients | J Clin Psychiatry | 2010 | III *(T3)* | OE-F2 |
| REF-191 | Original | Carbon M et al. | Neuromotor adverse effects youth SGA 12 weeks | JACAAP | 2015 | II | OE-F2 |
| REF-192 | Revisão | Wijdicks EFM, Ropper AH | Neuroleptic Malignant Syndrome | NEJM | 2024 | II | OE-F2 |
| REF-193 | Guideline | APA | Resource Document on Catatonia | APA | 2025 | Consenso | OE-F2 |
| REF-194 | Consenso | Gurrera RJ et al. | NMS diagnostic criteria — Delphi | J Clin Psychiatry | 2011 | III | OE-F2 |
| REF-195 | Revisão | Robottom BJ et al. | Movement disorders emergencies — hypokinetic | Archives Neurology | 2011 | III *(T3)* | OE-F2 |
| REF-196 | Revisão | Gratz SS et al. | Treatment and management of NMS | Prog Neuro-Psychopharmacol | 1992 | IV *(T3)* | OE-F2 |
| REF-197 | Consenso | Siskind D et al. | ANC monitoring clozapine — global Delphi panel | Lancet Psychiatry | 2025 | III | OE-F3 |
| REF-198 | Original | Schulte PFJ et al. | Risk of clozapine-associated agranulocytosis and regulations | Schizophrenia Research | 2024 | II | OE-F3 |
| REF-199 | Coorte | Rubio JM et al. | Long-term agranulocytosis risk — Finland cohort | Lancet Psychiatry | 2024 | II | OE-F3 |
| REF-200 | Revisão | Cohen D | Clozapine and gastrointestinal hypomotility | CNS Drugs | 2017 | III | OE-F3 |
| REF-201 | Farmacovigil. | Handley SA et al. | CIGH UK pharmacovigilance 1992–2017 | Br J Psychiatry | 2022 | III | OE-F3 |
| REF-202 | Coorte | Partanen JJ et al. | Ileus and pneumonia in clozapine — Finland 25-year | Am J Psychiatry | 2024 | II | OE-F3 |
| REF-203 | Coorte | Palmer SE et al. | Life-threatening CIGH — 102 cases | J Clin Psychiatry | 2008 | II | OE-F3 |
| REF-204 | Original | Every-Palmer S et al. | Constipation screening diagnostic accuracy — clozapine | Schizophrenia Research | 2020 | II | OE-F3 |
| REF-205 | Revisão | Cohen D et al. | Beyond white blood cell monitoring — clozapine | J Clin Psychiatry | 2012 | III | OE-F3 |
| REF-206 | Original | Every-Palmer S et al. | Porirua Protocol for CIGH | CNS Drugs | 2016 | III | OE-F3 |
| REF-207 | Revisão | West S et al. | CIGH potentially life-threatening review | General Hospital Psychiatry | 2017 | III *(T3)* | OE-F3 |
| REF-208 | Revisão | Baptista T et al. | Expert review clozapine Latin America | Schizophrenia Research | 2024 | III | OE-F3 |
| REF-209 | Revisão | Baptista T et al. | Clozapine safety monitoring South America — scoping review | Schizophrenia Research | 2024 | III *(T3)* | OE-F3 |
| REF-210 | Revisão | Nielsen J et al. | Worldwide differences regulations clozapine | CNS Drugs | 2016 | III *(T3)* | OE-F3 |
| REF-211 | SR/NMA | Pillinger T et al. | 18 antipsychotics metabolic function — NMA (100 RCTs) | Lancet Psychiatry | 2019 | I | OE-F4 |
| REF-212 | Revisão | Newcomer JW | SGA and metabolic effects — comprehensive review | CNS Drugs | 2005 | III *(T3)* | OE-F4 |
| REF-213 | Revisão | Goldfarb M et al. | Severe mental illness and cardiovascular disease — JACC | JACC | 2022 | II | OE-F4 |
| REF-214 | Original | Smith ECC et al. | Antipsychotic drugs and dysregulated glucose homeostasis | JAMA Psychiatry | 2025 | II | OE-F4 |
| REF-215 | RCT | Zhang Y et al. | Metabolic effects 7 antipsychotics — short-term | J Clin Psychiatry | 2020 | II | OE-F4 |
| REF-216 | Coorte | Feng Y et al. | Longitudinal metabolic outcomes SGA treatment sequences | Psychological Medicine | 2025 | II | OE-F4 |
| REF-217 | NMA | Hamina A et al. | Comparative effectiveness antipsychotics — Finland | JAMA Network Open | 2024 | I | OE-F4 |
| REF-218 | Coorte | Vieira JCM et al. | Clozapine vs. non-clozapine Brazil — comparative effectiveness | Front Psychiatry | 2024 | II | OE-F3, OE-F4 |
| REF-219 | Coorte | Fulone I et al. | Switching SGA Brazil — 10-year cohort | Front Pharmacology | 2021 | II | OE-F4 |
| REF-220 | Revisão | Citrome L | Choosing among LAI antipsychotics — evidenced-based guide | CNS Spectrums | 2025 | III | OE-F4 |
| REF-221 | Revisão | de Filippis R et al. | Current and emerging LAI antipsychotics | Expert Opinion Drug Safety | 2021 | III *(T3)* | OE-F4 |
| REF-222 | Revisão | Faden J et al. | LAI risperidona overview | Expert Review Neurotherapeutics | 2024 | III *(T3)* | OE-F4 |
| REF-223 | Revisão | Volkow ND, Swanson JM | Adult Attention Deficit–Hyperactivity Disorder | NEJM | 2013 | II | OE-G1 |
| REF-224 | Revisão | Posner J et al. | Attention-Deficit Hyperactivity Disorder | Lancet | 2020 | II | OE-G1 |
| REF-225 | Guideline | Pujalte GGA et al. (AMSSM) | ADHD and the athlete — position statement 2023 | Clin J Sport Med | 2023 | Consenso | OE-G1, OE-G2 |
| REF-226 | Guideline | Olagunju AE, Ghoddusi F | ADHD in adults — AFP 2024 | Am Fam Physician | 2024 | Consenso | OE-G1, OE-G2, OE-G3, OE-G4 |
| REF-227 | Original | Ustun B et al. | WHO ASRS for DSM-5 | JAMA Psychiatry | 2017 | II | OE-G1 |
| REF-228 | Psicometria | Lewczuk K et al. | Cross-cultural ASRS 42 countries | J Attention Disorders | 2024 | II | OE-G1 |
| REF-229 | Psicometria | Kessler RC et al. | WHO ASRS validation | Psychological Medicine | 2005 | II | OE-G1 |
| REF-230 | Original | Hines JL et al. | ASRS for ADHD screening in primary care | J Am Board Fam Med | 2012 | II | OE-G1 |
| REF-231 | Revisão | Chamberlain SR et al. | ADHD positive screen caveats | Comprehensive Psychiatry | 2021 | III | OE-G1 |
| REF-232 | Original | Babinski DE et al. | ADHD screening outpatient psychiatric | Psychiatry Research | 2022 | III *(T3)* | OE-G1 |
| REF-233 | Original | van de Glind G et al. | ASRS in substance use disorder patients | Drug Alcohol Dependence | 2013 | II | OE-G1 |
| REF-234 | Revisão | Torres-Acosta N et al. | Cardiovascular effects ADHD therapies — JACC | JACC | 2020 | II | OE-G2 |
| REF-235 | Bula (FDA) | FDA | Lisdexamfetamine Drug Label 2025 | FDA | 2025 | — | OE-G2 |
| REF-236 | Guideline | Putukian M et al. (AMSSM) | ADHD and the athlete — position statement 2011 | Clin J Sport Med | 2011 | Consenso *(T3)* | OE-G2 |
| REF-237 | SR/NMA | Farhat LC et al. | Comparative cardiovascular safety ADHD medications | Lancet Psychiatry | 2025 | I | OE-G2, OE-G4 |
| REF-238 | Revisão | Cortese S | Pharmacologic treatment ADHD | NEJM | 2020 | II | OE-G2, OE-G4 |
| REF-239 | Coorte | Zhang L et al. | ADHD medications long-term CVD risk | JAMA Psychiatry | 2024 | II | OE-G2 |
| REF-240 | Guideline | Kooij JJS et al. | Updated European consensus adult ADHD | European Psychiatry | 2019 | Consenso | OE-G3 |
| REF-241 | Original | Adamou M et al. | Adult ADHD assessment quality assurance standard | Front Psychiatry | 2024 | III | OE-G3 |
| REF-242 | Revisão | Marshall P et al. | Diagnosing ADHD young adults — utility review | Clinical Neuropsychologist | 2020 | III | OE-G3 |
| REF-243 | Original | Nikolas MA et al. | Neurocognitive tests in adult ADHD assessment | Psychological Assessment | 2019 | II | OE-G3 |
| REF-244 | Original | Sibley MH | Guidelines first-time adult ADHD diagnosis | J Clin Exp Neuropsychology | 2021 | III | OE-G3 |
| REF-245 | Original | Nelson JM, Lovett BJ | Assessing ADHD in college students | Psychological Assessment | 2019 | III *(T3)* | OE-G3 |
| REF-246 | Revisão | Eng AG et al. | Evidence-based assessment for ADHD | Assessment | 2023 | III | OE-G3 |
| REF-247 | SR/MA | Radonjić NV et al. | Nonstimulant medications adult ADHD — SR/MA | CNS Drugs | 2023 | I | OE-G4 |
| REF-248 | SR | Verbeeck W et al. | Bupropion for adult ADHD — Cochrane | Cochrane Database | 2017 | I | OE-G4 |
| REF-249 | Revisão | Perugi G, Vannucchi G | Stimulants + atomoxetine in ADHD+bipolar | Expert Opinion Pharmacotherapy | 2015 | III | OE-G4 |
| REF-250 | SR | Mucci F et al. | ADHD with comorbid bipolar — SR | Current Medicinal Chemistry | 2019 | II | OE-G4 |
| REF-251 | Revisão | Perugi G et al. | Current and emerging pharmacotherapy ADHD | Expert Opinion Pharmacotherapy | 2019 | III *(T3)* | OE-G4 |
| REF-252 | Revisão | Pérez de los Cobos J et al. | ADHD and addiction — pharmacological dilemmas | Br J Clin Pharmacol | 2014 | III | OE-G4 |
| REF-253 | Revisão | Schubiner H | Substance abuse in patients with ADHD | CNS Drugs | 2005 | III *(T3)* | OE-G4 |
| REF-254 | Guideline | Greenhill LL et al. (AACAP) | Practice parameter stimulant medications | JACAAP | 2002 | Consenso *(T3)* | OE-G4 |
| REF-255 | Revisão | Barbuti M et al. | Treating ADHD with comorbid SUD | J Clin Med | 2023 | III | OE-G4 |
| REF-256 | Revisão | Simon N et al. | Methylphenidate in adults with ADHD and SUD | Curr Pharm Design | 2015 | III *(T3)* | OE-G4 |
| REF-257 | Guideline | ASAM/AAAP | Clinical practice guideline stimulant use disorder | J Addiction Medicine | 2024 | Consenso | OE-G4 |
| REF-258 | SR/MA | Zhang L et al. (2022) | Risk of CVD with ADHD medications — SR/MA | JAMA Network Open | 2022 | I | OE-G2 |
| REF-259 | Bula (FDA) | FDA | Strattera/Atomoxetine Drug Label 2025 | FDA | 2025 | — | OE-G4 |
| REF-260 | SR/MA | Sposito AC et al. | Cardiovascular safety naltrexone and bupropion | Obesity Reviews | 2021 | I | OE-G4 |
| REF-261 | Bula (FDA) | FDA | Clonidine Hydrochloride Drug Label 2020 | FDA | 2020 | — | OE-G4 |
| REF-262 | Bula (FDA) | FDA | Guanfacine Hydrochloride Drug Label 2024 | FDA | 2024 | — | OE-G4 |
| REF-263 | Original | Nasser A et al. | Viloxazine ER and QTc — evaluation | J Clin Psychiatry | 2020 | II | OE-G4 |
| REF-264 | SR/MA | Farhat LC et al. | Treatment outcomes with licensed/unlicensed stimulant doses | JAMA Psychiatry | 2024 | I | OE-G4 |
| REF-265 | Guideline | AAP | ADHD guideline update 2020 (via AAFP) | AAFP/AAP | 2020 | Consenso | OE-G2 |
| REF-266 | Revisão | Martinez-Raga J et al. | Risk serious cardiovascular ADHD medications | CNS Drugs | 2012 | III *(T3)* | OE-G2 |
| REF-267 | Revisão | Thapar A, Cooper M | Attention Deficit Hyperactivity Disorder | Lancet | 2016 | II *(T3)* | OE-G1 |
| REF-268 | Original | Loskutova NY et al. | Tablet-based ADHD screening primary care | J Attention Disorders | 2021 | III *(T3)* | OE-G1 |
| REF-269 | Original | Schneider BC et al. | Assessment adult ADHD clinical practice survey | J Attention Disorders | 2023 | III *(T3)* | OE-G3 |
| REF-270 | Revisão | Gonda X et al. | Pharmacological, neuromodulatory, psychotherapeutic ADHD | Pharmacology & Therapeutics | 2026 | III | OE-G4 |
| REF-271 | Revisão | Constantino JN, Charman T | Diagnosis of ASD — reconciling diversity | Lancet Neurology | 2016 | II | OE-H1 |
| REF-272 | Revisão | Hirota T, King BH | Autism Spectrum Disorder: A Review | JAMA | 2023 | II | OE-H1, OE-H2 |
| REF-273 | Guideline | Westby A, Coburn-Pierce M | ASD in Primary Care — AFP 2025 | Am Fam Physician | 2025 | Consenso | OE-H1, OE-H2 |
| REF-274 | Original | Whaling KM et al. | Streamlining adult autism diagnosis — telesaúde, n=234 | J Autism Dev Disord | 2025 | II | OE-H1 |
| REF-275 | Original | McQuaid GA et al. | Camouflaging in ASD — sex, gender, diagnostic timing | Autism | 2022 | II | OE-H1 |
| REF-276 | Revisão | Lai MC, Baron-Cohen S | Identifying the lost generation of adults with ASD | Lancet Psychiatry | 2015 | III | OE-H1 |
| REF-277 | Revisão | Rujeedawa T, Zaman SH | ASD in adult females — diagnosis and management | Int J Environ Res Public Health | 2022 | III | OE-H1 |
| REF-278 | Original | Kentrou V et al. | Perceived misdiagnosis in autistic adults | EClinicalMedicine | 2024 | II | OE-H1 |
| REF-279 | Qualitativo | Garcia-Simon MI et al. | Females with late ASD diagnosis — experiences | Nursing Research | 2025 | III *(T3)* | OE-H1 |
| REF-280 | SR | Zhuang S et al. | Camouflaging and mental health in autistic people — mixed SR | Clinical Psychology Review | 2023 | II | OE-H1 |
| REF-281 | Revisão | Alaghband-Rad J et al. | Camouflage and masking behavior in adult autism | Front Psychiatry | 2023 | III *(T3)* | OE-H1 |
| REF-282 | Original | Brugha T et al. | Testing adults for ASD — AQ in mental health service | Int J Methods Psychiatr Res | 2020 | III | OE-H1 |
| REF-283 | Original | Ashwood KL et al. | Predicting ASD diagnosis with AQ | Psychological Medicine | 2016 | II | OE-H1 |
| REF-284 | Original | Ritvo RA et al. | RAADS-R — international validation | J Autism Dev Disord | 2011 | II | OE-H1 |
| REF-285 | Original | Andersen LM et al. | Swedish RAADS-R validation | J Autism Dev Disord | 2011 | II | OE-H1 |
| REF-286 | Original | Rausch J et al. | German RAADS-R / RADS-R validation | Eur Arch Psychiatry Clin Neurosci | 2024 | II | OE-H1 |
| REF-287 | Original | Picot MC et al. | French RAADS-R validation and diagnostic accuracy | J Autism Dev Disord | 2020 | II | OE-H1 |
| REF-288 | Original | Robinson J et al. | Three screening measures for adult autism | PLoS One | 2025 | II | OE-H1 |
| REF-289 | Original | Maddox BB et al. | Accuracy ADOS-2 in adults with psychiatric conditions | J Autism Dev Disord | 2017 | II | OE-H1 |
| REF-290 | Original | Fusar-Poli L et al. | ADOS-2 + ADI-R in adults without ID | J Autism Dev Disord | 2017 | II | OE-H1 |
| REF-291 | SR | Baghdadli A et al. | Screening and diagnostic tools autism adults — SR | European Psychiatry | 2017 | I | OE-H1 |
| REF-292 | Revisão | Carroll HM et al. | Differential diagnosis of ASD in adults | Expert Review Neurotherapeutics | 2025 | III | OE-H1 |
| REF-293 | Revisão | Lehnhardt FG et al. | Investigation and DD of Asperger in adults | Deutsches Arzteblatt | 2013 | III *(T3)* | OE-H1 |
| REF-294 | Revisão | Curnow E et al. | Diagnostic assessment autism adults — ADOS-2 | Front Psychiatry | 2023 | III | OE-H1 |
| REF-295 | SR/MA | Salazar de Pablo G et al. | Pharmacological interventions irritability ASD | JACAAP | 2023 | I | OE-H2 |
| REF-296 | SR/NMA | Meza N et al. | Atypical antipsychotics for ASD — Cochrane NMA | Cochrane Database | 2025 | I | OE-H2 |
| ~~REF-297~~ | ~~Bula (FDA)~~ | ~~FDA~~ | ~~Risperidone Drug Label 2025~~ | ~~2025~~ | ~~—~~ | ~~OE-H2~~ | ⚠️ **REMOVIDA — DUPLICATA de REF-048** (Risperidone/Paliperidone 2025-2026; usar REF-048 para AFIs de TEA) |
| REF-298 | Bula (FDA) | FDA | Aripiprazole Drug Label 2024/2025 (consolidated) | FDA | 2024 | — | OE-H2 |
| REF-299 | SR | Iffland M et al. | Pharmacological intervention irritability/aggression/SIB ASD — Cochrane | Cochrane Database | 2023 | I | OE-H2 |
| REF-300 | Guideline | Manter MA et al. | Pharmacological treatment autism — guidelines (Lurie Center BMC) | BMC Medicine | 2025 | Consenso | OE-H2 |
| REF-301 | SR | Persico AM et al. | Pediatric psychopharmacology of ASD — SR Part I | Prog Neuro-Psychopharmacol | 2021 | I | OE-H2 |
| REF-302 | Revisão | Gannon S, Osser DN | Algorithm for core symptoms ASD in adults | Psychiatry Research | 2020 | Consenso | OE-H2 |
| REF-303 | Bula (FDA) | FDA | Mirtazapine Drug Label 2023 | FDA | 2023 | — | OE-H2 |
| REF-304 | RCT | McDougle CJ et al. | Mirtazapine for anxiety in ASD youth — pilot RCT | Neuropsychopharmacology | 2022 | II | OE-H2 |
| REF-305 | RCT | Scahill L et al. | Guanfacine ER for hyperactivity in ASD | Am J Psychiatry | 2015 | II | OE-H2 |
| REF-306 | RCT | Politte LC et al. | Guanfacine ER in ASD + ADHD — secondary outcomes | Neuropsychopharmacology | 2018 | II | OE-H2 |
| REF-307 | Revisão | Doyle CA, McDougle CJ | Pharmacologic treatments ASD behavioral symptoms | Dialogues Clin Neurosci | 2012 | III *(T3)* | OE-H2 |
| ~~REF-308~~ | ~~Revisão~~ | ~~Simon GE et al.~~ | ~~Management of Depression in Adults~~ | ~~2024~~ | ~~II~~ | ~~OE-H2~~ | ⚠️ **REMOVIDA — DUPLICATA EXATA de REF-077** (mesmo artigo JAMA Simon 2024; manter REF-077 em OE-D5) |
| REF-309 | SR/MA | Zhou MS et al. | Pharmacologic treatment restricted/repetitive behaviors ASD | JACAAP | 2020 | I | OE-H2 |
| REF-310 | SR/NMA | Siafis S et al. | Pharmacological and dietary-supplement treatments ASD | Molecular Autism | 2022 | I | OE-H2 |
| REF-311 | SR | Ali D et al. | Burnout as experienced by autistic people | Clinical Psychology Review | 2025 | II | OE-H2 |
| REF-312 | Delphi | Higgins JM et al. | Defining autistic burnout — Delphi | Autism | 2021 | III | OE-H2 |
| ~~REF-313~~ | ~~Original~~ | ~~Parker G, Tavella G~~ | ~~Distinguishing burnout from clinical depression~~ | ~~2021~~ | ~~III~~ | ~~OE-H2~~ | ⚠️ **REMOVIDA — DUPLICATA de REF-137** (Parker & Tavella 2021 J Affect Disord; mesmo paper indexado em OE-H2 por engano) |
| REF-314 | SR/NMA | Ding X et al. | Non-pharmacological interventions anxiety/depression ASD — NMA | Front Psychiatry | 2025 | I | OE-H2 |
| REF-315 | RCT | Sizoo BB, Kuiper E | CBT and MBSR in adults with ASD | Research Dev Disabilities | 2017 | II | OE-H2 |
| REF-316 | RCT | Russell A et al. | ADEPT feasibility RCT — CBT for depression in autistic adults | Autism | 2020 | II | OE-H2 |
| REF-317 | RCT | Russell A et al. | Guided self-help — ADEPT RCT | Health Technology Assessment | 2019 | II | OE-H2 |
| REF-318 | Coorte | El Baou C et al. | Primary care psychological therapy autistic adults | Lancet Psychiatry | 2023 | II | OE-H2 |
| REF-319 | Revisão | Lord C et al. | Autism Spectrum Disorder | Lancet | 2018 | II | OE-H1 |
| REF-320 | Revisão | Sharp C | Personality Disorders | NEJM | 2022 | II | OE-I1 |
| REF-321 | Revisão | Leichsenring F et al. | Borderline Personality Disorder: A Review | JAMA | 2023 | II | OE-I1, OE-I2 |
| REF-322 | Revisão | Bohus M et al. | Borderline Personality Disorder | Lancet | 2021 | II | OE-I1, OE-I2 |
| REF-323 | Revisão | Kaess M, Cavelti M | Early detection and intervention BPD | J Child Psychol Psychiatry | 2025 | II | OE-I1 |
| REF-324 | Revisão | Kaess M et al. | BPD in adolescence | Pediatrics | 2014 | III *(T3)* | OE-I1 |
| REF-325 | Original | Fox KR et al. | SITBI-R — development, reliability, validity | Psychological Assessment | 2020 | II | OE-I1 |
| REF-326 | Original | Yen S et al. | BPD criteria and suicide attempts — CLPS 10 years follow-up | JAMA Psychiatry | 2021 | II | OE-I1 |
| REF-327 | Original | Pérez S et al. | BPD with/without suicide attempts and NSSI | Psychiatry Research | 2014 | III *(T3)* | OE-I1 |
| REF-328 | Original | Hepp J et al. | Suicidality predictors from NSSI — acquired capability | J Affective Disorders | 2025 | II | OE-I1 |
| REF-329 | Original | Knorr AC et al. | Predicting suicidal continuum from NSSI | Psychiatry Research | 2019 | II | OE-I1 |
| REF-330 | Revisão | Reichl C, Kaess M | Self-harm in context of BPD | Current Opinion Psychology | 2021 | III | OE-I1, OE-I2 |
| REF-331 | SR | Storebø OJ et al. | Psychological therapies for BPD — Cochrane 2020 (75 RCTs) | Cochrane Database | 2020 | I | OE-I2 |
| REF-332 | Revisão | Cohen D et al. | Effect of psychotherapy on BPD — AFP 2022 | Am Fam Physician | 2022 | Consenso | OE-I2 |
| REF-333 | SR/MA | Stoffers-Winterling JM et al. | Psychotherapies for BPD — focused SR/MA BJPsych | British J Psychiatry | 2022 | I | OE-I2 |
| REF-334 | RCT | Linehan MM et al. | DBT for high suicide risk BPD — RCT + component analysis | JAMA Psychiatry | 2015 | I | OE-I2 |
| REF-335 | Revisão | Mendez-Miller M et al. | BPD — AFP 2022 | Am Fam Physician | 2022 | Consenso | OE-I2 |
| REF-336 | RCT | Brodsky BS et al. | DBT vs. SSRI suicidal behavior BPD — RCT 2025 | Am J Psychiatry | 2025 | I | OE-I2 |
| REF-337 | Revisão | Bateman AW et al. | Treatment of personality disorder | Lancet | 2015 | II | OE-I2 |
| REF-338 | SR/NMA | Gerolymos C et al. | Pharmacological treatments BPD — NMA 2026 (35 RCTs) | Molecular Psychiatry | 2026 | I | OE-I2 |
| REF-339 | SR | Stoffers-Winterling JM et al. | Pharmacological interventions BPD — Cochrane 2022 (46 RCTs) | Cochrane Database | 2022 | I | OE-I2 |
| REF-340 | SR | Stoffers J et al. | Pharmacological interventions BPD — Cochrane 2010 | Cochrane Database | 2010 | I *(T3)* | OE-I2 |
| REF-341 | Revisão | Pascual JC et al. | Pharmacological management BPD and comorbidities | CNS Drugs | 2023 | III | OE-I2 |
| REF-342 | Revisão | Gunderson JG | BPD — NEJM 2011 | NEJM | 2011 | III *(T3)* | OE-I1, OE-I2 |
| REF-343 | Revisão | Ilagan GS, Choi-Kain LW | GPM-A for adolescents with BPD | Current Opinion Psychology | 2021 | III | OE-I1 |
| REF-344 | RCT | Chanen AM et al. | MOBY trial — early intervention BPD youth | JAMA Psychiatry | 2022 | I | OE-I1 |
| REF-345 | Revisão | Bourvis N et al. | Interventions in adolescents with BPD | J Clin Med | 2023 | III | OE-I1 |
| REF-346 | Revisão | Selby EA et al. | NSSI and BPD developmental dynamics | Current Psychiatry Reports | 2022 | III *(T3)* | OE-I1 |
| REF-347 | SR | Bosworth C et al. | Caregiver involvement in psychotherapy for BPD youth | Clin Psychol Psychother | 2024 | II | OE-I1 |
| REF-348 | Guideline | APA | 2025 Updates to DSM-5-TR Criteria and Text | APA | 2025 | Consenso | OE-J1 |
| REF-349 | Revisão | Mitchell JE, Peterson CB | Anorexia Nervosa | NEJM | 2020 | II | OE-J1, OE-J2 |
| REF-350 | Revisão | Zipfel S et al. | AN: Aetiology, Assessment, and Treatment | Lancet Psychiatry | 2015 | II | OE-J1, OE-J2 |
| REF-351 | Guideline | APA | 2024 Updates to DSM-5-TR Criteria and Text | APA | 2024 | IV *(supersedido pela versão 2025 — REF-348; reclassificado de II→IV pela auditoria)* | OE-J1 |
| REF-352 | Guideline | Hornberger LL, Lane MA | Identification and Management of Eating Disorders in Children/Adolescents | Pediatrics | 2020 | Consenso | OE-J1, OE-J2 |
| REF-353 | Revisão | Attia E, Walsh BT | Eating Disorders: A Review | JAMA | 2025 | II | OE-J1, OE-J2 |
| REF-354 | Guideline | USPSTF et al. | Screening for Eating Disorders in Adolescents and Adults | JAMA | 2022 | III *(USPSTF Grade I em adultos — insuficiência de evidência; Grade B apenas em adolescentes; reclassificado de I→III pela auditoria)* | OE-J1 |
| REF-355 | Guideline | Crone C et al. (APA) | APA Practice Guideline for Treatment of Eating Disorders | Am J Psychiatry | 2023 | Consenso | OE-J1, OE-J2 |
| REF-356 | Guideline | Arnold MJ | Treating Patients With Eating Disorders — AFP 2024 | Am Fam Physician | 2024 | Consenso | OE-J2 |
| REF-357 | Guideline | Hampl SE et al. | Clinical Practice Guideline Evaluation/Treatment Obesity Children | Pediatrics | 2023 | Consenso | OE-J1 |
| REF-358 | Revisão | Staller K et al. | Eating Disorders and GI Disorders | Lancet Gastroenterology | 2023 | III | OE-J1 |
| REF-359 | Original | Bandesh K et al. | Normative Range Blood Biochemical Adolescents | PLoS One | 2019 | III *(T3)* | OE-J1 |
| ~~REF-360~~ | ~~Revisão~~ | ~~Brito ES, Ventura CAA~~ | ~~Involuntary Psychiatric Admission Brazil vs England~~ | ~~2019~~ | ~~III~~ | ~~OE-J1~~ | ⚠️ **REMOVIDA — DUPLICATA de REF-023** (mesmo paper, indexado novamente em OE-J1) |
| ~~REF-361~~ | ~~Revisão~~ | ~~Schmeling J et al.~~ | ~~Compulsory Treatment Portuguese-Speaking Countries~~ | ~~2024~~ | ~~III~~ | ~~OE-J1~~ | ⚠️ **REMOVIDA — DUPLICATA de REF-024** (mesmo paper, indexado novamente em OE-J1) |
| REF-362 | Revisão | Clausen L | Perspectives on Involuntary Treatment AN | Front Psychiatry | 2020 | III | OE-J1 |
| REF-363 | Revisão | Douzenis A, Michopoulos I | Involuntary Admission AN | Int J Law Psychiatry | 2015 | III *(T3)* | OE-J1 |
| REF-364 | Revisão | Appelbaum PS, Rumpf T | Civil Commitment Anorexic Patient | Gen Hosp Psychiatry | 1998 | III *(T3)* | OE-J1 |
| REF-365 | Revisão | Trapani S, Rubino C | Medical Complications AN | Pediatrics | 2025 | II | OE-J2 |
| REF-366 | Revisão | Treasure J et al. | Eating Disorders | Lancet | 2020 | II | OE-J1, OE-J2 |
| REF-367 | Revisão | Cederholm T, Bosaeus I | Malnutrition in Adults | NEJM | 2024 | II | OE-J2 |
| REF-368 | Guideline | da Silva JSV et al. | ASPEN Consensus Recommendations for Refeeding Syndrome | Nutr Clin Pract | 2020 | Consenso | OE-J2 |
| REF-369 | Revisão | Schuetz P et al. | Management Disease-Related Malnutrition | Lancet | 2021 | II | OE-J2 |
| REF-370 | RCT | Garber AK et al. | Refeeding Optimize Inpatient Gains AN — RCT HCR vs LCR | JAMA Pediatrics | 2020 | I | OE-J2 |
| REF-371 | Revisão | Haas V et al. | Practice-Based Evidence Accelerated Re-Nutrition AN | JACAAP | 2021 | III | OE-J2 |
| REF-372 | Revisão | Klein DA et al. | Eating Disorders in Primary Care — Diagnosis and Management | Am Fam Physician | 2020 | Consenso | OE-J2 |
| REF-373 | Bula (FDA) | FDA | Lithium Carbonate Drug Labels — múltiplas versões (2022–2025) | FDA | 2025 | — *(contexto DDI apenas — near-duplicata de REF-028; usar REF-028 para AFIs gerais de lítio; REF-373 apenas para seção de interações OE-K2)* | OE-K2 |
| REF-374 | Original | Scherf-Clavel M et al. | Drug-Drug Interactions Lithium + Cardiovascular/Anti-Inflammatory | Pharmacopsychiatry | 2020 | III | OE-K2 |
| REF-375 | Revisão | Finley PR | Drug Interactions With Lithium: An Update | Clin Pharmacokinetics | 2016 | III | OE-K2 |
| REF-376 | Revisão | Finley PR, Warner MD, Peabody CA | Clinical Relevance Drug Interactions Lithium | Clin Pharmacokinetics | 1995 | III *(T3)* | OE-K2 |
| REF-377 | Bula (FDA) | FDA | Lamotrigine Drug Label 2026 | FDA | 2026 | — | OE-K2 |
| REF-378 | Revisão | Smith PEM | Initial Management of Seizure in Adults | NEJM | 2021 | II | OE-K2 |
| REF-379 | SR | Quiles C, de Leon J, Verdoux H | BZD + Clozapine Co-Prescription — SR + Expert Rec. | Expert Opinion Drug Metab Toxicol | 2025 | II | OE-K2 |
| REF-380 | Revisão | Hassamal S et al. | Tramadol: Understanding Risk of Serotonin Syndrome | Am J Medicine | 2018 | III | OE-K2 |
| REF-381 | Revisão | Nelson EM, Philbrick AM | Avoiding Serotonin Syndrome: Tramadol + SSRIs | Annals Pharmacotherapy | 2012 | IV *(pré-2015; mecanismo coberto por REF-380 + Bula REF-382; reclassificado de II→IV pela auditoria)* | OE-K2 |
| REF-382 | Bula (FDA) | FDA | Tramadol Hydrochloride Drug Label 2025 | FDA | 2025 | — | OE-K2 |
| REF-383 | Consenso | Anrys P et al. | International Consensus List DDI in Older People (66 interações) | JAMDA | 2021 | II | OE-K2 |
| REF-384 | Guideline | Croke L | Beers Criteria Inappropriate Medication Use Older Patients — AFP 2019 | Am Fam Physician | 2019 | IV *(supersedido pelo Update 2024 — REF-385; reclassificado de I→IV pela auditoria)* | OE-K2 |
| REF-385 | Guideline | Arnold MJ | Beers Criteria Update 2024 — AFP | Am Fam Physician | 2024 | Consenso | OE-K2 |
| REF-386 | Guideline | AGS Expert Panel | Guiding Principles Care Older Adults Multimorbidity | JAGS | 2012 | Consenso | OE-K2 |
| REF-387 | Revisão | Rubenstein C et al. | The Age-Friendly Geriatric Assessment | Am Fam Physician | 2025 | Consenso | OE-K2 |
| REF-388 | Original | Pinkoh R et al. | Psychotropic DDI Identification Utility — Drugs.com, Lexicomp, Epocrates | PLoS One | 2023 | III | OE-K2 |
| REF-389 | Revisão | Mallet L, Spinewine A, Huang A | Challenge Managing Drug Interactions Elderly | Lancet | 2007 | III | OE-K2 |
| REF-390 | Original | Alagiakrishnan K et al. | Physicians' Use CDS Medication Management Elderly (SMART) | Clin Interventions Aging | 2016 | II | OE-K2 |
| REF-391 | Original | Chang TM et al. | Voluntary vs. Involuntary Psychiatric Admissions Brazil | Cad Saude Publica | 2013 | III | OE-REF1 |
| REF-392 | Original | Schneider M et al. | Compulsory Psychiatric Admissions Basel-Stadt 2013–2022 | Int J Social Psychiatry | 2023 | III | OE-REF1 |
| REF-393 | Original | Marty S et al. | Psychiatric Emergency Decision-Making Involuntary Admission | Front Psychiatry | 2019 | III | OE-REF1 |
| REF-394 | SR/MA | Walker S et al. | Clinical/Social Factors Involuntary Hospitalization | Lancet Psychiatry | 2019 | II | OE-REF1 |
| REF-395 | Revisão | Kelly BD | Rooman + Winterwerp: Real Therapeutic Measures | Int J Law Psychiatry | 2024 | III | OE-REF1 |
| REF-396 | Original | Brayley J et al. | Legal Criteria Involuntary Mental Health — Clinician Performance | Med J Australia | 2015 | III | OE-REF1 |
| REF-397 | Original | Hotzy F et al. | Involuntary Admission Compliance Law — Referring Physicians | Int J Law Psychiatry | 2019 | III | OE-REF1 |
| REF-398 | Original | Brissos S et al. | Compulsory Psychiatric Treatment Checklist (CTC) — Development | Int J Law Psychiatry | 2017 | III | OE-REF1 |
| REF-399 | Original | O'Callaghan AK et al. | Objective Necessity Involuntary Treatment — Legal Admission Status | Int J Law Psychiatry | 2022 | III | OE-REF1 |
| REF-400 | SR/Consenso | Fiorillo A et al. | EUNOMIA Study: Improving Involuntary Admissions | European Psychiatry | 2011 | III | OE-REF1 |
| REF-401 | Original | Perrigo TL, Williams KA | Evidence Based Guideline Civil Commitment Assessment | Community Mental Health | 2016 | III | OE-REF1 |
| REF-402 | SR | Wasserman D et al. | Compulsory Admissions Mental Disorders 40 European Countries | European Psychiatry | 2020 | III | OE-REF1 |
| REF-403 | Revisão | Ramos A, Castaldelli-Maia JM | Key Features CAPS-AD Brazil | Int Review Psychiatry | 2025 | III | OE-REF2 |
| REF-404 | Original | Sampaio ML, Bispo Júnior JP | Comprehensive Mental Health Care CAPS Brazil | BMC Public Health | 2021 | III | OE-REF2 |
| REF-405 | Original | Castanheira ERL et al. | Primary Health Care São Paulo — SUS Guidelines | Cad Saude Publica | 2023 | III | OE-REF2 |
| REF-406 | Original | Amaral CEM et al. | Mental Healthcare Brazil — Four Large Cities | Cad Saude Publica | 2021 | III | OE-REF2 |
| REF-407 | Original | Fernandes CJ et al. | Healthcare Coverage Index RAPS — Psychiatric Reform | Cad Saude Publica | 2020 | III | OE-REF2 |
| REF-408 | Original | Bastos LBR et al. | Coordinating Brazilian Unified Health System | Rev Saude Publica | 2020 | III *(T3)* | OE-REF2 |
| ~~REF-409~~ | ~~Revisão~~ | ~~Paim J et al.~~ | ~~Brazilian Health System: History, Advances, Challenges~~ | ~~2011~~ | ~~III~~ | ~~OE-REF2~~ | ⚠️ **REMOVIDA — supersedida por REF-411** (Castro et al. 2019, mesmo tema; REF-409 é pré-2015) |
| REF-410 | Original | Paiva do Carmo Mercedes B et al. | Profile CAPS Brazil 2013–2019 | PLoS One | 2024 | III | OE-REF2 |
| REF-411 | Revisão | Castro MC et al. | Brazil's Unified Health System: First 30 Years | Lancet | 2019 | III *(T3)* | OE-REF2 |
| REF-412 | SR | Fontenelle LF et al. | Utilization SUS by Privately Insured | Cad Saude Publica | 2019 | III | OE-REF2 |
| REF-413 | Revisão | Rodrigues DLG | Challenges and Opportunities SUS | Public Health | 2025 | III *(T3)* | OE-REF2 |
| REF-414 | Original | Oliveira RAD et al. | Barriers Access Services Five Health Regions Brazil | Cad Saude Publica | 2019 | III *(T3)* | OE-REF2 |
| REF-415 | Delphi | Liu Y et al. | DDI Screening Indicators Elderly Psychiatry | BMC Psychiatry | 2024 | III | OE-K2 |
| REF-416 | SR | Forgerini M et al. | Drug Interactions Elderly Mental Behavioral Disorders | Archives Gerontology | 2020 | II | OE-K2 |
| REF-417 | Guideline | AGS | Guidelines Older Adults Diabetes Mellitus 2013 | JAGS | 2013 | Consenso *(T3)* | OE-K2 |
| REF-418 | Revisão | Steinman MA, Hanlon JT | Managing Medications Clinically Complex Elders | JAMA | 2010 | III | OE-K2 |
| REF-419 | Revisão | Benetos A et al. | Polypharmacy Aging Patient — Management Octogenarians | JAMA | 2015 | III | OE-K2 |


---

## TABELA MESTRE DE AFIRMAÇÕES CLÍNICAS

> Cada afirmação extraída dos relatórios recebe um ID único, nível de evidência e rastreabilidade até a referência.

| AFI-ID | Cluster | Código OE | Afirmação | Nível Evid. | Grau Rec. | REF-ID | Notas / Divergências |
|--------|---------|-----------|-----------|-------------|-----------|--------|----------------------|
<!-- REL-01: AFI-001 a AFI-025 (Gate P0) — ver Relatório 01 abaixo -->
| AFI-001 | B | OE-B1 | C-SSRS é o instrumento de triagem suicida mais amplamente adotado, endossado pela APA, VA e Joint Commission | I | A | REF-002, REF-003, REF-008 | CFM não exige instrumento específico (REF-004) |
| AFI-002 | B | OE-B1 | 7 itens mínimos obrigatórios: ideação passiva, ideação ativa, plano, intenção, acesso a meios, tentativas prévias, suporte social | I | A | REF-001, REF-002, REF-006, REF-008 | Convergência de todos os frameworks |
| AFI-003 | B | OE-B1 | C-SSRS breve: 6 perguntas em cascata; Q3–Q5 só se Q2 positivo | I | A | REF-001 | Estrutura validada para setting ambulatorial |
| AFI-004 | B | OE-B1 | C-SSRS prediz tentativas não-fatais futuras: OR 3,14 (IC95% 1,86–5,31) | I | A | REF-009 | Meta-análise 27 amostras independentes |
| AFI-005 | B | OE-B1 | C-SSRS prediz tentativas de suicídio: OR 2,78 (IC95% 1,82–4,24) | I | A | REF-009 | Idem |
| AFI-006 | B | OE-B1 | Ideação atual acrescenta poder preditivo à história de tentativa; OR 4,8 (IC95% 2,23–10,32) em adolescentes | I | A | REF-002 | Relevante para gate de seguimento |
| AFI-007 | B | OE-B1 | CFM exige documentação detalhada e individualizada; não exige instrumento validado | IV | — | REF-004, REF-005 | **Divergência CFM × APA** — protocolo deve cumprir ambos |
| AFI-008 | B | OE-B1 | CFM Art. 46: permite quebra de sigilo em risco iminente, mesmo sem consentimento | IV (Legal) | Obrigatório | REF-004, REF-005 | **Divergência CFM × NICE** — NICE deixa a critério clínico |
| AFI-009 | B | OE-B2 | Transtorno psiquiátrico é o maior fator isolado de risco; depressão, TAB e esquizofrenia aumentam OR de suicídio >3× | II | A | REF-012, REF-013 | — |
| AFI-010 | B | OE-B2 | Tentativa prévia é o fator preditor isolado mais potente; recorrência mais provável nos primeiros 3–6 meses | II | A | REF-012, REF-013 | Deve ser capturado obrigatoriamente em triagem |
| AFI-011 | B | OE-B2 | TAB: risco > MDD — ideação 29,2% vs. 17,3%; tentativa 18,8% vs. 4,78%; óbito 1,73% vs. 0,48% | II | A | REF-015 | Estado misto = maior risco; primeiro ano de doença |
| AFI-012 | B | OE-B2 | Esquizofrenia: maior risco no início da doença; fatores = sintomas depressivos, sexo M, sintomas positivos, insight | II | A | REF-012, REF-013 | — |
| AFI-013 | B | OE-B2 | MDD: risco máximo em episódio grave com ansiedade, agitação ou controle de impulsos prejudicado | II | A | REF-012, REF-014 | — |
| AFI-014 | B | OE-B2 | Fatores demográficos de risco: sexo M (maior taxa de óbito), início jovem, solteiro/separado/divorciado, baixo NSE, desemprego, história familiar, ACEs | II | A | REF-012, REF-014, REF-015 | — |
| AFI-015 | B | OE-B2 | Comorbidades amplificadoras de risco: transtorno por uso de substâncias, TP borderline/antissocial, impulsividade/agitação | II | A | REF-012, REF-014, REF-015 | Cruzamento com clusters I e substâncias |
| AFI-016 | B | OE-B2 | Fatores protetores: casamento, filhos, ansiedade comórbida, acesso a SM, pertencimento, resolução de problemas, espiritualidade, emprego | II | A | REF-008, REF-014 | Devem ser avaliados ativamente em todo retorno |
| AFI-017 | B | OE-B2 | Adolescentes (14–17): TDAH e TEA comórbidos, bullying, discriminação e distúrbios do sono aumentam risco | II | A | REF-015, REF-017 | Relevante para escopo etário parcial do protocolo |
| AFI-018 | B | OE-B3 | Conduta de alto risco: não deixar paciente sozinho + medidas ambientais + acionar SAMU/UPA + SPI + notificar família (CFM Art. 46) | Consenso | A | REF-006, REF-008, REF-011, REF-012 | Adaptado para setting SEM contenção local |
| AFI-019 | B | OE-B3 | SPI (Stanley-Brown): 6 passos, 15–30 min, cópia escrita; deve ser iniciado antes da transferência quando possível | I | A | REF-020, REF-021 | CVV 188 como recurso brasileiro no Passo 5 |
| AFI-020 | B | OE-B3 | SPI+ reduz comportamento suicida 45% em 6 meses vs. cuidado usual (OR 0,56; IC95% 0,33–0,95) | I | A | REF-020 | — |
| AFI-021 | B | OE-B3 | Meta-análise: intervenções de prevenção reduzem tentativas (OR 0,69) e melhoram vinculação ao seguimento (OR 2,74) | I | A | REF-021 | — |
| AFI-022 | B | OE-B3 | Lei 10.216/2001 Art. 6: internação involuntária permitida quando há risco ao paciente/outros, sem consentimento | IV (Legal) | Obrigatório | REF-023, REF-024 | — |
| AFI-023 | B | OE-B3 | Lei 10.216/2001 Art. 9: internação involuntária deve ser notificada ao Ministério Público em 72 horas | IV (Legal) | Obrigatório | REF-023, REF-024 | Item de documentação mandatório no protocolo |
| AFI-024 | B | OE-B3 | Follow-up telefônico em 72h pós-alta associado a redução de comportamento suicida e maior engajamento no tratamento | I | B | REF-020 | Desejável mas fora do escopo do ambulatório (implementar como orientação) |
| AFI-025 | B | OE-B3 | Risco intermediário (ideação sem plano/meios, ou tentativa prévia sem intenção atual): follow-up intensificado + SPI + reavaliação em cada consulta | Consenso | B | REF-008 | — |
| AFI-026 | K/D | OE-D2 | Lítio é o estabilizador de humor padrão-ouro para TAB-I; 1ª linha para mania aguda e manutenção | I | A | REF-027, REF-042 | CANMAT/ISBD 2018 + JAMA Review 2023 |
| AFI-027 | K/D | OE-D2 | Faixa terapêutica lítio: mania aguda/misto 0,8–1,2 mEq/L; manutenção 0,8–1,0 mEq/L | I | A | REF-027, REF-028, REF-029 | Amostras SEMPRE como nível vale 12h pós-dose |
| AFI-028 | K/D | OE-D2 | Idosos/maior sensibilidade: alvo de manutenção de lítio 0,6–0,8 mEq/L | III | B | REF-029, REF-030 | Nota de alerta para idosos no protocolo |
| AFI-029 | K/D | OE-D2 | Baseline lítio: creatinina+eGFR, TSH, T4L, cálcio, eletrólitos, hemograma, teste gravidez; ECG se >40a ou risco CV | I | A | REF-027, REF-028 | — |
| AFI-030 | K/D | OE-D2 | Iniciação lítio (0–6m): litemia 5–7d após cada ajuste, depois 1–2 semanas até estabilização; renal 1m e 3m; tireóide/cálcio 3m | I | A | REF-027, REF-028, REF-029 | — |
| AFI-031 | K/D | OE-D2 | Manutenção lítio (>6m): litemia cada 3m (1º ano) → cada 6m; creatinina/eGFR cada 6m; TSH/T4L 6–12m; cálcio+eletrólitos anual | I | A | REF-027, REF-029 | ECG/hemograma somente se indicação clínica |
| AFI-032 | K/D | OE-D2 | Toxicidade lítio: leve 1,5–2,0 / moderada 2,0–2,5 / grave >2,5 mEq/L; grave → hemodiálise | I | A | REF-028, REF-029 | Use como limiar de alerta no JSON (clinicalExpression) |
| AFI-033 | K/D | OE-D2 | Precipitantes de toxicidade do lítio: desidratação, hiponatremia, AINEs, inibidores da ECA, diuréticos | II | A | REF-028, REF-029 | Deve ser capturado na tela de medicamentos em uso (interação) |
| AFI-034 | K/D | OE-D2 | Contraindicação absoluta: eGFR <30 mL/min; precaução com dose reduzida+monitoramento frequente: eGFR 30–89 | I | A | REF-027, REF-028 | Alert flag mandatório no protocolo |
| AFI-035 | K/D | OE-D3 | Faixa terapêutica valproato: 50–100 µg/mL | I | A | REF-031, REF-027 | — |
| AFI-036 | K/D | OE-D3 | Baseline valproato: ALT, AST, hemograma c/plaquetas, amônia, coagulação (se indicado), teste gravidez obrigatório | I | A | REF-031, REF-027 | — |
| AFI-037 | K/D | OE-D3 | Iniciação valproato (0–6m): nível sérico 1–2 semanas após início, depois cada 1–3m; LFTs + hemograma/plaquetas mesmos intervalos | I | A | REF-027, REF-031, REF-032 | Maior risco hepatotoxicidade idiossincrática e trombocitopenia neste período |
| AFI-038 | K/D | OE-D3 | Manutenção valproato (>6m): LFTs, hemograma, nível sérico cada 6–12m; anual se estável >2 anos sem ajuste | I/II | A | REF-027, REF-033 | SR suporta dispensa de follow-up anual >2a se sem ajuste |
| AFI-039 | K/D | OE-D3 | Valproato — teratogenicidade: ~9% malformações congênitas maiores; ~25% se dose >1.450mg/dia; ~4× > outras monoterapias | I | A | REF-035, REF-037 | EURAP Registry (Tomson 2018, n=7.355 exposições) |
| AFI-040 | K/D | OE-D3 | Se valproato em MIE: documentar aconselhamento, prescrever contracepção eficaz, ácido fólico ≥0,4mg/dia, programa de prevenção | I | A (Mandatório) | REF-037, REF-038 | AAN/AES/SMFM 2024; alert flag de máxima prioridade |
| AFI-041 | K/D | OE-D3 | Evitar valproato em mulheres em idade fértil quando clinicamente viável (AAN/AES/SMFM) | I | A | REF-037 | **Divergência G5**: prática pode divergir da diretriz — registrar |
| AFI-042 | K/D | OE-K1 | CFM/ABP não possuem resoluções numeradas específicas para monitoramento de estabilizadores/antipsicóticos na literatura acessível | IV | — | REF-040 | Protocolo deve referenciar CANMAT/ISBD explicitamente; transparência mandatória |
| AFI-043 | K/D | OE-K1 | Carbamazepina: faixa terapêutica 4–12 µg/mL | II | A | REF-043, REF-044 | — |
| AFI-044 | K/D | OE-K1 | Baseline carbamazepina: hemograma c/diferencial/plaquetas, LFTs, sódio, ureia, creatinina, urinálise, nível CBZ; HLA-B*1502 se descendência asiática; ECG se risco CV | I | A | REF-043, REF-027 | HLA-B*1502 → risco de Stevens-Johnson |
| AFI-045 | K/D | OE-K1 | Iniciação CBZ (0–6m): hemograma+LFTs a cada 2 semanas por 2 meses, depois mensalmente; sódio+renal mensalmente; nível CBZ após dose estável | I | A | REF-043, REF-044 | — |
| AFI-046 | K/D | OE-K1 | Manutenção CBZ (>6m): hemograma+LFTs+sódio cada 3–6m; renal cada 6–12m; nível CBZ cada 6–12m | I | A | REF-027, REF-043 | — |
| AFI-047 | K/D | OE-K1 | CBZ é potente indutor enzimático hepático — revisar interações em toda nova medicação | II | A | REF-043, REF-044 | Impacta lítio, valproato, antipsicóticos, contraceptivos |
| AFI-048 | K/D | OE-K1 | Todos os antipsicóticos atípicos: baseline peso/IMC/CC/PA/glicemia/HbA1c/lipídios; repetir 3m; depois anualmente | I | A | REF-027, REF-045, REF-054 | Meta-análise Mitchell 2011: glicemia basal medida em apenas 44,3% na prática real (REF-049) |
| AFI-049 | K/D | OE-K1 | EPS: avaliação em toda consulta durante iniciação; a cada 6–12m em manutenção; cada 3m em idosos | I | A | REF-045, REF-046, REF-047 | — |
| AFI-050 | K/D | OE-K1 | Prolactina: monitoramento de rotina não universal; indicar se sintomático (galactorreia, amenorreia, disfunção sexual) ou uso de risperidona/paliperidona | II | B | REF-048, REF-057 | Monitoramento mais frequente em mulheres |
| AFI-051 | K/D | OE-K1 | Olanzapina: maior risco metabólico; LFTs periódicos (ALT>200 IU/L em 2% pré-marketing) | II | B | REF-050 | — |
| AFI-052 | K/D | OE-K1 | Clozapina — ANC baseline obrigatório; não iniciar se ANC <1.500/µL | I | A (Mandatório) | REF-052, REF-051 | — |
| AFI-053 | K/D | OE-K1 | Clozapina — ANC: semanal por 6m → quinzenal meses 7–12 → mensal após 1 ano | I | A (Mandatório) | REF-052, REF-054 | Risco grave de neutropenia maior nas primeiras 18 semanas |
| AFI-054 | K/D | OE-K1 | Clozapina: monitorar miocardite no 1º mês; maioria dos EAs emerge em 3m, quase todos em 6m | II | A | REF-051, REF-052 | Exceções: ganho de peso, CAD, cardiomiopatia, convulsões |
| AFI-055 | K/D | OE-K1 | Quetiapina: risco de prolongamento de QTc; ECG se risco CV ou medicação QT-prolongante concomitante | II | B | REF-053, REF-055, REF-056 | — |
| AFI-056 | K/D | OE-K1 | Clozapina e olanzapina: maior risco metabólico entre antipsicóticos atípicos — monitoramento metabólico intensificado | II | A | REF-050, REF-052 | — |
| AFI-057 | K/D | OE-K1 | Adherência ao monitoramento metabólico é baixa na prática real: glicemia basal medida em 44,3%, colesterol em 41,5% | I | — | REF-049 | Justifica protocolo estruturado no Daktus — é exatamente onde agrega valor |
| AFI-058 | K/D | OE-K1 | CBZ — ECG obrigatório em pré-existência de BAV, arritmia ou IC; novos sintomas CV durante tratamento → ECG urgente | II | A | REF-043 | Alert flag no protocolo |
| AFI-059 | K/D | OE-K1 | Alias clinicalExpression proposto: `exige_ecg` = lítio OR clozapina OR antipsicótico_atípico OR ISRS em dose alta OR estimulante OR CBZ+risco_CV | I/Consenso | A | REF-027, REF-043, REF-052 | Derivado diretamente do INTELIGENCIA_CONSOLIDADA — padrão já validado |
| AFI-060 | D | OE-D1 | EDM DSM-5-TR: ≥5 sintomas em 2 semanas; pelo menos 1 = humor deprimido ou anedonia; 9 sintomas candidatos | Consenso | A | REF-059, REF-061 | Fonte primária do protocolo diagnóstico |
| AFI-061 | D | OE-D1 | Adolescentes (14–17): irritabilidade pode substituir humor deprimido no EDM; limiar de ≥5 sintomas se mantém | Consenso | A | REF-059, REF-060 | Relevante para escopo etário parcial |
| AFI-062 | D | OE-D1 | Episódio maníaco: humor elevado/expansivo/irritável + energia por ≥7 dias + ≥3 sintomas (4 se só irritável); com prejuízo/hospitalização/psicose | Consenso | A | REF-059, REF-062 | Características psicóticas → automaticamente TAB-I |
| AFI-063 | D | OE-D1 | Episódio hipomaníaco: mesmo perfil maníaco, ≥4 dias, SEM prejuízo marcado/hospitalização/psicose | Consenso | A | REF-059, REF-062 | Distinção central TAB-I vs. TAB-II |
| AFI-064 | D | OE-D1 | Especificador misto (EDM): ≥3 sintomas maníacos na maioria dos dias; limiar 3 (não 2) — rebaixar para 2 triplica prevalência sem melhorar validade | II | A | REF-059, REF-064 | — |
| AFI-065 | D | OE-D1 | TAB-I: ≥1 episódio maníaco na vida (EDM não obrigatório). TAB-II: ≥1 hipomaníaco + ≥1 EDM + SEM história de mania | Consenso | A | REF-059, REF-065, REF-066 | — |
| AFI-066 | D | OE-D1 | TAB-II NÃO é forma mais leve: razão depressão:hipomania até 39:1; risco suicida equivalente ao TAB-I | I | A | REF-065 | Importante para comunicação clínica |
| AFI-067 | D | OE-D1 | Pitfall crítico: TAB-II frequentemente diagnosticado como TDM; delay diagnóstico médio >10 anos | II | A | REF-065 | → justifica triagem de bipolaridade em toda depressão |
| AFI-068 | D | OE-D1 | MDQ: sens. 80%, espec. 70%; HCL-32: sens. 82%, espec. 57% — instrumentos livres para rastreio de bipolaridade | II | B | REF-065 | Usar em toda consulta de depressão como triagem |
| AFI-069 | D | OE-D1 | Features sugestivas de bipolaridade em deprimido: início precoce, hiperfagia, hipersonia, psicose, história familiar TAB, episódios frequentes, resposta inadequada a antidepressivos | II | A | REF-062 | — |
| AFI-070 | D | OE-D4 | PHQ-9: instrumento de triagem mais robusto no Brasil; validado em >10.000 adultos, 27 estados; estrutura unidimensional, invariante demograficamente | II | A | REF-067, REF-068 | Único instrumento com normativos locais brasileiros |
| AFI-071 | D | OE-D4 | Pontos de corte PHQ-9 brasileiros: muito baixo 0–6 / baixo 7–13 / moderado 14–19 / alto 20–23 / muito alto ≥24 | II | A | REF-067 | PHQ-9 ≥24 = urgência / considerar hospitalização |
| AFI-072 | D | OE-D4 | PHQ-9 item 9 positivo (ideação de morte) → acionar avaliação de risco suicida imediatamente | II | A (Mandatório) | REF-067, REF-097 | Gatilho de segurança no MBC |
| AFI-073 | D | OE-D4 | HAM-D validado no Brasil; sem normativos locais; usar limiares internacionais: leve 8–16 / moderado 17–23 / grave ≥24 | II | B | REF-069 | — |
| AFI-074 | D | OE-D4 | MADRS validado no Brasil; limiar para hospitalização em depressão bipolar: ≥24; pontos de corte ROC disponíveis | II | B | REF-069, REF-070 | Tabela completa de corte no REL-03 |
| AFI-075 | D | OE-D4 | YMRS validado português; ICC 0,97; grave ≥25; threshold hospitalização: ≥25 + psicose ou risco | II | A | REF-071 | Aplicar em toda consulta de pacientes com TAB |
| AFI-076 | D | OE-D4 | Adolescentes (14–17): SMFQ validado no Brasil corte >6 / T-score >55 para TDM | II | B | REF-074 | PHQ-8/PHQ-9 invariante para adolescentes em contexto latino-americano |
| AFI-077 | D | OE-D5 | Antidepressivos de 2ª geração são 1ª linha para TDM moderado a grave (CANMAT 2023, ACP 2023) | I | A | REF-075, REF-076 | — |
| AFI-078 | D | OE-D5 | CANMAT 2023 — 1ª linha com evidence superior: escitalopram, mirtazapina, paroxetina, sertralina, venlafaxina XR | I | A | REF-075, REF-078 | Todas disponíveis no Brasil e aprovadas ANVISA |
| AFI-079 | D | OE-D5 | Meta-análise Cipriani (522 RCTs, 116.477 pts): todos 21 antidepressivos superiores ao placebo; escitalopram, mirtazapina, venlafaxina, vortioxetina = melhor eficácia+aceitabilidade | I | A | REF-079 | Referência mestre para comparação de antidepressivos |
| AFI-080 | D | OE-D5 | ANVISA: vilazodona e levomilnacipran NÃO aprovados → excluir de protocolos BR; agomelatina aprovada ANVISA (não FDA) → pode ser opção local | II | A (Mandatório) | REF-075, REF-078 | Compliance regulatório brasileiro |
| AFI-081 | D | OE-D5 | Seleção individualizada: mirtazapina (insônia/anorexia), ISNRs (dor comórbida), bupropiona (fadiga/disfunção sexual), vortioxetina (sintomas cognitivos) | II | B | REF-075, REF-077 | — |
| AFI-082 | D | OE-D5 | Iniciar antidepressivo com 1/3–1/2 da dose usual; titular para faixa mínima terapêutica em 1–2 semanas | II | A | REF-075, REF-077 | — |
| AFI-083 | D | OE-D5 | ACP: follow-up inicial 2 semanas; depois cada 4–6 semanas até remissão; PHQ-9 em toda consulta | Consenso | A | REF-076, REF-097 | — |
| AFI-084 | D | OE-D5 | Melhora precoce ≥20% PHQ-9 em 4 semanas prediz resposta futura; ausência de qualquer benefício em 4 semanas → escalar dose ou trocar | II | A | REF-075, REF-077 | — |
| AFI-085 | D | OE-D5 | Sem melhora >50% em 8 semanas → reavaliação diagnóstica + estratégias de 2ª linha | II | A | REF-075, REF-078 | — |
| AFI-086 | D | OE-D5 | Depressão Resistente ao Tratamento (DRT): falha em ≥2 ensaios adequados (dose terapêutica + ≥6–8 semanas + adesão confirmada); afeta ≥30% dos TDM | I | A | REF-075, REF-084, REF-086 | Excluir pseudo-resistência antes do diagnóstico |
| AFI-087 | D | OE-D5 | Staging DRT: Maudsley Staging Model (MSM) recomendado — 3 dimensões: ensaios falhos, gravidade (CGI), duração | III | B | REF-087, REF-086 | — |
| AFI-088 | D | OE-D5 | 2ª linha DRT por NMA: ECT (OR 12,86), esketamina IN (aprovada ANVISA+FDA), aripiprazol augmentação (OR 1,9), quetiapina XR 150-300mg (NNT=9), lítio augmentação, rTMS | I | A | REF-092, REF-093 | ECT = mais eficaz agudo; disponível em SUS terciário |
| AFI-089 | D | OE-D5 | Esketamina intranasal: indicada para DRT grave com suicidalidade aguda; aprovada FDA + ANVISA; disponibilidade SUS terciária (limitada) | I | A | REF-084, REF-092 | — |
| AFI-090 | D | OE-D5 | Critérios de encaminhamento para DRT especializado: ≥2 ensaios falhos, <50% redução PHQ-9, suicidalidade/psicose/catatonia, necessidade de neuromodulação ou esketamina | Consenso | A | REF-084, REF-095 | — |
| AFI-091 | D | OE-D5 | Remissão (PHQ-9 <5): manter dose terapêutica por ≥4–9 meses; depressão recorrente/crônica: manutenção ≥2 anos | II | A | REF-075, REF-076 | — |
| AFI-092 | D | OE-D5 | MBC: PHQ-9 em toda consulta + alertas automáticos em ≥10 (avaliação), ≥20 (intensificação), item 9+ (suicidalidade) | I | A | REF-097, REF-099 | Fundamento técnico para automação no Daktus |
| AFI-093 | D | OE-D5 | Adolescentes (14–17): fluoxetina = único antidepressivo com evidência robusta e aprovação regulatória para depressão; psicoterapia 1ª linha em leve; fluoxetina+TCC para moderada-grave | I | A | REF-081, REF-082, REF-083 | Monitoramento obrigatório de suicidalidade nas primeiras semanas |
| AFI-094 | E | OE-E1 | TAG DSM-5-TR: preocupação excessiva ≥6 meses, ≥3/6 sintomas, sofrimento clínico; crianças: apenas 1/6 sintomas (divergência crítica pediátrica) | Consenso | A | REF-059, REF-104, REF-105 | — |
| AFI-095 | E | OE-E1 | Transtorno do Pânico: ataques recorrentes inesperados + ≥4/13 sintomas + ≥1 mês de preocupação/mudança comportamental maladaptativa | Consenso | A | REF-059, REF-104, REF-109 | — |
| AFI-096 | E | OE-E1 | Fobia Social: medos de scrutinínio social ≥6 meses; crianças: manife- stação em pares (choro, congelamento, mutismo) | Consenso | A | REF-059, REF-105 | — |
| AFI-097 | E | OE-E1 | TOC: obsessões e/ou compulsões >1h/dia OU sofrimento/prejuízo; crianças pequenas podem não articular fins dos comportamentos | Consenso | A | REF-059, REF-116 | TOC exige doses ISRS mais altas que indicação antidepressiva |
| AFI-098 | E | OE-E1 | TEPT DSM-5-TR: 4 clusters (intrusão, evitação, cognição/humor negativo, excitação) ≥1 mês; crianças ≤6 anos: critérios modificados c/ manifestacões comportamentais | Consenso | A | REF-059, REF-108 | — |
| AFI-099 | E | OE-E1 | TEPT complexo (CPTSD ICD-11): distúrbios adicionais de auto-organização; alguns casos atendem DSM-5 mas não ICD-11 — documentar cuidadosamente | II | B | REF-164 | Especialmente relevante em população pediátrica |
| AFI-100 | E | OE-E1 | Exclusão orgânica obrigatória antes de diagnóstico psiquiátrico primário quando sintomas físicos proeminentes, atípicos ou paciente com FR médicos | Consenso | A | REF-059, REF-103 | DSM-5-TR + AAFP |
| AFI-101 | E | OE-E1 | Etiologias orgânicas a excluir: hipertireoidismo, hiperparatireoidismo, feocromocitoma, FA/TSV, TEP, asma, DPOC, convulsões, disfunção vestibular, hipoglicemia, SUB | II | A | REF-103, REF-104, REF-109 | — |
| AFI-102 | E | OE-E1 | Features sugestivas de etiologia orgânica: início >45 anos, sintomas atípicos (vertigem, perda de consciência, disartria, amnésia), ausência de gatilhos, má resposta a tratamento psiquiátrico | II | A | REF-103, REF-109 | — |
| AFI-103 | E | OE-E1 | Workup sintoma-específico: taquicardia → ECG+TSH+glicemia+urina; dispneia → oximetria+espirometria+imagem; dor torácica → ECG+enzimas+eco; tontura → ECG+glicemia+neurologia | II | A | REF-110, REF-113 | Template estruturado para prontuário |
| AFI-104 | E | OE-E1 | POTS/hipotensão ortostática: queda PA sistólica ≥20 mmHg ou diastólica ≥10 mmHg em 3 min; POTS: FC >30 bpm em adultos durante active stand test | Consenso | B | REF-110, REF-111 | ACC 2022 |
| AFI-105 | E | OE-E1 | Precipitantes farmacológicos: broncodilatadores, simpatomiméticos, esteroides, caféina, retirada de benzodiazepínicos | II | A | REF-103, REF-105 | Capturar na tela de medicações em uso |
| AFI-106 | E | OE-E2 | ISRSs: 1ª linha para depressão/TAG E para TOC; TOC exige doses mais altas do que o teto antidepressivo | I | A | REF-116, REF-117 | Sertralina, fluoxetina, fluvoxamina, paroxetina, clomipramina (TOC) |
| AFI-107 | E | OE-E2 | Citalopram: >40 mg/dia contraindicado por FDA/ANVISA por risco de QTc; dose máxima: 40 mg/dia | I | A (Mandatório) | REF-118, REF-120 | Alert flag de máxima prioridade no protocolo |
| AFI-108 | E | OE-E2 | Escitalopram: risco QTc dose-dependente; ECG obrigatório se ≥20 mg/dia ou fatores de risco presentes | II | A | REF-120, REF-123 | — |
| AFI-109 | E | OE-E2 | Hierarquia de risco QTc entre ISRSs: citalopram > escitalopram > sertralina/fluvoxamina/fluoxetina > paroxetina (menor risco) | I | A | REF-119, REF-120 | — |
| AFI-110 | E | OE-E2 | Citalopram prolonga QTc ~16,7 ms a 60 mg/dia de forma dose-dependente | I | A | REF-120 | Meta-análise |
| AFI-111 | E | OE-E2 | ECG baseline indicado se ≥2 fatores de risco: idade >65, sexo F, medicação QTc-prolongante, doença cardíaca, distúrbio eletrolítico, dose excessiva; OU citalopram/escitalopram em alta dose | III | B | REF-125, REF-055 | Consenso holandezês + AMP |
| AFI-112 | E | OE-E2 | Follow-up ECG: 1–2 semanas após início ou ajuste; depois cada 3–6 meses se dose de risco ou FR persistentes | III | B | REF-125, REF-126 | — |
| AFI-113 | E | OE-E2 | QTc >500 ms: descontinuar/reduzir dose imediatamente + corrigir eletrólitos (K, Mg, Ca) + encaminhamento urgente | Consenso | A (Mandatório) | REF-126, REF-128 | — |
| AFI-114 | E | OE-E2 | QTc 450–499 ms (H) / 470–499 ms (F): revisar FR + considerar redução de dose ou troca para agente de menor risco | Consenso | B | REF-055, REF-128 | Limiares sexo-específicos |
| AFI-115 | E | OE-E2 | Setting com acesso limitado a ECG: preferir ISRSs de menor risco (sertralina, fluoxetina, fluvoxamina, paroxetina) | II | B | REF-120, REF-126 | — |
| AFI-116 | E | OE-E3 | Burnout ICD-11: QD85 — fenômeno ocupacional, NÃO transtorno médico; não incluído no DSM-5-TR | IV | — | REF-129 | Fundamental para orientação correta no protocolo |
| AFI-117 | E | OE-E3 | 3 dimensões OMS do burnout: (1) esgotamento/exaustão, (2) distância mental/cinismo do trabalho, (3) redução da eficácia profissional | IV | — | REF-129, REF-130 | — |
| AFI-118 | E | OE-E3 | Burnout ≠ TDM ≠ TAG: contexto-específico (ocupacional); correlaciona com depressão (r≈0,52) e ansiedade (r≈0,46) mas construtos dissociáveis por análise de rede | I | — | REF-140, REF-141 | — |
| AFI-119 | E | OE-E3 | Burnout não deve ser tratado com antidepressivos ou ansiolíticos; tratar depressão ou ansiedade comórbidas com diretrizes específicas | III | A (Mandatório) | REF-130, REF-135 | Ponto de confusão clínica frequente |
| AFI-120 | E | OE-E3 | MBI-HSS (22 itens): padrão-ouro para profissionais de saúde; validado em Português BR (ω>0,70) | II | A | REF-142, REF-143 | — |
| AFI-121 | E | OE-E3 | OLBI (15 itens): validado para trabalhadores gerais BR; cobre exaustão e desengajamento | II | B | REF-146 | — |
| AFI-122 | E | OE-E3 | BAT-12 (12 itens): validado no Brasil para saúde + trabalhadores gerais; melhor alternativa breve ao MBI/OLBI | II | B | REF-147 | Recomendado para triagem ambulatorial |
| AFI-123 | E | OE-E3 | BAT4 (4 itens): invarância de medida cross-nacional confirmada; aguarda validação formal em Português BR | II | C | REF-148 | — |
| AFI-124 | E | OE-E3 | BCSQ-12: validado para APS BR; distingue 3 subtipos: frenético, sub-desafiado e desgastado | II | B | REF-149 | — |
| AFI-125 | E | OE-E4 | 1ª linha farmacológica TEPT: ISRSs (APA 2025, NICE 2018, VA/DoD 2023); sertalina 50–200 mg e paroxetina 20–60 mg FDA-aprovados para TEPT; fluoxetina e venlafaxina 75–225 mg também 1ª linha | I | A | REF-150, REF-151, REF-153 | Cochrane 2022: ISRSs RR 0,66 (IC95% 0,59–0,74) vs. placebo |
| AFI-126 | E | OE-E4 | Benzodiazepínicos CONTRAINDICADOS em TEPT: sem eficácia + risco de dependência + piora de sintomas | I | A (Mandatório) | REF-151 | VA/DoD 2023 + NICE 2018 |
| AFI-127 | E | OE-E4 | Cannabis e derivados: contraindicados em TEPT (VA/DoD 2023) | Consenso | A | REF-151 | — |
| AFI-128 | E | OE-E4 | Psicoterapias focadas em trauma 1ª linha: TCC-trauma, PE, CPT (APA: “strongly recommends”); EMDR (APA: “suggests”); VA/DoD recomenda PE, CPT e EMDR como forte | I | A | REF-150, REF-151 | TF > não-TF: SMD g=0,17–0,23 |
| AFI-129 | E | OE-E4 | EMDR: igualmente eficaz ao TCC-trauma; maior taxa de perda de diagnóstico de TEPT (86%); custo-efetividade favorável | I | A | REF-158, REF-159 | 75% TCC; 28% terapia centrada no presente |
| AFI-130 | E | OE-E4 | Encaminhamento obrigatório para psicoterapia especializada: TEPT moderado-grave, falha de manejo ambulatorial, TEPT complexo/dissocição grave, preferência do paciente, suicidalidade | Consenso | A | REF-150, REF-151 | APA 2025 + NICE 2018 |
| AFI-131 | E | OE-E4 | Manejo ambulatorial adequado enquanto aguarda encaminhamento: TEPT leve + bom suporte + recusa informada → ISRS + facilitar encaminhamento | Consenso | B | REF-150 | — |
| AFI-132 | E | OE-E4 | Telessaúde para psicoterapia focada em trauma: recomendada quando protocolo validado e acesso presencial limitado | Consenso | B | REF-151 | — |
| AFI-133 | E | OE-E4 | PDS-3 (3 itens): validada em Português BR; ROC=0,97, sens 86,4%, espec 93,5%, α=0,78 — ferramenta eficiente de triagem TEPT | II | B | REF-161 | — |
| AFI-134 | E | OE-E1 | CPTSD ICD-11 vs. TEPT DSM-5: alguns casos cumprem critérios DSM-5-TR mas não ICD-11 (menor prevalência por critérios mais restritivos); avaliar e documentar | II | B | REF-164 | Especialmente relevante em população pediátrica e adolescentes |
| AFI-135 | E | OE-E1 | DSM-5-TR 2024–2025: sem mudanças substanciais nos critérios de ansiedade/TOC/TEPT; clarificação da distinção entre transtorno de ajustamento e transtornos ansiosos | Consenso | — | REF-162 | — |
| AFI-136 | F | OE-F1 | Esquizofrenia DSM-5-TR: ≥2 dos 5 domínios (delu, aluc, discurso desorg, cpt desorg/catoníco, neg) por ≥1 mês; ≥1 deve ser deluções/alucinacões/discurso; sinais contínuos ≥6 meses + prejuízo funcional | Consenso | A | REF-059, REF-165 | — |
| AFI-137 | F | OE-F1 | Exclusões obrigatórias para esquizofrenia: T. esquizoafetivo, T. humor com caract. psicóticas, SUB e condição médica geral | Consenso | A | REF-059 | — |
| AFI-138 | F | OE-F1 | T. esquizoafetivo: Critério A esquizofrenia + episódio de humor maior simultâneo; deluções/alucinacões presentes ≥2 semanas SEM humor; humor na maioria da duração total | Consenso | A | REF-059 | — |
| AFI-139 | F | OE-F1 | T. psicótico breve: ≥1 sintoma positivo por ≥1 dia a <1 mês; retorno total ao nível pré-mórbido | Consenso | A | REF-059, REF-166 | — |
| AFI-140 | F | OE-F1 | FRS de Schneider: NÃO são mais critérios no DSM-5-TR ou ICD-11; sens 57–62% / espec 75–94%; perderíamos ~40% dos casos se exclusivos — usar apenas como indicador suplementar | I | B | REF-169, REF-170 | Cochrane 2015 |
| AFI-141 | F | OE-F1 | Indicadores de hospitalização em psicose: suicidalidade grave, incapacidade de autocuidado, agressividade/risco a terceiros, primeiro episódio sem suporte adequado | Consenso | A | REF-165, REF-047 | — |
| AFI-142 | F | OE-F2 | Risco EPS proporcional à ocupação D2: janela terapêutica 60–80%; EPS aumentam substancialmente acima de 75–85% | II | A | REF-179 | — |
| AFI-143 | F | OE-F2 | Hierarquia de risco EPS: haloperidol (OR 7,56) >> risperidona/paliperidona (intermediário) >> aripiprazol/brexpiprazol/cariprazina (baixo EPS, akathisia proeminente) > olanzapina/quetiapina > clozapina (OR 0,06–0,40, menor de todos) | I | A | REF-179, REF-180 | NMA Leucht 2013 |
| AFI-144 | F | OE-F2 | Prevalência pooled de EPS por antipsicóticos: parkinsonismo ~20%, acatisia ~11%, discinesia tardia ~7% | I | A | REF-184 | SR/MA observacional |
| AFI-145 | F | OE-F2 | Escalas de monitoramento EPS: SAS (parkinsonismo) + BARS (acatisia) + AIMS (discinesia tardia) — os 3 usados em conjunto em toda consulta na iniciação | Consenso | A | REF-185, REF-186 | AAFP e VA/DoD |
| AFI-146 | F | OE-F2 | Protocolo EPS iniciação (0–12 semanas): AIMS + SAS + BARS em toda consulta; pós-estabilização: a cada 6 meses; a cada 3 meses para agentes de alto risco ou >65 anos | Consenso | A | REF-047, REF-185 | VA/DoD 2023 + AAFP 2021 |
| AFI-147 | F | OE-F2 | SNM — critérios de internação: hipertermia >38°C (≥2 ocasiões) + rigidez "cano de chumbo" + alteração do estado mental + instabilidade autonômica (FC ≥25% baseline) + CK ≥4× LSN | III | A (Mandatório) | REF-192, REF-194 | — |
| AFI-148 | F | OE-F2 | Distonia grave → internação imediata: comprometimento laríngeo com via aérea comprometida, disfagia ou sintomas refratários | IV | A (Mandatório) | REF-177 | — |
| AFI-149 | F | OE-F2 | Jovens adultos (18–25): maior risco distonia aguda e acatisia; usar doses iniciais menores + titulação gradual; preferir SGAs com menor risco EPS | III | A | REF-189, REF-190, REF-191 | — |
| AFI-150 | F | OE-F3 | Clozapina — não iniciar se ANC <1.500/µL (geral) ou <1.000/µL (BEN); confirmar qualquer <1.500/µL com repetição em 24h | Consenso | A (Mandatório) | REF-052, REF-197 | FDA + ANVISA |
| AFI-151 | F | OE-F3 | Clozapina ANC: semanal 6 meses → quinzenal meses 7–12 → mensal após 1 ano | Consenso | A | REF-052 | FDA/ANVISA |
| AFI-152 | F | OE-F3 | ANC <500/µL: descontinuação imediata (mandatória). ANC 500–999/µL: interromper + monitoramento diário + hematologista. ANC 1.000–1.499/µL: 3×/semana sem ajuste de dose | Consenso | A (Mandatório) | REF-052 | — |
| AFI-153 | F | OE-F3 | Troponina + PCR: baseline + semanal durante 1º mês para detecção de miocardite induzida por clozapina (VA/DoD 2023) | Consenso | B | REF-047 | — |
| AFI-154 | F | OE-F3 | CIVH afeta 32–75% dos pacientes; mortalidade por íleo 25–43,7% vs. agranulocitose 2,2–4,2% — CIVH é o risco letal mais prevalente da clozapina | II | A | REF-200, REF-202, REF-203 | — |
| AFI-155 | F | OE-F3 | Triagem subjetiva de constipação: sensibilidade apenas 18% para CIVH objetiva — não confiar em queixas espontâneas; avaliação obrigatória em toda consulta | II | A (Mandatório) | REF-204 | — |
| AFI-156 | F | OE-F3 | Protocolo Porirua: docusato 100 mg 2×/dia + senna 8,6 mg 2×/dia (profilaxia universal); macrogol 3350 em casos refratários | III | B | REF-206 | Profilaxia universal recomendada |
| AFI-157 | F | OE-F3 | Anticolinérgicos concomitantes à clozapina: CONTRAINDICADOS — aumentam incidência e fatalidade de íleo | III | A (Mandatório) | REF-200, REF-207 | — |
| AFI-158 | F | OE-F3 | ANVISA Brasil: registro obrigatório no Programa Nacional de Monitoramento de Clozapina antes do início; dispensação condicionada à confirmação em tempo real no sistema | Consenso | A (Mandatório) | REF-208, REF-209 | — |
| AFI-159 | F | OE-F3 | Brasil: nível sérico de clozapina NÃO disponível no SUS; limiar BEN reconhecido pela ANVISA mas não descrito na bula brasileira | III | — | REF-208 | — |
| AFI-160 | F | OE-F3 | Delphi global 2025: propõe limiar ANC para suspensão 1,0×10⁹/L (geral) / 0,5×10⁹/L (BEN Duffy-null); monitoramento após 2 anos pode ser descontinuado — ainda não adotado universalmente | III | C | REF-197 | — |
| AFI-161 | F | OE-F4 | Hierarquia de risco metabólico (NMA Pillinger 2019, 100 RCTs): clozapina = pior em TODOS os parâmetros; olanzapina = 2ª; aripiprazol/brexpiprazol/cariprazina/lurasidona/ziprasidona = perfil mais benigno | I | A | REF-211 | — |
| AFI-162 | F | OE-F4 | Ganho de peso médio vs. placebo: haloperidol −0,23 kg; aripiprazol ~0; ziprasidona ~0,5; risperidona ~1; quetiapina ~1,5; olanzapina ~2,5; clozapina +3,01 kg | I | A | REF-211 | — |
| AFI-163 | F | OE-F4 | Disregulação glicemia ≠ ganho de peso: lurasidona e quetiapina associadas a aumentos de HbA1c apesar de menor ganho de peso (Smith 2025) | II | B | REF-214 | — |
| AFI-164 | F | OE-F4 | Monitoramento metabólico — iniciação (baseline + 12 semanas): peso+IMC+CA, glicemia em jejum/HbA1c e perfil lipídico | Consenso | A | REF-045, REF-211 | Olanzapina FDA avisa hiperglicemia |
| AFI-165 | F | OE-F4 | Monitoramento metabólico — manutenção: peso cada 3 meses (1º ano) → anual; glicemia/lipídios cada 6 meses (1º ano) → anual | Consenso | A | REF-045, REF-211 | — |
| AFI-166 | F | OE-F4 | LAI para prevenção de recaída: paliperidona palmitato 3M, aripiprazol LAI, olanzapina LAI e clozapina entre os de melhor desempenho (NMA finlandesa Hamina 2024) | I | A | REF-217 | — |
| AFI-167 | F | OE-F4 | SUS Brasil — antipsicóticos orais disponíveis: clozapina, olanzapina, risperidona, quetiapina, ziprasidona; LAIs: paliperidona 1M/3M, risperidona LAI, aripiprazol LAI, olanzapina LAI (acesso limitado) | III | A | REF-208, REF-219 | — |
| AFI-168 | F | OE-F4 | Clozapina no Brasil: maior taxa de permanência (menor troca: 37,6/100 pessoa-anos) + vantagem de sobrevivência vs. não-clozapina (HR morte 1,21 para não-clozapina) | II | A | REF-218, REF-219 | — |

| AFI-169 | G | OE-G1 | TDAH adulto DSM-5-TR: >=5/9 sintomas em desatenção OU hiperatividade-impulsividade; persistência >=6 meses; início antes dos 12 anos; >=2 contextos; prejuízo funcional claro | Consenso | A | REF-059, REF-223 | Limiar adulto = 5 (vs. 6 em <17 anos) |
| AFI-170 | G | OE-G1 | 3 apresentações TDAH: combinada (A1+A2), predominantemente desatenta (A1), predominantemente hiperativa-impulsiva (A2) — "apresentação" substituiu "subtipo" para refletir instabilidade desenvolvimental | Consenso | A | REF-059 | — |
| AFI-171 | G | OE-G1 | Informante colateral fortemente recomendado em TDAH; auto-relato isolado sujeito a viés de recordação e limitação de insight | Consenso | A | REF-223, REF-226 | — |
| AFI-172 | G | OE-G1 | ASRS v1.1 (WHO): 6 itens, <1 minuto; adaptado para Português BR; VPN ~100% em atenção primária; instrumento de rastreio mais utilizado mundialmente | II | A | REF-227, REF-228, REF-229 | — |
| AFI-173 | G | OE-G1 | ASRS v1.1 — limitações críticas: VPP pode ser 11,5% na população geral; em psiquiatria ambulatorial 54,8% rastrearam positivo mas apenas 11,9% tinham diagnóstico formal — rastreio positivo EXIGE avaliação clínica completa | II | A (Mandatório) | REF-231, REF-232 | — |
| AFI-174 | G | OE-G2 | ECG pré-estimulantes: abordagem risco-baseada, NÃO universal; AAP afirma não haver evidência de aumento de morte súbita cardíaca com medicações de TDAH | I | A | REF-225, REF-226, REF-265 | AAP + AMSSM + NICE |
| AFI-175 | G | OE-G2 | Indicações de ECG pré-estimulante: (1) cardiopatia/cardiomiopatia/arritmia grave pessoal; (2) hist. familiar de morte súbita/síndrome arrítmica hereditária; (3) síncope inexplicada ou palpitações em repouso; (4) achados cardiovasculares anormais | Consenso | A | REF-235, REF-236 | — |
| AFI-176 | G | OE-G2 | Sem fatores de risco cardiovascular: apenas PA e FC baseline são suficientes antes de iniciar estimulante | Consenso | A | REF-226 | — |
| AFI-177 | G | OE-G2 | Durante terapia estimulante: FC repouso >120 bpm persistente, arritmia ou PA sistólica >p95 em 2 ocasiões -> reduzir dose + encaminhar a especialista | Consenso | B | REF-238 | — |
| AFI-178 | G | OE-G3 | Avaliação neuropsicológica: NÃO obrigatória na rotina de TDAH; indicada apenas em cenários específicos: sem informante, comorbidade confundidora, suspeita de simulação, incapacidade legal | Consenso | A | REF-226, REF-240 | AAFP + EPA + UKAAN |
| AFI-179 | G | OE-G3 | Nikolas 2019: abordagem combinada (auto-relato + informante + hist. familiar + variabilidade de TR) classificou corretamente 87% dos casos — suporte ao valor adjunto da neuropsicológica em casos complexos | II | B | REF-243 | — |
| AFI-180 | G | OE-G4 | Atomoxetina: melhor não-estimulante para TDAH adulto; g=-0,48 (IC95% -0,64 a -0,33) vs. placebo; sem potencial de abuso; aprovada ANVISA | I | A | REF-247 | — |
| AFI-181 | G | OE-G4 | Guanfacina: g=-0,66 vs. placebo; reduz PA sistólica ~10 mmHg e FC ~7 bpm; uso off-label para TDAH no Brasil | II | B | REF-247 | — |
| AFI-182 | G | OE-G4 | Bupropiona: SMD=-0,50 (evidência baixa qualidade); sem aumento de MACE; opção em comorbidade depressiva; não aumenta risco de mania | I | C | REF-247, REF-248 | Cochrane 2017 |
| AFI-183 | G | OE-G4 | TDAH + TAB: estabilizar humor PRIMEIRO (lítio, valproato); depois introduzir atomoxetina (40 mg -> 80-100 mg em 2-4 semanas) OU bupropiona; estimulantes apenas após estabilização sustentada do humor | Consenso | A | REF-249, REF-250 | — |
| AFI-184 | G | OE-G4 | TDAH + SUD ativo (<=3-6 meses): estimulantes geralmente CONTRAINDICADOS; atomoxetina preferida (sem potencial de abuso); ATX melhora sintomas TDAH mas não reduz craving consistentemente | III | A | REF-255, REF-252 | — |
| AFI-185 | G | OE-G4 | TDAH + remissão sustentada SUD (>=3-6 meses): estimulante pode ser considerado; preferir liberação prolongada ou pró-droga (lisdexanfetamina, metilfenidato CR) pelo menor potencial de abuso | III | B | REF-255, REF-257 | — |
| AFI-186 | G | OE-G4 | Medidas de mitigação de risco TDAH + SUD: acordos de substâncias controladas, revisão PDMP, triagem urinária aleatória, contagem de comprimidos, aumento da frequência de consultas | Consenso | A | REF-257 | ASAM/AAAP 2024 |
| AFI-187 | G | OE-G4 | Se psicose se desenvolver durante estimulante: CONTRAINDICADOS imediatamente | Consenso | A (Mandatório) | REF-226, REF-238 | — |
| AFI-188 | G | OE-G4 | Seguimento TDAH estável: cada 3 meses; mensal durante ajuste de dose; PA + FC em toda consulta; peso cada 6 meses | Consenso | A | REF-226 | AAFP 2024 |
| AFI-189 | G | OE-G4 | Titulação de estimulante: iniciar baixo + aumentar gradualmente (semanal ou quinzenal); guiado por resposta clínica e tolerabilidade, não pelo peso | Consenso | A | REF-238, REF-264 | — |
| AFI-190 | G | OE-G4 | Lisdexanfetamina: 30 mg/dia -> titular 10-20 mg/semana -> máx 70 mg/dia | Consenso | A | REF-235 | FDA label |
| AFI-191 | G | OE-G4 | Viloxazina ER: eficácia comparável à atomoxetina; sem risco de QTc; aumento FC +5,8 bpm; NÃO disponível no Brasil (FDA-approved; não aprovada ANVISA) | II | C | REF-247, REF-263 | — |
| AFI-192 | H | OE-H1 | TEA DSM-5-TR Critério A: déficits persistentes em TODAS as 3 áreas — reciprocidade socioemocional, comunicação não verbal, relacionamentos; presente desde desenvolvimento precoce | Consenso | A | REF-059, REF-271 | — |
| AFI-193 | H | OE-H1 | TEA DSM-5-TR Critério B: >=2 de 4 CNR — movimentos/discurso repetitivos, insistência em sameness, interesses fixados com intensidade anormal, hiper/hiporreatividade sensorial | Consenso | A | REF-059 | — |
| AFI-194 | H | OE-H1 | Gravidade TEA: 3 níveis baseados em suporte necessário (nível 1/2/3) especificados SEPARADAMENTE para comunicação social E CNR; "alto/baixo funcionamento" ELIMINADOS do DSM-5-TR | Consenso | A | REF-059, REF-271, REF-273 | — |
| AFI-195 | H | OE-H1 | Camouflaging: assimilação + compensação + masking; mulheres autistas reportam maior camouflaging; 77% mulheres + 62% homens autistas receberam >=1 diagnóstico psiquiátrico incorreto (ansiedade/depressão/TPB/alimentar) | II | A | REF-275, REF-278 | — |
| AFI-196 | H | OE-H1 | Fenótipo feminino TEA: interesses em pessoas/animais (não objetos), habilidades conversacionais superficiais melhores, indicadores sutis (timidez, perfeccionismo, exigência de lealdade). Masking contribui para burnout, confusão de identidade e diagnóstico tardio | III | B | REF-276, REF-277 | — |
| AFI-197 | H | OE-H1 | Preditores de TEA em adultos (Whaling 2025, n=234): reciprocidade socioemocional OR=5,21; comunicação não verbal OR=4,82; relacionamentos OR=3,63; rotinas OR=2,57; CNR OR=2,20 | II | B | REF-274 | — |
| AFI-198 | H | OE-H1 | AQ (Autism Spectrum Quotient): sens 77-79%, espec 29-77% (espec reduzida em populações clínicas); cutoff >=26 para encaminhamento | II | B | REF-282, REF-283 | — |
| AFI-199 | H | OE-H1 | RAADS-R: sens 92,5-97%, espec 71-100%; cutoff >=65 (original) / >=81 (alemão); FPR 55,6% em psiquiatria; inclui sintomas sensório-motores DSM-5 | II | B | REF-284, REF-285, REF-286, REF-287 | — |
| AFI-200 | H | OE-H1 | ADOS-2 Módulo 4: sens 91%, espec 76% em adultos; espec cai para 30% em adultos com psicose; pontuação ABAIXO do cutoff NÃO deve excluir TEA em indivíduos com alto masking | II | A (Mandatório) | REF-289, REF-290 | — |
| AFI-201 | H | OE-H2 | Risperidona e aripiprazol: únicos FDA-aprovados para irritabilidade em TEA; SMD 1,07-1,18 vs. placebo | I | A | REF-295, REF-296 | Cochrane NMA 2025 |
| AFI-202 | H | OE-H2 | Risperidona em TEA: iniciar 0,5 mg 1-2x/dia; titular >=2 semanas; alvo 1-3 mg/dia | Consenso | A | REF-048 | — |
| AFI-203 | H | OE-H2 | Aripiprazol em TEA: iniciar 2 mg/dia; titular >=1 semana (até +5 mg/semana); alvo 5-15 mg/dia | Consenso | A | REF-298 | — |
| AFI-204 | H | OE-H2 | ALERTA DE CLASSE — antipsicóticos em TEA: risco de EPS (RR 2,36) e ganho de peso (RR 2,40) AUMENTADOS vs. população psiquiátrica geral; pacientes TEA têm maior sensibilidade; usar menor dose efetiva com reavaliação periódica | I | A (Mandatório) | REF-296, REF-299 | Cochrane NMA + Cochrane SR 2023 |
| AFI-205 | H | OE-H2 | Princípio "start low, go slow" em TEA: doses iniciais 1/3-1/2 das doses habituais; titulação em intervalos de 1-2 semanas; monitorar metabólico + EPS + mudanças comportamentais | Consenso | A (Mandatório) | REF-300, REF-302 | Lurie Center BMC 2025 |
| AFI-206 | H | OE-H2 | TEA + ansiedade: buspirona e mirtazapina PREFERIDAS sobre ISRSs; ISRSs carregam risco de ativação comportamental, agitação e aumento de estereotipias em TEA | Consenso | B | REF-300 | Lurie Center 2025 |
| AFI-207 | H | OE-H2 | Mirtazapina em TEA: 15 mg/noite; titular em 15 mg a cada 1-2 semanas; máx 45 mg/dia. Pilot RCT: 47% "muito melhorado" vs. 20% placebo (PARS, within-group ES=1,76) | II | B | REF-304 | — |
| AFI-208 | H | OE-H2 | TEA + TDAH: guanfacina ER 1ª linha (1 mg -> 1-4 mg/dia; ES=1,67 em hiperatividade; 50% resposta vs. 9,4% placebo); ATX 2ª linha (40->80-100 mg, ES~0,5); metilfenidato com cautela (risco ativação/estereotipias) | II | A | REF-305, REF-306, REF-259 | — |
| AFI-209 | H | OE-H2 | TEA + depressão: duloxetina, mirtazapina, bupropiona e vortioxetina PREFERIDAS sobre ISRSs (Lurie Center guidelines) | Consenso | B | REF-300 | — |
| AFI-210 | H | OE-H2 | Burnout autístico: exaustão profunda + perda de habilidades adquiridas + aumento de traços autísticos; precipitado por masking prolongado + sobrecarga sensorial/social; cronico/intermitente; NÃO é TDM | II | A | REF-311, REF-312 | SR 48 estudos, ~4.000 participantes |
| AFI-211 | H | OE-H2 | Diferenciação burnout vs. TDM: etiologia (masking/sobrecarga vs. biopsicossocial); síntomas (perda de habilidades vs. humor/anedonia); resposta (redução demandas vs. ativação/antidepressivos) | III | A | REF-312 | — |
| AFI-212 | H | OE-H2 | Ativação comportamental pode PIORAR burnout autístico — Delphi liderado por autistas: intervenções devem priorizar modificação ambiental e redução de demandas, não ativação | Consenso | A (Mandatório) | REF-312 | — |
| AFI-213 | H | OE-H2 | Psicoterapias em TEA (NMA Ding 2025): MBSR melhor para ansiedade (SMD=-0,84, SUCRA 91,4%); TCC adaptada melhor para depressão (SMD=-0,77, SUCRA 90,1%); taxa de recuperação em atenção primária: apenas 32,9% (vs. meta UK 50%) | I | A | REF-314, REF-315, REF-318 | — |
| AFI-214 | I | OE-I1 | TPB DSM-5-TR: padrão pervasivo de instabilidade em relacionamentos/autoimagem/afetos + impulsividade; início vida adulta jovem; pervasivo em múltiplos contextos; diagnóstico = >=5 de 9 critérios | Consenso | A | REF-059, REF-320, REF-321 | — |
| AFI-215 | I | OE-I1 | 9 critérios TPB: (1) esforços frenéticos para evitar abandono; (2) relacionamentos instáveis idealização/desvalorização; (3) perturbação identidade; (4) impulsividade >=2 áreas; (5) comportamentos/gestos suicidas ou automutilação; (6) instabilidade afetiva; (7) vazio crônico; (8) raiva intensa; (9) ideação paranoide/dissociação relacionadas ao estresse | Consenso | A | REF-059, REF-320 | — |
| AFI-216 | I | OE-I1 | AMPD (DSM-5-TR Seção III): >=2/4 domínios de funcionamento (identidade, autodireção, empatia, intimidade) + >=4/7 traços patológicos com obrigatoriamente impulsividade, risk-taking OU hostilidade | Consenso | B | REF-321 | Complemento dimensional; modelo categorial permanece padrão |
| AFI-217 | I | OE-I1 | TPB em adolescentes: não proibido antes dos 18 anos; exige sintomas >=1 ano e não atribuíveis ao desenvolvimento normal; válido e confiável a partir dos 12 anos; prevalência clínica até 35,6% | II | A | REF-323, REF-324 | — |
| AFI-218 | I | OE-I1 | IVNS vs. comportamento suicida — distinção central: intenção de morrer. IVNS sem intenção → módulo TPB; SI com intenção/plano → Gate P0 (triagem de crise). C-SSRS e SITBI-R operacionalizam essa distinção | Consenso | A (Mandatório) | REF-059, REF-325 | — |
| AFI-219 | I | OE-I1 | Preditores independentes de tentativa suicida em TPB (CLPS, 10 anos, n=234): perturbação de identidade, esforços frenéticos para evitar abandono, sentimentos crônicos de vazio — mesmo controlando todos os outros critérios | II | A | REF-326 | Yen et al. JAMA Psychiatry 2021 |
| AFI-220 | I | OE-I1 | Escalada de IVNS de alto risco: frequência crescente (semanal/diária), maior gravidade médica (lesões profundas, sutura, hospitalização), múltiplos métodos, habituação à dor — todos associados à transição para comportamento suicida (capacidade adquirida) | II | A | REF-328, REF-329 | Hepp 2025, n=1.227 |
| AFI-221 | I | OE-I1 | Escalada de IVNS → ação obrigatória MESMO SEM intenção suicida: intensificar/encaminhar para DBT + monitoramento semanal ou a cada 2-3 dias + análise funcional comportamental | Consenso | A (Mandatório) | REF-322, REF-330 | — |
| AFI-222 | I | OE-I2 | DBT é a psicoterapia com maior evidência para TPB (Cochrane 2020, 75 RCTs, 4.507 participantes): SMD=-0,52 vs. TAU para gravidade de TPB; reduz IVNS (SMD=-0,28 a -0,54); melhora funcionamento psicossocial (SMD=-0,36); dropout ~27% | I | A | REF-331, REF-333 | — |
| AFI-223 | I | OE-I2 | DBT padrão = 4 componentes: terapia individual semanal (1h) + treino de habilidades em grupo semanal (1,5-2,5h) + coaching telefônico entre sessões + reunião de equipe semanal; pacote completo superior a versões parciais | I | A | REF-334 | Linehan JAMA Psychiatry 2015 |
| AFI-224 | I | OE-I2 | Encaminhamento para DBT: diagnóstico formal TPB (>=5/9 DSM-5-TR) + IVNS ou suicidalidade + padrões escalantes de autolesão + prejuízo psicossocial suficiente para intervenção intensiva ambulatorial | Consenso | A | REF-321, REF-331, REF-335 | — |
| AFI-225 | I | OE-I2 | Farmacoterapia em TPB: NENHUM medicamento aprovado FDA/UK; NICE recomenda CONTRA para sintomas centrais de TPB; crise aguda = agente único, dose mínima, <=1 semana | Consenso | A (Mandatório) | REF-321, REF-337, REF-339 | — |
| AFI-226 | I | OE-I2 | Crise aguda TPB: anti-histamínico sedativo (prometazina) OU antipsicótico baixa potência (quetiapina); NÃO benzodiazepínicos; insônia grave = Z-drugs dose mínima <=4 semanas | Consenso | A | REF-321 | NICE guideline |
| AFI-227 | I | OE-I2 | Melhor evidência sintoma-alvo em TPB (NMA Gerolymos 2026, 35 RCTs): topiramato 200-250 mg/dia (hostilidade/agressividade, evidência ALTA); lamotrigina 50-200 mg/dia (evidência moderada); aripiprazol 15 mg/dia (irritabilidade, evidência moderada) | I | B | REF-338 | Cochrane 2022: nenhuma classe com efeito consistente em desfechos primários |
| AFI-228 | I | OE-I2 | Polifarmácia em TPB: prevalente em até 80% dos pacientes (>=3 fármacos); sem benefício demonstrável; aumenta EAs + interações + não-adesão + prejudica aliança terapêutica; descontinuar medicamentos sem benefício antes de iniciar novos | III | A (Mandatório) | REF-341, REF-342 | — |
| AFI-229 | I | OE-I2 | Olanzapina em TPB: efeitos metabólicos, ganho de peso, sedação + possível aumento de comportamentos autolesivos; evitar ou monitorar rigorosamente | II | B | REF-322, REF-340 | — |
| AFI-230 | I | OE-I2 | Adolescentes 16-17 anos com perfil TPB — 3 ramos: (1) >=5/9 + >=1 ano + prejuízo significativo/escalada → serviços especializados; (2) critérios + <1 ano + prejuízo leve-moderado + sem risco → diagnóstico provisório + GPM-A + família; (3) sintomas sublimiares/transitórios → watchful waiting a cada 4-6 semanas | Consenso | A | REF-323, REF-343, REF-345 | — |
| AFI-231 | I | OE-I2 | Monitoramento TPB: semanal em DBT estável; semanal ou a cada 2-3 dias em IVNS escalante/intervenção farmacológica aguda; reavaliação em 3-7 dias após início de medicação; análise funcional comportamental a cada contato | Consenso | A | REF-322, REF-346 | — |
| AFI-232 | I | OE-I2 | Informante colateral (família/cuidador) em TPB: essencial pois <1/3 dos pacientes com comportamento suicida expressa sua intenção ao clínico; aumenta precisão diagnóstica, estratificação de risco e engajamento no tratamento | II | A | REF-326, REF-347 | — |
| AFI-233 | J | OE-J1 | AN DSM-5-TR — 3 critérios: (A) restrição calórica → peso significativamente baixo; (B) medo intenso de ganhar peso OU comportamento que interfere com ganho de peso; (C) perturbação na percepção do peso/forma OU ausência de reconhecimento da gravidade. IMC <18,5 = abaixo do mínimo; IMC <17,0 = magreza moderada/grave | Consenso | A | REF-059, REF-348, REF-349 | — |
| AFI-234 | J | OE-J1 | AN subtipos: F50.01 (restritivo) = dieta/jejum/exercício sem B/P nos últimos 3 meses; F50.02 (purgativo) = episódios recorrentes de compulsão/purgação nos últimos 3 meses | Consenso | A | REF-059, REF-348 | — |
| AFI-235 | J | OE-J1 | AN — gravidade por IMC (adultos): leve >=17; moderada 16-16,99; grave 15-15,99; extrema <15. Gravidade pode ser aumentada para refletir sintomas, incapacidade ou necessidade de supervisão | Consenso | A | REF-059, REF-348 | — |
| AFI-236 | J | OE-J1 | BN DSM-5-TR: episódios recorrentes de compulsão + comportamentos compensatórios inadequados; >=1x/semana por >=3 meses; autoavaliação indevidamente influenciada por peso/forma. Gravidade (compensatórios/semana): leve 1-3; moderada 4-7; grave 8-13; extrema >=14 | Consenso | A | REF-059, REF-348 | — |
| AFI-237 | J | OE-J1 | TCAP (BED) DSM-5-TR: compulsão recorrente >=1x/semana por >=3 meses + >=3/5 características + distress marcado; AUSÊNCIA de comportamentos compensatórios regulares diferencia de BN. Mesma gradação de gravidade por frequência que BN | Consenso | A | REF-059, REF-348 | — |
| AFI-238 | J | OE-J1 | Limiares de internação em AN (integração APA + NICE/MARSIPAN + CFM): IMC <=15 (APA/CFM) ou <14 (MARSIPAN); FC <40-50 bpm; PA sistólica <80-90 mmHg; temperatura <35,5°C; QTc >450 ms; K+ <3,0 mmol/L; PO4 <0,5 mmol/L (MARSIPAN); ΔFC >20 bpm ou ΔPAS >20 mmHg ortostáticos | Consenso | A (Mandatório) | REF-349, REF-350, REF-355 | — |
| AFI-239 | J | OE-J1 | Adolescentes — limiares de internação em AN: NÃO usar IMC absoluto; usar percentis CDC. Red flags: IMC <5º percentil para idade/sexo OU <=75% do IMC mediano para idade/sexo/altura; queda cruzando >=2 linhas de percentil = avaliação imediata | Consenso | A | REF-352, REF-357 | — |
| AFI-240 | J | OE-J1 | Internação involuntária em AN no Brasil — 2 vias: (1) internação médica por instabilidade clínica aguda NÃO requer critérios de compromisso involuntário psiquiátrico; (2) internação involuntária psiquiátrica (Lei 10.216/2001 + CFM Resolução 2.057/2013) quando paciente recusa tratamento necessário E há risco médico iminente | IV (Legal) | A (Mandatório) | REF-023, REF-024 | — |
| AFI-241 | J | OE-J1 | Documentação obrigatória internação involuntária AN: diagnóstico DSM-5-TR + gravidade + parâmetros clínicos + justificativa de risco agudo + objetivos terapêuticos + base legal (Lei 10.216/2001 + CFM 2.057/2013) + comunicação de direitos ao paciente/representante + notificação ao Ministério Público em 72h + agenda de reavaliação e alta | IV (Legal) | A (Mandatório) | REF-023, REF-024 | — |
| AFI-242 | J | OE-J2 | AN tem a maior taxa de mortalidade entre os transtornos psiquiátricos; ~1/3 das mortes por complicações cardiovasculares; estado hipometabólico → ↓ massa cardíaca + bradicardia + hipotensão + QTc prolongado + risco de arritmia ventricular e morte súbita | II | A | REF-365, REF-366 | — |
| AFI-243 | J | OE-J2 | Síndrome de realimentação — prevenção ASPEN 2020: tiamina 100 mg VO/EV/dia (até 200 mg grave; 2 mg/kg até 100-200 mg em adolescentes) ANTES de iniciar alimentação + manter 5-7 dias; eletrólitos (K, PO4, Mg) antes do início + a cada 12h pelos primeiros 3 dias em pacientes de alto risco | Consenso | A (Mandatório) | REF-368 | — |
| AFI-244 | J | OE-J2 | Metas de suplementação profilática de eletrólitos na realimentação: K+ 2-4 mmol/kg/dia; PO4 0,3-0,6 mmol/kg/dia; Mg 0,2-0,4 mmol/kg/dia; multivitamínico oral completo >=10 dias; Na <1 mmol/kg/dia; fluidos <20 mL/kg/dia na fase inicial | Consenso | A | REF-368, REF-369 | — |
| AFI-245 | J | OE-J2 | Prescrição calórica inicial adultos: 1.500-2.000 kcal/dia + progressão ~33% da meta a cada 1-2 dias. Se eletrólitos caem precipitadamente: reduzir 50% e nova progressão gradual | Consenso | B | REF-349, REF-368 | — |
| AFI-246 | J | OE-J2 | Realimentação em adolescentes levemente/moderadamente desnutridos: evidência atual suporta 2.200-2.600 kcal/dia → ganho ~1,4-2 kg/semana. HCR vs. LCR (Garber RCT JAMA Pediatrics 2020, multicêntrico): HCR atingiu estabilização de FC mais rápida e maior ganho ponderal SEM aumento de complicações quando monitoramento eletrolítico foi rigoroso | I | A | REF-370, REF-371 | — |
| AFI-247 | J | OE-J2 | Red-flags para referência/internação imediata (ambulatório): IMC <=15 (adultos) ou <=75% IMC mediano/<5º percentil (adolescentes); FC <40 bpm; PAS <90 mmHg; ortostase: ΔFC >20 bpm ou ΔPAS >20 mmHg; temperatura <35,5°C; K+ <3,0 mEq/L; PO4 <0,8 mmol/L; Mg <1,5 mg/dL; QTc >450 ms (H) ou >470 ms (M); recusa alimentar aguda; purgação incontrolável; suicidalidade | Consenso | A (Mandatório) | REF-353, REF-355, REF-356 | — |
| AFI-248 | J | OE-J2 | Monitoramento ambulatorial TA: peso + IMC + SSVV (repouso + ortostáticos) + avaliação comportamental em TODA consulta; CBC + eletrólitos + função hepática e renal: baseline + cada 1-4 semanas conforme risco; ECG: baseline + se mudança clínica ou alteração laboratorial; frequência de consultas: semanal-quinzenal (fase aguda) → mensal (fase estável) | Consenso | A | REF-355, REF-356, REF-372 | — |
| AFI-249 | J | OE-J2 | Farmacoterapia aprovada: fluoxetina 60 mg/dia (FDA-aprovada para BN); lisdexanfetamina (FDA-aprovada para TCAP/BED); TCC = 1ª linha para BN e TCAP; terapia baseada na família (FBT) = 1ª linha para adolescentes com AN | Consenso | A | REF-353, REF-355 | — |
| AFI-250 | J | OE-J2 | Equipe multidisciplinar obrigatória em TA: clínico médico (avaliação física + complicações) + psiquiatra (psicoterapia + farmacoterapia + conformidade legal) + nutricionista (avaliação nutricional + plano alimentar + supervisão reabilitação). Transições de cuidado: comunicação contínua + critérios explícitos de escalada no plano terapêutico | Consenso | A | REF-355 | — |
| AFI-251 | K | OE-K2 | Lítio + AINEs: AINEs reduzem fluxo sanguíneo renal → ↓ clearance de lítio → níveis séricos aumentados. Toxicidade em 1-7 dias após início do AINE. Progressão: GI (náuseas/vômitos/diarreia) → neuromuscular (tremor/ataxia) → neuropsiquiátrico (confusão/disartria) → grave (convulsões/coma/arritmias) | III | A | REF-373, REF-374, REF-375 | — |
| AFI-252 | K | OE-K2 | Manejo emergencial toxicidade lítio+AINE: descontinuar AMBOS imediatamente + dosagem urgente de lítio + função renal + eletrólitos + hidratação IV + monitoramento cardíaco. Hemodiálise: lítio sérico >2,5 mEq/L OU sintomas neurológicos graves | Consenso | A (Mandatório) | REF-373, REF-375 | — |
| AFI-253 | K | OE-K2 | Monitoramento lítio+AINE LP: nível de lítio 5-7 dias após início/interrupção de AINE; lítio q3mo; função renal (Cr + eFG) q3-6mo. Idosos >65: alvo 0,6-0,8 mEq/L (vs. 0,8-1,2 mEq/L); monitoramento q2-3mo; Beers Criteria: lítio potencialmente inapropriado com fármacos que prejudicam função renal | Consenso | A | REF-384, REF-385, REF-386 | — |
| AFI-254 | K | OE-K2 | Valproato + Lamotrigina: valproato inibe glicuronidação da lamotrigina → meia-vida: 26h → 70h (+165%) → risco de SJS e TEN. Janela crítica: 2-8 semanas (pode ser 5-10 dias com titulação rápida). Trigger de emergência: qualquer rash novo ± envolvimento mucoso ± febre ± linfadenopatia → descontinuar AMBOS + hospitalizar + dermatologia | Consenso | A (Mandatório) | REF-377, REF-378 | Bula FDA LTG + NEJM 2021 |
| AFI-255 | K | OE-K2 | Protocolo obrigatório valproato+LTG: iniciar LTG com METADE da dose usual; titular NO MÁXIMO a cada 2 semanas (exigência bula FDA). Monitoramento LP: TGO/TGP/GGT q3-6mo; exame de pele documentado em cada consulta | Bula FDA | A (Mandatório) | REF-377 | — |
| AFI-256 | K | OE-K2 | Clozapina + BZDs: risco de colapso cardiorrespiratório + pneumonia aspirativa + delirium. Protocolo Quiles SR 2025: evitar BZD na semana ANTES do início da CLZ + durante a primeira semana de titulação. Se BZD mantido: titulação muito lenta + monitoramento diário para delirium + vigilância de pneumonia por >=2 semanas | II | A (Mandatório) | REF-379 | — |
| AFI-257 | K | OE-K2 | ISRSs + Tramadol — síndrome serotoninérgica: duplo mecanismo (ambos aumentam 5-HT + ISRSs inibem metabolismo tramadol via CYP2D6). Diagnóstico: Critérios de Hunter. Início: horas a poucos dias (<24h mais frequente). Manejo: descontinuar AMBOS + BZDs (agitação/neuromusculares) + resfriamento externo (hipertermia) + ciproheptadina (moderado-grave) | III | A (Mandatório) | REF-380, REF-381, REF-382 | — |
| AFI-258 | K | OE-K2 | Critérios de Beers (AGS) — alertas DDI em psiquiatria para >65 anos: lítio potencialmente inapropriado com drogas que prejudicam função renal; BZDs evitar (dose mínima/duração mínima se necessários); tramadol com risco aumentado de SS e quedas — evitar se possível; revisão abrangente de medicamentos pelo menos anualmente | Consenso | A | REF-384, REF-385, REF-383 | — |
| AFI-259 | K | OE-REF1 | Lei 10.216/2001 — internação involuntária: excepcional; sem consentimento; a pedido de terceiro; exige: (1) diagnóstico de transtorno mental + (2) risco iminente para si/terceiros OU incapacidade grave de autocuidado + (3) falha documentada de alternativas menos restritivas | IV (Legal) | A (Mandatório) | REF-391, REF-394 | — |
| AFI-260 | K | OE-REF1 | Laudo médico circunstanciado (CFM 2.057/2013): diagnóstico CID-10/DSM-5 + exame estado mental + riscos específicos + justificativa + falha de menos restritivas + identidade do terceiro solicitante + assinatura + data + CRM. Notificação ao Ministério Público em 72h. Adição jurisprudencial (Rooman v. Bélgica): unidade receptora deve ser capaz de oferecer tratamento real | IV (Legal) | A (Mandatório) | REF-395, REF-396 | — |
| AFI-261 | K | OE-REF1 | Transferência privado→público: duplo laudo exigido. Laudo privado acompanha o paciente mas NÃO é suficiente por si só. A unidade receptora pública deve (1) avaliar o paciente independentemente + (2) emitir seu próprio laudo + (3) assumir responsabilidade pela notificação ao MP em 72h. Apenas 40% dos formulários de detenção abordam todos os critérios legais (Brayley) | IV (Legal) | A (Mandatório) | REF-396, REF-397 | — |
| AFI-262 | K | OE-REF1 | CTC — Checklist de Tratamento Compulsório (Brissos 2017): 25 itens + 4 clusters (Legal, Perigo, Histórico, Cognitivo); pontuação 0-50; cutoff 23,5 → sensibilidade 75% + especificidade 93,6% + acurácia 90% para predizer tratamento compulsório | III | B | REF-398, REF-399 | — |
| AFI-263 | K | OE-REF2 | Critérios CAPS III vs. internação: internação hospitalar indicada para — SI com plano+intenção+acesso a meios; tentativa recente com risco persistente; sem capacidade de safety planning. CAPS III indicado para — risco moderado-alto sem iminência imediata; crise intensiva até 14 dias sem necessidade de recursos médicos completos | Consenso | A (Mandatório) | REF-403, REF-404 | — |
| AFI-264 | K | OE-REF2 | CAPS III em São Paulo — política de "porta aberta"; encaminhamentos diretos de psiquiatras privados ambulatoriais aceitos para crises; comunicação direta com a unidade recomendada. Pacientes Amil/planos privados admitidos em CAPS III ou UPA → cobertura muda INTEGRALMENTE para SUS durante o episódio de crise, sem necessidade de autorização do plano. Amil retoma cobertura após alta | III | A | REF-403, REF-412 | Fontenelle: ~13% dos episódios de saúde de beneficiários privados vão ao SUS |
| AFI-265 | K | OE-K2 | Framework 4Ms para idosos em psiquiatria: What Matters (objetivos do paciente), Medication (revisão anual + desprescrição), Mentation (rastreio cognitivo), Mobility (risco de quedas). Alertas geriátricos automáticos >65 anos para DDIs de alto risco + Beers Criteria. Revisão abrangente de medicamentos: anualmente + após qualquer mudança aguda | Consenso | A | REF-387, REF-418, REF-419 | — |
| AFI-266 | K | OE-K2 | Suporte de decisão clínica (CDS) para DDIs: triagem ANTES da finalização do pedido; bancos com utilidade demonstrada: Lexicomp, Drugs.com, Epocrates (classificações de gravidade podem variar). Farmacêutico: reconciliar lista ativa + educar sobre OTC + interações alimentares. Documentar explicitamente: mecanismo DDI + cronograma de monitoramento + responsável pelo seguimento | Consenso | A | REF-388, REF-389, REF-390 | — |

---

## RELATÓRIOS CONSOLIDADOS

---

### RELATÓRIO 01 | OE-B1 · OE-B2 · OE-B3
**Tema:** Gate P0 — Triagem de Risco Suicida  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_01_GATE_P0.md`  
**Status:** ✅ Consolidado

#### Contexto da consulta
- **OE-B1:** Itens mínimos de triagem de risco suicida em ambulatório
- **OE-B2:** Fatores de risco por diagnóstico (depressão, TAB, esquizofrenia)
- **OE-B3:** Conduta após ideação com plano em contexto sem contenção local
- Pop. alvo: adultos primariamente; adolescentes sinalizados quando relevante
- Capacidade: sem contenção local → encaminhamento a UPA/SAMU/internação

#### Síntese das afirmações principais

**Gate P0 — estrutura mínima do C-SSRS (AFI-001 a AFI-006):**
- 7 itens mínimos obrigatórios em todo encontro com suspeita de risco
- C-SSRS: 6 perguntas em cascata, Q3–Q5 só se Q2 positivo
- Desempenho: OR 3,14 para tentativas não-fatais; OR 2,78 para tentativas

**Fatores de risco por diagnóstico (AFI-009 a AFI-017):**
- Tentativa prévia = preditor isolado mais potente; recorrência em 3–6 meses
- TAB tem risco maior que MDD em todas as métricas; estado misto = pico de risco
- Comorbidades amplificadoras: SUB, TPB, impulsividade/agitação

**Conduta de alto risco sem contenção (AFI-018 a AFI-025):**
- Sequência obrigatória: observação contínua → segurança ambiental → SAMU/UPA → SPI → notificação familiar (Art. 46 CFM)
- SPI: 6 passos, 15–30 min, eficácia comprovada (OR 0,56 para comportamento suicida)
- Lei 10.216/2001: internação involuntária + notificação MP em 72h são mandatórios e devem estar no protocolo de documentação

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes em conflito | Resolução adotada |
|---|-------------|-------------------|-------------------|
| 1 | Instrumento mandatório | CFM: avaliação individualizada (sem instrumento obrigatório) vs. APA/JointComm: C-SSRS recomendado (AFI-007) | Protocolo usa C-SSRS como estrutura + documentação individualizada conforme CFM |
| 2 | Notificação de família | CFM Art. 46: obrigatória em risco iminente, mesmo sem consentimento (AFI-008) vs. NICE: a critério clínico | Protocolo segue CFM (mais restritivo por ser contexto brasileiro) |
| 3 | Follow-up 72h | Recomendado por VA/DoD [REF-020] mas não operacionalizável no fluxo ambulatorial Daktus | Registrar como orientação ao paciente, fora da lógica do protocolo |

> **Gatilho G5 identificado (prática vs. evidência):** a prática relatada pelos psiquiatras de Pinheiros não inclui SPI formal. O protocolo deve apresentar o SPI como padrão baseado em evidência nível I, com nota de implementabilidade. Sem necessidade de SE — o relatório OE já resolve o conflito.

#### Referências deste relatório
26 referências. Todas registradas na Tabela Mestre (REF-001 a REF-026).

---

### RELATÓRIO 02 | OE-K1 · OE-D2 · OE-D3
**Tema:** Monitoramento Laboratorial — Lítio, Valproato, Carbamazepina, Antipsicóticos e Clozapina  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_02_MONITORAMENTO_FARMACOS.md`  
**Status:** ✅ Consolidado

#### Síntese das afirmações principais

**Lítio (OE-D2) — AFI-026 a AFI-034:**
- Padrão-ouro para TAB-I; faixa aguda 0,8–1,2 / manutenção 0,8–1,0 (idosos: 0,6–0,8) mEq/L; amostras sempre como vale 12h pós-dose
- Baseline completo; iniciação: litemia semanal até estabilização; renal 1m e 3m; manutenção: litemia a cada 3m (1º ano) → 6m
- Toxicidade gradeada: leve/moderada/grave (>2,5 → hemodiálise); precipitada por AINEs, IECA, diuréticos, desidratação
- Contraindicação absoluta: eGFR <30; precaução: eGFR 30–89

**Valproato (OE-D3) — AFI-035 a AFI-041:**
- Faixa alvo: 50–100 µg/mL; baseline inclui teste gravidez OBRIGATÓRIO
- Iniciação: nível + LFTs + hemograma a cada 1–3m; manutenção: cada 6–12m (anual se estável >2 anos)
- **Alert máximo**: ~9% malformações, ~25% se dose >1.450mg/dia; evitar em MIE quando viável; se usado: contracepção + ácido fólico + documentação

**Carbamazepina + Antipsicóticos (OE-K1) — AFI-042 a AFI-059:**
- CBZ: faixa 4–12 µg/mL; HLA-B*1502 se asiático; potente indutor enzimático — revisar DDIs sempre
- Antipsicóticos atípicos: protocolo metabólico universal (peso/IMC/glicemia/lipídios) baseline → 3m → anual; EPS em toda consulta na iniciação
- Clozapina: ANC semanal 6m → quinzenal → mensal; não iniciar se ANC <1.500/µL; risco máximo 18 primeiras semanas
- Adherência real ao monitoramento metabólico: apenas 44,3% (glicemia) e 41,5% (colesterol) — justifica protocolo estruturado (AFI-057)

#### Tabela de monitoramento consolidada

| Fármaco | Exame | Freq. iniciação (0–6m) | Freq. manutenção (>6m) | Limiar / Alerta | REF-ID |
|---------|-------|----------------------|----------------------|-----------------|--------|
| Lítio | Litemia | 5–7d pós-ajuste; depois 1–2 semanas | 3m (1º ano); 6m depois | Tox. leve ≥1,5; grave >2,5 mEq/L | REF-027, REF-028 |
| Lítio | Creatinina + eGFR | 1m e 3m | A cada 6m | eGFR <30: contraindicado | REF-027, REF-028 |
| Lítio | TSH + T4L | 3m | 6–12m | — | REF-027, REF-029 |
| Lítio | Cálcio + eletrólitos | 1–3m | Anual | — | REF-027 |
| Lítio | ECG | Baseline se >40a ou risco CV | Se indicação clínica | — | REF-028 |
| Valproato | Nível sérico | 1–2 semanas após início; depois 1–3m | 6–12m (anual se estável >2a) | Faixa alvo: 50–100 µg/mL | REF-031, REF-027 |
| Valproato | ALT/AST | Mesmos intervalos do nível sérico | 6–12m | — | REF-031, REF-033 |
| Valproato | Hemograma c/plaquetas | Mesmos intervalos do nível sérico | 6–12m | Trombocitopenia | REF-031 |
| Carbamazepina | Hemograma c/dif.+plaquetas | 2×/mês × 2m; depois mensal | 3–6m | Agranulocitose | REF-043 |
| Carbamazepina | LFTs | 2×/mês × 2m; depois mensal | 3–6m | — | REF-043 |
| Carbamazepina | Natremia | Mensal | 3–6m | Hiponatremia | REF-043 |
| Carbamazepina | Função renal | Mensal | 6–12m | — | REF-043 |
| Carbamazepina | Nível sérico CBZ | Após dose estável (3–7d pós-ajuste) | 6–12m | Faixa alvo: 4–12 µg/mL | REF-044 |
| Antipsicótico atípico | Peso + IMC + CC + PA | Baseline | 3m e anual | — | REF-027, REF-054 |
| Antipsicótico atípico | Glicemia / HbA1c | Baseline | 3m e anual | — | REF-027, REF-054 |
| Antipsicótico atípico | Perfil lipídico | Baseline | 3m e anual | — | REF-027, REF-054 |
| Antipsicótico atípico | EPS (clínico) | Toda consulta | 6–12m (3m em idosos) | — | REF-045, REF-046 |
| Olanzapina | LFTs | Baseline | Periodicamente | ALT >200 UI/L = alerta | REF-050 |
| Quetiapina | ECG (QTc) | Baseline se risco CV | Se sintomas ou nova medicação QT | — | REF-053, REF-055 |
| Risperidona/Paliperidona | Prolactina | Se sintomático | Se uso prolongado ou sintomático | — | REF-048, REF-057 |
| Clozapina | ANC | Baseline (não iniciar se <1.500) | Semanal 6m → quinzenal 6m → mensal | ANC <1.500/µL: suspender | REF-052, REF-054 |
| Clozapina | Peso+IMC+glicemia+lipídios | Baseline + periodicamente | Anual | — | REF-052 |
| Clozapina | LFTs + ECG | Baseline | Se indicação clínica | Miocardite 1º mês | REF-051, REF-052 |

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | CFM/ABP sem resolução numerada específica | REF-040 | Transparência no playbook: referenciar CANMAT 2018 + ISBD 2009 explicitamente |
| 2 | Valproato em MIE: evitar vs. usar com precauções | AAN/AES mandatório (REF-037) vs. prática real (REF-039) | Protocolo adota AAN/AES + flag de alerta máximo + checklist de precauções |
| 3 | Prolactina de rotina vs. apenas sintomática | Não universal para todos os AAs | Protocolo: apenas se sintomático OU risperidona/paliperidona |

#### Referências deste relatório
32 REF-IDs novos registrados na Tabela Mestre (REF-027 a REF-058).

---

### RELATÓRIO 03 | OE-D1 · OE-D4 · OE-D5
**Tema:** Humor — Critérios, Escalas e Depressão Resistente  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_03_HUMOR_ESCALAS_DRT.md`  
**Status:** ✅ Consolidado  
**Nota:** OE-E1–E4 (Ansiedade, TOC, TEPT, Burnout) cobrirão relatório dedicado.

#### Síntese das afirmações principais

**Critérios DSM-5-TR (OE-D1) — AFI-060 a AFI-069:**
- EDM: ≥5 sintomas/2 semanas, pelo menos 1 = humor deprimido ou anedonia; irritabilidade válida em adolescentes
- Maníaco: ≥7 dias + ≥3 sintomas; hipomaníaco: ≥4 dias, sem prejuízo marcado/psicose
- Especificador misto: ≥3 sintomas cruzados — limiar de 2 rejeitado por triplicar prevalência sem adicionar validade
- TAB-I vs. TAB-II: psicose = automaticamente maníaco = TAB-I; TAB-II não é forma mais leve (risco suicida equivalente)
- **Pitfall crítico:** delay diagnóstico TAB-II >10 anos → triagem obrigatória de bipolaridade em toda depressão (MDQ: sens 80%/espec 70%)

**Escalas validadas no Brasil (OE-D4) — AFI-070 a AFI-076:**
- PHQ-9: único com normativos locais brasileiros (n>10.000); cortes: moderado 14–19, urgência ≥24, item 9+ → gate de suicídio
- MADRS: sem normativos locais; hospitalização em depressão bipolar: ≥24
- YMRS: sem normativos locais; mania grave: ≥25
- Adolescentes: SMFQ validado no Brasil corte >6

**Antidepressivos e DRT (OE-D5) — AFI-077 a AFI-093:**
- 1ª linha CANMAT 2023: escitalopram, mirtazapina, paroxetina, sertralina, venlafaxina XR com eficácia superior
- Meta-análise Cipriani (522 RCTs): todos 21 superiores ao placebo; NMA valida hierarquia
- **ANVISA:** vilazodona + levomilnacipran NÃO aprovados; agomelatina aprovada localmente
- DRT: ≥2 ensaios adequados falhos; Maudsley Staging Model (3 dimensões) para staging; melhor evidência: ECT (OR 12,86) > esketamina > aripiprazol > quetiapina XR > lítio augmentação
- MBC: PHQ-9 toda consulta + alertas automáticos (≥10/≥20/item9+) — fundamento técnico para automação no Daktus

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | Especificador misto: limiar 2 vs. 3 sintomas | Zimmermann 2026 (REF-064) vs. prática clínica anterior | Protocolo adota limiar 3 (DSM-5-TR oficial, evidência 2026) |
| 2 | Escitalopram ANVISA para adolescentes | FDA-aprovado nos EUA; status ANVISA pendente de verificação | Protocolo: fluoxetina como 1ª linha para adolescentes; escitalopram com nota de verificação ANVISA |
| 3 | Esketamina no SUS | Aprovada ANVISA; disponibilidade SUS terciária muito limitada | Registrar como opção com nota de disponibilidade |

#### Referências deste relatório
44 REF-IDs novos registrados na Tabela Mestre (REF-059 a REF-102).  
Duplicatas identificadas e NÃO reduplicas: Ref 3 do relatório = REF-018; Ref 6 = REF-042.

---

### RELATÓRIO 04 | OE-E1 · OE-E2 · OE-E3 · OE-E4
**Tema:** Ansiedade, TOC, TEPT e Burnout  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_E1E4_ANSIEDADE_TOC_TEPT.md`  
**Status:** ✅ Consolidado  
*(Anteriormente denominado REL-03b)*

#### Síntese das afirmações principais

**Critérios e exclusão orgânica (OE-E1) — AFI-094 a AFI-105:**
- TAG: ≥6 meses + ≥3/6 sintomas (adultos) / 1/6 (crianças); Pânico: ataques inesperados + ≥4/13 sintomas + ≥1 mês; TOC: >1h/dia de obsessões/compulsões
- TEPT: 4 clusters ≥1 mês; CPTSD ICD-11: adiciona distúrbios de auto-organização — alguns casos DSM-5 ≠ ICD-11
- **Exclusão orgânica obrigatória** quando sintomas físicos proeminentes: workup sintoma-específico (ECG+TSH+glicemia, oximetria, enzimas)
- POTS: FC >30 bpm active stand; hipotensão ortostática: PA sist. ≥20 mmHg em 3 min

**ISRS doses e QTc (OE-E2) — AFI-106 a AFI-115:**
- **Citalopram: >40 mg/dia CONTRAINDICADO** (FDA/ANVISA); QTc dose-dependente
- Hierarquia de risco: citalopram > escitalopram > sertralina/fluvoxamina/fluoxetina > **paroxetina (menor)**
- ECG baseline se ≥2 FR ou citalopram/escitalopram em alta dose; follow-up 1–2 semanas; QTc >500 ms → descontinuar imediatamente
- Setting sem ECG: usar sertralina, fluoxetina, fluvoxamina ou paroxetina

**Burnout (OE-E3) — AFI-116 a AFI-124:**
- ICD-11 QD85: fenômeno ocupacional, NÃO transtorno médico; não incluído no DSM-5-TR
- NÃO tratar burnout com antidepressivos/ansiolíticos; tratar depressão/ansiedade comórbidas
- Instrumentos validados BR: MBI-HSS (padrão-ouro), OLBI, **BAT-12 (melhor breve)**; BCSQ-12 (subtipos APS)
- Correla móção burnout-depressão r≈0,52, mas construtos dissociáveis

**TEPT tratamento e encaminhamento (OE-E4) — AFI-125 a AFI-133:**
- 1ª linha: ISRSs (sertralina/paroxetina FDA-aprovadas); venlafaxina também 1ª linha
- **BZDs CONTRAINDICADOS; cannabis contraindicados**
- PE, CPT, TCC-trauma (APA: “strongly recommends”); EMDR (melhor custo-efetividade; 86% taxa de perda do diagnóstico)
- Encaminhamento para psicoterapia especializada: TEPT moderado-grave, falha ambulatorial, CPTSD, suicidalidade
- PDS-3 (3 itens): ROC=0,97, sens 86,4%, espec 93,5% — triagem eficiente em setting ambulatorial

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | TEPT DSM-5-TR vs. ICD-11 (CPTSD): prevalência diferente, critérios distintos | REF-164 | Protocolo deve usar DSM-5-TR como base; documentar diferença em notas clínicas |
| 2 | Burnout vs. TDM: confusão clínica frequente | REF-130, REF-137 | Processo diferencial: contexto-específico, reversibilidade, sintomas neurovegetativos |
| 3 | Escitalopram ANVISA em adolescentes | FDA aprovado; status ANVISA requer verificação | Protocolo: anotar incerteza; não usar como padrão em jovens |

#### Referências deste relatório
62 REF-IDs novos (REF-103 a REF-164).  
Duplicatas identificadas (não reduplicas): Ref 1 = REF-059; Ref 8 = REF-022; Ref 27 = REF-055.

---

### RELATÓRIO 05 | OE-F1 · OE-F2 · OE-F3 · OE-F4
**Tema:** Psicose, EPS, Clozapina e Risco Metabólico  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_05_PSICOSE_EPS_CLOZAPINA.md`  
**Status:** ✅ Consolidado

#### Síntese das afirmações principais

**Critérios psicóticos (OE-F1) — AFI-136 a AFI-141:**
- Esquizofrenia: ≥2/5 domínios ≥1 mês + sinais contínuos ≥6 meses; pelo menos 1 delução/alucinação/discurso desorganizado
- T. esquizoafetivo: Critério A + humor maior simultâneo; deluções/aluc. ≥2 semanas sem humor; humor na maioria do tempo
- T. psicótico breve: ≥1 sintoma positivo por 1 dia a <1 mês
- FRS de Schneider: NÃO são mais critérios DSM-5-TR/ICD-11; sens ~60%, espec ~85%; usar apenas como indicador suplementar

**EPS e escalas (OE-F2) — AFI-142 a AFI-149:**
- Janela terapêutica D2: 60–80% de ocupação; acima de 85% = EPS significativos
- SAS + BARS + AIMS: toda consulta na iniciação (0–12 semanas); cada 6 meses após (3 meses para alto risco/idosos)
- SNM: hipertermia + rigidez + alteração mental + insTab. autonômica + CK ≥4× → internação imediata
- Jovens 18–25: doses iniciais menores + titulação gradual

**Clozapina (OE-F3) — AFI-150 a AFI-160:**
- ANC baseline obrigatório; não iniciar se <1.500/µL; monitoramento semanal 6m → quinzenal → mensal
- **CIVH é o risco letal mais prevalente** (mortalidade íleo 25–44% vs. agranulocitose 2–4%); triagem subjetiva sens 18% apenas
- Protocolo Porirua: docusato + senna profilaticamente universal; anticolinérgicos CONTRAINDICADOS
- ANVISA: registro no Programa Nacional obrigatório; dispensação dependente de confirmação em tempo real

**Risco metabólico e efetividade (OE-F4) — AFI-161 a AFI-168:**
- Clozapina = pior perfil metabólico em todos os parâmetros; olanzapina = 2ª pior
- Disregulação glicemia ≠ ganho de peso; lurasidona e quetiapina: HbA1c elevada apesar de menor ganho
- Monitoramento: baseline + 12 semanas (iniciação) → cada 3–6 meses (1º ano) → anual
- SUS Brasil: clozapina tem menor troca e vantagem de sobrevivência vs. todos os outros antipsicóticos

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | FRS de Schneider: ~50% especialistas apoiam reintroduzir nos critérios | Moritz 2024 vs. DSM-5-TR/ICD-11 | Protocolo usa DSM-5-TR; FRS documentados como achado suplementar |
| 2 | Delphi 2025 propõe limiar ANC menor (1,0×10⁹/L) e discontinuação após 2 anos | Siskind 2025 vs. FDA label atual | Adotar FDA/ANVISA atual até regulatório ser atualizado |
| 3 | Lurasidona/cariprazina/brexpiprazol têm melhor perfil metabólico mas acesso limitado no SUS | REF-211 vs. REF-208 | Documentar preferência técnica mas recomendar alternativa SUS |

#### Referências deste relatório
58 REF-IDs novos (REF-165 a REF-222).  
Duplicatas identificadas (não reduplicas): Ref 1=REF-059; Ref 2=REF-045; Ref 6=REF-163; Ref 24=REF-047; Ref 37/38=REF-052; Ref 58=REF-050.

---

### RELATÓRIO 06 | OE-G1 · OE-G2 · OE-G3 · OE-G4
### RELATÓRIO 06 | OE-G1 · OE-G2 · OE-G3 · OE-G4
**Tema:** TDAH Adulto — Critérios, ECG, Neuropsicológica e Farmacoterapia  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_06_TDAH.md`  
**Status:** ✅ Consolidado

#### Síntese das afirmações principais

**Critérios e rastreio ASRS (OE-G1) — AFI-169 a AFI-173:**
- TDAH adulto: ≥5/9 sintomas em desatenção OU hiperatividade-impulsividade (vs. 6 em <17 anos); início antes dos 12 anos; ≥2 contextos; prejuízo funcional
- ASRS v1.1 (WHO): VPN ~100%, mas **VPP pode ser apenas 11,5%** — rastreio positivo EXIGE avaliação clínica completa
- Informante colateral fortemente recomendado; auto-relato isolado tem viés significativo

**ECG pré-estimulantes (OE-G2) — AFI-174 a AFI-177:**
- Abordagem **risco-baseada, não universal**; ECG rotineiro sem FR não recomendado (AAP, AMSSM, NICE)
- Indicado se: cardiopatia/cardiomiopatia pessoal, hist. familiar de morte súbita, síncope inexplicada, achados físicos anormais
- Sem FR: apenas PA + FC baseline
- Durante uso: FC >120 bpm ou PA >p95 em 2 ocasiões → reduzir dose + especialista

**Avaliação neuropsicológica (OE-G3) — AFI-178 a AFI-179:**
- NÃO obrigatória na rotina; indicar apenas quando: sem informante, comorbidade confundidora, simulacão suspeita, incapacidade legal
- Abordagem combinada (auto-relato + informante + hist. familiar + variabilidade TR) classificou 87% dos casos corretamente

**Não-estimulantes e comorbidades (OE-G4) — AFI-180 a AFI-191:**
- Atomoxetina: melhor não-estimulante (g=-0,48); sem potencial de abuso; ANVISA aprovada
- TDAH + TAB: **humor PRIMEIRO** (lítio/valproato) → atomoxetina ou bupropiona → estimulante só após
- TDAH + SUD ativo: estimulantes contraindicados; ATX preferida
- TDAH + SUD remissão: liberacão prolongada/pró-droga com mitigacão de risco (acordos + PDMP + urina aleatória)
- Viloxazina ER: eficácia comparavel ATX, sem risco QTc — **NÃO aprovada ANVISA**

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | AAFP 2024: ECG baseado em risco vs. prática clínica de pedir ECG rotineiro | REF-226 vs. prática | Protocolo adota AAP/AAFP: ECG só se FR presentes |
| 2 | Viloxazina ER: boa evidência mas não aprovada ANVISA | REF-247, REF-263 | Não incluir como opção-padrão no protocolo brasileiro |
| 3 | Neuropsicológica: acesso limitado no sistema suplementar brasileiro | Prática local | Reservar para casos onde impactará decisão clínica |

#### Referências deste relatório
48 REF-IDs novos (REF-223 a REF-270).  
Duplicata identificada: Ref 1 = REF-059 (DSM-5-TR).

---

### RELATÓRIO 07 | OE-H1 · OE-H2
**Tema:** TEA Adulto — Critérios, Rastreio e Farmacoterapia por Alvo Sintomático  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_07_TEA.md`  
**Status:** ✅ Consolidado

#### Síntese das afirmações principais

**Critérios DSM-5-TR TEA (OE-H1) — AFI-192 a AFI-200:**
- 5 critérios (A-E): deficit em TODAS as 3 areas de CSI + >=2/4 CNR + desenvolvimento precoce + prejuízo funcional
- 3 níveis de gravidade baseados em suporte (não por cognição); "alto funcionamento" ELIMINADO
- Masking: 77% mulheres + 62% homens receberam >=1 diagnóstico incorreto; fenótipo feminino com interesses em pessoas e indicadores sutis
- AQ (cutoff>=26): sens 77-79%; RAADS-R (cutoff>=65/81): sens 92-97%; ADOS-2 M4: sens 91% mas não exclui TEA se negativo em alto masking

**Farmacoterapia por alvo (OE-H2) — AFI-201 a AFI-213:**
- **Irritabilidade:** risperidona e aripiprazol FDA-aprovados (SMD 1,07-1,18); **risco EPS RR 2,36 + ganho peso RR 2,40 aumentados em TEA** (Cochrane NMA 2025)
- **"Start low, go slow" universal** em TEA: 1/3-1/2 das doses habituais
- **Ansiedade:** buspirona/mirtazapina preferidas; ISRSs com risco de ativação comportamental
- **TDAH comorbido:** guanfacina ER 1ª linha (ES 1,67); ATX 2ª linha; metilfenidato com cautela
- **Depressão:** duloxetina/mirtazapina/bupropiona/vortioxetina antes de ISRSs
- **Burnout autístico ≠ TDM:** ativação comportamental pode PIORAR burnout; priorizar modificação ambiental
- TCC adaptada (SMD=-0,77) e MBSR (SMD=-0,84) com melhor evidência psicoterapiiéutica

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | ADOS-2 abaixo do cutoff não exclui TEA em alto masking | REF-289 vs. prática clínica | Documentar explicitamente no relatório do ADOS-2 quando houver alto masking |
| 2 | Burning rate de recuperação de TCC em atenção primária = 32,9% em autistas vs. 50% meta | REF-318 | Psicoterapias DEVEM ser adaptadas especificamente para TEA |
| 3 | Lurasidona provavelmente sem benefício para irritabilidade em TEA | REF-296 | Não recomendar lurasidona para irritabilidade em TEA |

#### Referências deste relatório
49 REF-IDs novos (REF-271 a REF-319).  
Duplicatas identificadas: Ref 1 = REF-059 (DSM-5-TR); Ref 40 = REF-259 (Strattera FDA label); Ref 31 = FDA Orange Book (não rastreado).


---

### RELATÓRIO 08 | OE-I1 · OE-I2
**Tema:** Transtorno de Personalidade Borderline (TPB) — Critérios, IVNS, DBT e Farmacoterapia  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_08_TPB.md`  
**Status:** ✅ Consolidado

#### Síntese das afirmações principais

**Critérios e diagnóstico (OE-I1) — AFI-214 a AFI-220:**
- TPB: >=5/9 critérios; modelo politético; padrão pervasivo de instabilidade; início vida adulta jovem
- AMPD (Seção III): complemento dimensional — modelo categorial é o padrão clínico
- Em adolescentes: válido a partir dos 12 anos; exige >=1 ano + não atribuível ao desenvolvimento normal
- **IVNS vs. SI:** intenção de morrer é a distinção operacional central; SI com plano → Gate P0
- Preditores de tentativa suicida em TPB (CLPS 10 anos): perturbação de identidade + abandono + vazio crônico
- **Escalada de IVNS:** frequência crescente, maior gravidade, múltiplos métodos, habituação à dor → capacidade adquirida → ação obrigatória MESMO SEM intenção suicida

**DBT e encaminhamento (OE-I2) — AFI-221 a AFI-224:**
- **DBT é a única psicoterapia com evidência suficiente** para TPB (Cochrane 75 RCTs, SMD=-0,52)
- 4 componentes padrão: pacote completo superior a versões parciais
- Dropout ~27% (favorável para população TPB)

**Farmacoterapia (OE-I2) — AFI-225 a AFI-229:**
- **Nenhum medicamento aprovado** para TPB; NICE contra sintomas centrais
- Crise aguda: prometazina/quetiapina; **NÃO benzodiazepinínicos**
- Melhor sintoma-alvo: topiramato (evidência alta) > lamotrigina > aripiprazol (hostilidade/agressividade)
- **Polifarmácia (80% dos pacientes):** anti-padrão explícito — descontinuar antes de iniciar novos
- Olanzapina: pode aumentar comportamentos autolesivos — evitar

**Adolescentes e monitoramento (OE-I2) — AFI-230 a AFI-232:**
- 3 ramos: especializado / diagnóstico provisório + GPM-A / watchful waiting a cada 4-6 semanas
- Informante colateral essencial: <1/3 dos pacientes com comportamento suicida expressa ao clínico

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | Cochrane 2022: nenhuma classe medicamentosa tem efeito consistente em desfechos primários de TPB | REF-339 vs. prática | Evidenciar claramente no protocolo que farmacoterapia é adjuvante e sintoma-dirigida |
| 2 | Lamotrigina: falhou em RCT robusto de 12 meses apesar de promessa inicial | REF-322 | Não prescrever como tratamento de manutenção sem reavaliação regular |
| 3 | VA/DoD 2024: DBT não reduz significativamente tentativas suicidas (sobrevivência) | REF-336 | Comunicar ao usuário que DBT reduz IVNS mas efeito em tentativas não é robusto |

#### Referências deste relatório
28 REF-IDs novos (REF-320 a REF-347).  
Duplicatas prováveis: Refs 1, 7–12 já registradas no REL-01 (Gate P0 — C-SSRS, VA/DoD, Joint Commission).

---

### RELATÓRIO 09 | OE-J1 · OE-J2
**Tema:** Transtornos Alimentares — Critérios, Internação e Realimentação  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_09_T_ALIMENTARES.md`  
**Status:** ✅ Consolidado

#### Síntese das afirmações principais

**Critérios DSM-5-TR (OE-J1) — AFI-233 a AFI-241:**
- AN: 3 critérios A/B/C; 2 subtipos (F50.01 restritivo / F50.02 purgativo); gravidade por IMC (leve>=17 / moderada 16-16,99 / grave 15-15,99 / extrema <15)
- BN: compulsão + compensatório inadequado >=1x/semana por 3 meses; gravidade por frequência/semana
- TCAP/BED: compulsão sem compensatório regular + >=3/5 características
- **Limiares de internação** integrados APA + NICE/MARSIPAN + CFM: IMC <=15 (APA/CFM) ou <14 (MARSIPAN); FC <40-50; PAS <80-90; temperatura <35,5°C; QTc >450; K+ <3,0; PO4 <0,5
- Adolescentes: NUNCAusar IMC absoluto; percentis CDC; <=75% IMC mediano ou <5º percentil
- **Internação involuntária:** 2 vias (médica = urgência suficiente; psiquiátrica = Lei 10.216/2001 + CFM 2.057/2013); documentação com notificação ao MP em 72h

**Complicações e realimentação (OE-J2) — AFI-242 a AFI-250:**
- **AN = maior mortalidade entre os transtornos psiquiátricos**; ~1/3 das mortes CV [REF-365]
- **Síndrome de realimentação (ASPEN 2020):** tiamina 100 mg EV ANTES de alimentar; eletrólitos a cada 12h por 3 dias; metas: K+ 2-4 mmol/kg/dia, PO4 0,3-0,6 mmol/kg/dia, Mg 0,2-0,4 mmol/kg/dia
- **Adultos:** 1.500-2.000 kcal/dia, progressao +33% a cada 1-2 dias
- **Adolescentes (HCR, Garber RCT 2020):** 2.200-2.600 kcal/dia sem maior risco de complicações
- Red-flags para internação: IMC <=15; FC <40; PAS <90; K+ <3,0; QTc >450/470; recusa alimentar; suicidalidade
- Farmacoterapia: fluoxetina 60 mg (BN, FDA); lisdexanfetamina (TCAP, FDA); TCC 1ª linha BN/TCAP; FBT para adolescentes com AN

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | APA: BMI <=15 como limiar vs. MARSIPAN: <14 | REF-349, REF-350 | Protocolo usa <=15 como trigger principal + alert adicional para <14 indicando cuidado urgente |
| 2 | Evidênìia crescente para HCR em adolescentes (iniciar mais agressivo) vs. prática conservadora brasileira | REF-370 vs. prática | HCR recomendada com monitoramento eletrolítico rigoroso; NÃO é experimental |
| 3 | Lei 10.216/2001: não menciona explicitamente TA; extrapolada da jurisprudência de internação psiquiátrica | REF-360, REF-361 | Documentação deve citar resolução CFM 2.057/2013 para embasamento complementar |

#### Referências deste relatório
25 REF-IDs novos (REF-348 a REF-372).  
Duplicata: Ref 2 = REF-059 (DSM-5-TR APA 2022).

---

### RELATÓRIO 10 | OE-K2 · OE-REF1 · OE-REF2
**Tema:** Interações Medicamentosas, Internação Involuntária e CAPS III vs. Hospitalação  
**Data de recebimento:** 2026-02-27  
**Arquivo fonte:** `research/OE_RELATORIO_10_INTERACOES_INTERNACAO_CAPS.md`  
**Status:** ✅ Consolidado

#### Síntese das afirmações principais

**4 DDIs críticas (OE-K2) — AFI-251 a AFI-258:**
- **Lítio + AINEs:** toxicidade em 1-7 dias; emergencial = descontinuar + HD se Li>2,5 mEq/L; monitoramento: Li 5-7 dias pós-AINE; idosos >65: alvo 0,6-0,8 mEq/L
- **Valproato + Lamotrigina:** VPA aumenta t½ LTG em +165%; iniciar LTG com metade da dose + titular no máximo q2semanas (exigência FDA); qualquer rash = EMERGENCIAL
- **Clozapina + BZDs:** colapso cardiorrespiratório + pneumonia aspirativa; evitar BZD 1 semana antes + 1 semana após início CLZ; se mantido: titular CLZ muito lentamente + inspeção diária delirium >=2 semanas
- **ISRSs + Tramadol:** SS por duplo mecanismo; diagnóstico pelos Critérios de Hunter; manejo: descontinuar + BZDs + ciproheptadina (caso grave)
- **Alertas Beers Criteria (>65):** lítio, BZDs, tramadol identificados como potencialmente inapropriados; Framework 4Ms; revisão de medicamentos anual

**Internação involuntária (OE-REF1) — AFI-259 a AFI-262:**
- Lei 10.216/2001: excepcional; 3 requisitos cumulativos
- Laudo médico circunstanciado (CFM 2.057/2013): 10 domínios obrigatórios incluindo CID-10/DSM-5 + MP notificado em 72h
- Duplo laudo privado→público: unidade receptora avalia independentemente e assume responsabilidade pelo MP
- CTC (Brissos 2017): cutoff 23,5 → sens 75% + espec 93,6%

**CAPS III vs. internação (OE-REF2) — AFI-263 a AFI-265:**
- Internação: SI com plano+intenção+acesso a meios; tentativa recente; sem capacidade de safety planning
- CAPS III: risco moderado-alto sem iminência imediata; crise intensiva até 14 dias
- **Pacientes Amil em CAPS III ou UPA → cobertura integral pelo SUS, sem autorização do plano**; retoma plano na alta
- CDS DDI: triagem antes de finalizar pedido; Lexicomp/Drugs.com/Epocrates; papel central do farmacêutico

#### Divergências ou lacunas identificadas

| # | Divergência | Fontes | Resolução |
|---|-------------|--------|----------|
| 1 | Severidade DDI pode variar entre bases (Lexicomp vs. Drugs.com vs. Epocrates) | REF-388 | Usar mais de uma base quando houver dúvida; preferir bulas FDA como fonte primária |
| 2 | CAPS III em SP: alguns requerem cadastro prévio na UBS para admissões rotineiras | REF-403, REF-404 | Para crises: contato direto com a unidade para confirmar disponibilidade |
| 3 | Janela inicial da SS com tramadol pode ser menor que 24h ou até dias | REF-380 | Monitorar ativa e continuamente nas primeiras 72h de uso concomitante |

#### Referências deste relatório
47 REF-IDs novos (REF-373 a REF-419).  
Duplicatas: Ref 25 = REF-360 (Brito/Ventura IJLP); Refs 38–42 = de REL-01 (Gate P0); Refs 8, 12, 13 = possíveis de REL-02/REL-05.

---

## GLOSSÁRIO DE SIGLAS

| Sigla | Significado |
|-------|-------------|
| APA | American Psychiatric Association |
| CANMAT | Canadian Network for Mood and Anxiety Treatments |
| CFM | Conselho Federal de Medicina |
| C-SSRS | Columbia Suicide Severity Rating Scale |
| CVV | Centro de Valorização da Vida (188) |
| DBT | Dialectical Behavior Therapy |
| DSM-5-TR | Diagnostic and Statistical Manual, 5th ed., Text Revision |
| NICE | National Institute for Health and Care Excellence |
| SPI | Safety Planning Intervention (Stanley-Brown) |
| TFG | Taxa de Filtração Glomerular |
| TAG | Transtorno de Ansiedade Generalizada |
| TAB | Transtorno Afetivo Bipolar |
| TCAP | Transtorno de Compulsão Alimentar Periódica |
| TDAH | Transtorno do Déficit de Atenção com Hiperatividade |
| TEA | Transtorno do Espectro Autista |
| TOC | Transtorno Obsessivo-Compulsivo |
| TEPT | Transtorno de Estresse Pós-Traumático |
| TPB | Transtorno de Personalidade Borderline |
| UPA | Unidade de Pronto Atendimento |
| VA/DoD | Department of Veterans Affairs / Department of Defense |

---

## LOG DE ATUALIZAÇÕES

| Data | Relatório | Quem atualizou | O que foi adicionado |
|------|-----------|----------------|----------------------|
| 2026-02-27 | — | Claude (setup inicial) | Estrutura do banco criada, índice e templates vazios |
| 2026-02-27 | REL-01 (OE-B1, B2, B3) | Antigravity | 26 REF-IDs, 25 AFI-IDs; Gate P0 consolidado; divergências registradas; OE-B1/B2/B3 → ✅ |
| 2026-02-27 | REL-02 (OE-K1, D2, D3) | Antigravity | 32 REF-IDs (REF-027–058), 34 AFI-IDs (AFI-026–059); tabela de monitoramento completa; alertas teratogenicidade valproato; OE-K1/D2/D3 → ✅ |
| 2026-02-27 | REL-03 (OE-D1, D4, D5) | Antigravity | 44 REF-IDs (REF-059–102), 34 AFI-IDs (AFI-060–093); critérios DSM-5-TR Humor, escalas BR, antidepressivos CANMAT 2023, DRT e MBC; OE-D1/D4/D5 → ✅ |
| 2026-02-27 | REL-04 (OE-E1, E2, E3, E4) | Antigravity | 62 REF-IDs (REF-103–164), 42 AFI-IDs (AFI-094–135); ansiedade/TOC/TEPT, exclusão orgânica, ISRS+QTc, burnout ICD-11, psicoterapias TEPT |
| 2026-02-27 | REL-05 (OE-F1, F2, F3, F4) | Antigravity | 58 REF-IDs (REF-165–222), 33 AFI-IDs (AFI-136–168); critérios esquizofrenia/esquizoafetivo/psicótico breve, FRS, escalas EPS, SNM, clozapina+ANVISA+CIVH+Porirua, NMA metabólica |
| 2026-02-27 | REL-06 (OE-G1, G2, G3, G4) | Antigravity | 48 REF-IDs (REF-223–270), 23 AFI-IDs (AFI-169–191); TDAH adulto DSM-5-TR, ASRS v1.1 (VPP 11,5%!), ECG risco-baseado, neuropsicológica condicional, ATX/guanfacina/bupropiona, protocolo TAB+TDAH e SUD+TDAH |
| 2026-02-27 | REL-07 (OE-H1, H2) | Antigravity | 49 REF-IDs (REF-271–319), 22 AFI-IDs (AFI-192–213); critérios TEA adulto DSM-5-TR, camouflaging + fenótipo feminino, AQ/RAADS-R/ADOS-2, farmacoterapia por alvo (risperidona/aripiprazol/guanfacina/ATX/mirtazapina), burnout autístico vs. TDM |
| 2026-02-27 | REL-08 (OE-I1, I2) | Antigravity | 28 REF-IDs (REF-320–347), 19 AFI-IDs (AFI-214–232); critérios TPB (9 critérios + AMPD), IVNS vs. SI + preditores CLPS, escalada IVNS, DBT Cochrane (75 RCTs SMD-0,52), NMA Gerolymos 2026 (topiramato/lamotrigina/aripiprazol), anti-padrão polifarmácia 80%, manejo adolescentes 3 ramos |
| 2026-02-27 | REL-09 (OE-J1, J2) | Antigravity | 25 REF-IDs (REF-348–372), 18 AFI-IDs (AFI-233–250); critérios AN/BN/BED DSM-5-TR, limiares de internação integrados (APA+MARSIPAN+CFM), internação involuntária (Lei 10.216+CFM 2.057/2013), complicações CV, realimentação ASPEN 2020, HCR vs. LCR (Garber RCT), red-flags ambulatoriais |
| 2026-02-27 | REL-10 (OE-K2, REF1, REF2) | Antigravity | 47 REF-IDs (REF-373–419), 16 AFI-IDs (AFI-251–266); 4 DDIs críticas (Li+AINE/VPA+LTG/CLZ+BZD/ISRS+Tramadol) com janelas+manejo+monitoramento, alertas Beers Criteria >65, lei 10.216+CFM 2.057/2013+duplo laudo, CTC Brissos, CAPS III vs. internação, cobertura SUS para pacientes Amil, Framework 4Ms |

> ✅ **BANCO DE EVIDÊNCIAS COMPLETO** | v2.0 | 419 REF-IDs | 266 AFI-IDs | 10/10 relatórios consolidados
