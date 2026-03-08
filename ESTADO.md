# ESTADO.md — SNAPSHOT CANÔNICO DO AMBIENTE
*Atualizado: 2026-03-08*

---

## O QUE É ESTE AMBIENTE

Ambiente daktus para produção de conteúdo clínico estruturado.

Este repositório concentra o Stage 1 do pipeline:
- briefing,
- arquitetura,
- evidências,
- auditoria,
- playbook,
- JSON.

A validação automatizada e a etapa posterior de QA podem ocorrer em fluxos, ferramentas ou repositórios complementares.

---

## BRANCH-BASE OFICIAL

Este campo deve registrar o branch-base usado como referência de continuidade entre sessões e agentes.

- Branch-base oficial: `main`

Se este valor mudar, atualizar também `HANDOFF.md`.

---

## ESTADO ATUAL CONSOLIDADO

### Frente 1 — Ginecologia
- Status macro: referência madura do pipeline
- Papel atual: benchmark estrutural, arquitetural e histórico de auditoria
- Situação: artefato de referência já disponível no ambiente

### Frente 2 — Psiquiatria
- Status macro: especialidade ativa
- Fase atual consolidada: **Fase 5 — QA iterativo (patches de design)**
- Gate clínico: playbook auditado ✅ | JSON v0.1.1 produzido ✅ | Auditoria PASSOU — 0 BLOQUEANTES ✅
- Artefato ativo: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.1.json`
  - 9 nodes, 8 edges, 75 questões
  - Nó summary (Processamento Clínico): 3 expressões de risco C-SSRS corrigidas
  - Nó conduta enfermagem (pausa): handoff enfermagem → médico
  - Nó 6 (Conduta Medicina): 9 alertas, 25 exames TUSS, 13 encaminhamentos, 9 medicamentos
  - 0 BLOQUEANTES na auditoria | 44 revisão (escopo v0.1.2–v0.1.4)
- Artefatos de suporte:
  - `tools/GUIA_DESIGN_UX.md` — guia de design UX consolidado
  - `scripts/audit_design_v01.py` — auditoria estrutural
  - `scripts/patch_vdraft_to_v011.py` — script de patch aplicado
- Próximo passo macro: QA clínico do v0.1.1 no preview Daktus, depois patch v0.1.2

### Infraestrutura do ambiente
- Status macro: refatoração lean inicial integrada
- Situação atual:
  - `AGENTE.md` definido como ponto único de entrada;
  - `HANDOFF.md` definido como estado operacional curto;
  - `ESTADO.md` mantido como snapshot canônico;
  - `CLAUDE.md` reduzido a bootstrap mínimo;
  - `SKILL.md` reposicionado como orchestrator do pipeline.
- Próximo passo macro: consolidar uso do novo regime e alinhar workflows, sub-skills e rotinas auxiliares ao boot centralizado

---

## ARTEFATOS CANÔNICOS

### Arquivos-mestre de operação
- `AGENTE.md` — ponto único de entrada
- `HANDOFF.md` — estado operacional curto
- `ESTADO.md` — snapshot canônico
- `CLAUDE.md` — bootstrap mínimo
- `SKILL.md` — orchestrator do pipeline
- `README.md` — visão estável do ambiente

### Método agnóstico
- `tools/skills/*/SKILL.md`
- `tools/AGENT_PROMPT_PROTOCOLO_DAKTUS.md`
- `tools/PADROES_ARQUITETURA_JSON.md`
- `tools/GUARDRAIL_EVIDENCIAS.md`
- `tools/CONTEXTO_FERRAMENTAS_E_METODOS.md`
- `tools/KICKSTART_NOVA_ESPECIALIDADE.md`

### Registro e rastreabilidade
- `history/session_NNN.md`

### Frentes ativas
- `especialidades/ginecologia/`
- `especialidades/psiquiatria/`

### Referências read-only
- `referencia/`

---

## DECISÕES CRÍTICAS VIGENTES

- Nunca avançar de fase sem liberação explícita do usuário ou gate documental claro.
- Ginecologia é benchmark estrutural, não fonte para copiar lógica clínica.
- O ambiente opera por progressive disclosure: ler apenas a fase ativa e os apoios necessários.
- `HANDOFF.md` é a camada operacional curta; `ESTADO.md` é o snapshot canônico.
- `history/` é registro arquivístico, não ponto de entrada primário.
- Projetos entregues ficam em `referencia/`; frentes ativas ficam em `especialidades/`.
- Toda sessão significativa deve produzir continuidade rastreável.
- Instrução explícita do usuário tem prioridade sobre snapshots antigos, conforme a ordem de autoridade definida em `AGENTE.md`.

---

## ÚLTIMA SESSÃO INTEGRADA

- Sessão: session_015 — Fase 5 Psiquiatria — Patch v0.1.1 (2026-03-08)
- Commit: ver HANDOFF.md
- Foco: GUIA_DESIGN_UX.md, audit_design_v01.py, patch vdraft→v0.1.1 (25 modificações, 0 BLOQUEANTES)

---

## PRÓXIMO PASSO MACRO

1. QA clínico do v0.1.1 no ambiente de preview Daktus.
2. Patch v0.1.2 — conectar uids de alta prioridade à conduta (A3 prioridade 1).
3. Patch v0.1.3 — mapear scores diagnósticos a thresholds de conduta.
4. Patch v0.1.4 — avaliar uids informativos (manter, conectar ou remover).
5. Aprovar e promover versão para v1.0.0 após QA completo.

---

## ORDEM MÍNIMA DE RETOMADA

1. `AGENTE.md`
2. `HANDOFF.md`
3. `ESTADO.md`
4. `SKILL.md`
5. sub-skill da fase atual
6. `history/session_XXX.md` mais recente, se necessário