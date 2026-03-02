# Relatório de Processo — Protocolo de Psiquiatria Ambulatorial
**Daktus/Amil | Content Team | Março 2026**
**Para:** Gabriel — Head de Conteúdo

---

## 1. Contexto e Objetivo

O projeto desenvolveu a Ficha Clínica de Psiquiatria para a plataforma Daktus, documentando cada etapa com profundidade suficiente para transformá-la em **skill reutilizável** de um pipeline de produção de conteúdo médico.

---

## 2. Etapas Executadas

| Fase | Entregável | Status |
|------|-----------|--------|
| 0 — Briefing e arquitetura de nós | Mapa clínico + clusters prioritários | ✅ Completa |
| 1 — Ingestão de evidências | Banco v3.0 — 412 REFs ativas, 266 AFIs | ✅ Completa |
| 2 — Auditoria do banco | AUDITORIA_MASTER.md — classificação TIER 1/2/3 | ✅ Completa |
| 3 — Playbook clínico | `playbook_psiquiatria.md` — 645 linhas | ✅ Completa |
| 4 — Revisão clínica (humana) | — | ⏳ Pendente |
| 5 — Codificação JSON + QA | `ficha_psiquiatria.json` | ⏳ Pendente |

**Fase 0 — Briefing:** Mapeamento das demandas relatadas pelos psiquiatras de Pinheiros. Comorbidades prioritárias (TDM, TAB, Esquizofrenia, TDAH, TEA, TOC, TPB, Transtornos Alimentares), exames críticos (ECG, litemia, valproato, clozapina) e encaminhamentos frequentes foram consolidados em um mapa de clusters que guiou toda a coleta de evidências.

**Fase 1 — Ingestão de evidências:** 10 relatórios do OpenEvidence processados em temas clínicos específicos (Gate P0/Suicídio, Monitoramento de Fármacos, Transtornos do Humor, Ansiedade/TOC/TEPT, Psicose/EPS, TDAH, TEA, TPB, Transtornos Alimentares, Interações/Internação/CAPS). O banco foi estruturado com dupla indexação: REF-ID (referência bibliográfica) + AFI-ID (afirmação clínica vinculada). Esse modelo garante rastreabilidade total — toda afirmação do playbook remonta a uma fonte verificável.

**Fase 2 — Auditoria:** Todas as 412 referências ativas foram classificadas em TIER 1 (147 — guidelines APA, CANMAT, NICE, CFM, FDA/ANVISA, RCTs de alto nível), TIER 2 (182 — condicionais, sem equivalente TIER 1) e TIER 3 (83 — contexto, excluídas do playbook). Nove AFIs órfãs — que citavam apenas referências de baixa qualidade — foram corrigidas antes da redação. Isso impediu que evidência fraca contaminasse o conteúdo final.

**Fase 3 — Playbook:** 645 linhas organizadas por **classe farmacológica** (não por síndrome), com tabelas padronizadas de 6 colunas: `Fármaco | Indicação Clínica | Posologia | Observações | Refs | NE`. Seções: Gate P0 com C-SSRS e plano de segurança, 19 condições diagnósticas (CID-10 + critério DSM-5-TR), exames baseline e monitoramento de fármacos de janela estreita, terapêuticas §1–§9 (Antidepressivos, Estabilizadores, Antipsicóticos, TDAH, Psicoterapias, Nichos, Crise EPS/SNM, Burnout, DDIs), 12 KPIs auditáveis.

---

## 3. Nuances Críticas de Decisão

**Auditoria antecipada do banco.** A pré-auditoria (antes da redação do playbook) foi uma decisão estratégica deliberada. A razão REF/AFI original era 1,57 — indicando redundância considerável. Um banco inflado com evidências de baixa pertinência contamina o playbook com complexidade desnecessária e dificulta a hierarquização clínica. A auditoria foi feita antes, não depois.

**Estrutura por classe farmacológica.** O template original organizava as terapêuticas por síndrome. Essa estrutura foi abandonada após análise de UX da ficha. Na prática ambulatorial, o psiquiatra prescreve por classe: um ISRS pode ser indicado para TDM, TAG, TOC e Pânico simultaneamente. A coluna "Indicação Clínica" resolve o problema sem duplicar linhas.

**Guardrails de evidência (G1–G6).** O pipeline inclui protocolo formal de interrupção quando há: conflito entre fontes de alto nível, ausência de diretriz nacional, evidência anterior a 2022 em área de evolução rápida, afirmação de alto impacto sem fonte verificável, ou divergência entre prática clínica relatada e evidência formal. O agente para e emite uma Solicitação de Evidência — não decide por conta própria em situações de incerteza clínica.

---

## 4. Aprendizados Operacionais

**Progressive disclosure preserva qualidade.** Carregar apenas a skill da fase atual — em vez de um system prompt monolítico — mantém o agente focado e preserva a janela de contexto para o trabalho real. A analogia direta é o conceito de Half Loop: o agente executa uma tarefa por vez, com contexto limpo, guiado por um PRD (aqui, o `SKILL.md`) e um progress tracker (os session logs). A qualidade das fases intermediárias melhora significativamente.

**Session logs como ponto de encontro entre agentes.** Dois agentes distintos (Antigravity para conteúdo clínico; Claude Code para operações de arquivo, Git e validação JSON) operam sobre os mesmos artefatos. O session log mais recente é o único ponto de sincronização necessário — qualquer instância que o leia sabe o estado exato do projeto.

**Banco de evidências como autoridade única.** Toda afirmação do playbook existe porque está indexada no banco. Isso elimina divergências entre seções e permite auditoria automatizada via script (`audit_references.py`).

---

## 5. Skills Extraídas e Replicabilidade

O projeto produziu, além do protocolo, **7 skills exportáveis** — arquivos `.md` com instruções estruturadas que ensinam o agente a executar cada fase com precisão:

| Skill | Função |
|-------|--------|
| `briefing-arquitetura` | Mapear briefing clínico em arquitetura de nós |
| `ingestao-evidencias` | Ingerir relatórios OpenEvidence no banco |
| `auditoria-banco` | Classificar REFs em TIER 1/2/3 antes do playbook |
| `redacao-playbook` | Redigir playbook cluster por cluster com rastreamento de evidências |
| `auditoria-playbook` | Citation scan + semantic scan + coverage scan |
| `codificacao-json` | Paper design → TUSS → JSON Daktus → validação |
| `qa-entrega` | Checklist de 28 pontos pré-entrega para homologação |

Cada skill é especialidade-agnóstica. A única adaptação necessária para um novo projeto é o mapa de clusters do Briefing (Fase 0). O custo marginal de cada ficha subsequente cai à medida que as skills amadurecem com o uso.

O repositório completo (skills + banco + playbook + session logs + scripts) está versionado no GitHub e pode ser clonado e operado em qualquer máquina, com qualquer modelo de linguagem, via interface de chat ou CLI.

---

## 6. Conclusão Executiva

O projeto de Psiquiatria gerou dois produtos para a Daktus. O primeiro é o playbook clínico e o segundo é o **modelo operacional compartilhável**: um pipeline documentado que transforma o processo de criação de conteúdo médico em um conjunto de skills especializadas, portáveis e reutilizáveis.

A tese central é validada: documentar com profundidade o que o agente precisa saber para executar com excelência é equivalente a construir um PRD operacional. Esse PRD, associado a um prompt de inicialização simples e a skills especializadas por fase, cria um sistema que entrega resultado consistente independentemente do agente, da interface ou do computador.

As próximas especialidades podem reutilizar o mesmo pipeline com adaptação apenas no Briefing. O ativo real deste projeto é a infraestrutura que a produziu.
