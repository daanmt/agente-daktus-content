# session_015.md — Fase 5 Psiquiatria: Patch v0.1.1

**Data:** 2026-03-08
**Fase:** Fase 5 — QA iterativo (patches de design)
**Especialidade:** Psiquiatria
**Base:** `amil-ficha_psiquiatria-vdraft.json` (modificações manuais do usuário)

---

## Resumo da sessão

Sessão iniciada com o usuário entregando a versão `vdraft` do JSON de psiquiatria,
com modificações manuais que representavam seus princípios de design revisados.
A sessão produziu o patch v0.1.1 a partir do vdraft, zerando todos os BLOQUEANTES de design.

---

## Artefatos entregues pelo usuário no início da sessão

- `amil-ficha_psiquiatria-vdraft.json` — modificações do usuário incluindo:
  - Labels Q1-Q7 do Gate P0 → nomes clínicos descritivos
  - 6 perguntas binárias do Gate P0 convertidas para `select: "boolean"`
  - Novo nó `summary` (processamento clínico) com 3 expressões de risco C-SSRS
  - Novo nó `conduta` de enfermagem com `"conduta": "pausa"` (handoff enfermagem → médico)
  - Triagem separada em dois nós (Identificação + Triagem Enfermagem)
  - `suporte_social` como multiChoice com 6 fatores protetores

---

## Sequência de ações

### 1. Análise do vdraft e planejamento

Exploração sistemática do vdraft para identificar:
- Estrutura de 9 nós (vs 6 do v0.1.0)
- Problemas nas fórmulas do summary node (sintaxe incorreta, variáveis inexistentes)
- Referências a `nivel_risco_p0` na conduta (variável não existente no vdraft)
- Perguntas `spi_realizado` e `internacao_indicada_p0` no nó de enfermagem (devem ir para medicina)
- Conversões boolean pendentes em Nós 3 e 4
- Referência `ideacao_suicida` inexistente em `ideacao_com_plano`

### 2. Script de patch: `patch_vdraft_to_v011.py`

25 modificações em 7 grupos:

| Grupo | Descrição | Modificações |
|-------|-----------|-------------|
| A | Fórmulas do summary node | 3 |
| B | Conduta: nivel_risco_p0 → expressões booleanas | 3 |
| C | Mover spi_realizado e internacao_indicada_p0 para Medicina | 4 |
| D | Corrigir expressao de ideacao_com_plano | 1 |
| E | Boolean conversões iniciais Nó 4 (ciclagem_rapida, especificador_misto) | 2 |
| F | Corrigir expressao vpa_mie_consentimento | 1 |
| G | Boolean conversões residuais Nós 3 e 4 (10 uids) | 10 |

### 3. Fórmulas C-SSRS corrigidas (Grupo A)

```python
risco_suicidio_alto:
  (ideacao_ativa is True) and (
    (ideacao_com_plano is True) or (ideacao_com_intencao is True) or
    (ideacao_com_metodo is True) or (tentativa_previa is True) or
    (acesso_meios_letais is True)
  )

risco_suicidio_intermediario:
  (ideacao_ativa is True) and (ideacao_com_plano is False) and
  (ideacao_com_intencao is False) and (tentativa_previa is True)

risco_suicidio_baixo:
  (ideacao_ativa is True) and (ideacao_com_plano is False) and
  (ideacao_com_intencao is False) and (tentativa_previa is False) and
  (not('sem_fatores_protetores' in suporte_social))
```

### 4. Resultado da auditoria final v0.1.1

```
A1 choice→boolean BLOQUEANTE:  0  ✅
A2 labels enum BLOQUEANTE:      0  ✅
A4 conduta sem condicao BLOQ:   0  ✅
TOTAL BLOQUEANTES: 0

A1 revisão (choice 2-opções legítimas): 4
A3 uid sem impacto (revisão): 40  ← escopo v0.1.2–v0.1.4
```

---

## Artefatos produzidos

| Arquivo | Status |
|---------|--------|
| `tools/GUIA_DESIGN_UX.md` | ✅ (commitado em sessão anterior) |
| `scripts/audit_design_v01.py` | ✅ (commitado em sessão anterior) |
| `scripts/patch_vdraft_to_v011.py` | ✅ commitado |
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.1.json` | ✅ commitado |
| `HANDOFF.md` | ✅ atualizado |
| `ESTADO.md` | ✅ atualizado |

---

## Pendências para v0.1.2 / v0.1.3

### v0.1.2 — Conectar uids de alta prioridade à conduta

- `primeiro_episodio_psicotico` → verificar conduta existente (alerta 9)
- `esquizofrenia_refrataria` → candidato a conduta de clozapina
- `comportamento_suicida_recorrente` → candidato a alerta/encaminhamento TCD/CAPS-II
- `acesso_meios_letais` → lethal means counseling
- `internacao_psiq_previa` — histórico para conduta diferenciada

### v0.1.3 — Mapear scores a thresholds de conduta

- MADRS ≥20 → depressão moderada-grave
- YMRS ≥20 → mania grave (urgência)
- Y-BOCS ≥16 → TOC moderado-grave (TCC/ERP)
- PCL-5 ≥33 → TEPT clínico (EMDR)

### TUSS pendentes (desde v0.1.0)

- HLA-B*1502: `codigo: []` — pendente codificação ANS
- Troponina+PCR: `codigo: []` — pendente codificação institucional

---

## Próxima sessão recomendada

1. QA clínico no ambiente de preview Daktus (percorrer 3 perfis com v0.1.1)
2. Abrir patch v0.1.2
