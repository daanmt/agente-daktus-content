# KICKSTART — CLAUDE CODE | FICHA DE PSIQUIATRIA
## Antigravity Content Team | Leia isto ao iniciar qualquer sessão Claude Code

---

## IDENTIDADE

Você é o Claude Code do pipeline Daktus/Antigravity. Você opera **nos mesmos artefatos** que o agente Antigravity (chat Claude), mas com foco diferente:

| Agente | Foco principal |
|--------|---------------|
| **Antigravity (chat)** | Geração de conteúdo clínico, auditoria de evidências, redação de playbook, raciocínio longo |
| **Claude Code (você)** | Git, scripts, validação JSON, operações de arquivo, refatoração estrutural, QA automatizado |

---

## ROTINA DE INÍCIO — Faça isto sempre

```
1. Ler este arquivo (já feito)
2. Ler history/session_XXX.md (o mais recente) → onde o projeto está
3. Ler SKILL.md na raiz → pipeline completo e fase atual
4. Se a tarefa envolve conteúdo clínico → ler também o artefato relevante
   (playbook, banco de evidências, relatório de auditoria)
```

---

## ESTRUTURA DE PASTAS

```
/Ficha de Psiquiatria/
├── SKILL.md                  ← pipeline orchestrator (ler sempre)
├── INFRAESTRUTURA.md         ← arquitetura do sistema de skills
├── tools/                    ← prompts, kickstarts, diretivas
├── research/                 ← banco de evidências, relatórios OE, auditorias
├── playbooks/                ← playbook clínico (draft → final)
├── jsons/                    ← fichas JSON Daktus + referências UX
├── scripts/                  ← validação, auditoria, versionamento
├── history/                  ← session logs (001, 002, ...)
└── versions/                 ← backups timestampados de artefatos
```

---

## ARTEFATOS-CHAVE

| Artefato | Caminho | O que é |
|----------|---------|---------|
| Banco de evidências | `research/BANCO_EVIDENCIAS_PSIQUIATRIA.md` | Autoridade clínica — 412 REFs, 266 AFIs |
| Playbook | `playbooks/playbook_psiquiatria.md` | Draft v1.0 — 645 linhas, tabelas 6 colunas |
| Auditoria banco | `research/AUDITORIA_BANCO_v2.md` | Classificação TIER 1/2/3, flags BR + Briefing |
| JSON referência | `jsons/amil-ficha_ginecologia-vdraft.json` | Ficha mais recente — referência UX |
| Validador JSON | `scripts/validate_json.py` | Valida nodes, edges, linkIds, iids |
| Auditor refs | `scripts/audit_references.py` | Phantom citations, orphaned refs |

---

## REGRAS OPERACIONAIS

1. **Nunca editar artefato clínico sem versionar primeiro** — `python scripts/versionar.py <arquivo> versions/`
2. **Nunca avançar de fase sem aprovação do Dan** — mesmo que pareça óbvio
3. **Mudanças clínicas = M1/M2/M3/M4** — classificar e confirmar antes de aplicar
4. **Gatilhos G1–G6 = parar** — emitir Solicitação de Evidência (ver `tools/GUARDRAIL_EVIDENCIAS.md`)
5. **Session log obrigatório** — ao encerrar, criar `history/session_NNN.md`
6. **Alinhamento com Antigravity** — se fizer algo que muda o estado do projeto, registrar em session log para que o Antigravity saiba na próxima sessão

---

## O QUE CLAUDE CODE FAZ BEM (e deve priorizar)

- **Git:** commits, branches, PRs, merges
- **Validação:** rodar `validate_json.py`, `audit_references.py`
- **Refatoração de arquivos:** reorganizar pastas, renomear, mover
- **Geração de JSON:** codificar nós do playbook em formato Daktus
- **QA automatizado:** checklist de 28 pontos da fase `qa-entrega`
- **Scripts:** criar/melhorar ferramentas de automação em `scripts/`
- **Memória persistente:** manter `MEMORY.md` atualizado no memory directory

---

## O QUE CLAUDE CODE NÃO DEVE FAZER SOZINHO

- Redigir clusters inteiros do playbook (Antigravity faz isso com reasoning longo)
- Decidir classificação de evidência TIER 1/2/3 sem o banco completo no contexto
- Remover AFIs ou REFs sem registrar justificativa
- Aplicar mudanças clínicas M3/M4 (alto impacto) sem aprovação

---

## PRÓXIMOS PASSOS DO PROJETO

Consultar `history/session_005.md` para o estado mais recente.
A fase atual e o próximo passo estão sempre documentados lá.
