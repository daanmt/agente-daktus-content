# SKILL — REDAÇÃO DO PLAYBOOK CLÍNICO
## `redacao-playbook` | Fase 1

> **Pré-condição de boot:** esta skill é invocada após boot completo via `AGENTE.md`.
> `HANDOFF.md` deve ter sido lido e a fase atual confirmada antes de executar qualquer ação aqui.


---

## O QUE ESTA SKILL FAZ

Produz a documentação clínica que justifica cada decisão da ficha JSON. O playbook é o "porquê" da ficha — cada exame, alerta e condicional tem uma seção correspondente que explica o raciocínio clínico e cita a evidência de suporte.

**O playbook não é o JSON.** Ele documenta o raciocínio; o JSON o implementa.

---

## ARQUIVOS DE REFERÊNCIA AO INICIAR

```
research/BANCO_EVIDENCIAS_{ESP}.md     ← fonte de todas as afirmações
research/AUDITORIA_BANCO_v1.md         ← saber quais REFs são TIER 1/2/3
research/OE_RELATORIO_00_BRIEFING.md   ← arquitetura de clusters aprovada
history/session_XXX.md                 ← onde o projeto parou
```

## ARQUIVO DE SAÍDA

```
playbooks/playbook_{esp}_vDRAFT.md
```

---

## ORDEM DE PRODUÇÃO DOS CLUSTERS

Definida no briefing da especialidade. **Regra geral de priorização:**

1. **Gate de segurança** (risco agudo) — sempre primeiro, pois é bloqueante para toda a ficha
2. **Triagem e anamnese** — base de todas as condicionais
3. **Módulo transversal** (ex: monitoramento de fármacos, rastreio preventivo) — aplica a múltiplos diagnósticos
4. **Módulos por condição clínica específica** — na ordem de prevalência da especialidade
5. **Encaminhamentos e condutas de saída**

**Nunca começar um cluster antes de o anterior estar completo e aprovado.**

---

## ESTRUTURA DE CADA SEÇÃO DO PLAYBOOK

```markdown
### [Nome do Cluster / Seção]

**Justificativa clínica:**
[Por que este conteúdo está na ficha — problema clínico que resolve]

**Afirmações clínicas e fontes:**
| AFI-ID | Afirmação | REF-IDs | Tier | Nível |
|--------|-----------|---------|------|-------|

**Lógica condicional:**
[Quando este conteúdo aparece / o que condiciona sua exibição no formulário]

**Indicação de exames (se aplicável):**
| Exame | Indicação clínica | Código TUSS | CID | Nível de evidência |
|-------|------------------|-------------|-----|-------------------|

**Alertas e thresholds:**
| Condição | Threshold | Conduta sugerida | Fonte |
|----------|-----------|-----------------|-------|
```

---

## SEÇÕES OBRIGATÓRIAS DO PLAYBOOK FINAL

1. Introdução e mudanças de paradigma
2. Panorama epidemiológico
3. Dados da operadora e aderência (quando disponíveis)
4. Objetivos do protocolo
5. Estratégias de rastreio / condução por condição
6. Exames e suas indicações clínicas (tabelas com nível de evidência)
7. Exames proscritos (o que não pedir e por quê)
8. Calculadoras, escalas e instrumentos
9. Metas auditáveis e KPIs
10. Referências

---

## SOLICITAÇÃO DE EVIDÊNCIA — QUANDO E COMO EMITIR

Emitir ao identificar qualquer dos gatilhos abaixo. **Parar o trabalho** naquele ponto até resposta.

| Gatilho | Situação |
|---------|---------|
| **G1** | Conflito entre duas fontes de nível equivalente sobre o mesmo ponto |
| **G2** | Afirmação relevante sem nenhum REF de suporte no banco |
| **G3** | Guideline com mais de 3 anos como única fonte de ponto crítico |
| **G4** | Dado epidemiológico relevante sem fonte brasileira disponível |
| **G5** | Indicação de exame sem código TUSS identificado |
| **G6** | Threshold de alerta com impacto clínico direto e fontes divergentes |

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 SOLICITAÇÃO DE EVIDÊNCIA #N
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GATILHO: G[N]
ARTEFATO: Playbook {especialidade} — Seção "[nome]"
PONTO DE PARADA: [decisão que está bloqueada]

CONTEXTO CLÍNICO:
[Cenário clínico específico que precisa da evidência]

CONFLITO / GAP:
[Fonte A diz X. Fonte B diz Y. OU: não há fonte para Z.]

PERGUNTA PARA OPENEVIDENCE:
[Pergunta clínica estruturada — específica, com população, intervenção e outcome]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## PROTOCOLO DE MUDANÇA DURANTE REVISÃO

Para cada mudança solicitada pelo usuário:

```
PROPOSTA DE MUDANÇA #N
Classe: M1 (editorial) / M2 (clínica) / M3 (estrutural) / M4 (referência)
Item afetado: [seção + trecho]
Mudança solicitada: [descrição]
Base clínica atual: [guideline + ano]
Avaliação: SUPORTADA / CONFLITANTE / SEM EVIDÊNCIA
Ação proposta: [texto alternativo]
Impacto em outras seções: [lista ou "nenhum"]
```

**Nunca aplicar sem confirmação explícita do usuário.**

Após aplicar mudanças M2/M3/M4, re-verificar se novas inconsistências de referência foram criadas.

---

## ENTREGA DA FASE 1

```
RELATÓRIO DE ESTADO — FASE 1
- Clusters completos: N/N
- Afirmações citadas no playbook: N
- Solicitações de Evidência emitidas: N | respondidas: N
- AFIs usadas sem TIER 1/2 de suporte: N (listadas)
- Arquivo: playbooks/playbook_{esp}_vDRAFT.md
- AGUARDANDO AUTORIZAÇÃO PARA FASE 2 (auditoria do playbook)
```
