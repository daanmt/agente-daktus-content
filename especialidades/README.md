# especialidades/

Esta pasta contem os **artefatos de produto** de cada especialidade desenvolvida.

Cada subpasta e uma especialidade com seus proprios:
- `research/` — banco de evidencias, auditorias, relatorios OpenEvidence
- `playbooks/` — playbook clinico validado
- `jsons/` — fichas JSON implementadas na plataforma Daktus
- `history/` — log de sessoes de trabalho

## Especialidades disponíveis

| Especialidade | Status | Playbook | JSON |
|--------------|--------|---------|------|
| ginecologia | Auditoria JSON (sessao 008) — aguardando Dan aplicar C1-C4 | v1.0 auditado | vdraft2 em revisao |
| psiquiatria | Fase 3 — aguardando revisao clinica de Dan | v1.0 | nao iniciado |

## Especialidades entregues (referencia — ficam na raiz)

Fichas ja entregues na plataforma. JSONs e playbooks ficam em `jsons/` e `playbooks/` na raiz como referencia transversal.

| Especialidade | JSON | Playbook |
|--------------|------|---------|
| cardiologia | `jsons/amil-ficha_cardiologia-v2.0.9.json` | `playbooks/Playbook Clinico — Ficha de Cardiologia...` |
| reumatologia | `jsons/inclua-ficha_reumatologia-v1.1.0.json` | `playbooks/playbook_reumatologia.md` |

## Para iniciar nova especialidade

1. Copiar o template: `cp tools/KICKSTART_NOVA_ESPECIALIDADE.md tools/KICKSTART_{NOVA}.md`
2. Criar subpasta: `mkdir -p especialidades/{nova}/research/`
3. Seguir o pipeline em `SKILL.md`
4. Usar `specialidades/psiquiatria/` como referencia de estrutura
