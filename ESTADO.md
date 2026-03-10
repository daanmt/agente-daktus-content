# ESTADO.md — SNAPSHOT CANÔNICO DO AMBIENTE
*Atualizado: 2026-03-10 (session_022)*

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
- Fase atual consolidada: **Fase 5 — QA iterativo → próximo: QA clínico no preview Daktus**
- Gate clínico: playbook auditado ✅ | JSON v0.2.2 produzido ✅ | Auditoria PASSOU — 0 BLOQUEANTES ✅
- Artefato ativo: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.2.json`
  - 9 nodes, 8 edges, 94 IIDs
  - **37 perguntas** (era 42 em v0.2 — usuário removeu 5 escores; era 66 em v0.1.2)
  - Nó 6 (Conduta Medicina): **28 medicamentos**, 0 BLOQUEANTES
  - TUSS: 100% populados ✅ | MEVO: 19/28 (9 não no catálogo Amil — documentado)
  - v0.2.2 = vdraft (2) do usuário + correções estruturais (4 grupos de bugs) + 11 fármacos adicionados (session_022)
- Artefatos de suporte:
  - `tools/GUIA_DESIGN_UX.md` — guia de design UX + DSL rules (§2.1 + §5 atualizados)
  - `skills/daktus-json-coding/scripts/validate_json.py` — validação estrutural generalizada
  - `scripts/audit_design_v01.py` — auditoria estrutural (legado)
  - `scripts/patch_vdraft_to_v011.py` — patch v0.1.1
  - `scripts/patch_v011_to_v012.py` — patch v0.1.2
  - `scripts/patch_v012_improvements.py` — quality patch v0.1.2 (46 mod.)
  - `scripts/patch_v012_conditional_fix.py` — validador/corretor DSL
  - `scripts/patch_v012_to_v02.py` — patch v0.2 (24 remoções + 12 simplificações)
  - `scripts/patch_v021_fixes.py` — fixes de alertas e metadata v0.2.1 (session_021)
  - `scripts/patch_v021_to_v03_codigos.py` — TUSS/MEVO population (session_021)
  - `scripts/patch_vdraft2_to_v022.py` — correção estrutural + 11 fármacos (session_022)
- Próximo passo macro: QA clínico de v0.2.2 no preview Daktus (4 perfis críticos)

### Infraestrutura do ambiente
- Status macro: arquitetura de duas camadas implementada (session_020)
- Situação atual:
  - `AGENTE.md` definido como ponto único de entrada;
  - `HANDOFF.md` definido como estado operacional curto;
  - `ESTADO.md` mantido como snapshot canônico;
  - `CLAUDE.md` reduzido a bootstrap mínimo;
  - `SKILL.md` reposicionado como orchestrator do pipeline;
  - `skills/` = nova camada de skills exportáveis padrão Anthropic;
  - `skills/daktus-json-coding/` = skill piloto (SKILL.md + references/ + scripts/ + assets/).
- Próximo passo macro: validar skill piloto em uso real; deprecar `tools/skills/codificacao-json/` quando skill exportável provar-se funcional

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
- `tools/skills/*/SKILL.md` — sub-skills do pipeline interno
- `tools/AGENT_PROMPT_PROTOCOLO_DAKTUS.md`
- `tools/PADROES_ARQUITETURA_JSON.md`
- `tools/GUARDRAIL_EVIDENCIAS.md`
- `tools/CONTEXTO_FERRAMENTAS_E_METODOS.md`
- `tools/KICKSTART_NOVA_ESPECIALIDADE.md`

### Skills exportáveis (padrão Anthropic)
- `skills/daktus-json-coding/` — compila playbook auditado em JSON Daktus

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

- Sessão: session_022 — Correção estrutural + fármacos faltantes → v0.2.2 (2026-03-10)
- Foco: benchmarking e correção de 4 grupos de bugs estruturais nos medicamentos, adição de 11 fármacos essenciais do playbook
- Resultado: 0 BLOQUEANTES, 28 medicamentos, schema 28/28 canônico, MEVO 19/28, metadata.version = "0.2.2"

---

## PRÓXIMO PASSO MACRO

1. QA clínico de v0.2.2 no preview Daktus (4 perfis críticos):
   - Alto risco suicida com acesso a meios → verificar restrição de meios letais
   - Mulher grávida em uso de valproato → verificar alerta gestante+VPA + Valproato como prescrição
   - Esquizofrenia refratária → verificar indicação de clozapina (25mg agora presente)
   - TDAH com TDM → verificar prescrições simultâneas (Metilfenidato + Bupropiona)
2. Confirmar 9 MEVOs ausentes com equipe Amil (ver `history/session_022_report_farmacologia.md`).
3. Confirmar Escitalopram MEVO 20945 (inserido manualmente, não verificado no Mevo..xlsx).
4. v0.3 — adicionar fármacos de 2ª linha (Fluvoxamina, Clomipramina, Guanfacina XR, Prazosina, Buspirona) + encaminhamentos faltantes.
5. Promover para v1.0.0 após QA completo.

---

## ORDEM MÍNIMA DE RETOMADA

1. `AGENTE.md`
2. `HANDOFF.md`
3. `ESTADO.md`
4. `SKILL.md`
5. sub-skill da fase atual
6. `history/session_XXX.md` mais recente, se necessário