# session_019.md — Auditoria end-to-end + Promoção para v0.2

**Data:** 2026-03-09
**Fase:** Fase 5 — QA iterativo → preparação para QA clínico
**Especialidade:** Psiquiatria
**Base:** `amil-ficha_psiquiatria-v0.1.2.json`
**Output:** `amil-ficha_psiquiatria-v0.2.json`

---

## Resumo da sessão

O usuário identificou que perguntas deletadas em seu vdraft foram reintroduzidas pelo agente, e solicitou auditoria end-to-end completa para identificar tudo que pode ser removido antes da promoção para v0.2 (primeira versão revisada conjuntamente).

**Resultado final: 24 perguntas removidas (66 → 42), 12 condicionais de conduta corrigidas, 0 BLOQUEANTES.**

---

## Achados da auditoria

### Grupo A — Re-adicionadas pelo agente, deletadas pelo usuário no vdraft (6)

| UID | Conduta que referenciava | Ação |
|-----|--------------------------|------|
| `spi_realizado` | Alerta SPI intermediário | Removida; condição simplificada para `risco_suicidio_intermediario is True` |
| `neuropsicologica_indicada` | Encaminhamento Neuropsicólogo | Removida; condição simplificada para `'tdah' in diagnostico_ativo` |
| `tept_psicoterapia_indicada` | Encaminhamento TF-CBT/EMDR | Removida; condição simplificada para `'tept' in diagnostico_ativo` |
| `nutri_encaminhada` | Encaminhamento Nutricionista | Removida; condição simplificada |
| `tpb_em_tcd` | Encaminhamento TCD | Removida; condição simplificada para `'tpb' in diagnostico_ativo` |
| `tea_comorbidades` | — (0 conduta) | Removida diretamente |

### Grupo B — Orphans diagnósticas (0 conduta, 0 referências downstream) (10)

`tab_fase_diagnostica`, `mdq_aplicado`, `burnout_criterios_tdm`, `especificador_misto`, `tdah_apresentacao`, `sintomas_cardiacos_tdah`, `tea_nivel_suporte`, `tpb_autolesao_ativa`, `tpb_sintoma_alvo`, `ciclagem_rapida`

### Grupo C — Monitoramento farmacológico sem conduta (8, confirmado pelo usuário)

`litio_fase`, `litemia_valor`, `vpa_fase`, `vpa_nivel`, `vpa_labs_recentes`, `cbz_nivel`, `anc_valor`, `ap_tempo_uso`

*Nota: `litemia_valor` e `anc_valor` são valores numéricos. Os campos interpretativos (`litemia_dentro_faixa`, `anc_dentro_limite`) que seriam necessários para alertas de toxicidade não existiam no JSON — foram descobertos como UIDs mortos nas condições de conduta.*

### Grupo D — UIDs não definidos em condições de conduta (bugs — 7 items nunca disparavam)

| Item | UID inexistente | Correção |
|------|----------------|---------|
| Alerta CLOZAPINA ANC | `anc_dentro_limite` | → `'clozapina' in medicamentos_em_uso` (lembrete permanente); nome e conteúdo reescritos |
| Encaminhamento Cardiologia (cláusula) | `anc_dentro_limite` | → Cláusula removida |
| Alerta VPA + MIE | `vpa_mie_consentimento` | → `sexo_feminino_ie is True and 'valproato' in medicamentos_em_uso` |
| Alerta TAB + AD sem estabilizador | `ad_sem_estabilizador` | → condição direta via `medicamentos_em_uso` |
| Encaminhamento Emergência (cláusula) | `encaminhamento_urgencia_necessario` | → Cláusula removida |
| Exame HLA-B*1502 (gate) | `cbz_hla_realizado` | → Gate removido; dispara sempre para CBZ |
| Exame Prolactina (gate) | `prolactina_sintomatic` | → Gate removido; dispara sempre para risperidona |

---

## Resultado final — v0.2

```
Perguntas: 42 (era 66)
Itens de conduta: 79
BLOQUEANTES: 0  ✅
UIDs indefinidos residuais: 0  ✅
```

---

## Artefatos produzidos

| Arquivo | Ação |
|---------|------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.json` | criado — versão revisada conjuntamente |
| `scripts/patch_v012_to_v02.py` | criado — script de promoção v0.1.2 → v0.2 |
| `HANDOFF.md` | atualizado — session_019 documentada, artefato ativo = v0.2 |
| `ESTADO.md` | atualizado — session_019 como última sessão integrada |
| `history/session_019.md` | criado — este arquivo |

---

## Filosofia aplicada nesta sessão

> **Protocolo enxuto:** remover perguntas que não modificam a conduta e cujas respostas podem ser inferidas de outros campos ou tratadas pelo clínico sem suporte explícito da ficha. Não criar lógica adicional sem reaproveitar a lógica existente.

---

## Próxima sessão recomendada

1. QA clínico de v0.2 no preview Daktus — 3 perfis críticos:
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta gestante+VPA
   - Esquizofrenia refratária → indicação de clozapina
2. Promover para v1.0.0 após aprovação clínica
