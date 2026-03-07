# session_014.md — Fase 4 Psiquiatria: Completação do JSON

**Data:** 2026-03-07
**Fase:** Fase 4 — Codificação JSON (conclusão)
**Especialidade:** Psiquiatria
**Commits:** `9d33d01`, `459b6b4`

---

## Resumo da sessão

Esta sessão completou a Fase 4 (codificação JSON) da especialidade de Psiquiatria,
retomando do estado pendente da sessão anterior (script inject_no4_no5.py já escrito,
aguardando execução).

---

## Sequência de ações

### 1. Execução de inject_no4_no5.py

Script escrito na sessão anterior foi executado com sucesso:
- Nó 4 (`node-psiq-04-diagnostico`): 30 questões em 6 blocos diagnósticos
- Nó 5 (`node-psiq-05-farmacos`): 17 questões de monitoramento farmacológico
- Validação: 260 iids únicos, 0 erros

**Commit:** `9d33d01` — `feat(psiquiatria): inject Nós 4 + 5`

### 2. Inspecção da estrutura de nó Conduta

Leitura de referências (cardiologia worktree, ginecologia) para confirmar:
- Tipo correto: `"conduct"` (não `"custom"` como constava no paper design)
- Chave do conteúdo: `condutaDataNode` com subcampos `exame`, `encaminhamento`,
  `medicamento`, `mensagem`, `orientacao`
- Estrutura de `exame`: 15+ campos incluindo `codigo[{iid, sistema, codigo}]`,
  `tipoAmostra`, `programacaoDosagem`, etc.
- Estrutura de `encaminhamento`: `indicacao`, `especialidadeTexto`, `categorias`
- Estrutura de `mensagem` (alertas): `id`, `nome`, `condicao`, `conteudo`, `observacao`

### 3. Escrita e execução de inject_no6.py

Nó 6 completo produzido com base na Parte 4 do paper design:

**Alertas (mensagem) — 9 itens:**
1. ⛔ Gate P0 — Risco Alto: Internação
2. ⚠️ Gate P0 — Risco Intermediário: SPI
3. ⛔ Clozapina ANC <1.000
4. ⚠️ VPA + MIE aconselhamento
5. ⚠️ TAB + AD sem estabilizador
6. ⛔ AN sinais de alarme
7. ⚠️ Clozapina — miocardite
8. ⚠️ Toxicidade de lítio
9. ℹ️ Primeiro episódio psicótico

**Exames (exame) — 25 itens com TUSS:**
- Grupo lítio: litemia, creatinina, TSH, cálcio, ureia
- Grupo VPA: ácido valpróico, ALT/TGP, AST/TGO, amônia
- Grupo CBZ: carbamazepina, sódio, HLA-B*1502 (sem TUSS — pendente)
- Hemograma (cobre clozapina/CBZ/VPA)
- Grupo AP atípicos: glicemia, HbA1c, colesterol, triglicerídeos, prolactina
- Beta-HCG (MIE + lítio/VPA)
- ECG 12 derivações
- Grupo 1º episódio: hemograma, TSH, VDRL, HIV, troponina+PCR (sem TUSS)

**Encaminhamentos — 13 itens:**
ERP-TOC, EMDR-TEPT, TCD-TPB, TCC, neuropsicólogo, nutricionista, SAMU,
CAPS-II, CAPS-AD, neurologia, cardiologia, med. trabalho, endocrinologia

**Medicamentos — 9 itens:**
Escitalopram, sertralina, fluoxetina, lítio, lamotrigina, metilfenidato,
lisdexanfetamina, biperideno, propranolol

### 4. clinicalExpressions — Nó 1

5 expressões clínicas adicionadas ao Nó 1 (invariante do plano):
- `estabilizadores_humor` — lítio, VPA, CBZ, lamotrigina
- `antipsicóticos_atipicos` — clozapina, olanzapina, quetiapina, risperidona, aripiprazol
- `exige_ecg` — TCA ou ecg_indicado_psico ativo
- `sexo_feminino_ie` — female + age 12–55
- `monitoramento_metabolico_ap` — APs de alto risco metabólico

**Commit:** `459b6b4` — `feat(psiquiatria): inject Nó 6 + clinicalExpressions`

### 5. Validação estrutural final

```
JSON VALIDO
  Nodes: 6, Edges: 5
  Total questões: 83
  clinicalExpressions (Nó 1): 5
  Nó 6 conduta: exame=25, medicamento=9, encaminhamento=13, mensagem=9
  Question iids: 260 únicos: 260
  Validação: PASSOU — 0 erros
```

### 6. QA clínico — 3 perfis

| Perfil | Resultado |
|--------|-----------|
| Alto risco suicida | Alerta P0 ativo, SAMU encaminhado, ISRS disponível ✅ |
| TDM leve (sem psicofármaco) | Sem exames, ISRS disponível, TCC encaminhado ✅ |
| TAB + lítio + VPA (mulher fértil) | Alerta VPA+MIE, 9 exames de monitoramento, Beta-HCG, lítio/lamotrigina ✅ |

---

## Artefatos produzidos

| Arquivo | Status |
|---------|--------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json` | ✅ completo (6 nodes) |
| `scripts/inject_no4_no5.py` | ✅ commitado |
| `scripts/inject_no6.py` | ✅ commitado |
| `HANDOFF.md` | ✅ atualizado |
| `ESTADO.md` | ✅ atualizado |

---

## Pendências para Fase 5

- TUSS de HLA-B*1502: campo `codigo: []` — pendente codificação pela equipe ANS
- TUSS de Troponina+PCR: campo `codigo: []` — pendente codificação institucional
- Revisão clínica completa das condicionais pelo usuário
- Promoção de versão `1.0.0-draft` → `1.0.0` após aprovação

---

## Próxima sessão recomendada

Fase 5 — QA final:
1. Abrir JSON no ambiente de preview Daktus
2. Percorrer os 3 perfis de paciente no sistema
3. Ajustar condicionais ou conteúdo conforme feedback
4. Aprovar e promover versão
