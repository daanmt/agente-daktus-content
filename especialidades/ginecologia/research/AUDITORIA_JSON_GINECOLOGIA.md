# Auditoria de Qualidade — Ficha de Ginecologia (Amil)
**Versao analisada:** `amil-ficha-ginecologia-v1.0.0.json`
**Versoes anteriores:** vdraft1, vdraft2
**Playbook de referencia:** `especialidades/ginecologia/playbooks/playbook_ginecologia_auditado.md`
**Sessao 007:** 2026-03-03 — analise inicial (vdraft1)
**Sessao 008:** 2026-03-03 — atualizacao (vdraft2)
**Sessao 011:** 2026-03-04 — auditoria v1.0.0 + feedback Gabriel
**Status:** Correcoes criticas pendentes (is True + typo DXA)

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
| C-MED | conduct | 38 ex / 23 med / 17 enc / 20 msg | Conduta medica |

**Roteamento:** pacientes com queixa cursam N4 E N5; sem queixa vao direto a N5.

---

## Summary — clinicalExpressions (v1.0.0)

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

## Achados Pendentes — CRITICOS

---

### C2 — `espessamento_endometrial_significativo`: usos sem `is True` (PARCIAL)

**Corrigido:**
- Histeroscopia (L3050): `espessamento_endometrial_significativo is True` ✓

**Ainda bare:**
- Encaminhamento GO Oncologico (L5297): `('pos_menopausa' in sua_padrao) and espessamento_endometrial_significativo`
- Mensagem alerta espessura (L5700): `espessamento_endometrial_significativo`

**Correcao:** Adicionar `is True` nos dois usos bare.

**Feedback Dan (sessao 011):** Identificado e reportado ao Gabriel na 1:1. Gabriel confirmou que vai corrigir.

---

### C3 — `trh_indicada`: usos sem `is True` (PARCIAL)

**Corrigido:**
- Progesterona micronizada (L5087): `(trh_indicada is True) and (histerectomia_previa is False)` ✓

**Ainda bare (4 usos):**
- Estradiol 1mg (L5056): `trh_indicada`
- Estradiol adesivo (L5118): `trh_indicada and ('obesidade' in comorbidades or ...)`
- Tibolona (L5180): `trh_indicada\nand (not 'ca_mama_pessoal' in ...)`
- Mensagem TRH janela (L5710): `trh_indicada`

**Correcao:** Substituir `trh_indicada` por `trh_indicada is True` em todos. Remover `\n` da condicao da tibolona.

**Feedback Dan (sessao 011):** Identificado na 1:1 com Gabriel. Pendente correcao.

---

### C4 — `alto_risco_mama`: usos sem `is True` (PARCIAL)

**Corrigido:**
- Mamografia (L2842): `alto_risco_mama is True` ✓
- USG mama (L2894): `alto_risco_mama is True` ✓
- RM mama (L2946): `(alto_risco_mama is True)` ✓

**Ainda bare (1 uso):**
- Orientacao rastreamento mama (L2438): `(age >= 40 and age <= 74) or 'queixa_mamaria' in queixa_principal or alto_risco_mama`

**Correcao:** `alto_risco_mama is True`

**Feedback Dan (sessao 011):** Gabriel ja corrigiu os exames; falta a orientacao.

---

### NEW-C1 — TYPO: `seletec_any` na condicao de DXA

**Linha 3154 — Densitometria ossea:**
```
...or seletec_any(historia_social, 'tabagismo', 'etilismo_pesado')
```

**Impacto:** `seletec_any` nao e funcao valida. Mulher pos-menopausada <65 com tabagismo ou etilismo pesado NAO tera DXA solicitada. O playbook lista ambos como fatores de risco.

**Correcao:** `selected_any(historia_social, 'tabagismo', 'etilismo_pesado')`

**Feedback Dan (sessao 011):** Bug novo descoberto na v1.0.0. Prioridade critica.

---

### NEW-C2 — clinicalExpressions bare na orientacao cervical

**Linha 2429 — Orientacao "Rastreamento cervical (HPV)":**
```
(rastreio_cervical_habitual) or (rastreio_cervical_intensificado) or ('nic2_mais' in hist_oncologico and ...) or (co_teste_papanicolau)
```

Tres clinicalExpressions bare (sem `is True`). Os exames correspondentes (HPV DNA, Citopatologia) usam `is True` corretamente — problema isolado na orientacao.

**Correcao:** Adicionar `is True` nas tres.

---

## Achados Pendentes — IMPORTANTES

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

## Resultado de Scripts de Validacao (sessao 011)

**validate_json.py:** ✓ JSON valido — 8 nodes, 7 edges
**audit_logic.py:** 0 criticos, 0 altos, 5 medios (2 variaveis esperadas nao definidas + 3 numeric guards)

---

## Resumo de Prioridades para Correcao (v1.0.0 → v1.0.1)

| # | Achado | Severidade | Acao |
|---|--------|-----------|------|
| NEW-C1 | `seletec_any` typo na DXA | CRITICO | Corrigir para `selected_any` |
| C2 | `espessamento_endometrial_significativo` bare (2 usos) | CRITICO | Adicionar `is True` |
| C3 | `trh_indicada` bare (4 usos) | CRITICO | Adicionar `is True` |
| C4 | `alto_risco_mama` bare (1 uso — orientacao) | CRITICO | Adicionar `is True` |
| NEW-C2 | 3 clinicalExpressions bare na orientacao cervical | MODERADO | Adicionar `is True` |
| NEW-I2 | CID creatinina incorreto (E78.5) | MODERADO | Alterar para CID renal |
| I3 | `hpv_resultado_nd` sem conduta | MODERADO | Adicionar mensagem |
| I4 | `diu_contraindicacao` sem uso | BAIXO | Adicionar alerta CI absoluta |
| — | `historia_familiar_ca` em N1 | SUGESTAO | Implementar + expandir summary |

**Total: 8 criticos (is True + typo), 3 moderados, 2 baixos/sugestao**

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
*Proxima acao: Dan aplica 8 correcoes criticas + 3 moderadas na plataforma Daktus*
