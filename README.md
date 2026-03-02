# Pipeline de Criação de Conteúdo Médico — Daktus/Amil
### Caso de uso: Ficha Clínica de Psiquiatria Ambulatorial

> **Este repositório documenta dois produtos simultâneos:** o protocolo clínico de psiquiatria para a plataforma Daktus, e o **modelo operacional** que o produziu — um pipeline skill-based replicável para qualquer especialidade médica.

---

## O que é isto

Um agente de IA orquestrou, do briefing à entrega, a criação de um protocolo clínico especializado. Todo o processo foi documentado com profundidade suficiente para ser extraído como conjunto de skills reutilizáveis — portáveis, versionadas e operáveis por qualquer agente, em qualquer máquina, via chat ou CLI.

A tese: **documentar o processo com a mesma rigorosidade do produto final transforma o know-how operacional em infraestrutura**.

---

## O Pipeline

```
BRIEFING → INGESTÃO DE EVIDÊNCIAS → AUDITORIA → PLAYBOOK → REVISÃO CLÍNICA → JSON → QA → ENTREGA
```

Cada fase é executada por uma **sub-skill dedicada** (`tools/skills/`), carregada sob demanda (progressive disclosure). O agente lê apenas a skill da fase atual — preservando janela de contexto e mantendo foco operacional.

```
SKILL.md (orchestrator)
│
├── briefing-arquitetura    → mapeia briefing em arquitetura de nós clínicos
├── ingestao-evidencias     → ingere relatórios OpenEvidence no banco bibliográfico
├── auditoria-banco         → classifica referências em TIER 1/2/3 antes do playbook
├── redacao-playbook        → redige clusters clínicos com rastreamento de evidências
├── auditoria-playbook      → citation scan + semantic scan + coverage scan
├── codificacao-json        → paper design → TUSS → JSON Daktus → validação
└── qa-entrega              → checklist de 28 pontos pré-entrega
```

O agente nunca avança de fase sem aprovação explícita. Cada sessão gera um log em `history/` — o ponto de sincronização entre instâncias e entre sessões.

---

## Estado do Projeto (Psiquiatria)

| Fase | Entregável | Status |
|------|-----------|--------|
| 0 — Briefing e arquitetura | Mapa de clusters clínicos | ✅ |
| 1 — Ingestão de evidências | Banco v3.0 — 412 REFs, 266 AFIs | ✅ |
| 2 — Auditoria do banco | AUDITORIA_MASTER.md — TIER 1/2/3 | ✅ |
| 3 — Playbook clínico | `playbook_psiquiatria.md` — 645 linhas | ✅ |
| 4 — Revisão clínica (humana) | — | ⏳ |
| 5 — JSON + QA | `ficha_psiquiatria.json` | ⏳ |

---

## Estrutura do Repositório

```
/
├── SKILL.md                        # Orchestrator — ler ao iniciar qualquer sessão
├── INFRAESTRUTURA.md               # Arquitetura do pipeline e lógica de skills
│
├── tools/
│   ├── skills/                     # 7 sub-skills — carregadas por fase
│   ├── KICKSTART_PSIQUIATRIA.md    # Onboarding para Antigravity (chat)
│   ├── CLAUDECODE_KICKSTART.md     # Onboarding para Claude Code (CLI)
│   ├── GUARDRAIL_EVIDENCIAS.md     # Protocolo de gestão de evidências (G1–G6)
│   ├── PROMPT_ALINHAMENTO_MULTIAGENTE.md  # Prompt reutilizável para novos projetos
│   └── ...                         # Demais documentos de instrução
│
├── research/
│   ├── BANCO_EVIDENCIAS_PSIQUIATRIA.md   # v3.0 — autoridade clínica (412 REFs, 266 AFIs)
│   ├── AUDITORIA_MASTER.md               # Classificação TIER 1/2/3 + flags BR/Briefing
│   └── OE_RELATORIO_01..10.md            # 10 relatórios OpenEvidence por tema
│
├── playbooks/
│   └── playbook_psiquiatria.md     # v1.0 — referência cross-especialidade incluída
│
├── jsons/                          # Fichas de referência UX (ginecologia, cardiologia, reumatologia)
├── scripts/                        # validate_json.py · audit_references.py · versionar.py
├── history/                        # Session logs 001–006 — rastreabilidade completa
└── versions/                       # Backups timestampados de artefatos
```

---

## O Banco de Evidências

| Métrica | Valor |
|---------|-------|
| Referências ativas | 412 |
| TIER 1 — guidelines, RCTs de alto nível | 147 |
| TIER 2 — condicionais | 182 |
| TIER 3 — contexto (excluídas do playbook) | 83 |
| Afirmações clínicas indexadas (AFIs) | 266 |
| Relatórios OpenEvidence ingeridos | 10 |

Cada AFI é rastreável até sua(s) REF(s). Cada REF tem Tier, flag BR-relevante e flag Briefing-central. Nenhuma afirmação do playbook existe sem âncora verificável no banco.

---

## Operação Multi-Agente

Dois agentes operam sobre os mesmos artefatos com responsabilidades distintas:

| Agente | Interface | Responsabilidade |
|--------|-----------|-----------------|
| **Antigravity** | Claude chat (contexto longo) | Raciocínio clínico, auditoria de evidências, redação de conteúdo |
| **Claude Code** | CLI / worktree | Git, scripts, validação JSON, organização de arquivos, QA automatizado |

**Sincronização:** `history/session_XXX.md` — lido por ambos ao iniciar. Qualquer agente que altere o estado do projeto registra no log.

---

## Replicabilidade

As skills são **especialidade-agnósticas**. A única adaptação necessária para um novo projeto é o mapa de clusters do Briefing. O repositório inclui `tools/PROMPT_ALINHAMENTO_MULTIAGENTE.md` — prompt reutilizável para onboarding de qualquer novo projeto neste mesmo modelo operacional.

Projetos já produzidos com versões anteriores do pipeline: Reumatologia, Cardiologia, Ginecologia.
