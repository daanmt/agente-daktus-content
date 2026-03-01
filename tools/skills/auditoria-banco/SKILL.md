# SKILL — AUDITORIA DO BANCO DE EVIDÊNCIAS
## `auditoria-banco` | Fase 2 (antecipada)

---

## O QUE ESTA SKILL FAZ

Classifica todas as referências do banco em TIER 1/2/3, elimina redundância entre AFIs, identifica lacunas e gera o relatório de auditoria. Este relatório é o filtro que garante que o playbook seja construído sobre as fontes de maior qualidade disponíveis.

**Por que antes do playbook:** Um banco inflado com referências de baixa relevância contamina o playbook com complexidade desnecessária e fragiliza citações. É mais rápido auditar o banco agora do que consertar o playbook depois.

---

## ARQUIVO DE ENTRADA

```
research/BANCO_EVIDENCIAS_{ESP}.md     ← banco completo (todas as ingestões feitas)
```

## ARQUIVO DE SAÍDA

```
research/AUDITORIA_BANCO_v1.md         ← relatório de auditoria (aprovado pelo usuário antes de avançar)
```

---

## CRITÉRIOS DE CLASSIFICAÇÃO

| Tier | Critério |
|------|---------|
| **TIER 1 — Manter obrigatório** | Guideline de sociedade de referência de alto nível (APA, NICE, CFM, CANMAT, VA-DoD, etc.), RCT ou SR/NMA em periódico de alto impacto (NEJM, Lancet, JAMA, Cochrane), legislação brasileira, bula FDA/ANVISA com informação sem equivalente já listado no banco |
| **TIER 2 — Manter condicional** | Revisão narrativa de qualidade moderada em periódico indexado, estudo observacional relevante, validação psicométrica de instrumento usado no protocolo, consenso de especialistas — sem TIER 1 equivalente cobrindo o mesmo ponto |
| **TIER 3 — Candidato à remoção** | Repete o que TIER 1 já cobre; publicação anterior a 2015 com equivalente mais recente no banco; população sem generalização para o contexto do protocolo; sustenta apenas notas de divergência |

---

## PROTOCOLO DE EXECUÇÃO

**Trabalhar em blocos de 50 referências.** Confirmar cada bloco com o usuário antes de avançar.

### Para cada REF-ID:
1. Identificar tipo de publicação e rigor metodológico
2. Verificar se outro REF já cobre o mesmo ponto com maior autoridade
3. Atribuir Tier
4. Atribuir flags 🇧🇷 e 🎯
5. Justificar em 1 linha

### Para cada AFI-ID:
1. Verificar se tem ao menos uma REF TIER 1 ou TIER 2 de suporte
2. Identificar **AFIs órfãs** (sem REF de suporte válido)
3. Identificar **AFIs redundantes** (mesma afirmação em dois AFI-IDs diferentes)
4. Propor consolidação — nunca deletar sem registro

**REFs TIER 3 não são deletadas** — são marcadas para não aparecer como citações primárias no playbook.

---

## ESTRUTURA DO `AUDITORIA_BANCO_v1.md`

```markdown
# AUDITORIA DO BANCO DE EVIDÊNCIAS — {Especialidade}
## Data: AAAA-MM-DD

## Sumário executivo
| Métrica | Valor |
|---------|-------|
| Total de REFs analisadas | N |
| TIER 1 | N (X%) |
| TIER 2 | N (X%) |
| TIER 3 (candidatos) | N (X%) |
| Com flag 🇧🇷 | N |
| Com flag 🎯 | N |
| Com ambas as flags | N |
| AFIs órfãs | N |
| AFIs redundantes consolidadas | N |

## Tabela de classificação
| REF-ID | Tier | 🇧🇷 | 🎯 | Justificativa |
|--------|------|-----|-----|--------------|

## AFIs ajustadas
[Lista de consolidações com justificativa. Nada se perde silenciosamente.]

## Recomendações para o playbook
### Áreas com evidência mais robusta (TIER 1 + flag 🎯)
### Lacunas e dependência de literatura não-brasileira
```

---

## CRITÉRIO DE CONCLUSÃO

```
[ ] Todas as REFs classificadas em TIER 1/2/3
[ ] Flags 🇧🇷 e 🎯 atribuídas
[ ] AFIs órfãs identificadas e tratadas
[ ] AFIs redundantes consolidadas
[ ] research/AUDITORIA_BANCO_v1.md gerado e salvo
[ ] APROVAÇÃO DO USUÁRIO ANTES DE INICIAR O PLAYBOOK
```
