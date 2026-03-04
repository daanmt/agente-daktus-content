# Session 003 — Pré-Auditoria do Banco de Evidências
**Data:** 2026-02-27 | **Agente:** Antigravity | **Projeto:** Ficha de Psiquiatria Daktus

---

## Objetivo da Sessão
Executar a auditoria pré-rascunho do banco de evidências (DIRETIVA_AUDITORIA_ANTIGRAVITY.md) e assimilar a arquitetura técnica de nós Daktus (BRIEFING_ARQUITETURA_NOS_DAKTUS.md).

## O Que Foi Feito

### 1. Leitura de documentos de instrução
- `BRIEFING_ARQUITETURA_NOS_DAKTUS.md` — Assimilado. Correção conceitual crítica: **nó = tela**, não módulo temático. Ficha terá 6 nós: Triagem, Gate P0, Anamnese, Diagnóstico ativo, Monitoramento de fármacos, Conduta.
- `DIRETIVA_AUDITORIA_ANTIGRAVITY.md` — Critérios TIER 1/2/3 aplicados.

### 2. Atualização do task.md
- Etapas 1-5 marcadas como concluídas
- Etapas 6a-6h concluídas (auditoria gerada)
- Etapa 7 (playbook draft) aguarda aprovação

### 3. Geração de AUDITORIA_BANCO_v1.md
> Arquivo: `/research/AUDITORIA_BANCO_v1.md`

Todos os 419 REF-IDs classificados em 4 blocos:
- **Bloco 1** (REF-001–100): Gate P0 + Farmacologia + Humor
- **Bloco 2** (REF-101–222): Ansiedade/OCD/TEPT/Burnout + Psicose/EPS/CLZ/Metabólico  
- **Bloco 3** (REF-223–347): TDAH + TEA + TPB Borderline
- **Bloco 4** (REF-348–419): T. Alimentares + DDI + Internação + CAPS

### 4. Sumário executivo da auditoria

| Tier | Qtd | % |
|------|-----|---|
| TIER 1 (manter obrigatório) | ~163 | ~39% |
| TIER 2 (manter condicional) | ~173 | ~41% |
| TIER 3 (candidatos a remoção) | ~83 | ~20% |
| Com flag 🇧🇷 | ~42 | ~10% |
| Com flag 🎯 Briefing-central | ~231 | ~55% |

**Duplicata identificada:** REF-308 = REF-077 (mesmo artigo JAMA Simon 2024)  
**AFI redundantes:** AFI-083 e AFI-084 devem ser consolidadas

### 5. Principais lacunas detectadas
1. CAPS III em SP: sem dado de tempos de espera reais
2. VPA teratogenicidade: sem dado BR (EURAP é europeu)
3. ASRS TDAH: sem validação formal em PT-BR
4. DBT para TPB: disponibilidade e custo no sistema suplementar
5. Burnout: sem guideline clínico produzido para contexto BR

## Decisões Tomadas

| Decisão | Detalhe |
|---------|---------|
| Estratégia de blocos para a auditoria | 4 blocos de ~100 REF-IDs para respeitar limite de tokens |
| TIER 3 não serão removidos do banco | Mantidos para contexto histórico e divergências; apenas não serão citados no playbook |
| Nós Daktus confirmados: 6 | Triagem, Gate P0, Anamnese, Diagnóstico, Fármacos, Conduta |

## Próximos Passos (Sessão 004)
1. **Dan aprova** AUDITORIA_BANCO_v1.md
2. Iniciar Fase 1 Playbook — começar pelo **Cluster B (Gate P0)** que é incontornável
3. Cada seção do playbook citará AFI-IDs do banco como fonte
4. Após playbook aprovado: JSON dos 6 nós

## Arquivos Modificados
- `/research/AUDITORIA_BANCO_v1.md` — **NOVO** — relatório de auditoria completo
- `/history/session_003.md` — **NOVO** — este arquivo
- `task.md` (artifact) — atualizado: etapas 6a-6h concluídas
