# SKILL — INGESTÃO DE EVIDÊNCIAS
## `ingestao-evidencias` | Fase contínua

> **Pré-condição de boot:** esta skill é invocada após boot completo via `AGENTE.md`.
> `HANDOFF.md` deve ter sido lido e a fase atual confirmada antes de executar qualquer ação aqui.


---

## O QUE ESTA SKILL FAZ

Ingere relatórios do OpenEvidence (ou qualquer fonte bibliográfica estruturada), extrai referências e afirmações clínicas, e mantém o banco de evidências do projeto atualizado, sem duplicatas, com nível de evidência explícito e rastreabilidade completa.

---

## ARQUIVO MESTRE DO PROJETO

```
research/BANCO_EVIDENCIAS_{ESP}.md
```

Este é o arquivo mais importante do projeto. Toda afirmação clínica do playbook deve rastrear até uma entrada deste arquivo. Se ele não existir ao iniciar a skill, **criá-lo antes de qualquer ingestão**.

### Estrutura mínima do banco ao criar:

```markdown
# BANCO DE EVIDÊNCIAS — {ESPECIALIDADE}
## Versão: 1.0 | Iniciado em: AAAA-MM-DD

---

## SEÇÃO 1 — REFERÊNCIAS

| REF-ID | Fonte / Autores | Ano | Tipo | Resumo de uso no protocolo |
|--------|----------------|-----|------|---------------------------|

---

## SEÇÃO 2 — AFIRMAÇÕES CLÍNICAS (AFIs)

| AFI-ID | Afirmação | REF-IDs de suporte | Cluster | Nível |
|--------|-----------|-------------------|---------|-------|

---

## LOG DE INGESTÕES

| Data | Fonte | REFs adicionadas | AFIs adicionadas |
|------|-------|-----------------|-----------------|
```

---

## PROTOCOLO DE INGESTÃO DE RELATÓRIO

### Passo 1 — Verificar duplicatas de referências

Para cada referência do relatório recebido:
1. Buscar no banco por título parcial, DOI ou autores principais
2. Se já existe → anotar o REF-ID existente; **não criar novo**
3. Se não existe → criar REF-ID sequencial (REF-001, REF-002, ...)

```
⚠️ DUPLICATA IDENTIFICADA
REF-ID existente: REF-XXX | Título: [...]
Ação: mantido REF-ID original. Novas AFIs associadas ao REF-ID existente.
```

### Passo 2 — Extrair afirmações clínicas

Para cada afirmação relevante do relatório:
1. Formular como afirmação **objetiva e testável** (não vaga)
2. Associar aos REF-IDs corretos
3. Identificar o cluster a que pertence (conforme mapeamento do briefing)
4. Classificar o nível de evidência (tabela abaixo)

**Boa AFI:** "C-SSRS ≥ 2 em ideação com plano indica alto risco suicida [REF-001]"
**AFI ruim:** "Risco suicida deve ser avaliado"

### Passo 3 — Atualizar o banco

- Adicionar novos REFs na Seção 1
- Adicionar novas AFIs na Seção 2
- Atualizar o log de ingestões

---

## CLASSIFICAÇÃO DE NÍVEL DE EVIDÊNCIA

| Nível | Critério |
|-------|---------|
| **A** | RCT ou SR/NMA de alta qualidade (NEJM, Lancet, JAMA, Cochrane) |
| **B** | Guideline de sociedade de referência (APA, NICE, CFM, VA-DoD, CANMAT, etc.), coorte de grande escala |
| **C** | Revisão narrativa, consenso de especialistas, validação psicométrica |
| **D** | Opinião de especialista, série de casos, dado epidemiológico sem controle |

---

## FLAGS OBRIGATÓRIAS

| Flag | Critério |
|------|---------|
| 🇧🇷 | Legislação BR, validação em população brasileira, protocolo aplicável ao sistema suplementar nacional |
| 🎯 | Sustenta diretamente os clusters prioritários identificados no briefing |

---

## SAÚDE DO BANCO — MÉTRICA DE REFERÊNCIA

**Razão REF/AFI > 2,0 = banco inflado.** Acima disso, revisar antes de avançar para a auditoria.

---

## OUTPUT DE CADA INGESTÃO

```
INGESTÃO CONCLUÍDA — [Nome do relatório]
- Novas REFs adicionadas: N (REF-XXX a REF-YYY)
- REFs existentes reutilizadas: N
- Novas AFIs adicionadas: N (AFI-XXX a AFI-YYY)
- AFIs consolidadas: N
- Clusters cobertos: [lista]
- Estado do banco: N REFs | N AFIs | Razão: X.X
```
