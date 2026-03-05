# Auditoria de Qualidade — Ficha de Ginecologia (Amil)
**Versao analisada:** `amil-ficha-ginecologia-v1.0.0.json`
**Versoes anteriores:** vdraft1, vdraft2
**Playbook de referencia:** `especialidades/ginecologia/playbooks/playbook_ginecologia_auditado.md`
**Sessao 007:** 2026-03-03 — analise inicial (vdraft1)
**Sessao 008:** 2026-03-03 — atualizacao (vdraft2)
**Sessao 011:** 2026-03-04 — auditoria v1.0.0 + feedback Gabriel
**Sessao 012:** 2026-03-04 — varredura end-to-end + 5 orientacoes adicionadas
**Status:** Criticos e moderados resolvidos. I3 e I4 aguardam decisao clinica.

---

## Estrutura do JSON (8 nos — identica desde vdraft1)

| No | Tipo | Questoes | Descricao |
|----|------|----------|-----------|
| N1 | custom | 9 | Triagem + rastreio historico |
| N2 | custom | 6 | Anamnese clinica |
| N3 | custom | 13 | Entrada de exames anteriores |
| C-ENF | conduct | 1 msg | Breakpoint enfermeiro |
| N4 | custom | 22 | Fluxo sintomatic |
| N5 | custom | 17 | Fluxo seguimento (resultados) |
| Summary | summary | 7 exprs | Processamento silencioso |
| C-MED | conduct | 39 ex / 23 med / 16 enc / 20 msg / **16 ori** | Conduta medica |

**Roteamento:** pacientes com queixa cursam N4 E N5; sem queixa vao direto a N5.

---

## Summary — clinicalExpressions (v1.0.0)

| Nome | Formula |
|------|---------|
| `alto_risco_mama` | `selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama', 'hfam_ca')` |
| `rastreio_cervical_habitual` | `(age >= 25) and (age <= 64) and ('hpv_nunca' in hpv or 'hpv_mais_5a' in hpv) and (histerectomia_previa is False)` |
| `rastreio_cervical_intensificado` | `(age >= 25) and (not 'hpv_menos_1a' in hpv) and ((imunocomprometimento is True) or ('nic2_mais' in hist_oncologico)) and (histerectomia_previa is False)` |
| `co_teste_papanicolau` | `((imunocomprometimento is True) and (age >= 25) and (not 'papa_menos_1a' in papa)) or (('nic2_mais' in hist_oncologico) and (histerectomia_previa is True) and (not 'papa_menos_1a' in papa))` |
| `trh_indicada` | `('svm_moderado' in svm_intensidade or 'svm_grave' in svm_intensidade) and ('sem_ci_trh' in contraindicacao_trh)` |
| `espessamento_endometrial_significativo` | `(('trouxe_usgtv' in exames_recentes) and ('usgtv_espessamento' in usgtv_achados)) or (((espessura_endometrial > 4 and not 'trh' in muc) or (espessura_endometrial > 8 and 'trh' in muc)) and ('menopausa' in status_menstrual))` |
| `poi_suspeita` | `(fsh_resultado > 25) and (age < 45)` |

---

## Resolucoes vdraft1 → vdraft2 → v1.0.0

| Achado | Status | O que mudou |
|--------|--------|------------|
| C1-antigo: `pos_coital` → colposcopia direta | **RESOLVIDO (vdraft2)** | Movido para citopatologia |
| C3-antigo: BI-RADS 3 → encaminhamento mastologia | **RESOLVIDO (vdraft2)** | Removido; BI-RADS 3 tratado por USG |
| C4-antigo: VitD para toda menopausa | **RESOLVIDO (vdraft2)** | Removido gate universal |
| C6-antigo: DXA sem FR <65 | **RESOLVIDO (vdraft2)** | tabagismo + etilismo adicionados |
| M1: HIV/HCV sem trigger por idade | **RESOLVIDO (vdraft2)** | Age gates adicionados |
| M2: Lipidograma sem trigger por idade | **RESOLVIDO (vdraft2)** | `age >= 40` adicionado |
| M3: Galactorreia sem entry point | **RESOLVIDO (vdraft2)** | queixa_mamaria incluido |
| C1-biopsia: Biopsia + CAF iguais | **RESOLVIDO (vdraft2)** | CAF so NIC3; biopsia NIC2+NIC3 |
| **C1** — espessamento formula OR quebrada | **RESOLVIDO (v1.0.0)** | Parenteses e menopausa gate restaurados |
| **I1** — LSIL → colposcopia imediata | **RESOLVIDO (v1.0.0, decisao clinica)** | Manter conservador — Gabriel+Dan |
| **I2** — `cito_nao_realizada` preselected | **RESOLVIDO (v1.0.0)** | Gabriel removeu preselected |
| Hemograma restritivo (feedback Gabriel) | **RESOLVIDO (v1.0.0)** | Ampliado: `not 'trouxe_lab' in exames_recentes` |
| Creatinina ausente (feedback Gabriel) | **RESOLVIDO (v1.0.0)** | Adicionada: `selected_any(comorbidades, 'has', 'dm')` |

---

## Achados — RESOLVIDOS EM v1.0.0 (verificados na sessao 012)

Varredura end-to-end linha a linha confirmou que TODOS os criticos e moderados estao corrigidos:

| Achado | Sessao identificada | Status v1.0.0 |
|--------|--------------------|--------------:|
| C2 — `espessamento_endometrial_significativo` bare (2 usos) | 011 | **RESOLVIDO** — busca retornou vazio |
| C3 — `trh_indicada` bare (4 usos) | 011 | **RESOLVIDO** — busca retornou vazio |
| C4 — `alto_risco_mama` bare (orientacao mama) | 011 | **RESOLVIDO** — `is True` confirmado |
| NEW-C1 — typo `seletec_any` na DXA | 011 | **RESOLVIDO** — `selected_any` correto |
| NEW-C2 — 3 clinicalExpressions bare na orientacao cervical | 011 | **RESOLVIDO** — `is True` confirmado |
| NEW-I2 — CID creatinina incorreto (E78.5) | 011 | **RESOLVIDO** — CID Z13.6 confirmado |

---

## Achados Pendentes — DECISAO CLINICA NECESSARIA

---

### I3 — `hpv_resultado_nd` sem conduta definida

A opcao `hpv_resultado_nd` ("Nao disponivel / nao lembra") existe em `hpv_resultado` mas nenhuma mensagem, conduta ou encaminhamento e gateada por ela. Medico sem orientacao.

**Sugestao:** Mensagem: "HPV positivo — resultado sem discriminacao de subtipo. Solicitar novo exame com genotipagem parcial para conduta especifica."

**Feedback Dan (sessao 011):** Pendente — nao discutido na 1:1.

---

### I4 — `diu_contraindicacao` coletado sem uso

A questao coleta CI ao DIU (gestacao, DIP ativa, distorcao cavitaria) mas nenhum item de conduta e gateado por ela. Sistema pode orientar insercao mesmo com gestacao declarada.

**Sugestao:** Mensagem de alerta: `selected_any(diu_contraindicacao, 'gestacao', 'dip_ativa') → "Insercao de DIU contraindicada no momento."`.

**Feedback Dan (sessao 011):** Pendente — nao discutido na 1:1.

---

### NEW-I1 — Hemograma com condicao excessivamente ampla (DECISAO CONSCIENTE)

**Condicao:** `(not 'trouxe_lab' in exames_recentes)` — aparece para toda paciente que nao trouxe exames.

**Playbook:** Hemograma como "rastreamento anual" (evidencia C).

**Decisao:** Gabriel optou por ampliar: "essa ficha ja vai mudar, galera vai chiar... melhor deixar mais aberta" (1:1, min 06:19).

**Acao:** Nenhuma correcao. Decisao documentada.

---

### NEW-I2 — Creatinina com CID incorreto

**Linha 4151:** CID `E78.5` (hiperlipidemia) para exame de creatinina. Deveria ser CID de avaliacao renal (ex: `N18.9` DRC ou `Z13.6` rastreio nefropatia).

**Impacto:** Administrativo — pode causar glosa. Nao afeta clinica.

---

### NEW-I3 — Variaveis `anemia_laboratorial` e `alt_tsh` no script mas nao no JSON

O script `audit_logic.py` espera `anemia_laboratorial` e `alt_tsh` como clinicalExpressions, mas elas nao existem na ficha de ginecologia. O script tem lista hardcoded que pode nao se aplicar a todas as fichas.

**Acao:** Verificar se essas variaveis sao necessarias para ginecologia. Se nao, remover da lista expected do script.

---

## Achados Informacionais

---

### F1 — `alto_risco_mama` incompleto (lesoes proliferativas)

**Formula atual:** `selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama')`

**Playbook lista alto risco tambem:** lesoes proliferativas (HLA, HDA, CLIS, CDIS), familiar 1o grau CA mama/ovario, risco >=20% Tyrer-Cuzick/IBIS.

Implementacao depende da adicao de `historia_familiar_ca` (ver sugestao abaixo).

---

### F2 — Testosterona / DHEA / 17-OHP: comportamento documentado

Disparam com `not 'sem_sinais' in hiperandrogenismo_sinais`. A questao so aparece em N4 quando ha queixa relevante. Fora do N4, variavel nula = exames nao disparam. Comportamento correto e intencional.

---

## Sugestao de Nova Pergunta — `historia_familiar_ca`

**Justificativa:** Canceres tem padroes hereditarios distintos. Ausencia de historia familiar na triagem e uma lacuna:
- CA mama/ovario: BRCA1/2, familiar 1o grau
- CA endometrio/colorretal: Sindrome de Lynch
- CA colo do utero: HPV-dependente, pouca hereditariedade

**Localizacao:** N1 (triagem/enfermagem), sempre visivel

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
```

**Impacto nas clinicalExpressions:**

`alto_risco_mama` expandiria para:
```
(selected_any(hist_oncologico, 'brca', 'rt_toracica', 'ca_mama'))
or (selected_any(historia_familiar_ca, 'fam_ca_mama', 'fam_ca_ovario', 'fam_brca_conhecido'))
```

Nova expression `lynch_suspeita`:
```
selected_any(historia_familiar_ca, 'fam_ca_endometrio', 'fam_ca_coloretal')
```

**Status:** NAO implementada na v1.0.0. Nao discutida na 1:1. Melhoria futura.

---

## Novas Orientacoes — Adicionadas na Sessao 012

5 orientacoes clinicas faltantes foram adicionadas ao C-MED (total: 11 → 16):

| # | Nome | Condicao |
|---|------|----------|
| 12 | Infertilidade e investigacao da fertilidade | `infertilidade_associada is True` |
| 13 | Incontinencia urinaria | `incontinencia_urinaria is True` |
| 14 | Insuficiencia ovariana prematura (POI) | `poi_suspeita is True` |
| 15 | Hepatites virais e HIV: sorologias alteradas | `('hiv_reagente' in hiv_resultado) or (...)` |
| 16 | Hiperandrogenismo e virilizacao | `not 'sem_sinais' in hiperandrogenismo_sinais` |

Cada orientacao tem narrativa (texto paciente) preenchida. `conteudo` mantido vazio (padrao das demais).

---

## Resultado de Scripts de Validacao (sessao 012)

**validate_json.py:** JSON valido — 8 nodes, 7 edges, 16 orientacoes
**audit_logic.py (sessao 011):** 0 criticos, 0 altos — medios confirmados como falsos positivos na sessao 012

---

## Resumo de Status (pos-sessao 012)

| # | Achado | Status | Acao pendente |
|---|--------|--------|--------------|
| C2 | `espessamento_endometrial_significativo` bare | **RESOLVIDO** | — |
| C3 | `trh_indicada` bare | **RESOLVIDO** | — |
| C4 | `alto_risco_mama` bare | **RESOLVIDO** | — |
| NEW-C1 | typo `seletec_any` DXA | **RESOLVIDO** | — |
| NEW-C2 | 3 bare orientacao cervical | **RESOLVIDO** | — |
| NEW-I2 | CID creatinina incorreto | **RESOLVIDO** | — |
| Orientacoes (5 topics) | Infertilidade, IU, POI, Hepatites, Hiperandrogenismo | **ADICIONADAS (s012)** | — |
| I3 | `hpv_resultado_nd` sem conduta | PENDENTE | Decisao clinica Dan |
| I4 | `diu_contraindicacao` sem uso | PENDENTE | Decisao clinica Dan |
| — | `historia_familiar_ca` em N1 | SUGESTAO | Implementar + expandir summary |

**Status atual: ZERO criticos, ZERO moderados tecnicos. Pendencias sao decisao clinica.**

---

## Log de Feedback — 1:1 Gabriel Paes (2026-03-04)

### Decisoes tomadas:
- **I1 (LSIL):** Manter colposcopia para LSIL — abordagem conservadora
- **I2 (preselected):** Gabriel removeu preselected de `cito_nao_realizada`
- **Hemograma:** Ampliado para rastreamento universal (sem trouxe_lab)
- **Creatinina:** Adicionada para HAS/DM
- **HPV condicional:** Gabriel sugere tirar condicional da pergunta de resultado HPV (nao pre-marcada)

### Proximos passos acordados:
1. Gabriel faz ultima rodada de testes → salva rascunho → avisa Dan
2. Dan aplica correcoes is True + typo DXA + CID
3. Dan e Gabriel gravam Loom videos (cenarios clinicos) para modelador Paulo
4. Proximas especialidades: Pediatria, depois Psiquiatria
5. Skills environment: alinhar com Humberto, deadline fim de Abril

---

## Escopo excluido desta auditoria (decisoes ja tomadas)
- `trouxe_exames` / `age` como campos base
- Formato geral de queixa_principal com `nenhuma_queixa`
- Histerectomia_previa como proxy de menopausa cirurgica (conservador, intencional)
- Biopsia para NIC2 + NIC3 (biopsia confirma antes de CAF) — aceitavel
- Hemograma amplo — decisao consciente do Gabriel

---

*Sessao 007: analise inicial vdraft1 — Claude Code 2026-03-03*
*Sessao 008: atualizacao vdraft2 + DOCX + feedback Dan — Claude Code 2026-03-03*
*Sessao 011: auditoria v1.0.0 + feedback 1:1 Gabriel — Claude Code 2026-03-04*
*Sessao 012: varredura end-to-end, confirmacao correcoes, +5 orientacoes — Claude Code 2026-03-04*
*Proxima acao: Dan decide I3 (hpv_resultado_nd) e I4 (diu_contraindicacao)*
