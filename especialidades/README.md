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
| psiquiatria | Fase 3 — aguardando revisao clinica de Dan | v1.0 | nao iniciado |

## Para iniciar nova especialidade

1. Copiar o template: `cp tools/KICKSTART_NOVA_ESPECIALIDADE.md tools/KICKSTART_{NOVA}.md`
2. Criar subpasta: `mkdir -p especialidades/{nova}/research/`
3. Seguir o pipeline em `SKILL.md`
4. Usar `specialidades/psiquiatria/` como referencia de estrutura
