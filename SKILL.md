# SKILL — PIPELINE DE PRODUÇÃO DAKTUS
## Orchestrator | Antigravity Content Team

---

## O QUE ESTA SKILL FAZ

Esta é a skill mestra do pipeline de produção de fichas clínicas Daktus. Ela define a arquitetura de pastas de qualquer projeto, descreve todas as sub-skills disponíveis e determina quando invocar cada uma. O agente **nunca avança de fase sem aprovação explícita do usuário**.

---

## ARQUITETURA CANÔNICA DE PROJETO

Todo projeto de ficha clínica Daktus deve seguir esta estrutura de pastas. Ao iniciar um projeto novo, verificar se a estrutura existe; se não, criá-la.

```
/{especialidade}/
│
├── tools/                             ← skills e documentos de instrução do agente
│   └── skills/                        ← esta pasta (pipeline de produção)
│
├── research/                          ← evidências e banco bibliográfico
│   ├── BANCO_EVIDENCIAS_{ESP}.md      ← ARQUIVO MESTRE de referências e AFIs
│   ├── AUDITORIA_BANCO_v1.md          ← resultado da auditoria pré-playbook
│   └── OE_{tema}_{N}.md               ← relatórios brutos do OpenEvidence
│
├── history/                           ← rastreabilidade de sessões
│   └── session_{NNN}.md              ← log de cada sessão (001, 002, ...)
│
├── playbooks/                         ← documentação clínica
│   ├── playbook_{esp}_vDRAFT.md
│   └── playbook_{esp}_vFINAL.md      ← aprovado clinicamente
│
├── jsons/                             ← fichas produzidas
│   ├── ficha_{esp}_v{versao}.json    ← ficha Daktus validada
│   └── referencia/                    ← JSONs de outras especialidades para referência UX
│
└── scripts/                           ← automação e validação
    ├── validate_json.py
    ├── audit_references.py
    └── versionar.py
```

**Arquivo mais importante do projeto:** `research/BANCO_EVIDENCIAS_{ESP}.md`
É a autoridade clínica. Toda afirmação do playbook deve rastrear até uma entrada deste arquivo.

---

## SUB-SKILLS DISPONÍVEIS

| Skill | Pasta | Invocar quando |
|-------|-------|----------------|
| `briefing-arquitetura` | `/tools/skills/briefing-arquitetura/` | Início de projeto — especialidade nova |
| `ingestao-evidencias` | `/tools/skills/ingestao-evidencias/` | Ao receber relatório do OpenEvidence |
| `auditoria-banco` | `/tools/skills/auditoria-banco/` | Antes de iniciar qualquer cluster do playbook |
| `redacao-playbook` | `/tools/skills/redacao-playbook/` | Após auditoria do banco aprovada |
| `auditoria-playbook` | `/tools/skills/auditoria-playbook/` | Após draft completo de cada cluster |
| `codificacao-json` | `/tools/skills/codificacao-json/` | Após playbook aprovado clinicamente |
| `qa-entrega` | `/tools/skills/qa-entrega/` | Antes de entregar para homologação |

---

## SEQUÊNCIA INVIOLÁVEL DE FASES

```
FASE 0  →  briefing-arquitetura      (mapa de nós aprovado)
        ↓
        →  ingestao-evidencias        (loop contínuo — relatórios OE chegam ao longo do projeto)
        ↓
FASE 2* →  auditoria-banco           (pré-auditoria antecipada antes do playbook)
        ↓
FASE 1  →  redacao-playbook          (cluster por cluster — ordem definida na skill)
        ↓
FASE 2  →  auditoria-playbook        (citation, semantic, coverage scans)
        ↓
FASE 3  →  [revisão clínica humana — sem skill]
        ↓
FASE 4  →  codificacao-json          (paper design → TUSS → JSON → validação)
        ↓
FASE 5  →  qa-entrega                (28 checks antes da entrega)
```

*A Fase 2 de auditoria do banco é antecipada por decisão estratégica — banco inflado contamina o playbook.

---

## REGRAS GERAIS DE COMPORTAMENTO

1. **Sempre ler** `history/session_XXX.md` antes de qualquer ação — saber onde o projeto parou.
2. **Sempre ler** a sub-skill da fase atual antes de produzir qualquer artefato.
3. **Nunca assumir contexto** — verificar arquivos antes de operar.
4. **Toda mudança clínica** requer classificação M1/M2/M3/M4 e confirmação antes de aplicar.
5. **Solicitações de Evidência** são emitidas quando há conflito entre fontes (gatilhos G1–G6, definidos na skill `redacao-playbook`).
6. O arquivo `BANCO_EVIDENCIAS_{ESP}.md` é a autoridade clínica do projeto — nenhuma afirmação no playbook existe sem rastreamento até ele.

---

## INICIAR SESSÃO — ROTINA PADRÃO

```
1. Ler /history/session_XXX.md        → onde paramos, o que está aberto
2. Ler BANCO_EVIDENCIAS_{ESP}.md      → estado atual do banco
3. Ler sub-skill da fase atual        → o que fazer agora
4. Executar — registrar em session_YYY.md ao encerrar
```

---

## OPERAÇÃO MULTI-AGENTE — ANTIGRAVITY + CLAUDE CODE

O projeto opera com dois agentes que compartilham os mesmos artefatos:

| Agente | Interface | Foco |
|--------|-----------|------|
| **Antigravity** | Chat Claude (contexto longo) | Geração de conteúdo clínico, auditoria de evidências, redação de playbook, raciocínio longo |
| **Claude Code** | CLI / worktree | Git, scripts, validação JSON, refatoração estrutural, QA automatizado, operações de arquivo |

### Regras de convivência

1. **Ponto de encontro:** `history/session_XXX.md` — ambos os agentes leem o log mais recente ao iniciar.
2. **Qualquer agente que mude o estado do projeto** registra em session log para que o outro saiba.
3. **Kickstart específico:** Antigravity usa `tools/KICKSTART_PSIQUIATRIA.md`; Claude Code usa `tools/CLAUDECODE_KICKSTART.md`.
4. **Conflito de edição:** se ambos editaram o mesmo arquivo, prevalece a versão com session log mais recente.
5. **Delegação:** Dan decide qual agente executa cada tarefa. Na dúvida, perguntar.

---

## RETROALIMENTAÇÃO — COMO A SKILL MELHORA COM O TEMPO

Ao final de cada projeto, identificar padrões não cobertos pelas skills e emitir:

```
🔧 MELHORIA DE SKILL #N
Skill: [nome da sub-skill]
Situação não coberta: [descrição]
Comportamento atual do agente: [o que fez]
Comportamento esperado: [o que deveria fazer]
Proposta de adição: [texto sugerido para a skill]
```

Versionar a pasta `/tools/skills/` no Git. Cada projeto deixa a skill melhor para o próximo.
