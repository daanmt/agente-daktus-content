# INTELIGÊNCIA CONSOLIDADA DE PROJETOS — REUMATOLOGIA E CARDIOLOGIA

> **Documento complementar ao sistema de instruções do agente Daktus.**  
> Sintetiza os aprendizados extraídos dos projetos de Reumatologia e Cardiologia para alimentar o desenvolvimento de novos protocolos (Psiquiatria, Neurologia, etc.).  
> Leia este documento junto com `AGENT_PROMPT_PROTOCOLO_DAKTUS.md`, `CONTEXTO_FERRAMENTAS_E_PLANEJAMENTO_PSIQUIATRIA.md` e `GUARDRAIL_EVIDENCIAS.md`.

---

## PARTE I — NOVOS PADRÕES DE ARQUITETURA JSON

### 1.1 Alias de Classe Farmacológica (padrão Reumatologia)

O padrão mais reutilizável da reumatologia: em vez de referenciar medicamentos individuais em cada condicional de exame, criar `clinicalExpressions` por classe terapêutica e usar os aliases downstream.

```json
{ "name": "cdmards", "formula": "selected_any(medicamentos_atuais, 'mtx', 'lef', 'ssz')" },
{ "name": "bdmards", "formula": "selected_any(medicamentos_atuais, 'adalimumabe', 'etanercepte', 'infliximabe', 'certolizumabe', 'golimumabe', 'abatecepte', 'tocilizumabe', 'rituximabe')" },
{ "name": "ijak", "formula": "selected_any(imunobiologicos_atuais, 'tofacitinibe', 'baricitinibe', 'upadacitinibe')" }
```

**Por que usar:** quando um exame de monitoramento é indicado para toda uma classe (ex: hemograma para qualquer cDMARD, TGO/TGP para MTX + LEF), a condicional vira `cdmards is True` ao invés de listar 10 medicamentos individualmente. Manutenção é trivial — adicionar um novo fármaco à classe não exige alterar nenhuma condicional downstream.

**Aplicação direta em Psiquiatria:**

```json
{ "name": "estabilizadores_humor", "formula": "selected_any(medicamentos_em_uso, 'litio', 'valproato', 'carbamazepina', 'lamotrigina')" },
{ "name": "antipsicóticos_atipicos", "formula": "selected_any(medicamentos_em_uso, 'quetiapina', 'risperidona', 'olanzapina', 'aripiprazol', 'ziprasidona', 'clozapina', 'lurasidona')" },
{ "name": "exige_ecg", "formula": "selected_any(medicamentos_em_uso, 'litio', 'clozapina') or antipsicóticos_atipicos is True or selected_any(medicamentos_em_uso, 'citalopram', 'escitalopram', 'amitriptilina', 'clomipramina')" }
```

---

### 1.2 Expressão Agregadora Diagnóstico + Suspeita (padrão Reumatologia)

Para especialidades com diagnósticos confirmados E suspeitas em investigação simultâneos:

```json
{
  "name": "quadros_inflamatorios",
  "formula": "selected_any(doenca_reumatologica, 'artrite_reumatoide', 'gota', 'lupus') or selected_any(suspeita_clinica, 'ar_hd', 'fibro_hd', 'gota_hd', 'lupus_hd')"
}
```

**Regra:** criar sempre dois campos separados — `diagnostico_confirmado` e `hipotese_diagnostica` — e uma expressão agregadora que une os dois. Isso garante que exames de investigação sejam acessíveis para pacientes sem diagnóstico fechado.

**Aplicação em Psiquiatria:** essencial para o cluster de humor, onde um paciente pode estar "em investigação de TAB" sem diagnóstico confirmado, mas já precisar de litemia basal.

---

### 1.3 Gate de Negação Composta para Clearance (padrão Cardiologia)

Para qualquer output que exige ausência de uma lista de contraindicações:

```json
{
  "id": "atestado_atividade_fisica",
  "condicao": "('sem_sintomas_cardio' in main) and not selected_any(ecg_resultado, 'onda_q', 'isquemia', 'bav') and not selected_any(comorbidades, 'hipercolesterolemia_familiar', 'drc', 'daop') and (pre_sincope_contexto != 'esforco')"
}
```

**Regra geral:** `output_seguro = condicao_positiva AND NOT selected_any(lista_blocante)`. Qualquer item na lista blocante cancela o output. Reutilizável em psiquiatria para: liberação de estimulante (TDAH) sem contra-indicação cardíaca, alta hospitalar, receita de controlado sem risco de automedicação/overdose.

---

### 1.4 Sintoma com Contexto Obrigatório no Mesmo Nó (padrão Cardiologia)

Quando um sintoma tem subtipos com risco radicalmente diferente, a pergunta de contexto DEVE aparecer no mesmo nó, condicionalmente:

```json
{
  "uid": "pre_sincope_contexto",
  "expressao": "'pre_sincope' in sintomas_cardio",
  "select": "single",
  "options": [
    {"id": "repouso", "label": "Em repouso ou sem relação clara"},
    {"id": "esforco", "label": "Durante ou imediatamente após esforço físico"}
  ]
}
```

**Regra:** se o contexto estiver em nó separado, existe risco real de não ser preenchido. O contexto que muda a conduta deve ser capturado na mesma sessão que o sintoma.

**Aplicação em Psiquiatria:** ideação suicida ativa vs. passiva; alucinação auditiva imperativa vs. comentativa; automutilação com vs. sem intenção suicida — todos precisam de contextualização no mesmo nó onde o sintoma é capturado.

---

### 1.5 Boolean Gate → Texto Livre Condicional (padrão Reumatologia)

Padrão sistemático para hábitos e histórico:

```json
{ "uid": "tabagismo", "select": "boolean" },
{ "uid": "tabagismo_detalhe", "expressao": "tabagismo is True", "select": "string" }
```

**Por que não usar texto livre direto:** booleanos são usáveis em condicionais downstream (`tabagismo is True` pode acionar rastreamento de DPOC, risco CV, etc.). Texto livre não é parseável. O campo de detalhe captura a narrativa sem perder a capacidade de raciocínio lógico.

---

### 1.6 Variáveis "Holder" para Cálculos Externos (padrão Cardiologia)

Quando um escore não pode ser calculado internamente pela plataforma:

```json
{
  "name": "rf_cl_cad_escore",
  "formula": "false",
  "description": "Holder para escore calculado externamente. Valor chega via integração.",
  "template": ""
}
```

**Regra:** se o cálculo tem mais de 3 variáveis ou pesos não-lineares (Framingham, PREVENT, CHADS-VASc, litemia em janela terapêutica, etc.), declarar como holder externo. Documentar obrigatoriamente: nome do escore, DOI da referência, faixa etária da população validada, thresholds de classificação.

**Aplicação em Psiquiatria:** MEEM/MoCA pontuação total, PHQ-9, GAD-7 — se a plataforma não calcular automaticamente, declarar como holders com campo numérico de entrada.

---

## PARTE II — ERROS DOCUMENTADOS E REGRAS DERIVADAS

### 2.1 Copy-paste de `iid` (Reumatologia — Bug Anti-β2GPI)

**O que aconteceu:** ao criar um exame baseado em outro existente, o campo `iid` foi copiado sem alterar. Dois exames ficaram com o mesmo `iid`.

**Regra derivada:** ao criar qualquer exame no nó conduta a partir de um existente, o campo `iid` é o PRIMEIRO a ser alterado, antes de qualquer outro. O QA deve incluir verificação de unicidade de `iid` em todo o catálogo de exames.

**Script de verificação:**
```python
import json
from collections import Counter

d = json.load(open('ficha.json'))
conduta_nodes = [n for n in d['nodes'] if n['id'].startswith('conduta-')]
iids = []
for node in conduta_nodes:
    for item in node['data'].get('conduta', {}).get('exames', []):
        iids.append(item.get('iid', ''))
    for orient in node['data'].get('conduta', {}).get('orientacao', []):
        iids.append(orient.get('id', ''))

duplicates = {iid: count for iid, count in Counter(iids).items() if count > 1}
print(f"IIDs duplicados: {duplicates or 'nenhum'}")
```

---

### 2.2 Campo com Dupla Função (Reumatologia — `Q-alergias-medicamentos`)

**O que aconteceu:** um campo capturava "alergias medicamentosas E outras comorbidades" — duas informações distintas num único string. Quando um novo campo de antecedentes foi adicionado, o título tornou-se redundante e confuso.

**Regra derivada:** revisar os títulos e funções de todos os campos no mesmo nó sempre que uma nova pergunta for adicionada. Um campo = uma informação. Nunca usar "e/ou" no título de um campo de coleta.

---

### 2.3 Adição de Patologia sem Validação de Escopo (Reumatologia — SAF)

**O que aconteceu:** SAF (Síndrome Antifosfolípide) foi identificada como lacuna evidente. O instinto foi adicionar completamente ao protocolo. A decisão correta foi adicionar apenas o exame com condicional restrita e sinalizar a lacuna de playbook como pendente.

**Regra derivada:** escopo de protocolo é decisão clínica do médico responsável, não técnica do agente. Quando um exame surge sem protocolo estabelecido, o padrão correto é:
1. Adicionar o exame com condicional conservadora (suspeita explicitamente marcada pelo médico)
2. Sinalizar a lacuna de playbook como item pendente com status "aguardando validação clínica"
3. Não expandir o protocolo para cobrir a síndrome completa sem autorização

---

### 2.4 Sintoma sem Contexto de Risco (Cardiologia — Bug Síncope P0)

**O que aconteceu:** o protocolo perguntava SE houve pré-síncope mas não capturava o CONTEXTO (esforço vs. repouso). Pacientes com pré-síncope de esforço — risco de morte súbita 5–30% — recebiam o mesmo tratamento que síncope vasovagal benigna.

**Regra derivada:** qualquer sintoma onde o CONTEXTO muda a gravidade em uma ordem de magnitude exige captura de contexto no mesmo nó. Identificar esses sintomas antes de implementar o nó, não depois.

**Para psiquiatria:** ideação suicida passiva vs. ativa vs. com plano vs. com tentativa prévia — cada nível tem conduta completamente diferente e deve ser capturado na mesma pergunta, não inferido.

---

### 2.5 Diagnóstico em Espectro com Trigger Único (Cardiologia — Bug HAS)

**O que aconteceu:** `'has' in comorbidades` exigia diagnóstico confirmado. Médico com paciente em investigação de HAS era forçado a marcar "hipertensa" para liberar exames de rastreamento — workaround documentado em feedback real.

**Regra derivada:** condições diagnósticas que existem em espectro (confirmado / suspeito / em investigação) NUNCA devem ter trigger único. Sempre mapear três caminhos:

```
condição confirmada OR sintoma sugestivo OR marcador "em investigação"
```

**Para psiquiatria:** depressão pode ser `diagnostico_confirmado = 'depressao'` OR `sintomas_humor_deprimido is True` OR `'investigando_depressao' in motivo_consulta`.

---

### 2.6 Campo de Resultado de Exame Inacessível no Fluxo Novo (Reumatologia)

**O que aconteceu:** `exame_resultado` existia apenas no nó de Seguimento. Pacientes novos que trazem exames não conseguiam registrar os resultados.

**Regra derivada:** campos de registro de dados externos (exames trazidos pelo paciente, resultados anteriores) devem sempre estar no trecho universal do fluxo — acessível a qualquer tipo de paciente. Nunca em ramificações exclusivas de follow-up.

---

### 2.7 Calculadora sem Documentação de Escore (Cardiologia — Bug #23)

**O que aconteceu:** o protocolo referenciava "risco CV" sem especificar qual escore era aplicado — se PREVENT, Framingham, SCORE ou ESC DAC-specific. São escores diferentes com populações e thresholds diferentes.

**Regra derivada:** toda calculadora de risco ou escore clínico no protocolo deve ter metadados obrigatórios como campos `description` no JSON:
- Nome exato do escore
- DOI ou referência da publicação original  
- Faixa etária da população validada
- Thresholds de classificação (baixo / intermediário / alto)

Se não souber qual escore a plataforma usa internamente, bloquear o desenvolvimento e perguntar antes de prosseguir.

---

### 2.8 Gate de Segurança com Bypass Silencioso (Cardiologia — Bug ECG #10)

**O que aconteceu:** o protocolo solicitava ECG, mas não exigia que o resultado fosse interpretado antes de liberar o atestado de atividade física. ECG ficava "pendente" e o sistema liberava o paciente assim mesmo.

**Regra derivada:** gate de segurança deve ser tecnicamente impossível de contornar, não apenas visualmente alertado. A condicional de liberação deve exigir que o campo de resultado esteja preenchido:

```
output_seguro = exame_solicitado AND resultado_exame != '' AND resultado_exame != 'pendente'
```

Verificar no QA: preencher dados que deveriam bloquear + tentar emitir output. O sistema deve tornar o output impossível, não apenas exibir aviso.

---

## PARTE III — GESTÃO DE EVIDÊNCIAS — CONFLITOS RESOLVIDOS

### 3.1 Critérios Diagnósticos em Múltiplas Versões (Reumatologia — Fibromialgia)

**Conflito:** ACR publicou critérios em 2010 e revisão em 2016; EULAR tem recomendações terapêuticas próprias de 2017 com divergências sobre fármacos específicos (ex: gabapentina).

**Resolução adotada:** critérios diagnósticos = ACR 2010/2016 (mais recentes e específicos para diagnóstico). Recomendações terapêuticas = EULAR 2017 (mais recentes e incorporam evidências posteriores). Onde houve divergência de fármaco, documentado como "evidência moderada" sem forçar consenso inexistente.

**Regra derivada:** critério diagnóstico e conduta terapêutica podem vir de guidelines diferentes do mesmo ano ou distintos. Sempre citar separadamente qual guideline fundamenta cada parte.

---

### 3.2 Exame Adicionado por Feedback sem Protocolo Completo (Reumatologia — Anti-β2GPI / SAF)

**Conflito:** médica sinalizou necessidade do Anti-β2GPI, mas SAF não constava no playbook original.

**Resolução adotada:** Anti-β2GPI adicionado ao catálogo com condicional restrita (`'saf_hd' in suspeita_clinica`). SAF incluída como hipótese diagnóstica. Expansão completa do playbook para SAF marcada como pendente de validação.

**Regra derivada:** feedback clínico que menciona exame sem protocolo estabelecido → adicionar com condicional restrita + sinalizar gap de playbook. Não ignorar o feedback, não expandir sem autorização.

---

### 3.3 Diretriz Internacional mais Recente vs. Prática Ambulatorial Local (Reumatologia — GIOP/ACR 2022)

**Conflito:** ACR 2022 tem threshold de risco e esquema de tratamento sofisticados para GIOP. A realidade operacional do ambulatório Amil/Daktus não comporta a implementação integral.

**Resolução adotada:** conceito e triagem = ACR 2022 (densitometria obrigatória para corticoide crônico). Limiares de tratamento = simplificados para o contexto. O playbook documenta a diretriz completa; o protocolo implementa o subset executável.

**Regra derivada:** quando diretriz internacional é mais completa que o operacionalizável no contexto, documentar os dois níveis explicitamente: "diretriz recomenda X; este protocolo implementa Y por [razão]". A divergência não é suprimida — é registrada.

---

### 3.4 Atualização de Diretriz durante o Desenvolvimento (Cardiologia — MRPA vs. MAPA)

**Conflito:** diretrizes antigas priorizavam MAPA; SBC 2025 equiparou MRPA como alternativa válida.

**Resolução adotada:** oferecer as duas opções como equivalentes, documentando a SBC 2025 como referência. Não substituir MAPA, não ignorar a atualização.

**Regra derivada:** quando uma diretriz é atualizada durante o desenvolvimento de um protocolo, não é necessário reconstruir do zero — é necessário identificar exatamente quais afirmações mudam, atualizar apenas essas afirmações com a nova referência, e verificar se há impacto em condicionais do JSON.

---

### 3.5 Calculadora de Risco com Múltiplas Opções (Cardiologia — PREVENT vs. Framingham)

**Conflito:** múltiplos médicos questionaram qual escore estava sendo aplicado. PREVENT (AHA 2024) inclui variáveis não disponíveis no Framingham.

**Resolução adotada:** migrar para PREVENT como padrão primário (AHA 2024, população 30–79 anos, prevenção primária). Documentar que Framingham é obsoleto para essa aplicação. Manter Framingham apenas se PREVENT não disponível por limitação da plataforma.

**Regra para psiquiatria:** quando múltiplas escalas existem para o mesmo construto (PHQ-9 vs. HAM-D para depressão; BPRS vs. PANSS para psicose), escolher uma como padrão primário com justificativa explícita. Documentar as alternativas como equivalentes válidas. Não usar duas escalas para o mesmo construto sem motivo clínico específico.

---

## PARTE IV — CHECKLIST DE QA AMPLIADO

Esta seção complementa o checklist de QA padrão do `AGENT_PROMPT_PROTOCOLO_DAKTUS.md` com os itens descobertos nos projetos de Reumatologia e Cardiologia.

```
VERIFICAÇÕES ADICIONAIS — DERIVADAS DOS PROJETOS

INTEGRIDADE REFERENCIAL DO CATÁLOGO DE EXAMES:
[ ] Unicidade de `iid` em todo o catálogo do nó conduta (script Python)
[ ] Nenhum campo `iid` contém referência ao nome de outro exame (ex: "anti-ccp-tuss-id" num campo de Anti-β2GPI)

COBERTURA POR TIPO DE PACIENTE:
[ ] Para cada campo uid, verificar: está acessível no fluxo de PRIMEIRO ATENDIMENTO?
[ ] Para cada campo uid, verificar: está acessível no fluxo de RETORNO / FOLLOW-UP?
[ ] Campos de resultado de exames externos: acessíveis em ambos os fluxos?

REVISÃO DE TÍTULOS PÓS-ADIÇÃO:
[ ] Após qualquer nova pergunta adicionada: revisar títulos dos campos adjacentes no mesmo nó
[ ] Nenhum campo com "e/ou" no título (= dois campos distintos mal colapsados)

GATES DE SEGURANÇA:
[ ] Todo gate P0 (síncope de esforço, ideação suicida com plano, etc.) é tecnicamente não-contornável
[ ] Gate de resultado obrigatório: exame solicitado só libera conduta APÓS resultado preenchido
[ ] Testado com cenário de bypass: preencher inputs que deveriam bloquear e verificar que o output é impossível

CALCULADORAS E ESCORES:
[ ] Toda calculadora tem metadados: nome do escore, referência, população validada, thresholds
[ ] Holders de variáveis externas estão documentados com `description` explícita
[ ] Se múltiplas escalas existem para o mesmo construto: apenas uma é padrão primário, com justificativa

ESCOPO EXPLICITADO:
[ ] Playbook lista explicitamente o que ESTÁ fora do escopo (condições não cobertas)
[ ] Exames adicionados por feedback clínico sem protocolo completo: marcados como "condicional restrita + gap pendente"

CONSISTÊNCIA FARMACOLÓGICA:
[ ] Aliases de classe farmacológica (clinicalExpressions): todos os fármacos da classe estão listados?
[ ] Nova adição de fármaco ao formulário → verificar se deve ser adicionado a algum alias existente
```

---

## PARTE V — PARTICULARIDADES CLÍNICAS TRANSVERSAIS

Aprendizados clínicos que o agente deve internalizar como princípios gerais, independente da especialidade em desenvolvimento.

### 5.1 Sintoma físico pode ser diagnóstico psiquiátrico (Cardiologia → Psiquiatria)

Taquicardia, dispneia, dor torácica e tontura — frequentes em cardiologia — têm alta prevalência como manifestações somáticas de transtornos de ansiedade e pânico. O agente que desenvolver a ficha de psiquiatria deve garantir que sintomas físicos listados no briefing (taquicardia, por exemplo) sejam capturados como sintomas ansiosos, não apenas como achados cardiovasculares isolados.

### 5.2 Histórico ginecológico é dado diagnóstico em reumatologia (e vice-versa)

Perdas gestacionais recorrentes + tromboses = SAF até prova em contrário. O agente que desenvolver qualquer especialidade com população feminina deve tratar o histórico gestacional como dado diagnóstico, não apenas de contextualização. Para psiquiatria: depressão pós-parto, psicose puerperal e exacerbações de TAB no puerpério exigem o mesmo raciocínio.

### 5.3 Corticoides crônicos disparam trilha obrigatória transversal

Em qualquer especialidade, paciente em corticosteroide crônico (>3 meses) tem risco de GIOP, diabetes esteroide e imunossupressão. O agente deve verificar se a especialidade em desenvolvimento tem interface com uso crônico de corticoides e garantir que essa trilha esteja presente. Em psiquiatria: menos relevante como medicação do próprio protocolo, mas comum como comorbidade de condição clínica associada.

### 5.4 Gate de segurança P0 tem precedência absoluta sobre qualquer fluxo

Todo protocolo tem pelo menos um gate P0 — uma condição onde o fluxo normal para completamente e o único output possível é "investigar/encaminhar urgente". Identificar esse gate antes de mapear qualquer outro nó. Em cardiologia é a síncope de esforço. Em reumatologia é febre + artrite aguda (artrite séptica?). Em psiquiatria é a ideação suicida com plano. O gate P0 nunca é opcional, nunca é contornável, e é o primeiro elemento a ser implementado e testado.

### 5.5 A tabela de exames do playbook é o artefato mais valioso

De todos os formatos de documentação testados, a tabela com colunas `Exame | TUSS | Indicação clínica | Frequência | Referência | Nível de evidência` é consistentemente o elemento mais útil do playbook para o processo de implementação JSON. Ela é a ponte direta entre a diretriz e o catálogo. Em todos os projetos futuros, esta tabela deve ser o primeiro artefato construído na Fase 1, antes da prosa do playbook.

---

*Fim do documento. Versão 1.0 — 2026-02-27. Sintetizado a partir dos projetos de Reumatologia (v1.0.10 → v1.1.0) e Cardiologia (Amil/AMB).*
