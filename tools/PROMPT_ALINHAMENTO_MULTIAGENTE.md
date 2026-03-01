# PROMPT REUTILIZÁVEL — ALINHAMENTO MULTI-AGENTE
## Para uso em qualquer projeto operado via Antigravity + Claude Code
## Antigravity Content Team | v1.0 | 2026-03-01

---

## QUANDO USAR ESTE PROMPT

Cole este prompt no Claude Code ao iniciar um novo projeto (ou ao integrar o Claude Code em um projeto que já existia apenas no Antigravity/chat). Ele executa três coisas:

1. **Auditoria de infraestrutura** — verifica se a estrutura de pastas, skills e artefatos estão no lugar certo
2. **Setup de memória** — cria a memória persistente do Claude Code para o projeto
3. **Protocolo de convivência** — estabelece como Antigravity e Claude Code coexistem sem conflito

---

## PROMPT — COPIE DAQUI PARA BAIXO

---

Você é o Claude Code do pipeline Daktus/Antigravity. Estou te integrando a um projeto que pode já ter histórico de sessões via Antigravity (chat Claude). Seu trabalho é se alinhar ao projeto e estabelecer a infraestrutura para que ambos os agentes (você e o Antigravity) operem nos mesmos artefatos sem conflito.

### CONTEXTO

- **Projeto:** [NOME DO PROJETO — ex: IPUB, Ficha de Ginecologia, etc.]
- **Raiz do projeto:** [CAMINHO COMPLETO — ex: C:\Users\daanm\OneDrive\Desktop\Daktus\IPUB]
- **Já tem histórico no Antigravity?** [SIM/NÃO]
- **Tem SKILL.md ou INFRAESTRUTURA.md?** [SIM/NÃO — se não, será necessário criar]

### O QUE FAZER — Execute nesta ordem

#### FASE 1 — Reconhecimento

1. Liste toda a árvore de arquivos e pastas do projeto (excluindo `.git/` e `.claude/`)
2. Identifique se existe `SKILL.md`, `INFRAESTRUTURA.md`, `history/`, `tools/`, `research/`, `playbooks/`, `jsons/`, `scripts/`, `versions/`
3. Leia o session log mais recente em `history/` (se existir) para entender o estado do projeto
4. Leia `SKILL.md` e/ou `INFRAESTRUTURA.md` (se existirem) para entender a arquitetura esperada

#### FASE 2 — Auditoria de integridade

Compare a estrutura real contra a arquitetura canônica e reporte:

1. **Pastas faltantes** — quais das pastas canônicas não existem?
2. **Skills deslocadas** — sub-skills que estão em `mnt/`, na raiz, ou soltas em `tools/` ao invés de `tools/skills/{nome}/SKILL.md`?
3. **Artefatos fantasma** — arquivos referenciados nos session logs que não existem no disco (provavelmente gerados no chat e nunca exportados)?
4. **Arquivos supersedidos** — diretivas de sessão, logs de chat, documentos de fase já concluída que estão misturados com skills ativas?
5. **Pastas órfãs** — diretórios como `mnt/`, `user-data/`, etc. que são resíduo de export?

Apresente o relatório em formato de tabela antes de executar qualquer correção. Aguarde minha aprovação.

#### FASE 3 — Correções (após aprovação)

1. **Mover sub-skills** para `tools/skills/{nome}/SKILL.md` (local canônico)
2. **Arquivar** documentos supersedidos em `history/` com nome descritivo
3. **Remover** pastas órfãs de export
4. **Criar pastas faltantes** da arquitetura canônica

#### FASE 4 — Setup multi-agente

1. **Criar `tools/CLAUDECODE_KICKSTART.md`** com:
   - Identidade do Claude Code no projeto
   - Rotina de início (ler session log → ler SKILL.md → ler artefato da fase atual)
   - Lista de artefatos-chave com caminhos
   - Regras operacionais (versionamento, gatilhos, aprovação)
   - O que Claude Code faz vs. o que Antigravity faz

2. **Adicionar seção "OPERAÇÃO MULTI-AGENTE" ao `SKILL.md`** (se já existir) com:
   - Tabela: Antigravity = conteúdo clínico/raciocínio longo | Claude Code = Git/scripts/JSON/QA/arquivos
   - Regras de convivência:
     - Ponto de encontro: `history/session_XXX.md`
     - Qualquer agente que mude estado → registra em session log
     - Kickstarts separados (Antigravity → `KICKSTART_{ESP}.md`, Claude Code → `CLAUDECODE_KICKSTART.md`)
     - Conflito de edição → prevalece session log mais recente
     - Delegação → Dan decide

3. **Salvar memória persistente** no memory directory do Claude Code (`MEMORY.md` + arquivos de detalhe) com:
   - Estado atual do projeto (fase, artefatos existentes, pendências)
   - Convenções do projeto
   - Divisão de agentes

#### FASE 5 — Session log

Criar `history/session_NNN.md` documentando:
- O que foi feito nesta sessão
- Correções aplicadas
- Artefatos fantasma identificados (se houver)
- Estado final da estrutura de pastas
- Próximos passos

### REGRAS

- Não editar conteúdo clínico — apenas reorganizar estrutura
- Não remover nada sem registrar a justificativa no session log
- Não assumir que arquivos existem — verificar antes de referenciar
- Se o projeto não tem `SKILL.md`, perguntar se devo criar um baseado no template canônico
- Aguardar aprovação explícita antes de mover/remover arquivos

---

*Fim do prompt reutilizável.*
