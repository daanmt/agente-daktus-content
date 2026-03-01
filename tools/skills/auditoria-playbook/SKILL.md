# SKILL — AUDITORIA DO PLAYBOOK
## `auditoria-playbook` | Fase 2

---

## O QUE ESTA SKILL FAZ

Verifica a integridade clínica e bibliográfica do playbook antes de traduzí-lo em JSON. Detecta citações fantasmas, referências sem uso, afirmações sem suporte e gaps de cobertura de exames.

---

## ARQUIVOS DE ENTRADA

```
playbooks/playbook_{esp}_vDRAFT.md     ← playbook a auditar
research/BANCO_EVIDENCIAS_{ESP}.md     ← fonte de verdade das referências
```

## ARQUIVO DE SAÍDA

```
playbooks/relatorio_auditoria_playbook.md
```

---

## VARREDURAS DISPONÍVEIS

### citation_scan — Varredura de Citações

Detecta **phantoms** (citações no texto sem entrada na seção de referências) e **orphans** (referências listadas que nunca são citadas no texto).

```bash
# Citações únicas no corpo (excluindo seção de referências)
grep -oP '(?<=\[)\d+(?=\])' <(sed '/^## Referências/,$d' playbook.md) | sort -n | uniq

# Números listados na seção de referências
grep -oP '^\d+(?=\.)' <(sed -n '/^## Referências/,$p' playbook.md) | sort -n
```

Output:
```
citation_scan RESULTADO
- Citações únicas no corpo: N
- Referências listadas: N
- Phantoms (citados, sem referência): [lista]
- Orphans (listados, nunca citados): [lista]
- STATUS: PASS / FAIL
```

---

### semantic_scan — Varredura Semântica

Para cada citação, verifica se o conteúdo da referência sustenta semanticamente a afirmação que a cita. Detecta citações usadas para suportar o que a referência não afirma.

Output por problema identificado:
```
⚠️ INCONSISTÊNCIA SEMÂNTICA
Afirmação no playbook: [texto]
Referência citada: REF-ID — [título]
Problema: A referência trata de [X], não de [Y] como citado.
Ação: [A] Buscar REF alternativa | [B] Remover citação | [C] Reformular afirmação
```

---

### exam_coverage_scan — Varredura de Cobertura de Exames

Para cada exame mencionado no playbook, verificar se está completo:

| Check | Critério |
|-------|---------|
| ✅ Indicação clara | Condição clínica explícita para solicitar |
| ✅ TUSS mapeado | Código TUSS presente |
| ✅ CID associado | CID de entrada para liberação |
| ✅ Condição de liberação | Exame é condicional ou universal no nó de conduta |

Output:
```
exam_coverage_scan RESULTADO
- Exames identificados: N
- Com TUSS: N/N
- Com CID: N/N
- Com indicação clara: N/N
- Exames com gap: [lista detalhada]
- STATUS: PASS / FAIL  ← qualquer gap = FAIL
```

---

### sync_scan — Consistência Playbook ↔ JSON

Executar **após** a codificação JSON (Fase 4). Compara exames do playbook com exames no nó de conduta do JSON.

```
sync_scan RESULTADO
- Exames no playbook: N
- Exames no JSON (conduta): N
- No playbook, ausentes no JSON: [lista]
- No JSON, ausentes no playbook: [lista]
- STATUS: PASS / FAIL
```

---

## PROTOCOLO DE RESOLUÇÃO DE ISSUES

Para cada FAIL, registrar:

```
ISSUE #N
Tipo: phantom | orphan | semântico | gap de exame | sync
Localização: [seção + trecho do playbook]
Descrição: [o que está errado]
Ação proposta: [A–D]
Status: ABERTO → AGUARDANDO CONFIRMAÇÃO DO USUÁRIO
```

Após confirmação, aplicar, classificar como M1/M2/M3/M4 e registrar na sessão.

---

## ENTREGA DA FASE 2

```
RELATÓRIO DE ESTADO — FASE 2
- citation_scan: PASS / FAIL (N issues)
- semantic_scan: PASS / FAIL (N issues)
- exam_coverage_scan: PASS / FAIL (N issues)
- Issues abertos: N | Issues resolvidos: N
- Arquivo: playbooks/relatorio_auditoria_playbook.md
- Playbook aprovado pelo usuário? [sim / aguardando]
- AGUARDANDO AUTORIZAÇÃO PARA FASE 3 (revisão clínica)
```
