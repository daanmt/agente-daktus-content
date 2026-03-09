# session_021.md — Análise de melhorias v0.2.1: fixes + TUSS/MEVO

**Data:** 2026-03-09
**Fase:** Fase 5 — QA iterativo
**Especialidade:** Psiquiatria
**Base:** `amil-ficha_psiquiatria-v0.2.1.json` (ajustes manuais do usuário sobre v0.2)
**Output:** `amil-ficha_psiquiatria-v0.2.1.json` (versão final, in-place)

---

## Resumo da sessão

O usuário fez ajustes manuais em v0.2 (removeu 5 escores, corrigiu ECG com `selected_any`, deixou metadata como "draft") e solicitou análise de melhorias com base nos padrões de qualidade acumulados, playbook e benchmarking. A sessão realizou a auditoria end-to-end de v0.2.1, identificou e corrigiu todos os problemas encontrados, e populou os códigos TUSS/MEVO ausentes.

**Resultado:** 0 BLOQUEANTES ✅ | TUSS 100% populados ✅ | MEVO 8/13 populados (5 não no catálogo Amil) | metadata.version = "0.2.1" ✅

---

## Mudanças do usuário (v0.2 → v0.2.1 draft)

| Mudança | Impacto |
|---------|---------|
| Removeu escores: PHQ-9, YMRS, MADRS, YBOCS, PCL-5 | 5 perguntas removidas (42 → 37) |
| Corrigiu ECG `expressao` para usar `selected_any` | Melhoria de DSL ✅ |
| metadata.version = "draft" | Não identificado na versão final |

---

## Problemas encontrados e corrigidos

### GRUPO α — 5 alertas com UIDs de escores inexistentes (BLOQUEANTES)

Substituídos por condições baseadas em `episodio_atual_humor` e `diagnostico_ativo`:

| Alerta (nome original) | Condição antiga | Condição nova |
|------------------------|----------------|---------------|
| DEPRESSÃO GRAVE — MADRS ≥20 | `madrs_score >= 20` | `selected_any(episodio_atual_humor, 'depressao_moderada', 'depressao_grave')` |
| MANIA GRAVE — YMRS ≥20 | `ymrs_score >= 20` | `selected_any(episodio_atual_humor, 'mania', 'hipomania')` |
| TOC MODERADO-GRAVE — Y-BOCS ≥16 | `ybocs_score >= 16` | `'toc' in diagnostico_ativo` |
| TEPT CLÍNICO — PCL-5 ≥33 | `pcl5_score >= 33` | `'tept' in diagnostico_ativo` |
| DEPRESSÃO GRAVE — PHQ-9 ≥15 | `(phq9_score >= 15) and not(madrs_score >= 20)` | `selected_any(episodio_atual_humor, 'depressao_leve')` |

### GRUPO β — 2 condições de medicamento com `madrs_score` residual

Após remoção dos escores, Quetiapina e Aripiprazol tinham cláusula `or (madrs_score >= 20)` que nunca disparava. Removida.

### GRUPO γ — metadata.version

Atualizado de `"draft"` para `"0.2.1"`.

---

## TUSS populados (2 exames)

| Exame | Código TUSS | Termo oficial |
|-------|------------|---------------|
| HLA-B*1502 (genotipagem) | 40306887 | Genotipagem do sistema HLA |
| Troponina + Proteína C-reativa (PCR) | 40302571 + 40308391 | Troponina / PCR quantitativa |

---

## MEVO populados (8 de 13 medicamentos)

| Medicamento | Códigos MEVO |
|-------------|-------------|
| Sertralina 50mg | 08994 |
| Fluoxetina 20mg | 42541 |
| Lítio 300mg | 42533 |
| Lamotrigina 25mg | 35451 |
| Quetiapina 25/50/100mg | 15067 + 29137 |
| Olanzapina 5/10mg | 31921 + 34587 |
| Risperidona 1/2mg | 35806 + 35807 |
| Aripiprazol 10/15mg | 35461 + 32613 |

**5 medicamentos SEM código MEVO** (não encontrados no `Mevo..xlsx` com dosagem correspondente):
- Escitalopram 10mg (Mevo tem 20mg — dose inicial 10mg não cadastrada)
- Metilfenidato LP 18mg
- Lisdexanfetamina 20mg
- Biperideno 2mg
- Propranolol 20mg

*Ação recomendada: confirmar cobertura com equipe Amil.*

---

## Gap analysis playbook vs v0.2.1 (descobertas da auditoria)

O gap analysis extenso revelou que a maioria dos gaps identificados inicialmente já estavam presentes em v0.2.1 (agente não os conhecia). Estado atual:

### Surpresas positivas (já presentes em v0.2.1)
- Lítio 300mg como prescrição ✅
- Lamotrigina 25mg como prescrição ✅
- Encaminhamento Neurologia ✅
- Encaminhamento Medicina do Trabalho ✅
- Encaminhamento Endocrinologia ✅
- Encaminhamento Nutricionista (TA) ✅
- CAPS II ✅

### Gaps reais identificados (para roadmap v0.3)

**Prescrições faltantes:**
- Antidepressivos: Venlafaxina, Duloxetina, Bupropiona, Mirtazapina
- Estimulantes TDAH: Atomoxetina, Guanfacina
- BZDs (Clonazepam, Lorazepam)
- Clozapina como prescrição (existe só como alerta de monitoramento)
- Valproato como prescrição (existe como monitoramento)

**Encaminhamentos faltantes:**
- Infectologia
- Psiquiatria terciária (para refratários não-esquizofrenia)

---

## Resultado final — v0.2.1

```
Perguntas: 37 (era 42 em v0.2 — usuário removeu 5 escores)
Alertas (mensagem): 21 (conduta médica) + 3 (handoff enfermagem) = 24
Medicamentos: 13
Encaminhamentos: 13
Exames: 25
Total conduta: 79 IIDs
BLOQUEANTES: 0  ✅
UIDs de escores residuais: 0  ✅
TUSS vazios: 0  ✅
MEVO populados: 8/13 (5 não no catálogo Amil atual)
```

---

## Artefatos produzidos

| Arquivo | Ação |
|---------|------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.1.json` | atualizado — fixes + TUSS/MEVO |
| `scripts/patch_v021_fixes.py` | criado — documentação dos fixes de alertas + metadata |
| `scripts/patch_v021_to_v03_codigos.py` | criado — TUSS/MEVO lookup e população |
| `HANDOFF.md` | atualizado — session_021 documentada, artefato ativo = v0.2.1 |
| `ESTADO.md` | atualizado — session_021 como última sessão integrada |
| `history/session_021.md` | criado — este arquivo |

---

## Próxima sessão recomendada

1. **QA clínico de v0.2.1 no preview Daktus** — 3 perfis críticos:
   - Alto risco suicida com acesso a meios → verificar restrição de meios letais
   - Mulher grávida em uso de valproato → alerta GESTANTE + VPA
   - Esquizofrenia refratária → indicação clozapina
2. **Confirmar 5 MEVOs faltantes** com equipe Amil (Escitalopram 10mg, Metilfenidato LP, Lisdexanfetamina, Biperideno, Propranolol)
3. **v0.3 — roadmap clinico:** expandir prescrições (Venlafaxina, Bupropiona, Valproato como Rx, Clozapina como Rx, Atomoxetina) + encaminhamentos faltantes (Infectologia, Psiq. terciária)
4. Promover para v1.0.0 após QA clínico aprovado
