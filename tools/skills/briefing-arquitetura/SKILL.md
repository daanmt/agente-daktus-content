# SKILL — BRIEFING E ARQUITETURA DE NÓS
## `briefing-arquitetura` | Fase 0

---

## O QUE ESTA SKILL FAZ

Transforma o briefing clínico recebido da equipe médica em uma arquitetura de nós documentada, validada e pronta para orientar todas as fases do pipeline. Esta fase define o esqueleto da ficha — erros aqui se propagam para toda a esteira de produção.

---

## ARQUIVOS ESPERADOS AO INICIAR

```
/{especialidade}/
├── research/                     ← pode estar vazio no início
└── history/session_001.md        ← criar se não existir
```

O briefing chega como texto da equipe clínica (colado na conversa ou em arquivo). Não há template rígido de entrada — o agente extrai o que precisa.

---

## O QUE EXTRAIR DO BRIEFING

| Elemento | O que buscar |
|----------|-------------|
| **Problema clínico** | Por que a ficha atual falha? O que os médicos reclamam? |
| **Comorbidades frequentes** | Lista de condições que o protocolo deve cobrir |
| **Sintomas mais relatados** | Para mapear perguntas de triagem |
| **Exames comumente solicitados** | Para antecipar mapeamento TUSS |
| **Encaminhamentos frequentes** | Para o nó de conduta |
| **Perfil do paciente** | Faixa etária, contexto (ambulatorial, internação, urgência?) |
| **Contexto da operadora** | Regras de cobertura, sistema (ANS/TUSS, SUS, privado puro) |

---

## ARTEFATO DE SAÍDA — RELATÓRIO DE BRIEFING

Salvar em: `research/OE_RELATORIO_00_BRIEFING.md`

```markdown
# RELATÓRIO DE BRIEFING — {Especialidade}
## Data: AAAA-MM-DD

### 1. Contexto clínico
[Especialidade, operadora, perfil do paciente, problema identificado]

### 2. Mapeamento de clusters temáticos
| Cluster | Conteúdo clínico | Obrigatoriedade | Nó proposto |
|---------|-----------------|-----------------|-------------|
| A | [tema] | Obrigatório | Nó X |
| B | [tema — gate de segurança se aplicável] | Obrigatório | Nó 2 |
| ... | | | |

### 3. Proposta de arquitetura de nós
| Posição | Nó | Label | Clusters atendidos |
|---------|-----|-------|-------------------|
| 1 | Triagem | Enfermagem | A parcial |
| 2 | Gate [risco] | [Nome do gate] | B |
| ... | | | |

### 4. Perguntas abertas para o usuário
[Máx. 6 questões críticas para decisões de design que o agente não consegue responder sozinho]
```

---

## PRINCÍPIOS DE DESIGN DE NÓS

**Regra fundamental: cada nó = uma tela a mais para o médico preencher. Menos nós = melhor UX.**

| Princípio | Regra |
|-----------|-------|
| Nós por conteúdo, não por diagnóstico | Não criar 1 nó por doença — usar condicionais inline |
| Gate de segurança é incontornável | Sempre Nó 2, logo após triagem. Se a especialidade tem risco agudo (suicídio, IAM, etc.), esse gate nunca pode ser o último nó |
| Condicionais dentro do nó | Usar lógica condicional interna antes de criar um nó novo |
| Preselected para o estado mais comum | Reduz cliques para o caso típico |
| Conduta conservadora | Melhor mostrar algo extra do que esconder algo necessário |

**Nunca fazer:**
- 1 nó por diagnóstico (inviável na prática clínica)
- Perguntas abertas (`string`) onde seleção múltipla resolve
- Conduta genérica sem condicional (mostra o mesmo para todos)
- Gate de segurança como último nó
- Exames sem código TUSS na conduta

---

## REFERÊNCIA UX

Consultar o JSON mais recente de especialidade entregue como referência de UX (localizado em `jsons/referencia/`). Ele representa o padrão atual de protocolo enxuto que o time espera.

---

## CRITÉRIO DE CONCLUSÃO

```
[ ] Clusters mapeados com nós correspondentes
[ ] Gate de segurança posicionado como Nó 2 (se aplicável à especialidade)
[ ] Número de nós justificado com princípio UX
[ ] Perguntas abertas listadas (máx. 6)
[ ] Relatório salvo em research/OE_RELATORIO_00_BRIEFING.md
[ ] APROVAÇÃO DO USUÁRIO ANTES DE AVANÇAR PARA INGESTÃO DE EVIDÊNCIAS
```
