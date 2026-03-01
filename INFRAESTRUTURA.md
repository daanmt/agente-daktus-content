# INFRAESTRUTURA DE SKILLS — PIPELINE DAKTUS
## Antigravity Content Team | v2.0 | 2026-03-01

---

## VISÃO GERAL

Este documento descreve a arquitetura de inteligência portátil do pipeline de produção de fichas clínicas Daktus. Não é um agente autônomo — é um conjunto de **skills que o agente lê sob demanda**, conforme a fase em que o projeto se encontra.

O princípio central: ao invés de um system prompt monolítico que carrega todo o know-how de todas as fases simultaneamente, o agente carrega apenas a skill da fase atual. Isso preserva a janela de contexto, mantém o foco operacional e torna a infraestrutura exportável para qualquer especialidade.

---

## ARQUITETURA CANÔNICA DE PROJETO

Todo projeto segue esta estrutura de pastas. **Ela deve existir antes de qualquer trabalho começar.**

```
/{especialidade}/
│
├── tools/
│   └── skills/                            ← esta pasta — o pipeline completo
│       ├── SKILL.md                       ← orchestrator (ler sempre ao iniciar)
│       ├── INFRAESTRUTURA.md             ← este documento
│       ├── briefing-arquitetura/
│       │   └── SKILL.md
│       ├── ingestao-evidencias/
│       │   └── SKILL.md
│       ├── auditoria-banco/
│       │   └── SKILL.md
│       ├── redacao-playbook/
│       │   └── SKILL.md
│       ├── auditoria-playbook/
│       │   └── SKILL.md
│       ├── codificacao-json/
│       │   └── SKILL.md
│       └── qa-entrega/
│           └── SKILL.md
│
├── research/
│   ├── BANCO_EVIDENCIAS_{ESP}.md          ← ARQUIVO MESTRE — autoridade clínica do projeto
│   ├── AUDITORIA_BANCO_v1.md             ← resultado da auditoria pré-playbook
│   └── OE_{tema}_{N}.md                  ← relatórios brutos do OpenEvidence
│
├── history/
│   └── session_{NNN}.md                  ← log de cada sessão (001, 002, ...)
│
├── playbooks/
│   ├── playbook_{esp}_vDRAFT.md
│   ├── relatorio_auditoria_playbook.md
│   └── playbook_{esp}_vFINAL.md
│
├── jsons/
│   ├── ficha_{esp}_v{versao}.json
│   ├── relatorio_qa_{esp}.md
│   └── referencia/                        ← JSONs de outras especialidades (referência UX)
│
└── scripts/
    ├── validate_json.py
    ├── audit_references.py
    └── versionar.py
```

---

## LÓGICA DE ATIVAÇÃO (PROGRESSIVE DISCLOSURE)

O agente conhece todas as skills pelo `SKILL.md` do orchestrator — que lista apenas nome e descrição de uma linha de cada sub-skill. O conteúdo completo de cada skill só é lido quando aquela fase é ativada. Isso mantém a janela de contexto livre para o trabalho real.

**System prompt mínimo sugerido para qualquer projeto:**

```
Você é o agente de produção de fichas clínicas Daktus da Antigravity.
Siga sempre o pipeline em /tools/skills/SKILL.md.

Sub-skills disponíveis (leia apenas a da fase atual):
- briefing-arquitetura: mapear briefing clínico em arquitetura de nós
- ingestao-evidencias: ingerir relatórios OpenEvidence no banco
- auditoria-banco: classificar referências em TIER 1/2/3 antes do playbook
- redacao-playbook: redigir o playbook clínico cluster por cluster
- auditoria-playbook: citation_scan, semantic_scan, exam_coverage_scan
- codificacao-json: paper design, TUSS, geração de JSON Daktus, validação
- qa-entrega: checklist de 28 pontos antes da entrega para homologação

Antes de qualquer ação: ler /history/session_XXX.md para saber onde o projeto parou.
Nunca avançar de fase sem aprovação explícita do usuário.
```

---

## FLUXO DE DADOS ENTRE SKILLS

```
[briefing-arquitetura]
    ↓ mapa de nós aprovado
    
[ingestao-evidencias] ←─────────────────────────┐
    ↓ (loop contínuo — relatórios chegam         │
       ao longo de todas as fases)               │
    ↓                                            │
[auditoria-banco]                                │
    ↓ AUDITORIA_BANCO_v1.md aprovado             │
    ↓                                            │
[redacao-playbook] — emite Solicitações ─────────┘
    ↓ cluster por cluster, aprovado pelo usuário
    ↓
[auditoria-playbook]
    ↓ citation + semantic + coverage = PASS
    ↓
[revisão clínica — humana]
    ↓ aprovação clínica
    ↓
[codificacao-json]
    ↓ JSON válido
    ↓
[qa-entrega]
    ↓ 28 checks ✅
    → ENTREGA para homologação
```

---

## ARTEFATOS PRODUZIDOS POR PROJETO

| Artefato | Localização | Produzido por |
|----------|------------|--------------|
| `OE_RELATORIO_00_BRIEFING.md` | `research/` | briefing-arquitetura |
| `BANCO_EVIDENCIAS_{ESP}.md` | `research/` | ingestao-evidencias |
| `AUDITORIA_BANCO_v1.md` | `research/` | auditoria-banco |
| `playbook_{esp}_vDRAFT.md` | `playbooks/` | redacao-playbook |
| `relatorio_auditoria_playbook.md` | `playbooks/` | auditoria-playbook |
| `playbook_{esp}_vFINAL.md` | `playbooks/` | aprovação pós-revisão clínica |
| `ficha_{esp}_v{versao}.json` | `jsons/` | codificacao-json |
| `relatorio_qa_{esp}.md` | `jsons/` | qa-entrega |
| `session_{NNN}.md` | `history/` | toda sessão ao encerrar |

---

## COMPARAÇÃO: AGENTE MONOLÍTICO vs. SKILLS

| Dimensão | Agente monolítico | Skills (este modelo) |
|----------|-------------------|---------------------|
| Janela de contexto | Carrega tudo sempre | Carrega apenas a fase atual |
| Manutenção | Requer redeploy | Editar o `.md` da sub-skill |
| Aprendizado | Estático após deploy | Retroalimentação contínua via Git |
| Portabilidade | Acoplado à plataforma | Pasta de arquivos — funciona em qualquer LLM |
| Versioning | Complexo | Git nativo sobre a pasta `/tools/skills/` |
| Foco operacional | Pode misturar fases | Cada sessão = uma fase = uma skill |
| Reproduzibilidade | Baixa | Alta — mesma pasta funciona para qualquer especialidade |

---

## RETROALIMENTAÇÃO — A SKILL MELHORA COM CADA PROJETO

Ao encerrar um projeto, identificar gaps e emitir:

```
🔧 MELHORIA DE SKILL #N
Skill: [nome da sub-skill]
Situação não coberta: [descrição do que aconteceu]
Comportamento atual: [o que o agente fez]
Comportamento esperado: [o que deveria ter feito]
Proposta de adição: [texto sugerido para a skill]
```

Versionar a pasta `tools/skills/` no Git. O histórico de melhorias é o ativo mais valioso do pipeline.

---

*Este pipeline é especialidade-agnóstico. A única adaptação necessária para um novo projeto é o nome `{ESP}` nos arquivos e o mapeamento de clusters no briefing.*
