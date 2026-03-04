# SKILL — PIPELINE DE PRODUCAO DAKTUS
## Orchestrator | Antigravity Content Team

---

## O QUE ESTA SKILL FAZ

Esta e a skill mestra do pipeline de producao de fichas clinicas Daktus. Define a arquitetura de pastas, descreve todas as sub-skills e determina quando invocar cada uma. O agente **nunca avanca de fase sem aprovacao explicita do usuario**.

---

## ARQUITETURA CANONICA DE PROJETO

```
agente-daktus-content/
├── ESTADO.md                 ← fonte de verdade do estado atual
├── CLAUDE.md                 ← protocolo de inicio de sessao
├── SKILL.md                  ← este arquivo (orchestrator)
├── README.md
│
├── tools/                    ← metodo agnostico
│   ├── skills/               ← 7 sub-skills (uma por fase)
│   ├── AGENT_PROMPT_PROTOCOLO_DAKTUS.md    ← instrucoes tecnicas JSON
│   ├── CONTEXTO_FERRAMENTAS_E_METODOS.md   ← como usar bash/python/git
│   ├── GUARDRAIL_EVIDENCIAS.md             ← gatilhos G1-G6
│   ├── KICKSTART_NOVA_ESPECIALIDADE.md     ← template de onboarding
│   └── PADROES_ARQUITETURA_JSON.md         ← padroes reutilizaveis
│
├── especialidades/
│   └── {nome}/
│       ├── research/         ← banco de evidencias, auditorias, relatorios OE
│       ├── playbooks/        ← playbook clinico (draft → final)
│       └── jsons/            ← fichas JSON produzidas
│
├── referencia/               ← JSONs e playbooks de projetos ja entregues (read-only)
│
├── history/                  ← UNICO diretorio de sessions (001, 002, ...)
│   └── session_{NNN}.md
│
└── scripts/                  ← automacao e validacao
    ├── validate_json.py
    ├── audit_references.py
    ├── audit_logic.py
    └── versionar.py
```

**Arquivo mais importante por especialidade:** `especialidades/{nome}/research/BANCO_EVIDENCIAS_{ESP}.md`
E a autoridade clinica. Toda afirmacao do playbook deve rastrear ate uma entrada deste arquivo.

---

## LOGICA DE ATIVACAO (PROGRESSIVE DISCLOSURE)

O agente conhece todas as skills por este orchestrator — que lista apenas nome e descricao de cada sub-skill. O conteudo completo de cada skill so e lido quando a fase e ativada. Isso preserva a janela de contexto para o trabalho real.

| Dimensao | Agente monolitico | Skills (este modelo) |
|----------|-------------------|---------------------|
| Janela de contexto | Carrega tudo sempre | Carrega apenas a fase atual |
| Manutencao | Requer redeploy | Editar o `.md` da sub-skill |
| Aprendizado | Estatico apos deploy | Retroalimentacao continua via Git |
| Portabilidade | Acoplado a plataforma | Pasta de arquivos — funciona em qualquer LLM |
| Foco operacional | Pode misturar fases | Cada sessao = uma fase = uma skill |
| Reproduzibilidade | Baixa | Alta — mesma pasta para qualquer especialidade |

---

## SUB-SKILLS DISPONIVEIS

| Skill | Pasta | Invocar quando |
|-------|-------|----------------|
| `briefing-arquitetura` | `/tools/skills/briefing-arquitetura/` | Inicio de projeto — especialidade nova |
| `ingestao-evidencias` | `/tools/skills/ingestao-evidencias/` | Ao receber relatorio do OpenEvidence |
| `auditoria-banco` | `/tools/skills/auditoria-banco/` | Antes de iniciar qualquer cluster do playbook |
| `redacao-playbook` | `/tools/skills/redacao-playbook/` | Apos auditoria do banco aprovada |
| `auditoria-playbook` | `/tools/skills/auditoria-playbook/` | Apos draft completo de cada cluster |
| `codificacao-json` | `/tools/skills/codificacao-json/` | Apos playbook aprovado clinicamente |
| `qa-entrega` | `/tools/skills/qa-entrega/` | Antes de entregar para homologacao |

---

## SEQUENCIA INVIOLAVEL DE FASES

```
FASE 0  →  briefing-arquitetura      (mapa de nos aprovado)
        ↓
        →  ingestao-evidencias        (loop continuo — relatorios OE chegam ao longo do projeto)
        ↓
FASE 2* →  auditoria-banco           (pre-auditoria antecipada antes do playbook)
        ↓
FASE 1  →  redacao-playbook          (cluster por cluster — ordem definida na skill)
        ↓
FASE 2  →  auditoria-playbook        (citation, semantic, coverage scans)
        ↓
FASE 3  →  [revisao clinica humana — sem skill]
        ↓
FASE 4  →  codificacao-json          (paper design → TUSS → JSON → validacao)
        ↓
FASE 5  →  qa-entrega                (28 checks antes da entrega)
```

*A Fase 2 de auditoria do banco e antecipada por decisao estrategica — banco inflado contamina o playbook.

---

## REGRAS GERAIS DE COMPORTAMENTO

1. **Sempre ler** `ESTADO.md` e `history/session_XXX.md` (mais recente) antes de qualquer acao.
2. **Sempre ler** a sub-skill da fase atual antes de produzir qualquer artefato.
3. **Nunca assumir contexto** — verificar arquivos antes de operar.
4. **Toda mudanca clinica** requer classificacao M1/M2/M3/M4 e confirmacao antes de aplicar.
5. **Solicitacoes de Evidencia** sao emitidas quando ha conflito entre fontes (gatilhos G1-G6, definidos na skill `redacao-playbook`).
6. O arquivo `BANCO_EVIDENCIAS_{ESP}.md` e a autoridade clinica do projeto — nenhuma afirmacao no playbook existe sem rastreamento ate ele.

---

## INICIAR SESSAO — ROTINA PADRAO

```
1. Ler ESTADO.md                     → onde estamos, o que esta aberto
2. Ler history/session_XXX.md        → ultima sessao detalhada
3. Ler sub-skill da fase atual       → o que fazer agora
4. Executar — registrar em session_YYY.md ao encerrar
```

---

## OPERACAO MULTI-AGENTE

O projeto opera com agentes que compartilham os mesmos artefatos:

| Agente | Interface | Foco |
|--------|-----------|------|
| **Antigravity** | Chat Claude (contexto longo) | Geracao de conteudo clinico, auditoria de evidencias, redacao de playbook, raciocinio longo |
| **Claude Code** | CLI / terminal | Git, scripts, validacao JSON, refatoracao estrutural, QA automatizado, operacoes de arquivo |

### Regras de convivencia

1. **Ponto de encontro:** `ESTADO.md` + `history/session_XXX.md` — todo agente le ao iniciar.
2. **Qualquer agente que mude o estado do projeto** registra em session log.
3. **Conflito de edicao:** prevalece a versao com session log mais recente.
4. **Delegacao:** Dan decide qual agente executa cada tarefa. Na duvida, perguntar.

---

## RETROALIMENTACAO — COMO A SKILL MELHORA COM O TEMPO

Ao final de cada projeto, identificar padroes nao cobertos pelas skills e emitir:

```
MELHORIA DE SKILL #N
Skill: [nome da sub-skill]
Situacao nao coberta: [descricao]
Comportamento atual do agente: [o que fez]
Comportamento esperado: [o que deveria fazer]
Proposta de adicao: [texto sugerido para a skill]
```

Versionar a pasta `/tools/skills/` no Git. Cada projeto deixa a skill melhor para o proximo.
