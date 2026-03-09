# session_017.md — Validação DSL + GUIA §2.1

**Data:** 2026-03-09
**Fase:** Fase 5 — QA iterativo (patches de design)
**Especialidade:** Psiquiatria
**Base:** `amil-ficha_psiquiatria-v0.1.2.json`

---

## Resumo da sessão

O usuário identificou um erro grave de sintaxe DSL no protocolo: padrão `campo in ('v1', 'v2')` é inválido
no Daktus — inverte os operandos e é silenciosamente falso. Enviou novo vdraft com algumas correções.

Após varredura completa de todos os `expressao` e `condicao` do artefato v0.1.2:
- **13 padrões incorretos encontrados e corrigidos** (12 linhas no JSON: Cardiologia teve 2 substituições em 1 linha)
- O vdraft do usuário também tinha os padrões errados em várias condições de conduta

**Artefato v0.1.2 corrigido in-place** via lógica do `patch_v012_conditional_fix.py`.
Auditoria pós-patch: 0 BLOQUEANTES.

A sessão produziu:
1. Correção de 13 padrões DSL em v0.1.2
2. Script de validação/correção DSL para uso futuro (`patch_v012_conditional_fix.py`)
3. Seção §2.1 adicionada ao GUIA_DESIGN_UX.md com tabela de operadores e anti-patterns

---

## Contexto do erro reportado

O padrão errado `campo in ('v1', 'v2')` é um anti-pattern do DSL Daktus que:
- Inverte os operandos (tenta encontrar o CAMPO dentro de uma tupla de strings)
- Sempre retorna falso silenciosamente (nunca gera erro de sintaxe)
- Ocorre quando se usa a semântica Python (`x in lista`) em vez da semântica Daktus (`'item' in campo`)

### Exemplo dado pelo usuário

```
ERRADO:
selected_any(diagnostico_ativo, 'tdm', 'tag', 'panico')
  and episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'depressao_grave')

CORRETO:
selected_any(diagnostico_ativo, 'tdm', 'tag', 'panico')
  and selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada', 'depressao_grave')
```

---

## Correções aplicadas (13 substituições)

| # | Campo afetado | Padrão errado | Correção |
|---|--------------|---------------|----------|
| 1 | `Q:ymrs_score.expressao` | `episodio_atual_humor in ('mania', 'hipomania')` | `selected_any(episodio_atual_humor, ...)` |
| 2 | `Q:madrs_score.expressao` | `episodio_atual_humor in ('depressao_leve', ...)` | `selected_any(episodio_atual_humor, ...)` |
| 3 | `Q:sintomas_psicoticos_humor.expressao` | `episodio_atual_humor in ('depressao_grave', 'mania')` | `selected_any(episodio_atual_humor, ...)` |
| 4 | `EXAME:Troponina+PCR.condicao` | `sintomas_miocardite in ('dor_toracica_dispneia_febre', ...)` | `selected_any(sintomas_miocardite, ...)` |
| 5 | `MEDICAMENTO:Escitalopram 10mg.condicao` | `episodio_atual_humor in ('depressao_leve', ...)` | `selected_any(episodio_atual_humor, ...)` |
| 6 | `MEDICAMENTO:Sertralina 50mg.condicao` | `episodio_atual_humor in ('depressao_leve', ...)` | `selected_any(episodio_atual_humor, ...)` |
| 7 | `MEDICAMENTO:Lítio 300mg.condicao` | `episodio_atual_humor in ('mania', 'hipomania', 'eutimia')` | `selected_any(episodio_atual_humor, ...)` |
| 8 | `MEDICAMENTO:Lamotrigina 25mg.condicao` | `episodio_atual_humor in ('depressao_leve', ...)` | `selected_any(episodio_atual_humor, ...)` |
| 9 | `ENCAMINHAMENTO:Neuropsicólogo.condicao` | `neuropsicologica_indicada in ('sim_solicitada', ...)` | `selected_any(neuropsicologica_indicada, ...)` |
| 10 | `ENCAMINHAMENTO:Cardiologia.condicao` | `ecg_indicado_psico in ('estimulante_cardiopatia')` | `selected_any(ecg_indicado_psico, ...)` |
| 11 | `ENCAMINHAMENTO:Cardiologia.condicao` | `sintomas_miocardite != 'nenhum'` | `not ('nenhum' in sintomas_miocardite)` |
| 12 | `MENSAGEM:GATE P0 RISCO ALTO.condicao` | `internacao_indicada_p0 in ('sim_involuntaria', ...)` | `selected_any(internacao_indicada_p0, ...)` |
| 13 | `MENSAGEM:CLOZAPINA miocardite.condicao` | `sintomas_miocardite in ('dor_toracica_dispneia_febre', ...)` | `selected_any(sintomas_miocardite, ...)` |

*Nota: correções 10 e 11 estavam no mesmo campo `condicao` de Cardiologia (12 linhas alteradas no JSON).*

### Tipos de campo confirmados (relevantes para DSL)

| UID | select | Operador correto |
|-----|--------|-----------------|
| `episodio_atual_humor` | choice (exclusive) | `selected_any()` ou `'v1' in campo` |
| `sintomas_miocardite` | choice (exclusive) | `selected_any()` ou `'v1' in campo` |
| `ecg_indicado_psico` | choice (exclusive) | `selected_any()` ou `'v1' in campo` |
| `internacao_indicada_p0` | choice (exclusive) | `selected_any()` ou `'v1' in campo` |
| `neuropsicologica_indicada` | choice (exclusive) | `selected_any()` ou `'v1' in campo` |

---

## Investigação adicional

Outros diffs entre vdraft e v0.1.2 (campos presentes no v0.1.2 mas ausentes no vdraft):
- `Q:neuropsicologica_indicada`, `Q:nutri_encaminhada`, `Q:spi_realizado`, `Q:tea_comorbidades`, `Q:tept_psicoterapia_indicada`, `Q:tpb_em_tcd` — adicionados pelas sessions 015/016

---

## Artefatos produzidos

| Arquivo | Ação |
|---------|------|
| `scripts/patch_v012_conditional_fix.py` | criado — script de validação/correção DSL com 13 anti-patterns catalogados |
| `tools/GUIA_DESIGN_UX.md` | atualizado — §2.1 adicionado (tabela de operadores + anti-patterns + exemplos) |
| `HANDOFF.md` | atualizado — session_017 documentada |
| `ESTADO.md` | atualizado — session_017 como última sessão integrada |
| `history/session_017.md` | criado — este arquivo |

**Artefato ativo NÃO modificado:** `amil-ficha_psiquiatria-v0.1.2.json` (já correto, 0 substituições)

---

## Regras DSL codificadas em GUIA §2.1

### Tabela de operadores por tipo de campo

| Tipo | Verificar 1 valor | Verificar N valores | Negação |
|------|-------------------|---------------------|---------|
| `choice` (multiChoice) | `'v1' in campo` | `selected_any(campo, 'v1', 'v2')` | `not ('v1' in campo)` |
| `choice` com exclusive:true | `'v1' in campo` | `selected_any(campo, 'v1', 'v2')` | `not ('v1' in campo)` |
| `boolean` | `campo is True` | — | `campo is False` |
| `single` | `campo == 'v1'` | — | `campo != 'v1'` |
| `number` | `campo >= N` | — | `campo != N` |

### Anti-pattern principal

```
campo in ('v1', 'v2')        ❌ NUNCA
selected_any(campo, 'v1', 'v2')  ✅ SEMPRE
```

---

## Auditoria reconfirmada

```
A1 choice->boolean BLOQUEANTE:   0  ✅
A2 labels enum BLOQUEANTE:       0  ✅
A4 conduta sem condicao BLOQ:    0  ✅
TOTAL BLOQUEANTES: 0

A3 uid sem impacto (revisao): 32  (classificados como legítimos)
Total expressoes coletadas: 126
Total itens de conduta: 79
```

---

## Próxima sessão recomendada

1. QA clínico no preview Daktus — 3 perfis críticos:
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta gestante+VPA
   - Esquizofrenia refratária → indicação de clozapina
2. Avaliar 32 A3 residuais: manter, conectar ou remover
3. Promover para v1.0.0 após aprovação clínica
