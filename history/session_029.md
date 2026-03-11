# session_029 — Merge do Gestor → v0.8.0

**Data:** 2026-03-11
**Tipo:** Patch arquitetural + enxugamento + limpeza editorial
**Base:** `amil-ficha_psiquiatria-v0.7.0.json`
**Output:** `amil-ficha_psiquiatria-v0.8.0.json`
**Script:** `scripts/patch_v070_to_v080.py`
**Mudanças aplicadas:** 49
**Validação:** 0 BLOQUEANTES ✅

---

## Contexto

O gestor editou uma versão prévia do JSON antes da publicação da v0.7.0. Como a v0.7.0 é qualitativamente superior (camada sindrômica com 25 clinicalExpressions, OR conservador em 22 medicamentos), a estratégia adotada foi:

> **Usar v0.7.0 como base e portar apenas as mudanças arquiteturais/enxugamento intencional do gestor.**

A camada sindrômica (Onda 5) permanece 100% intacta. Exames removidos na draft sem justificativa em áudio (HLA-B*1502, Troponina+PCR, Amônia) foram preservados.

---

## Mudanças aplicadas

### GRUPO A — Reforma arquitetural (fluxo único médico) — 10 mudanças

| Sub-grupo | Mudança |
|-----------|---------|
| A1 | Nó `conduta-a9ccd9ee-4962-4bf2-ae6a-a0f4fef7d7d9` (Conduta — Enfermagem) removido |
| A2 | 2 edges removidas: `e-node-psiq-03-anamnese-conduta-a9ccd9ee-...` e `e-conduta-a9ccd9ee-...-node-psiq-04-diagnostico` |
| A3 | Nova edge adicionada: `e-node-psiq-03-anamnese-node-psiq-04-diagnostico` (passagem direta) |
| A4 | `node-psiq-03-anamnese.data.condicionais[0].linkId` atualizado para `node-psiq-04-diagnostico` |
| A5 (6×) | 6 labels renomeados: eliminado sufixo "— Enfermagem" / "— Medicina" |

**Labels antes → depois:**
- `20e05d57-...`: "Triagem — Enfermagem" → "Avaliação inicial"
- `node-psiq-02-gate-p0`: "Triagem Suicídio — Enfermagem" → "Avaliação de risco de auto extermínio"
- `node-psiq-03-anamnese`: "Anamnese Psiquiátrica — Enfermagem" → "Antecedentes"
- `node-psiq-04-diagnostico`: "Fluxo de seguimento — Medicina" → "Fluxo de seguimento"
- `node-psiq-05-farmacos`: "Contexto adicional e fármacos — Medicina" → "Contexto adicional e fármacos"
- `node-psiq-06-conduta`: "Conduta — Medicina" → "Conduta"

---

### GRUPO B — Enxugamento da conduta — 8 mudanças

**B1 — 3 orientações ao paciente removidas:**
- `047563fa-...` ("Sobre seu diagnóstico")
- `a38db3ca-...` ("Sobre seus medicamentos")
- `orient-investigacao-001` ("Quadro em avaliação — o que esperar")

**B2 — 4 encaminhamentos removidos:**
- `260889e2-...` (CAPS II)
- `cd8fa3e9-...` (CAPS-AD)
- `a86867c6-...` (Emergência / SAMU 192)
- `8806bb9f-...` (Medicina do Trabalho)

**B3 — 1 mensagem removida:**
- `3f15ec15-...` ("GATE P0 — RISCO INTERMEDIÁRIO: SPI obrigatório") — linguagem de internação psiquiátrica inadequada para contexto de consultório particular

---

### GRUPO C — Pergunta exames_recentes — 1 mudança

- `uid: exames_recentes` (`63c45f46-...`) titulo:
  - **Antes:** `"<p><strong>Exames laboratoriais recentes:</strong></p>"`
  - **Depois:** `"<p><strong>Trouxe exames para avaliação?</strong></p>"`

---

### GRUPO D — Merge mensagens de gravidez — 4 mudanças

Duas mensagens separadas (GESTANTE+VALPROATO e GESTANTE+LÍTIO) unificadas em uma:

- **D1:** `8911c614-...` atualizado:
  - `nome`: "GESTANTE + VALPROATO — Contraindicação absoluta: substituir hoje" → "GESTANTE + PSICOTRÓPICO — Revisão urgente"
  - `condicao`: `gestante is True and 'valproato' in medicamentos_em_uso` → `gestante is True and selected_any(medicamentos_em_uso, 'valproato', 'litio')`
  - `conteudo`: merged com seção de lítio (separadas por `<hr/>`)
- **D2:** `977efeee-...` ("GESTANTE + LÍTIO") removida (standalone)

---

### GRUPO E — Limpeza de mensagens — 10 mudanças

**E1 — 3 nomes com acentos corrigidos/completos:**
- `fa6a2d13-...`: → "URGÊNCIA — MANIA GRAVE COM AGITAÇÃO/PSICOSE"
- `6a2c7758-...`: → "MANIA / HIPOMANIA — Avaliar internação se episódio maníaco grave"
- `9245499b-...`: → "SUBSTÂNCIA COMO CAUSA PRIMÁRIA — tratar dependência antes de psicofármaco"

**E2 — 7 mensagens com conteúdo atualizado (remoção/substituição de CAPS/SAMU):**

| ID (prefixo) | Mudança no conteúdo |
|-------------|---------------------|
| `72743c14` | Removido: "Considerar CAPS-II se sem recursos ambulatoriais." |
| `fa6a2d13` | "Contatar SAMU 192 ou encaminhar a servico de urgencia psiquiatrica." → "Encaminhar para serviço de urgência psiquiátrica." |
| `9245499b` | "CAPS-AD ou programa especializado de dependência" → "serviço especializado em dependência química" |
| `837ff5cb` | Removido bullet: "Considerar CAPS II para manejo ambulatorial intensivo se quadro complexo." |
| `960df136` | "Acionar SAMU 192 se risco imediato e incontrolavel." → "Contatar serviço de emergência se risco imediato e incontrolável." |
| `264c5116` | "Acionar SAMU 192 / encaminhar UPA imediatamente." → "Encaminhar para urgência psiquiátrica imediatamente." |
| `03f6c30b` | "encaminhar para CAPS-AD." → "encaminhar para serviço especializado em dependência química." |

---

### GRUPO F — Nova varredura de acentos — 20 correções

Campos alvo: `titulo`, `descricao`, `label`, `nome`, `conteudo`, `narrativa`

**F1 — Typos / acento na posição errada:**
- `heteroagressaão` → `heteroagressão` (extra 'a' eliminado)
- `abstiência` → `abstinência` (faltava 'n')
- `cansáço` → `cansaço` (acento na vogal errada, se presente)
- `Esforcxos` → `Esforços` (typo de digitação)
- `freneticos` → `frenéticos`

**F2 — Palavras sem acento (novas em v0.8.0):**
- `internacao` → `internação` | `psicotico/Psicotico` → `psicótico/Psicótico`
- `maniaco` → `maníaco` | `agitacao/Agitacao` → `agitação`
- `dependencia` → `dependência` | `notificacao` → `notificação`
- `involuntaria` → `involuntária` | `incontrolavel` → `incontrolável`
- `seguranca` → `segurança` | `servico/Servico` → `serviço`
- `fisicos` → `físicos` | `psicofarmaco` → `psicofármaco`
- `diagnostico` → `diagnóstico` | `ambulatorio` → `ambulatório`
- `urgencia/Urgencia` → `urgência` | `clinico` → `clínico`
- `vitima/Vitima` → `vítima` | `protecao` → `proteção`
- `emergencia` → `emergência` | `policia` → `polícia`
- `obrigatorio` → `obrigatório` | `prontuario` → `prontuário`
- `apos ` → `após ` | `intervencao` → `intervenção` | `criterio` → `critério`

---

## Resultado

| Métrica | v0.7.0 | v0.8.0 | Delta |
|---------|--------|--------|-------|
| Nodes | 9 | **8** | −1 |
| Edges | 8 | **7** | −1 |
| IIDs | 127 | **115** | −12 |
| clinicalExpressions | 25 | **25** | 0 ✅ |
| Orientações | 12 | **9** | −3 |
| Encaminhamentos | 13 | **9** | −4 |
| Mensagens | ~37 | **~35** | −2 |
| GESTANTE mensagens | 2 | **1** | −1 |
| Erros de validação | 0 | **0** | ✅ |

**Camada sindrômica:** 100% preservada (25 clinicalExpressions, OR conservador em 22 medicamentos, 5 exames/perguntas sindrômicos, roteamento node-04→node-05 expandido) ✅

---

## Critérios de aprovação

1. ✅ `Erros: 0`
2. ✅ Nó `conduta-a9ccd9ee-...` ausente
3. ✅ Edges da lista A2 ausentes
4. ✅ Edge `e-node-psiq-03-anamnese-node-psiq-04-diagnostico` presente
5. ✅ `node-psiq-03-anamnese.data.condicionais[0].linkId == "node-psiq-04-diagnostico"`
6. ✅ `node-psiq-06-conduta.data["label"] == "Conduta"`
7. ✅ Orientação `orient-investigacao-001` ausente
8. ✅ Orientação `047563fa` ausente
9. ✅ Encaminhamento `260889e2` (CAPS II) ausente
10. ✅ Mensagem `3f15ec15` ausente
11. ✅ Mensagem `977efeee` ausente
12. ✅ Mensagem `8911c614.condicao` contém `selected_any(medicamentos_em_uso, 'valproato', 'litio')`
13. ✅ `exames_recentes.titulo` contém "Trouxe exames para avaliação?"
14. ✅ clinicalExpressions = 25 no summary node
15. ✅ `metadata.version == "0.8.0"`

---

## Arquivos criados/modificados

| Arquivo | Ação |
|---------|------|
| `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.8.0.json` | criado (output) |
| `scripts/patch_v070_to_v080.py` | criado |
| `history/session_029.md` | criado (este arquivo) |
| `HANDOFF.md` | atualizado |
| `ESTADO.md` | atualizado |
