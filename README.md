# agente-daktus-content
### Pipeline de Criação de Conteúdo Médico — Daktus/Amil

> Estágio 1 do pipeline Daktus: transforma um briefing clínico em playbook estruturado e ficha JSON pronta para validação.
> Estágio 2 → [`agente-daktus-qa`](https://github.com/daanmt/agente-daktus-qa)

---

## O Pipeline Daktus

```
[agente-daktus-content]          →       [agente-daktus-qa]
 Briefing → Evidências                    Valida JSON contra playbook
 → Auditoria → Playbook                  → Identifica gaps e inconsistências
 → JSON                                  → Corrige e versiona
```

Dois repositórios, um pipeline. O `content` produz; o `qa` valida e corrige. O output do `content` é o input do `qa`.

---

## O que é este repositório

Um agente de IA orquestra, do briefing à entrega, a criação de protocolo clínico especializado para a plataforma Daktus. O processo inteiro é documentado como **skills exportáveis** — portáveis, versionadas, replicáveis para qualquer especialidade médica.

**Caso de uso atual:** Ficha Clínica de Psiquiatria Ambulatorial (parceria Amil)

**Casos anteriores:** Reumatologia, Cardiologia, Ginecologia

---

## Arquitetura de Skills

O pipeline opera por **progressive disclosure**: o agente carrega apenas a skill da fase atual, preservando janela de contexto e foco operacional.

```
SKILL.md  (orchestrator — lido sempre ao iniciar)
│
├── briefing-arquitetura    → mapeia briefing em arquitetura de nós clínicos
├── ingestao-evidencias     → ingere relatórios OpenEvidence no banco bibliográfico
├── auditoria-banco         → classifica referências em TIER 1/2/3 antes do playbook
├── redacao-playbook        → redige clusters clínicos com rastreamento de evidências
├── auditoria-playbook      → citation scan + semantic scan + coverage scan
├── codificacao-json        → paper design → TUSS → JSON Daktus → validação
└── qa-entrega              → checklist de 28 pontos pré-entrega
```

Cada skill é um `.md` com instruções estruturadas. Especialidade-agnóstica. A única adaptação por projeto é o mapa de clusters do Briefing (Fase 0).

---

## Estado do Projeto (Psiquiatria)

| Fase | Entregável | Status |
|------|-----------|--------|
| 0 — Briefing e arquitetura | Mapa de clusters clínicos | ✅ |
| 1 — Ingestão de evidências | Banco v3.0 — 412 REFs, 266 AFIs | ✅ |
| 2 — Auditoria do banco | AUDITORIA_MASTER.md — TIER 1/2/3 | ✅ |
| 3 — Playbook clínico | `playbook_psiquiatria.md` — 645 linhas | ✅ |
| 4 — Revisão clínica (humana) | — | ⏳ |
| 5 — JSON + QA | `ficha_psiquiatria.json` → agente-daktus-qa | ⏳ |

---

## Estrutura do Repositório

```
/
├── SKILL.md                        # Orchestrator — ler ao iniciar qualquer sessão
├── INFRAESTRUTURA.md               # Arquitetura do pipeline e lógica de skills
│
├── tools/
│   ├── skills/                     # 7 sub-skills — carregadas por fase
│   ├── KICKSTART_PSIQUIATRIA.md    # Onboarding Antigravity (chat)
│   ├── CLAUDECODE_KICKSTART.md     # Onboarding Claude Code (CLI)
│   ├── GUARDRAIL_EVIDENCIAS.md     # Protocolo de evidências (G1–G6)
│   └── PROMPT_ALINHAMENTO_MULTIAGENTE.md  # Prompt reutilizável para novos projetos
│
├── research/
│   ├── BANCO_EVIDENCIAS_PSIQUIATRIA.md   # v3.0 — 412 REFs, 266 AFIs
│   ├── AUDITORIA_MASTER.md               # TIER 1/2/3 + flags BR/Briefing
│   └── OE_RELATORIO_01..10.md            # 10 relatórios OpenEvidence
│
├── playbooks/
│   └── playbook_psiquiatria.md     # v1.0 — 645 linhas
│
├── jsons/                          # Fichas de referência UX
├── scripts/                        # validate_json.py · audit_references.py · versionar.py
├── history/                        # Session logs — rastreabilidade completa
└── versions/                       # Backups timestampados
```

---

## Banco de Evidências (v3.0)

| Métrica | Valor |
|---------|-------|
| Referências ativas | 412 |
| TIER 1 — guidelines, RCTs de alto nível | 147 |
| TIER 2 — condicionais | 182 |
| TIER 3 — contexto (excluídas do playbook) | 83 |
| Afirmações clínicas indexadas (AFIs) | 266 |
| Relatórios OpenEvidence | 10 |

---

## Operação Multi-Agente

| Agente | Interface | Responsabilidade |
|--------|-----------|-----------------|
| **Antigravity** | Claude chat | Raciocínio clínico, redação de conteúdo, auditoria de evidências |
| **Claude Code** | CLI / worktree | Git, scripts, validação JSON, organização, QA automatizado |

Sincronização via `history/session_XXX.md` — lido por ambos ao iniciar.

---

## Replicabilidade

O repositório inclui `tools/PROMPT_ALINHAMENTO_MULTIAGENTE.md` — prompt reutilizável para onboarding de qualquer novo projeto neste pipeline. Clone, preencha o briefing e execute: o agente conduz o restante.
