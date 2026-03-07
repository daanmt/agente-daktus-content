# SKILL — QA FINAL E ENTREGA
## `qa-entrega` | Fase 5

> **Pré-condição de boot:** esta skill é invocada após boot completo via `AGENTE.md`.
> `HANDOFF.md` deve ter sido lido e a fase atual confirmada antes de executar qualquer ação aqui.


---

## O QUE ESTA SKILL FAZ

Validação end-to-end do par playbook + JSON antes da entrega para homologação. Esta fase não produz conteúdo novo — verifica que tudo que foi produzido está correto, consistente e rastreável. Nenhum item crítico pode estar em aberto na entrega.

---

## ARQUIVOS VERIFICADOS

```
playbooks/playbook_{esp}_vFINAL.md
jsons/ficha_{esp}_v{versao}.json
research/BANCO_EVIDENCIAS_{ESP}.md
history/session_XXX.md (todos)
```

## ARQUIVO DE SAÍDA

```
jsons/relatorio_qa_{esp}.md
```

---

## CHECKLIST COMPLETO — 28 PONTOS

### Bloco 1 — Integridade do JSON (estrutural)

```
[ ] JSON é válido (parse sem erro)
[ ] Todas as edges têm IDs no formato e-{source}-{target}
[ ] Todos os linkIds nos condicionais existem como nodes
[ ] Nenhum node inalcançável (exceto intencionais documentados)
[ ] metadata.version é um UUID v4 válido
[ ] metadata.createdAt está em formato ISO 8601
[ ] Primeiro node está em position.x = 900
[ ] Nodes posicionados sequencialmente em incrementos de 900
[ ] IIDs únicos em todo o catálogo de condutas
```

### Bloco 2 — Clínico e de Segurança

```
[ ] Gate de segurança está no Nó 2 (incontornável)
[ ] Alerta de risco máximo é o PRIMEIRO item da conduta
[ ] Opções de risco máximo têm exclusive: false (múltipla seleção permitida)
[ ] Termo de ciência/responsabilidade presente no nó correspondente (se aplicável)
[ ] Breakpoint de resumo presente na sequência (se aplicável)
```

### Bloco 3 — Exames e TUSS

```
[ ] sync_scan: PASS (todos os exames do playbook estão no JSON e vice-versa)
[ ] Códigos TUSS mapeados ou sinalizados como pendentes com justificativa
[ ] CIDs de entrada documentados por exame
[ ] Periodicidade explícita em todos os exames de monitoramento
[ ] Condicionais de liberação de exames verificadas por inspeção
```

### Bloco 4 — Playbook

```
[ ] citation_scan: PASS (zero phantoms, zero orphans)
[ ] semantic_scan: PASS (zero inconsistências semânticas)
[ ] exam_coverage_scan: PASS (zero gaps de cobertura)
[ ] Todas as seções obrigatórias presentes (introdução a referências)
[ ] AFIs sem TIER 1/2 documentadas com justificativa de exceção
```

### Bloco 5 — Rastreabilidade e Gestão de Mudanças

```
[ ] Todas as mudanças aplicadas classificadas em M1–M4
[ ] Todas as mudanças têm confirmação do usuário registrada em sessão
[ ] Nenhuma mudança M2/M3/M4 sem re-verificação de referência
[ ] Log de sessões completo: session_001.md até a sessão final
[ ] AUDITORIA_BANCO_v1.md presente e aprovado
```

---

## FORMATO DO RELATÓRIO DE QA

```markdown
# RELATÓRIO QA — {Especialidade} — v{versão}
## Data: AAAA-MM-DD

### Resultado geral: ✅ APROVADO / ❌ REPROVADO

### Bloco 1 — JSON Estrutural
[ ✅/❌ ] [item] — [observação se necessário]
...

### Bloco 2 — Clínico e de Segurança
...

### Bloco 3 — Exames e TUSS
...

### Bloco 4 — Playbook
...

### Bloco 5 — Rastreabilidade
...

### Issues em aberto (se houver)
| # | Bloco | Descrição | Aceito com justificativa? |
|---|-------|-----------|--------------------------|

### Assinaturas
- Validação técnica (agente): ✅ AAAA-MM-DD
- Aprovação clínica (usuário): [ ] AGUARDANDO
```

---

## CRITÉRIO DE ENTREGA

**Todos os 28 checks devem estar ✅ antes da entrega para homologação.**

Issues do **Bloco 2 (segurança clínica)** nunca podem estar em aberto na entrega — sem exceção.

Issues dos demais blocos podem ser aceitos como pendência documentada, com aprovação explícita do usuário e justificativa registrada no relatório.

---

## ARTEFATOS FINAIS ENTREGUES

```
1. playbooks/playbook_{esp}_vFINAL.md     ← documentação clínica com referências auditadas
2. jsons/ficha_{esp}_v{versao}.json       ← JSON Daktus validado
3. jsons/relatorio_qa_{esp}.md            ← este checklist preenchido e assinado
```
