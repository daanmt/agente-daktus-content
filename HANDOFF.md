# HANDOFF.md — ESTADO OPERACIONAL CURTO
*Atualizado: 2026-03-07*

---

## ESTADO OPERACIONAL ATUAL

- Branch-base: `main`
- Última sessão integrada: refatoração inicial dos arquivos-mestre
- Especialidade/tema ativo: Psiquiatria + consolidação da infraestrutura lean do ambiente
- Fase atual: Fase 4 — codificação JSON
- Artefato em produção: arquitetura de transição para JSON de Psiquiatria sob o novo regime de boot e continuidade

---

## O QUE JÁ ESTÁ INTEGRADO

- `AGENTE.md` definido como ponto único de entrada
- `HANDOFF.md` instituído como estado operacional curto
- `ESTADO.md` reposicionado como snapshot canônico
- `CLAUDE.md` reduzido a bootstrap mínimo
- `SKILL.md` reposicionado como orchestrator do pipeline
- decisão de operar o ambiente sob lógica lean, state-driven e multiagente

---

## O QUE ESTÁ ABERTO AGORA

- validar, em uso real, a consistência do novo regime de boot
- alinhar workflows, sub-skills e documentos auxiliares ainda presos ao fluxo anterior
- registrar a primeira sessão completa já operando integralmente sob o novo modelo
- iniciar codificação JSON de Psiquiatria com base no playbook já auditado
- verificar se os caminhos documentados refletem exatamente a estrutura real do repositório local

---

## PRÓXIMO PASSO RECOMENDADO

1. confirmar que os arquivos-mestre refatorados já são a fonte operacional vigente;
2. revisar workflows e documentos auxiliares que ainda possam apontar para o fluxo antigo;
3. registrar `history/session_NNN.md` desta transição;
4. abrir a próxima sessão já usando `AGENTE.md` como boot obrigatório;
5. iniciar a execução disciplinada da Fase 4 de Psiquiatria.

---

## ARQUIVOS A LER NESTA CONTINUIDADE

1. `AGENTE.md`
2. `HANDOFF.md`
3. `ESTADO.md`
4. `SKILL.md`
5. `tools/skills/codificacao-json/SKILL.md`
6. artefatos de Psiquiatria em `especialidades/psiquiatria/`
7. benchmark de Ginecologia em `especialidades/ginecologia/`

---

## NÃO SOBRESCREVER SEM REVISAR

- fase atual de Psiquiatria
- branch-base oficial
- decisões críticas vigentes
- papel de Ginecologia como benchmark estrutural
- separação entre `HANDOFF.md` e `ESTADO.md`
- centralidade de `AGENTE.md` como ponto de entrada

---

## DIVERGÊNCIAS TEMPORÁRIAS / OVERRIDES

- Alguns snapshots antigos do repositório ainda podem refletir o fluxo anterior do ambiente.
- O estado operacional vigente é o definido pelos arquivos-mestre refatorados e pela ordem de autoridade descrita em `AGENTE.md`.
- Para Psiquiatria, seguir o estado operacional mais recente:
  - playbook auditado;
  - início do JSON liberado.