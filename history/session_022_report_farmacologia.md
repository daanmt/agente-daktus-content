# Relatório Farmacológico — session_022
**Data:** 2026-03-10
**Artefato:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.2.json`
**Script:** `scripts/patch_vdraft2_to_v022.py`

---

## Resumo executivo

| Métrica | vdraft (2) | v0.2.2 |
|---------|-----------|--------|
| Medicamentos | 16 | **28** |
| Schema canônico (posologia/mensagemMedico/via) | 9/16 | **28/28 ✅** |
| `nomeMed` preenchido | 13/16 | **28/28 ✅** |
| `condicionalMedicamento: "domiciliar"` | 15/16 | **28/28 ✅** |
| MEVO preenchido | 10/16 | **19/28** |
| MEVO sem código (fora catálogo Amil) | 6/16 | **9/28** |
| UUIDs canônicos (v4) | 13/16 | **28/28 ✅** |
| BLOQUEANTES estruturais | 0 | **0 ✅** |
| `metadata.version` | draft | **0.2.2 ✅** |

---

## Bugs corrigidos

### BUG 1 — Schema inconsistente: `conteudo` → `posologia`/`mensagemMedico`/`via`

6 itens de antipsicóticos atípicos usavam campos inválidos (`conteudo`/`observacao`) em vez do schema canônico. Corrigidos com conteúdo dose-específico por item:

| Medicamento | Ação |
|-------------|------|
| Quetiapina 50 mg | `conteudo` → `posologia` (50 mg/noite) + `mensagemMedico` (titulação/monitoramento) |
| Quetiapina 100 mg | `conteudo` → `posologia` (100 mg/noite) + `mensagemMedico` |
| Olanzapina 5 mg | `conteudo` → `posologia` (5 mg/noite) + `mensagemMedico` |
| Olanzapina 10 mg | `conteudo` → `posologia` (10 mg/noite) + `mensagemMedico` |
| Risperidona 1 mg | `conteudo` → `posologia` (1 mg/dia) + `mensagemMedico` |
| Risperidona 2 mg | `conteudo` → `posologia` (2 mg/dia) + `mensagemMedico` |

### BUG 2 — Aripiprazol: 1 item com 2 MEVOs → split em 2 itens canônicos

O item `Aripiprazol 10 mg / 15 mg` tinha `codigo: [MEVO 35461, MEVO 32613]` — estrutura inválida (um array de código por dose, não por fármaco). Substituído por:

- `Aripiprazol 10 mg` → MEVO 35461, `condicionalMedicamento: "domiciliar"` ✅
- `Aripiprazol 15 mg` → MEVO 32613, `condicionalMedicamento: "domiciliar"` ✅

### BUG 3 — `nomeMed` ausente

`nomeMed` ausente em Quetiapina 50 mg e Quetiapina 100 mg (cobertos pelo BUG 1). Aripiprazol coberto pelo BUG 2. Todos os 28 itens agora têm `nomeMed` ✅

### BUG 4 — IDs não-canônicos

3 IDs gerados em edição manual substituídos por UUID v4 válidos:

| ID original | Medicamento | UUID v4 gerado |
|-------------|-------------|----------------|
| `cf9ooj5a` | Quetiapina 100 mg | gerado pelo script |
| `5p6fdllf` | Olanzapina 10 mg | gerado pelo script |
| `0k5sfwqn` | Risperidona 2 mg | gerado pelo script |

---

## Fármacos adicionados (11)

### Antidepressivos

| Fármaco | Classe | MEVO | Condição DSL |
|---------|--------|------|--------------|
| Venlafaxina XR 75mg | IRSN | **42348** (37,5mg LP) | TDM/TAG/TEPT + depressão leve/moderada/grave |
| Duloxetina 60mg | IRSN | **35537** (60mg) | TDM/TAG + depressão moderada/grave |
| Bupropiona 150mg | IRND | `[]` | TDM/TDAH + depressão leve/moderada/grave |
| Mirtazapina 15mg | NaSSA | `[]` | TDM + depressão moderada/grave |
| Paroxetina 20mg | ISRS | **8751** (20mg) | TEPT/pânico/fobia social |

### Estabilizadores de humor

| Fármaco | Classe | MEVO | Condição DSL |
|---------|--------|------|--------------|
| Valproato de sódio 500mg | Estabilizador | **42471** (500mg) | TAB + mania/hipomania/eutimia |
| Carbamazepina 200mg | Estabilizador | `[]` | TAB + mania/hipomania |

### Antipsicóticos

| Fármaco | Classe | MEVO | Condição DSL |
|---------|--------|------|--------------|
| Haloperidol 5mg | Típico | **14996** (5mg) | Mania ou esquizofrenia |
| Clozapina 25mg | Atípico refratário | `[]` | `esquizofrenia_refrataria is True` |

### TDAH e Ansiolítico

| Fármaco | Classe | MEVO | Condição DSL |
|---------|--------|------|--------------|
| Atomoxetina 40mg | Não estimulante | `[]` | TDAH |
| Clonazepam 0,5mg | BZD | **40857** (2mg ref.) | TAG/pânico/fobia social |

---

## Pontos em aberto — requerem ação da equipe Amil/clínica

### 1. MEVO ausente em 9 medicamentos

Medicamentos presentes em v0.2.2 sem código MEVO no catálogo `referencia/Mevo..xlsx`:

| Medicamento | Status | Ação recomendada |
|-------------|--------|-----------------|
| Metilfenidato LP 18mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Lisdexanfetamina 20mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Biperideno 2mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Propranolol 20mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Bupropiona 150mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Mirtazapina 15mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Carbamazepina 200mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Clozapina 25mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |
| Atomoxetina 40mg | Não encontrado no Mevo..xlsx | Confirmar cobertura com Amil |

### 2. Escitalopram 10mg — código MEVO não verificado

O usuário inseriu manualmente `MEVO: 20945` em vdraft. Este código **não foi encontrado no `Mevo..xlsx`** (a planilha lista 20mg com código diferente).

- **Risco:** O código 20945 pode ser inválido ou de outra dosagem.
- **Ação:** Confirmar com equipe Amil se MEVO 20945 corresponde a Escitalopram 10mg.

### 3. Venlafaxina XR — apenas 37,5mg no catálogo Amil

O catálogo `Mevo..xlsx` tem apenas `Cloridrato de venlafaxina 37,5mg LP` (MEVO 42348). A ficha prescreve 75mg/dia.

- **Código usado:** 42348 (37,5mg LP) como referência de fármaco.
- **Posologia declarada:** 75 mg/dia = 2 cápsulas de 37,5 mg.
- **Ação:** Confirmar com Amil se a dispensação de 75mg é coberta com o código 42348 (quantidade × 2) ou se existe código específico para 75mg não constante na planilha.

### 4. Clonazepam — dose catalogo ≠ dose prescrita

Catálogo Amil lista Clonazepam 2mg (MEVO 40857). A ficha prescreve 0,5mg como dose inicial.

- **Código usado:** 40857 (2mg comprimido) como referência de fármaco.
- **Ação:** Confirmar com Amil se existe MEVO para Clonazepam 0,5mg ou se o código 40857 cobre qualquer apresentação do fármaco.

### 5. Medicamentos de 2ª linha não incluídos (fora do catálogo Amil)

Os seguintes fármacos de 2ª/3ª linha não foram incluídos em v0.2.2 por ausência no catálogo Mevo/Amil:

| Fármaco | Indicação | Status Mevo |
|---------|-----------|-------------|
| Fluvoxamina | TOC refratário | Ausente no Mevo..xlsx |
| Clomipramina | TOC grave | Ausente no Mevo..xlsx |
| Guanfacina XR | TDAH alternativo | Ausente no Mevo..xlsx |
| Prazosina | TEPT (pesadelos) | Ausente no Mevo..xlsx |
| Buspirona | TAG adjuvante | Ausente no Mevo..xlsx |

**Proposta:** Incluir em v0.3 sem código MEVO, com nota clínica no `mensagemMedico`, quando clinicamente indicado.

### 6. Conflito de prescrição — Bupropiona + Estimulantes em TDAH+TDM comórbido

A condição DSL da Bupropiona inclui `'tdah' in diagnostico_ativo`, que pode gerar prescrições simultâneas de Bupropiona + Metilfenidato/Lisdexanfetamina no mesmo paciente.

- **Risco clínico:** O médico deve avaliar a sequência terapêutica; combinação pode ser válida mas exige atenção.
- **Proposta:** Avaliar se a condição de Bupropiona deve ser restrita a `TDM isolado` sem TDAH ativo, ou manter com orientação no `mensagemMedico`.

### 7. Valproato — alerta gestante obrigatório não está no nó de conduta

A mensagem do `mensagemMedico` do Valproato menciona "CONTRAINDICADO na gestação (alerta GESTANTE+VPA obrigatório)". O alerta automatizado para gestantes em uso de Valproato (presente em v0.2.1 como alerta de conduta) deve ser validado no QA clínico.

- **Perfil crítico a testar:** Mulher grávida em uso de valproato → confirmar que o alerta aparece.

---

## Verificação MEVO adicional (session_022)

| Pesquisa | Resultado |
|----------|-----------|
| Venlafaxina 75mg LP no Mevo..xlsx | ❌ Apenas 37,5mg LP (MEVO 42348) encontrado |
| Paroxetina 20mg no Mevo..xlsx | ✅ MEVO 8751 confirmado |
| Duloxetina 60mg no Mevo..xlsx | ✅ MEVO 35537 confirmado |
| Valproato de sódio 500mg no Mevo..xlsx | ✅ MEVO 42471 confirmado |
| Haloperidol 5mg no Mevo..xlsx | ✅ MEVO 14996 confirmado |
| Clonazepam 2mg no Mevo..xlsx | ✅ MEVO 40857 confirmado (2mg; 0,5mg pendente) |

---

## Próximos passos

1. **Confirmar 9 MEVOs ausentes** com equipe Amil (ver tabela "Pontos em aberto #1")
2. **Confirmar Escitalopram MEVO 20945** — código inserido manualmente pelo usuário, não verificado no Mevo..xlsx
3. **Confirmar Venlafaxina 75mg** — cobertura com código 42348 ou código específico
4. **Confirmar Clonazepam 0,5mg** — código específico ou uso do 40857
5. **QA clínico de v0.2.2** no preview Daktus (3 perfis críticos de v0.2.1 + novo perfil gestante+VPA):
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta GESTANTE+VPA
   - Esquizofrenia refratária → indicação clozapina + alerta hemograma
   - TDAH com TDM → verificar prescrições simultâneas (Metilfenidato + Bupropiona)
6. **v0.3** — adicionar fármacos de 2ª linha sem MEVO (Fluvoxamina, Clomipramina, etc.) + encaminhamentos faltantes (Infectologia, Psiquiatria terciária)
7. **Promover para v1.0.0** após QA clínico aprovado
