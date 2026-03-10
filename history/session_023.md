# session_023.md — Análise de hiatos briefing + fechamento → v0.2.3

**Data:** 2026-03-10
**Fase:** Fase 5 — QA iterativo
**Especialidade:** Psiquiatria
**Base:** `C:\Users\daanm\Downloads\amil-ficha_psiquiatria-vdraft(3).json` (revisão manual do usuário sobre v0.2.2)
**Output:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.3.json`

---

## Resumo da sessão

O usuário entregou vdraft(3) com melhorias significativas (37 medicamentos com MEVOs confirmados manualmente, novas `clinicalExpressions` na triagem, `comorbidades_clinicas`, `outros_medicamentos_relevantes`, novos exames, novos encaminhamentos) e o briefing original dos psiquiatras da clínica Amil. A sessão realizou análise rigorosa de hiatos entre o que o briefing solicita e o que o protocolo entrega, identificou gaps por prioridade (P0/P1/P2/P3), e implementou todos os gaps P0, P1 e P2 no artefato v0.2.3.

**Resultado:** 0 BLOQUEANTES ✅ | 9 nodes | 8 edges | 105 IIDs | 37 medicamentos | 25 exames | 13 encaminhamentos | 22 mensagens | 5 orientações | metadata.version = "0.2.3" ✅

---

## Estado do artefato de entrada — vdraft(3)

| Elemento | Quantidade |
|----------|-----------|
| Medicamentos | 37 (com MEVOs confirmados pelo usuário) |
| Exames | 25 |
| Encaminhamentos | 13 |
| Mensagens/Alertas | 21 |
| Orientações | 4 |
| motivo_consulta opções | 11 |
| diagnostico_ativo opções | 18 |

### Melhorias implementadas pelo usuário em vdraft(3)
- `clinicalExpressions` na triagem: `estabilizadores_humor`, `antipsicóticos_atipicos`, `exige_ecg`, `sexo_feminino_ie`, `monitoramento_metabolico_ap`
- `comorbidades_clinicas` (9 opções): hipotireoidismo, DRC, diabetes, dislipidemia, epilepsia, cardiopatia, HIV, obesidade
- `outros_medicamentos_relevantes` (9 opções): AINEs, IECA/diuréticos, anticonvulsivantes, contraceptivos, tramadol, ritonavir, amiodarona, QT-prolongantes
- Novos exames: ALT/TGP, AST/TGO, Amônia sérica, CBZ sérico, Sódio, HLA-B*1502, B12+folato, Peso/IMC, PA/FC
- Novos encaminhamentos: Neurologia, Cardiologia, Medicina do Trabalho, Endocrinologia
- MEVOs confirmados para: Bupropiona XL, Mirtazapina, Carbamazepina, Clozapina, Atomoxetina, Biperideno, Propranolol, Clonazepam, Venlafaxina 75mg, Lisdexanfetamina 30/50/70mg, Metilfenidato 10mg, Concerta LP

---

## Análise de hiatos — briefing vs. vdraft(3)

### Diagnósticos
| Briefing | Status |
|----------|--------|
| TPB, Burnout, Depressão, TAG, Esquizofrenia, TEA, TDAH, TAB, TOC, Transtornos Alimentares | ✅ Todos cobertos |
| **Agressividade** | ❌ P0 AUSENTE |

### Motivo de consulta
| Item do briefing | Status |
|-----------------|--------|
| Humor deprimido, Sintomas ansiosos, Alucinações, Ideação suicida, Insônia, Alcoolismo/SPA/Tabagismo, Histórico pessoal | ✅ Cobertos |
| **Irritabilidade** | ⚠️ P1 PARCIAL (apenas tea_irritabilidade_grave) |
| **Sonolência excessiva** | ❌ P2 AUSENTE |
| **Astenia, Apatia, Anedonia, Isolamento social, Choro frequente, Inapetência** | ❌ P2 AUSENTES |
| Sedentarismo | P3 (sem captura) |

### Encaminhamentos
| Item do briefing | Status |
|-----------------|--------|
| Psicologia (TCC, ERP, TCD, TF-CBT) | ✅ Todos cobertos |
| **Neuropsicologia** | ⚠️ P1 PARCIAL (só TDAH; TEA + 1º psicótico não cobertos) |

### Exames
| Item do briefing | Status |
|-----------------|--------|
| ECG, TGO, TGP, Litemia, Dosagem VPA | ✅ Todos cobertos (TUSS populados) |

### Outros
| Item | Status |
|------|--------|
| **Histórico familiar psiquiátrico** | ❌ P2 AUSENTE |

---

## Mudanças aplicadas — 8 total

| # | Mudança | Tipo | Detalhes |
|---|---------|------|----------|
| 1 | `motivo_consulta` +3 opções | Add options | `irritabilidade`, `agressividade_comportamento`, `sonolencia_hipersonia` |
| 2 | `diagnostico_ativo` +1 opção | Add option | `agressividade` (TEI / F63.8) |
| 3 | Nova pergunta `historico_familiar_psiq` | New question | `node-psiq-03-anamnese` — multiChoice, 6 opções (nenhum, TAB, Esquizofrenia, TDAH, suicídio, outros familiar) |
| 4 | Nova pergunta `sintomas_depressivos_presentes` | New question | `node-psiq-04-diagnostico` — multiChoice, 6 opções (anedonia, apatia, astenia, isolamento_social, choro_frequente, inapetencia) — condicional a TDM/distimia/burnout/TPB/TAB |
| 5 | Neuropsicólogo: condição expandida | Edit condition | `'tdah' in diagnostico_ativo` → `selected_any(diagnostico_ativo, 'tdah', 'tea') or primeiro_episodio_psicotico is True` |
| 6 | +1 mensagem: alerta agressividade | Add message | Condição: `'agressividade' in diagnostico_ativo or 'agressividade_comportamento' in motivo_consulta` |
| 7 | +1 orientação: atividade física | Add orientacao | Condicional a transtornos de humor/ansiedade |
| 8 | `metadata.version` → "0.2.3" | Version bump | — |

---

## Cobertura de hiatos pós v0.2.3

| Prioridade | Gap | Status |
|-----------|-----|--------|
| P0 | Agressividade ausente | ✅ FECHADO |
| P1 | Neuropsicólogo só para TDAH | ✅ FECHADO |
| P1 | Irritabilidade sem captura | ✅ FECHADO |
| P2 | Apatia/Anedonia/Astenia/Isolamento/Choro/Inapetência | ✅ FECHADO |
| P2 | Sonolência excessiva | ✅ FECHADO |
| P2 | Histórico familiar psiquiátrico ausente | ✅ FECHADO |
| P3 | Sedentarismo sem orientação específica | ✅ FECHADO (orientação condicional) |
| P3 | Taquicardia como motivo isolado | Mantido como P3 — coberto por `ansiedade_panico` |

---

## Decisão de arquitetura — "sintomas como building blocks"

Conforme orientação do usuário, os sintomas do briefing são building blocks para lógica sindrômica. A implementação respeita a distinção enfermeiro/médico:

- **Nível enfermagem** (`motivo_consulta`): queixas identificáveis sem formação médica (irritabilidade, agressividade, sonolência)
- **Nível médico** (`node-psiq-04-diagnostico`): aprofundamento clínico por perfil diagnóstico (`sintomas_depressivos_presentes` condicionado a diagnósticos relevantes)
- **Padrão gate**: como o gate de suicídio (node-psiq-02-gate-p0), perguntas de aprofundamento só aparecem quando relevantes

---

## Artefatos produzidos

| Arquivo | Ação |
|---------|------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.3.json` | criado — v0.2.3 final |
| `scripts/patch_vdraft3_to_v023.py` | criado — script de patch |
| `HANDOFF.md` | atualizado — session_023 documentada, artefato ativo = v0.2.3 |
| `ESTADO.md` | atualizado — session_023 como última sessão integrada |
| `history/session_023.md` | criado — este arquivo |

---

## Próxima sessão recomendada

1. **QA clínico de v0.2.3** no preview Daktus (5 perfis críticos):
   - Alto risco suicida com acesso a meios → restrição de meios letais
   - Mulher grávida em uso de valproato → alerta GESTANTE+VPA + Valproato como prescrição
   - Esquizofrenia refratária → indicação clozapina + alerta hemograma
   - TDAH com TDM comórbido → prescrições simultâneas (Metilfenidato + Bupropiona)
   - **[novo]** Paciente com comportamento agressivo → alerta risco para terceiros
2. **Confirmar MEVOs** com equipe Amil (ver `history/session_022_report_farmacologia.md`)
3. **v0.3** — fármacos 2ª linha + encaminhamentos faltantes (Infectologia, Psiquiatria terciária)
4. Promover para v1.0.0 após QA clínico aprovado
