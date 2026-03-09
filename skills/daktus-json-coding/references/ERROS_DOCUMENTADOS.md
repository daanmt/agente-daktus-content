# Erros Documentados e Checklist QA

> Consolidado de `tools/PADROES_ARQUITETURA_JSON.md` Parts II + IV.
> Erros reais de Reumatologia, Cardiologia e Ginecologia com regras derivadas.

---

## Erros Documentados

### E1 — Copy-paste de `iid`

**O que aconteceu:** ao criar exame baseado em outro, o `iid` foi copiado sem alterar. Dois exames com mesmo `iid`.

**Regra:** ao criar exame a partir de existente, o `iid` é o PRIMEIRO campo a ser alterado. QA deve verificar unicidade em todo o catálogo.

---

### E2 — Campo com Dupla Função

**O que aconteceu:** um campo capturava "alergias medicamentosas E comorbidades" — duas informações num único string.

**Regra:** um campo = uma informação. Nunca usar "e/ou" no título. Revisar títulos adjacentes sempre que uma nova pergunta for adicionada ao mesmo nó.

---

### E3 — Patologia Adicionada sem Validação de Escopo

**O que aconteceu:** SAF foi identificada como lacuna e o instinto foi adicionar protocolo completo. Decisão correta: adicionar apenas exame com condicional restrita.

**Regra:** escopo de protocolo é decisão clínica, não técnica. Exame sem protocolo → condicional restrita + sinalizar gap pendente. Não expandir sem autorização.

---

### E4 — Sintoma sem Contexto de Risco

**O que aconteceu:** protocolo perguntava SE houve pré-síncope mas não capturava o CONTEXTO (esforço vs. repouso). Risco de morte 5-30% tratado igual a síncope benigna.

**Regra:** sintoma onde contexto muda gravidade em uma ordem de magnitude → captura de contexto no mesmo nó. Identificar ANTES de implementar.

---

### E5 — Diagnóstico em Espectro com Trigger Único

**O que aconteceu:** `'has' in comorbidades` exigia diagnóstico confirmado. Médico forçado a marcar "hipertensa" para liberar exames de rastreamento.

**Regra:** condições em espectro (confirmado / suspeito / em investigação) NUNCA com trigger único. Sempre: `confirmado OR suspeita OR em_investigacao`.

---

### E6 — Resultado de Exame Inacessível no Fluxo Novo

**O que aconteceu:** campo de resultado existia apenas no nó de Seguimento. Pacientes novos não conseguiam registrar.

**Regra:** campos de registro de dados externos devem estar no trecho universal — acessível a qualquer tipo de paciente.

---

### E7 — Calculadora sem Documentação de Escore

**O que aconteceu:** protocolo referenciava "risco CV" sem especificar qual escore (PREVENT, Framingham, SCORE). São escores diferentes com populações e thresholds diferentes.

**Regra:** toda calculadora deve ter metadados: nome exato, referência/DOI, população validada, thresholds. Se incerto, bloquear e perguntar.

---

### E8 — Gate de Segurança com Bypass Silencioso

**O que aconteceu:** ECG solicitado mas resultado não exigido antes de liberar atestado. Sistema liberava paciente com ECG "pendente".

**Regra:** gate de segurança deve ser tecnicamente impossível de contornar:
```
output_seguro = exame_solicitado AND resultado != '' AND resultado != 'pendente'
```

---

## Checklist QA Ampliado

### Integridade referencial

- [ ] Unicidade de `iid` em todo o catálogo do nó conduta
- [ ] Nenhum `iid` contém referência ao nome de outro exame

### Cobertura por tipo de paciente

- [ ] Todo uid acessível no fluxo de PRIMEIRO ATENDIMENTO
- [ ] Todo uid acessível no fluxo de RETORNO / FOLLOW-UP
- [ ] Campos de resultado de exames externos acessíveis em ambos os fluxos

### Revisão de títulos

- [ ] Após nova pergunta: revisar títulos dos campos adjacentes no mesmo nó
- [ ] Nenhum campo com "e/ou" no título

### Gates de segurança

- [ ] Todo gate P0 é tecnicamente não-contornável
- [ ] Gate de resultado: exame solicitado só libera conduta APÓS resultado preenchido
- [ ] Teste de bypass: inputs que deveriam bloquear → verificar que output é impossível

### Calculadoras e escores

- [ ] Toda calculadora tem metadados: nome, referência, população, thresholds
- [ ] Holders de variáveis externas com `description` explícita
- [ ] Apenas uma escala padrão por construto, com justificativa

### Escopo

- [ ] Playbook lista explicitamente o que está FORA do escopo
- [ ] Exames por feedback sem protocolo: condicional restrita + gap documentado

### Consistência farmacológica

- [ ] Aliases de classe: todos os fármacos listados
- [ ] Novo fármaco no formulário → verificar se deve entrar em alias existente
