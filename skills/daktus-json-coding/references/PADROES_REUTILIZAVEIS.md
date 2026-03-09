# Padrões Arquiteturais Reutilizáveis

> Consolidado de `tools/PADROES_ARQUITETURA_JSON.md` Part I + `tools/GUIA_DESIGN_UX.md` §4.
> Padrões extraídos de Reumatologia, Cardiologia e Ginecologia.

---

## 1. Alias de Classe Farmacológica

Em vez de listar medicamentos individuais em cada condicional, criar `clinicalExpressions` por classe terapêutica.

```json
{ "name": "estabilizadores_humor", "formula": "selected_any(medicamentos_em_uso, 'litio', 'valproato', 'carbamazepina', 'lamotrigina')" },
{ "name": "antipsicóticos_atipicos", "formula": "selected_any(medicamentos_em_uso, 'quetiapina', 'risperidona', 'olanzapina', 'aripiprazol', 'ziprasidona', 'clozapina', 'lurasidona')" }
```

**Quando usar:** exame de monitoramento indicado para toda uma classe (ex: hemograma para cDMARDs, litemia para estabilizadores). Adicionar novo fármaco = alterar apenas o alias.

---

## 2. Agregador Diagnóstico + Suspeita

Para especialidades com diagnósticos confirmados E suspeitas simultâneas:

```json
{
  "name": "quadros_inflamatorios",
  "formula": "selected_any(diagnostico_confirmado, 'ar', 'gota') or selected_any(hipotese_diagnostica, 'ar_hd', 'gota_hd')"
}
```

**Regra:** campos separados para `diagnostico_confirmado` e `hipotese_diagnostica` + expressão agregadora. Garante exames de investigação para pacientes sem diagnóstico fechado.

---

## 3. Gate de Negação Composta para Clearance

Para outputs que exigem ausência de contraindicações:

```
output_seguro = condicao_positiva AND NOT selected_any(lista_blocante)
```

Qualquer item na lista blocante cancela o output. Reutilizável para: liberação de estimulante sem contraindicação cardíaca, alta hospitalar, receita sem risco de overdose.

---

## 4. Sintoma com Contexto Obrigatório no Mesmo Nó

Quando um sintoma tem subtipos com risco radicalmente diferente, a pergunta de contexto DEVE aparecer no mesmo nó, condicionalmente:

```json
{
  "uid": "ideacao_suicida_contexto",
  "expressao": "ideacao_suicida is True",
  "select": "single",
  "options": [
    {"id": "passiva", "label": "Passiva — pensamentos de morte sem plano"},
    {"id": "ativa_sem_plano", "label": "Ativa — desejo de morrer sem plano concreto"},
    {"id": "ativa_com_plano", "label": "Ativa — plano formulado"}
  ]
}
```

**Regra:** contexto que muda a conduta deve ser capturado na mesma tela que o sintoma.

---

## 5. Boolean Gate com Texto Livre Condicional

Padrão para hábitos e histórico:

```json
{ "uid": "tabagismo", "select": "boolean" },
{ "uid": "tabagismo_detalhe", "expressao": "tabagismo is True", "select": "string" }
```

O booleano é usável em condicionais downstream. O texto livre captura narrativa sem perder capacidade lógica.

---

## 6. Variáveis Holder para Cálculos Externos

Quando um escore não pode ser calculado pela plataforma:

```json
{
  "name": "phq9_holder",
  "formula": "false",
  "description": "Holder para PHQ-9 calculado externamente."
}
```

**Regra:** se o cálculo tem mais de 3 variáveis ou pesos não-lineares, declarar como holder externo. Documentar: nome do escore, referência, população validada, thresholds.

---

## Preselection e Exclusividade — Padrões

### multiChoice (seleção múltipla)

```json
{ "id": "nenhuma_queixa", "label": "Nenhuma / rotina", "preselected": true,  "exclusive": true  },
{ "id": "queixa_a",       "label": "Queixa A",          "preselected": false, "exclusive": false },
{ "id": "queixa_b",       "label": "Queixa B",          "preselected": false, "exclusive": false }
```

- Primeiro item = estado neutro → `preselected: true, exclusive: true`
- Demais itens → `preselected: false, exclusive: false`
- Selecionar qualquer item clínico desmarca automaticamente o "nenhum"

### choice/single (seleção única)

```json
{ "id": "sem_risco",      "label": "Sem risco",      "preselected": true,  "exclusive": true },
{ "id": "baixo",          "label": "Baixo",          "preselected": false, "exclusive": true },
{ "id": "alto",           "label": "Alto",           "preselected": false, "exclusive": true }
```

- Todos os itens → `exclusive: true`
- Um item (mais comum/seguro) → `preselected: true`

---

## Template boolean (padrão canônico)

```json
{
  "uid": "gestante",
  "titulo": "<p><strong>Paciente gestante?</strong></p>",
  "condicional": "visivel",
  "expressao": "sexo_feminino_ie is True",
  "select": "boolean",
  "options": [],
  "defaultValue": "false"
}
```
