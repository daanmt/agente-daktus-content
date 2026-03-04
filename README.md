# agente-daktus-content
### Pipeline de Criacao de Conteudo Medico — Daktus

> Estagio 1 do pipeline Daktus: transforma briefing clinico em playbook estruturado e ficha JSON pronta para validacao.
> Estagio 2 → [`agente-daktus-qa`](https://github.com/daanmt/agente-daktus-qa)

---

## O Pipeline

```
[agente-daktus-content]          →       [agente-daktus-qa]
 Briefing → Evidencias                    Valida JSON contra playbook
 → Auditoria → Playbook                  → Identifica gaps
 → JSON                                  → Corrige e versiona
```

---

## Arquitetura de Skills

O pipeline opera por **progressive disclosure**: o agente carrega apenas a skill da fase atual, preservando janela de contexto e foco operacional.

```
SKILL.md  (orchestrator)
│
├── briefing-arquitetura    → mapeia briefing em arquitetura de nos clinicos
├── ingestao-evidencias     → ingere relatorios OpenEvidence no banco bibliografico
├── auditoria-banco         → classifica referencias em TIER 1/2/3 antes do playbook
├── redacao-playbook        → redige clusters clinicos com rastreamento de evidencias
├── auditoria-playbook      → citation scan + semantic scan + coverage scan
├── codificacao-json        → paper design → TUSS → JSON Daktus → validacao
└── qa-entrega              → checklist de 28 pontos pre-entrega
```

Cada skill e um `.md` com instrucoes estruturadas. Especialidade-agnostica.

---

## Estrutura do Repositorio

```
/
├── ESTADO.md               # Fonte de verdade — ler ao iniciar qualquer sessao
├── CLAUDE.md               # Protocolo de inicio de sessao
├── SKILL.md                # Orchestrator — pipeline completo
│
├── tools/
│   ├── skills/             # 7 sub-skills — carregadas por fase
│   └── *.md                # Instrucoes tecnicas, guardrails, padroes
│
├── especialidades/
│   ├── ginecologia/        # Auditoria JSON em andamento
│   └── psiquiatria/        # Fase 3 — aguardando revisao clinica
│
├── referencia/             # JSONs e playbooks de projetos entregues (read-only)
├── history/                # Session logs — rastreabilidade completa
└── scripts/                # Automacao: validate_json, audit_logic, audit_references
```

---

## Especialidades

| Especialidade | Status | Fase |
|--------------|--------|------|
| Ginecologia | Auditoria JSON | vdraft2 — aguardando correcoes C1-C4 |
| Psiquiatria | Fase 3 | Aguardando revisao clinica do playbook |
| Cardiologia | Entregue | Em `referencia/` |
| Reumatologia | Entregue | Em `referencia/` |

---

## Operacao Multi-Agente

| Agente | Interface | Responsabilidade |
|--------|-----------|-----------------|
| **Antigravity** | Claude chat | Raciocinio clinico, redacao de conteudo, auditoria de evidencias |
| **Claude Code** | CLI / terminal | Git, scripts, validacao JSON, organizacao, QA automatizado |

Sincronizacao via `ESTADO.md` + `history/session_XXX.md` — lidos por todos ao iniciar.
