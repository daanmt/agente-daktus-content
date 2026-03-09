# ESTADO.md — SNAPSHOT CANÔNICO DO AMBIENTE
*Atualizado: 2026-03-08 (session_016)*

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
- Gate clínico: playbook auditado ✅ | JSON v0.1.2 produzido ✅ | Auditoria PASSOU — 0 BLOQUEANTES ✅
- Artefato ativo: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json`
  - 9 nodes, 8 edges
  - Violações same-node corrigidas: 5 perguntas movidas entre nós (Grupos A)
  - Nó summary (Processamento Clínico): 3 expressões de risco C-SSRS corrigidas (session_015)
  - Nó conduta enfermagem (pausa): 3 mensagens de handoff por nível de risco adicionadas
  - Nó 6 (Conduta Medicina): 21 alertas, 25 exames TUSS (categorizados), 14 encaminhamentos, 13 medicamentos, 4 orientações (77 items total)
  - 0 BLOQUEANTES na auditoria | 32 A3 (contexto clínico + monitoramento farmacológico)
- Artefatos de suporte:
  - `tools/GUIA_DESIGN_UX.md` — guia de design UX consolidado
  - `scripts/audit_design_v01.py` — auditoria estrutural
  - `scripts/patch_vdraft_to_v011.py` — patch v0.1.1
  - `scripts/patch_v011_to_v012.py` — patch v0.1.2 (boolean fixes + alertas clínicos)
  - `scripts/patch_v012_improvements.py` — quality patch v0.1.2 (46 mod.: same-node, emojis, categorias, handoff, antipsicóticos, orientações, coesão)
- Próximo passo macro: QA clínico do v0.1.2 no preview Daktus

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

- Sessão: session_016 — Fase 5 Psiquiatria — Quality Patch v0.1.2 (2026-03-08)
- Foco: quality patch (46 mod.) — same-node fixes, emojis, categorias, handoff, antipsicóticos, orientações, coesão
- Resultado: 0 BLOQUEANTES | 32 A3 residuais (legítimos)

---

## PRÓXIMO PASSO MACRO

1. QA clínico do v0.1.2 no preview Daktus (3 perfis críticos).
2. Ajustar conduta e condicionais conforme feedback clínico.
3. Avaliar 32 uids A3 residuais: manter como contexto ou conectar a conduta.
4. Aprovar e promover versão para v1.0.0 após QA completo.

---

## ORDEM MÍNIMA DE RETOMADA

1. `AGENTE.md`
2. `HANDOFF.md`
3. `ESTADO.md`
4. `SKILL.md`
5. sub-skill da fase atual
6. `history/session_XXX.md` mais recente, se necessário