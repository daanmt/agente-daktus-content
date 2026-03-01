# DIRETIVA DE SESSÃO — ANTIGRAVITY
## De: Dan (via Claude Sonnet 4.6) | Data: 2026-02-27 | Sessão: Nova instância pós-troca de conta

---

## ⚠️ CORREÇÃO DE FASE — LEIA ANTES DE QUALQUER AÇÃO

Antes de continuar, leia os seguintes arquivos em sua totalidade, nesta ordem:
1. `/tools` — todos os documentos de instrução disponíveis
2. `/history/session_001.md` (se disponível) — registro da sessão anterior
3. `BANCO_EVIDENCIAS_PSIQUIATRIA.md` — estado atual do banco

O banco de evidências v2.0 está completo com 10 relatórios, 419 REF-IDs e 266 AFI-IDs. **Isso não significa que estamos prontos para construir o playbook ou a ficha JSON.**

### Onde estamos de verdade no projeto

O projeto segue um cronograma de fases sequenciais que deve ser respeitado integralmente:

```
Fase 0  ✅ Briefing completo — ENCERRADA
Fase 1  🔄 Playbook draft — EM PREPARAÇÃO (banco de evidências é insumo, não produto final)
Fase 2  ⏳ Auditoria de referências — PRÓXIMO PASSO IMEDIATO
Fase 3  ⏳ Revisão clínica com psiquiatras
Fase 4  ⏳ Implementação JSON
Fase 5  ⏳ QA final
```

**Estamos na transição Fase 0 → Fase 1, e o próximo passo obrigatório é a Fase 2 preliminar: auditoria do banco de evidências.**

A Fase 2 normalmente ocorre após o playbook draft. Neste projeto, vamos antecipar uma **pré-auditoria do banco** antes de iniciar o playbook — por uma razão prática e crítica que está descrita abaixo.

---

## TAREFA DESTA SESSÃO — Pré-auditoria do Banco de Evidências

### Por que fazer isso agora

O banco acumulou **419 referências** para sustentar **266 afirmações clínicas**. A razão referências/afirmações é de 1,57 — o que indica redundância considerável. Antes de qualquer nó do playbook ser escrito, precisamos de um banco enxuto, confiável e orientado ao contexto brasileiro. Um banco inflado com referências de baixa relevância ou aplicabilidade reduzida para o nosso cenário ambulatorial privado em São Paulo vai contaminar o playbook com complexidade desnecessária.

**O objetivo da pré-auditoria não é eliminar evidências — é garantir que cada afirmação clínica usada no playbook esteja sustentada pela referência de maior qualidade e maior pertinência disponível, sem redundância.**

---

## PROTOCOLO DE AUDITORIA — Execute nesta ordem exata

### ETAPA 1 — Inventário e classificação das referências (output: tabela)

Para cada REF-ID (001 a 419), classifique em uma das três categorias abaixo. Trabalhe em blocos de 50 por vez para não exceder contexto.

| Categoria | Critério |
|-----------|---------|
| **TIER 1 — Manter obrigatório** | Guideline de alto nível (APA, CANMAT, NICE, CFM, VA/DoD), RCT ou SR/NMA de alta qualidade (NEJM, Lancet, JAMA, Cochrane), legislação brasileira, bula FDA/ANVISA com informação sem equivalente em outra fonte já listada |
| **TIER 2 — Manter condicional** | Revisão narrativa de qualidade moderada, estudo observacional relevante, validação psicométrica de instrumento usado no protocolo, consenso de especialistas. Manter SOMENTE se não houver TIER 1 já na lista cobrindo o mesmo ponto |
| **TIER 3 — Candidato a remoção** | Revisão ou coorte que apenas repete o que uma guideline TIER 1 já cobre; fonte pré-2015 com equivalente mais recente disponível no banco; estudo de população não-brasileira ou não-ocidental sem generalização clara para o contexto; referência que sustenta apenas notas de rodapé ou divergências menores |

**Output desta etapa:** Uma tabela com três colunas — REF-ID | Tier | Justificativa (1 linha).

---

### ETAPA 2 — Consolidação de AFIs órfãs e AFIs redundantes (output: lista)

Após a classificação, identifique:

1. **AFIs órfãs:** AFI-IDs que citam SOMENTE referências TIER 3. Estas afirmações precisam ser avaliadas individualmente — ou encontramos uma referência TIER 1/2 equivalente, ou a afirmação é removida do banco.

2. **AFIs redundantes:** AFI-IDs que afirmam exatamente o mesmo ponto clínico com palavras diferentes. Consolidar em uma única AFI com a redação mais precisa e a referência de maior qualidade.

**Output desta etapa:** Lista de AFIs órfãs + lista de AFIs redundantes com proposta de consolidação.

---

### ETAPA 3 — Priorização por relevância ao contexto brasileiro e ao briefing (output: flags)

Para cada REF-ID TIER 1 e TIER 2 que sobrar, adicione um flag binário:

| Flag | Critério |
|------|---------|
| 🇧🇷 **BR-relevante** | Legislação brasileira, validação em população brasileira, protocolo com aplicabilidade direta ao sistema suplementar de saúde (Amil/ANS), ANVISA |
| 🎯 **Briefing-central** | A referência sustenta diretamente um dos clusters prioritários do briefing: Gate P0, monitoramento de fármacos (lítio/valproato/clozapina), ou comorbidades de maior volume (depressão, TAB, esquizofrenia, TDAH, TPB) |

Referências com ambos os flags (🇧🇷 + 🎯) são candidatas a **citação explícita no playbook** e nos nós JSON. As demais sustentam o banco internamente mas não precisam aparecer em todo lugar.

---

### ETAPA 4 — Relatório de auditoria (output: documento)

Ao final das etapas 1–3, gere um único documento `AUDITORIA_BANCO_v1.md` na raiz do projeto com:

1. **Sumário executivo** — quantas referências por tier, quantas AFIs consolidadas/removidas, qual a redução percentual
2. **Tabela completa de classificação** (REF-ID | Tier | BR-relevante | Briefing-central | Justificativa)
3. **Lista de AFIs ajustadas** — quais foram consolidadas, quais foram removidas, quais foram mantidas sem alteração
4. **Recomendações para o playbook** — os 5–10 pontos onde a auditoria revelou que o banco é mais robusto (alta evidência + alta relevância BR) e os 3–5 pontos onde há lacunas ou dependência excessiva de literatura não-brasileira

---

## REGRAS DESTA SESSÃO

1. **Não iniciar nenhum nó de playbook antes de concluir a auditoria.** O playbook começa na próxima sessão, após aprovação do relatório de auditoria.

2. **Não remover nenhuma AFI sem registrar a justificativa** no relatório de auditoria. Nada se perde silenciosamente.

3. **Em caso de dúvida sobre o contexto do projeto** (o que é o Daktus, como funciona o grafo, o que são os clusters A–K, o que é o Gate P0), leia os arquivos em `/tools` antes de assumir qualquer coisa. O briefing original está em `OE_RELATORIO_01_GATE_P0.md` e nos relatórios de sessão em `/history`.

4. **Trabalhe em blocos.** 419 referências não cabem em um único output sem degradar qualidade. Processe 50 por vez, confirme cada bloco antes de avançar.

5. **Registre esta sessão em `/history/session_XXX.md`** com o número correto de sequência ao final.

---

## CRITÉRIO DE CONCLUSÃO DESTA SESSÃO

A sessão está concluída quando:
- [ ] Todas as 419 referências estão classificadas em TIER 1/2/3
- [ ] Todas as AFIs foram revisadas para órfãs e redundâncias
- [ ] Flags BR-relevante e Briefing-central atribuídos
- [ ] `AUDITORIA_BANCO_v1.md` gerado e salvo na raiz
- [ ] Log de sessão atualizado em `/history`

**Após aprovação do relatório de auditoria por Dan, a próxima sessão iniciará o Cluster B (Gate P0) do playbook — o primeiro nó clínico a ser desenvolvido, por ser o mais crítico e o mais bem documentado no banco.**

---

*Aguardo confirmação de leitura dos arquivos em /tools antes do início da Etapa 1.*
