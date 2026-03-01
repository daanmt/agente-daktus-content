# Ficha Clínica de Psiquiatria — Daktus/Amil

Ficha clínica especializada de psiquiatria ambulatorial para a plataforma **Daktus**, em parceria com o plano de saúde **Amil**. Produz dois artefatos interdependentes: um **Playbook Clínico** (`.md`) e uma **Ficha JSON** (`.json`) implementável diretamente na plataforma.

---

## Estado do Projeto

| Fase | Status |
|------|--------|
| Fase 0 — Briefing e arquitetura | ✅ Completa |
| Ingestão de evidências (10 relatórios OE) | ✅ Completa |
| Auditoria do banco de evidências | ✅ Completa |
| **Fase 1 — Playbook clínico** | ✅ Completa |
| Fase 2 — Auditoria do playbook | ⏳ Pendente |
| Fase 3 — Revisão clínica (humana) | ⏳ Pendente |
| Fase 4 — Codificação JSON | ⏳ Pendente |
| Fase 5 — QA e entrega | ⏳ Pendente |

---

## Estrutura do Projeto

```
/
├── SKILL.md                  # Orchestrator do pipeline — ler sempre ao iniciar
├── INFRAESTRUTURA.md         # Arquitetura completa do sistema de skills
│
├── tools/
│   ├── skills/               # 7 sub-skills do pipeline (progressive disclosure)
│   │   ├── briefing-arquitetura/
│   │   ├── ingestao-evidencias/
│   │   ├── auditoria-banco/
│   │   ├── redacao-playbook/
│   │   ├── auditoria-playbook/
│   │   ├── codificacao-json/
│   │   └── qa-entrega/
│   ├── KICKSTART_PSIQUIATRIA.md       # Onboarding para Antigravity (chat)
│   ├── CLAUDECODE_KICKSTART.md        # Onboarding para Claude Code (CLI)
│   ├── GUARDRAIL_EVIDENCIAS.md        # Protocolo de gestão de evidências
│   └── ...                            # Demais documentos de instrução
│
├── research/
│   ├── BANCO_EVIDENCIAS_PSIQUIATRIA.md  # v3.0 — 412 REFs, 266 AFIs (autoridade clínica)
│   ├── AUDITORIA_MASTER.md              # Classificação TIER 1/2/3, flags BR + Briefing
│   └── OE_RELATORIO_01..10.md           # Relatórios brutos do OpenEvidence
│
├── playbooks/
│   └── playbook_psiquiatria.md  # v1.0 — 645 linhas, tabelas 6 colunas
│
├── jsons/                       # Fichas de referência UX (ginecologia, cardiologia, reumatologia)
├── scripts/                     # validate_json.py, audit_references.py, versionar.py
└── history/                     # Session logs 001–006
```

---

## Banco de Evidências (v3.0)

| Métrica | Valor |
|---------|-------|
| Referências ativas | 412 |
| TIER 1 — âncoras obrigatórias | 147 |
| TIER 2 — condicionais | 182 |
| TIER 3 — contexto | 83 |
| Afirmações clínicas (AFIs) | 266 |
| Relatórios OpenEvidence | 10 |

Temas cobertos: Gate P0 (risco suicida), monitoramento de fármacos (Lítio/VPA/CBZ/Clozapina), transtornos do humor, ansiedade/TOC/TEPT, psicose/EPS, TDAH, TEA, TPB, transtornos alimentares, interações medicamentosas e critérios de internação.

---

## Playbook (v1.0)

Estrutura por classe farmacológica (não por síndrome):

- **Gate P0** — rastreio de risco suicida (C-SSRS + plano de segurança + legislação)
- **Condições** — tabela diagnóstica (19 condições, CID-10 + critério DSM-5-TR)
- **Exames** — Baseline, monitoramento de estabilizadores, monitoramento de antipsicóticos, ECG, escalas
- **Terapêuticas §1–§9** — Antidepressivos, Estabilizadores, Antipsicóticos, TDAH, Psicoterapias, Nichos, Crise (EPS/SNM), Burnout, DDIs
- **KPIs auditáveis** — 12 metas clínicas mensuráveis

---

## Pipeline de Produção

```
Briefing → Ingestão OE → Auditoria do banco → Playbook → Auditoria → Revisão clínica → JSON → QA → Entrega
```

Baseado em **progressive disclosure**: cada sessão carrega apenas a skill da fase atual, preservando a janela de contexto. Ver `SKILL.md` para detalhes.

---

## Operação Multi-Agente

| Agente | Interface | Responsabilidade |
|--------|-----------|-----------------|
| **Antigravity** | Claude chat | Conteúdo clínico, auditoria de evidências, redação de playbook |
| **Claude Code** | CLI / worktree | Git, scripts, validação JSON, operações de arquivo |

**Ponto de encontro:** `history/session_XXX.md` — ambos os agentes leem o log mais recente ao iniciar qualquer sessão.
