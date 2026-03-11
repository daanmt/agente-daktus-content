# ESTADO.md — SNAPSHOT CANÔNICO DO AMBIENTE
*Atualizado: 2026-03-11 (session_029)*

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
- Gate clínico: playbook auditado ✅ | JSON v0.8.0 produzido ✅ | Auditoria PASSOU — 0 BLOQUEANTES ✅
- Artefato ativo: `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.8.0.json`
  - 8 nodes (−1 vs v0.7.0), 7 edges (−1 vs v0.7.0), 115 IIDs (−12 vs v0.7.0)
  - motivo_consulta: **14 opções** (inalterado)
  - diagnostico_ativo: **19 opções** (inalterado)
  - Triagem Enfermagem: **tipo_consulta** presente (shortcut retorno, Onda 2)
  - node-psiq-04-diagnostico: **23 perguntas** (inalterado)
  - node-psiq-05-farmacos: **7 perguntas** (inalterado)
  - Nó 6 (Conduta Medicina): **37 medicamentos** (inalterado), 25 exames, **9 encaminhamentos** (−4), **~35 mensagens** (−2), **9 orientações** (−3)
  - clinicalExpressions: **25** (preservadas 100% da Onda 5)
  - Fluxo: único médico — nó intermediário Conduta Enfermagem removido
  - 0 BLOQUEANTES ✅ | 10 eixos de discriminação sindrômica
  - v0.8.0 = v0.7.0 + Merge do Gestor session_029 + 49 mudanças
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
  - `scripts/patch_vdraft3_to_v023.py` — fechamento de hiatos do briefing (session_023)
  - `scripts/patch_v023_to_v030.py` — dissecção sindrômica intermediária (session_024)
  - `scripts/patch_v030_to_v040.py` — Onda 2: 4 eixos discriminatórios + shortcut retorno (session_025)
  - `scripts/patch_v040_to_v050.py` — Onda 3: 7 gaps + 2 bugs de segurança (session_026)
  - `scripts/patch_v050_to_v060.py` — Onda 4: Quality & Precision Reform (session_027)
  - `scripts/patch_v061_to_v070.py` — Onda 5: Reforma Sindrômica (session_028)
  - `scripts/patch_v070_to_v080.py` — Merge do Gestor: fluxo único médico + enxugamento (session_029)
- Próximo passo macro: QA clínico de v0.8.0 no preview Daktus (perfis críticos expandidos)

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

- Sessão: session_029 — Merge do Gestor → v0.8.0 (2026-03-11)
- Foco: reforma arquitetural (fluxo único médico, −1 nó, −1 edge) + enxugamento conduta (−3 orient, −4 encam, −2 msg) + merge GESTANTE + limpeza CAPS/SAMU + 20 acentos
- Resultado: 0 BLOQUEANTES, 115 IIDs, 25 clinicalExpressions (preservadas), 9 orientações, metadata.version = "0.8.0"

---

## PRÓXIMO PASSO MACRO

1. QA clínico de v0.8.0 no preview Daktus (perfis críticos expandidos):
   - **[Novo — Onda 5]** Depressão provável sem diagnóstico formal → Escitalopram via `candidato_isrs_depressao`
   - **[Novo — Onda 5]** TAG provável → Escitalopram/Sertralina/Venlafaxina via `tag_provavel`
   - **[Novo — Onda 5]** TDAH confirmado operacionalmente → Metilfenidato via `tdah_confirmado_operacional`
   - Alto risco suicida com acesso a meios → restrição de meios letais + fórmulas risco recalibradas
   - Mulher grávida em uso de valproato **ou lítio** → alerta GESTANTE+PSICOTRÓPICO (mensagem unificada)
   - Esquizofrenia refratária → clozapina + hemograma + orientação clozapina
   - TDAH com TDM → Metilfenidato (`tdah_confirmado_operacional`) + Bupropiona (`candidato_isrs_depressao`)
   - Depressão com rastreio bipolar positivo → alerta BIPOLAR NÃO DESCARTADO
   - **[Onda 3]** Primeiro episódio psicótico → alerta investigação orgânica
   - **[Onda 3]** Mania grave com psicose/agitação → mensagem urgência (sem SAMU — "serviço de urgência psiquiátrica")
2. Confirmar MEVOs com equipe Amil (ver `history/session_022_report_farmacologia.md`).
3. Confirmar Escitalopram MEVO 20945 (inserido manualmente, não verificado no Mevo..xlsx).
4. v0.9.0 / Onda 6 — fármacos de 2ª linha (Fluvoxamina, Clomipramina, Guanfacina XR, Prazosina, Buspirona) + limpeza de perguntas sem conduta (32 UIDs A3).
5. Promover para v1.0.0 após QA clínico completo.

---

## ORDEM MÍNIMA DE RETOMADA

1. `AGENTE.md`
2. `HANDOFF.md`
3. `ESTADO.md`
4. `SKILL.md`
5. sub-skill da fase atual
6. `history/session_XXX.md` mais recente, se necessário