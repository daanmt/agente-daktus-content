# session_022.md — Correção estrutural + fármacos faltantes → v0.2.2

**Data:** 2026-03-10
**Fase:** Fase 5 — QA iterativo
**Especialidade:** Psiquiatria
**Base:** `C:\Users\daanm\Downloads\amil-ficha_psiquiatria-vdraft (2).json` (revisão manual do usuário sobre v0.2.1)
**Output:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.2.json`

---

## Resumo da sessão

O usuário revisou manualmente o nó de conduta de v0.2.1, dividindo os antipsicóticos atípicos por dose (Quetiapina 50/100mg, Olanzapina 5/10mg, Risperidona 1/2mg) e adicionou MEVOs individuais por item. A sessão realizou benchmarking com a ficha de ginecologia, identificou 4 grupos de bugs estruturais, corrigiu todos, e adicionou 11 fármacos essenciais do playbook ausentes.

**Resultado:** 0 BLOQUEANTES ✅ | 28 medicamentos ✅ | Schema 28/28 canônico ✅ | `nomeMed` 28/28 ✅ | `condicionalMedicamento` 28/28 ✅ | MEVO 19/28 (9 fora do catálogo Amil) | metadata.version = "0.2.2" ✅

---

## Diagnóstico de entrada (vdraft 2)

| Bug | Itens afetados | Descrição |
|-----|---------------|-----------|
| BUG 1 | 6 itens | `conteudo`/`observacao` em vez de `posologia`/`mensagemMedico`/`via` |
| BUG 2 | 1 item | Aripiprazol com 2 MEVOs num array = doses agrupadas (inválido) |
| BUG 3 | 2 itens | `nomeMed` ausente em Quetiapina 50/100mg |
| BUG 4 | 3 itens | IDs não-canônicos: `cf9ooj5a`, `5p6fdllf`, `0k5sfwqn` |

---

## Bugs corrigidos

### BUG 1 — Schema normalization (6 itens)

| Medicamento | De | Para |
|------------|-----|------|
| Quetiapina 50 mg | `conteudo` + `observacao` | `posologia` (50mg/noite) + `mensagemMedico` + `via: "oral"` |
| Quetiapina 100 mg | `conteudo` + `observacao` | `posologia` (100mg/noite) + `mensagemMedico` + `via: "oral"` |
| Olanzapina 5 mg | `conteudo` + `observacao` | `posologia` (5mg/noite) + `mensagemMedico` + `via: "oral"` |
| Olanzapina 10 mg | `conteudo` + `observacao` | `posologia` (10mg/noite) + `mensagemMedico` + `via: "oral"` |
| Risperidona 1 mg | `conteudo` + `observacao` | `posologia` (1mg/dia) + `mensagemMedico` + `via: "oral"` |
| Risperidona 2 mg | `conteudo` + `observacao` | `posologia` (2mg/dia) + `mensagemMedico` + `via: "oral"` |

### BUG 2 — Aripiprazol split

`Aripiprazol 10 mg / 15 mg` (1 item, 2 MEVOs) → substituído por:
- `Aripiprazol 10 mg`: MEVO 35461, schema completo, `condicionalMedicamento: "domiciliar"` ✅
- `Aripiprazol 15 mg`: MEVO 32613, schema completo, `condicionalMedicamento: "domiciliar"` ✅

### BUG 3 — `nomeMed` ausente

`nomeMed` preenchido em Quetiapina 50 mg e 100 mg (coberto pela correção do BUG 1).

### BUG 4 — UUIDs não-canônicos

| ID original | Medicamento | Ação |
|------------|-------------|------|
| `cf9ooj5a` | Quetiapina 100 mg | Substituído por UUID v4 |
| `5p6fdllf` | Olanzapina 10 mg | Substituído por UUID v4 |
| `0k5sfwqn` | Risperidona 2 mg | Substituído por UUID v4 |

---

## Fármacos adicionados (11)

| Fármaco | Classe | MEVO | Condição DSL |
|---------|--------|------|--------------|
| Venlafaxina XR 75mg | IRSN | 42348 (37,5mg LP) | TDM/TAG/TEPT + depressão |
| Duloxetina 60mg | IRSN | 35537 | TDM/TAG + depressão moderada/grave |
| Bupropiona 150mg | IRND | `[]` | TDM/TDAH + depressão |
| Mirtazapina 15mg | NaSSA | `[]` | TDM + depressão moderada/grave |
| Paroxetina 20mg | ISRS | 8751 | TEPT/pânico/fobia social |
| Valproato de sódio 500mg | Estabilizador | 42471 | TAB + mania/hipomania/eutimia |
| Carbamazepina 200mg | Estabilizador | `[]` | TAB + mania/hipomania |
| Haloperidol 5mg | Antipsicótico típico | 14996 | Mania ou esquizofrenia |
| Clozapina 25mg | Antipsicótico refratário | `[]` | `esquizofrenia_refrataria is True` |
| Atomoxetina 40mg | Não estimulante TDAH | `[]` | TDAH |
| Clonazepam 0,5mg | BZD | 40857 (2mg ref.) | TAG/pânico/fobia social |

---

## Verificação MEVO — Venlafaxina

Pesquisa no `referencia/Mevo..xlsx` (coluna "Nome Medicamento"): apenas `Cloridrato de venlafaxina 37,5mg LP` (MEVO 42348). Sem versão 75mg no catálogo. Posologia declara: "75 mg/dia = 2 cápsulas de 37,5mg".

---

## Resultado final — v0.2.2

```
Perguntas:          37 (inalterado desde v0.2.1)
Medicamentos:       28 (era 16 em vdraft → +12)
Schema canônico:    28/28 ✅
nomeMed:            28/28 ✅
condicionalMed:     28/28 ✅
posologia:          28/28 ✅
MEVO preenchido:    19/28
MEVO vazio:          9/28 (Metilfenidato LP, Lisdexanfetamina, Biperideno, Propranolol,
                           Bupropiona, Mirtazapina, Carbamazepina, Clozapina, Atomoxetina)
UUIDs canônicos:    28/28 ✅
BLOQUEANTES:         0 ✅
Nodes:               9 | Edges: 8 | IIDs: 94
metadata.version:   "0.2.2" ✅
```

---

## Artefatos produzidos

| Arquivo | Ação |
|---------|------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.2.json` | criado — v0.2.2 final |
| `scripts/patch_vdraft2_to_v022.py` | criado — script de patch completo |
| `history/session_022_report_farmacologia.md` | criado — relatório com 7 pontos em aberto |
| `HANDOFF.md` | atualizado — session_022 documentada, artefato ativo = v0.2.2 |
| `ESTADO.md` | atualizado — session_022 como última sessão integrada |
| `history/session_022.md` | criado — este arquivo |

---

## Próxima sessão recomendada

1. **QA clínico de v0.2.2** no preview Daktus — 4 perfis críticos:
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta GESTANTE+VPA + Valproato como prescrição
   - Esquizofrenia refratária → indicação clozapina
   - TDAH com TDM comórbido → prescrições simultâneas (Metilfenidato + Bupropiona)
2. **Confirmar 9 MEVOs ausentes** com equipe Amil
3. **Confirmar Escitalopram MEVO 20945** — inserido manualmente pelo usuário, não verificado
4. **Confirmar Venlafaxina** — cobertura com código 42348 (37,5mg × 2) ou código específico 75mg
5. **v0.3** — fármacos de 2ª linha (Fluvoxamina, Clomipramina, Guanfacina XR, Prazosina, Buspirona) + encaminhamentos (Infectologia, Psiquiatria terciária)
6. Promover para v1.0.0 após QA clínico aprovado
