# CONTEXTO_FERRAMENTAS_E_METODOS.md — MÉTODOS OPERACIONAIS E APRENDIZADOS DE IMPLEMENTAÇÃO

## PAPEL DESTE DOCUMENTO

Este documento reúne práticas operacionais, heurísticas de trabalho e aprendizados de implementação acumulados no ambiente daktus.

Ele não é o ponto de entrada do ambiente.
O ponto de entrada é `AGENTE.md`.

Ele também não substitui:
- `HANDOFF.md` como estado operacional curto;
- `ESTADO.md` como snapshot canônico;
- `SKILL.md` como orchestrator do pipeline;
- a sub-skill específica da fase ativa.

Use este documento como apoio quando a sessão exigir método de execução, decisão operacional ou padrão de trabalho refinado.

---

## OBJETIVO

O objetivo deste documento é reduzir erro operacional, retrabalho e improviso técnico.

Ele existe para registrar:
- como trabalhar melhor dentro do ambiente;
- como usar referências maduras com disciplina;
- como modelar artefatos com mais previsibilidade;
- quais padrões já se mostraram eficazes em casos anteriores;
- quais erros recorrentes devem ser evitados.

---

## PRINCÍPIO CENTRAL

Ferramenta importa menos do que capacidade.

Este ambiente pode ser operado por diferentes agentes, interfaces e stacks locais.
Por isso, os métodos aqui descritos devem ser entendidos como capacidades operacionais, não como comandos obrigatórios de uma ferramenta específica.

As capacidades relevantes incluem, por exemplo:
- leitura de arquivos;
- comparação entre artefatos;
- busca contextual;
- edição cirúrgica de documentos;
- execução de scripts de validação;
- versionamento e registro de sessão.

Se a interface mudar, o método continua válido.
O nome da ferramenta pode mudar; a capacidade necessária continua a mesma.

---

## QUANDO USAR ESTE DOCUMENTO

Consulte este documento quando precisar:

- escolher uma estratégia de trabalho dentro de uma fase;
- operar com referências maduras sem copiar lógica clínica;
- decidir como estruturar paper design e JSON;
- reduzir risco em sessões mais técnicas;
- reaproveitar aprendizados consolidados de especialidades anteriores;
- evitar erros já conhecidos do ambiente.

Não use este documento como bootstrap.
Não use este documento para decidir fase atual sem antes ler o estado do ambiente.

---

## PRÉ-REQUISITO

Antes de usar este documento, o agente já deve ter lido:

1. `AGENTE.md`
2. `HANDOFF.md`, se existir
3. `ESTADO.md`
4. `SKILL.md`
5. a sub-skill da fase ativa, quando aplicável

Só depois disso este documento deve ser consultado como apoio.

---

## LÓGICA DE USO DAS FERRAMENTAS

### 1. Ler antes de editar
Sempre que possível:
- localizar o artefato correto;
- entender sua estrutura;
- identificar o ponto exato de alteração;
- só então editar.

Evite reescrever arquivos inteiros sem necessidade.
Prefira alterações cirúrgicas quando o artefato já estiver maduro.

### 2. Validar antes de expandir
Antes de criar novos blocos de lógica:
- revisar o que já existe;
- checar se o padrão já foi resolvido em outro artefato;
- usar benchmark estrutural quando houver.

Evite inventar estrutura nova se o ambiente já tiver um padrão consolidado.

### 3. Operar por fases, não por impulso
O método correto é:
- identificar a fase;
- abrir a instrução certa;
- ler apenas os apoios pertinentes;
- executar o próximo passo coerente.

Evite carregar contexto técnico de fases futuras antes da hora.

---

## USO DE REFERÊNCIAS MADURAS

Referências maduras são extremamente úteis, mas precisam ser usadas com disciplina.

Elas servem para:
- entender padrões de arquitetura;
- observar desenho de nós;
- aprender estilo de modelagem;
- revisar decisões que funcionaram bem;
- antecipar erros de implementação;
- acelerar paper design e JSON.

Elas não servem para:
- copiar lógica clínica entre especialidades;
- presumir perguntas, mensagens ou condutas;
- importar critérios clínicos sem ancoragem documental;
- justificar atalhos de fase.

Sempre separar:
- padrão estrutural reutilizável;
- conteúdo clínico específico da especialidade.

---

## HEURÍSTICA GERAL DE IMPLEMENTAÇÃO

Quando estiver produzindo artefatos técnicos, a ordem preferencial é:

1. entender o objetivo clínico do bloco;
2. localizar benchmark estrutural útil;
3. mapear a arquitetura antes de codificar;
4. definir dependências e condicionais;
5. só então escrever o artefato final;
6. validar consistência depois.

Essa ordem vale especialmente para:
- playbook;
- paper design;
- clinicalExpressions;
- condutas;
- JSON.

---

## APRENDIZADOS CONSOLIDADOS DO AMBIENTE

Os aprendizados abaixo já mostraram valor prático e devem ser preservados.

### 1. Ler JSON de referência antes de modelar nodes novos
Antes de criar arquitetura nova, observar artefatos maduros ajuda a:
- evitar inconsistência estrutural;
- reaproveitar padrões de roteamento;
- modelar nós com mais previsibilidade;
- reduzir retrabalho posterior.

### 2. O node `summary` costuma concentrar lógica importante
Em implementações maduras, o `summary` frequentemente cumpre mais do que uma função de resumo.
Ele pode:
- consolidar achados,
- ativar expressões clínicas,
- preparar a conduta,
- servir como ponte entre coleta e decisão.

Por isso, o `summary` deve ser modelado com atenção.
Não tratá-lo como mero fechamento decorativo.

### 3. `clinicalExpressions` devem nascer de necessidade real
Essas expressões não devem ser criadas por ornamento técnico.
Devem surgir quando forem necessárias para:
- consolidar variáveis clínicas,
- simplificar condicionais,
- capturar equivalências semânticas,
- organizar critérios compostos,
- sustentar a lógica da conduta ou do roteamento.

### 4. A ordem das condicionais importa
Quando há múltiplas regras, a ordem de avaliação afeta o comportamento do fluxo.
Por isso:
- primeiro mapear os cenários;
- depois organizar a precedência;
- só então codificar.

### 5. `expressao` deve simplificar, não obscurecer
Quando usada corretamente, a camada de expressão reduz duplicação e torna a lógica mais legível.
Quando usada mal, ela vira opacidade.

Regra prática:
- usar para consolidar lógica;
- evitar quando a regra simples puder ser lida diretamente.

### 6. Breakpoint é recurso clínico e técnico
O breakpoint não é apenas interrupção de fluxo.
Ele pode funcionar como:
- ponto de transição decisória;
- handoff entre blocos clínicos;
- mecanismo de segurança;
- limite natural entre coleta e conduta.

### 7. A conduta deve ser pensada cedo
Mesmo antes do JSON final, é útil pensar:
- quais saídas clínicas precisam existir;
- quais condições as ativam;
- que variáveis sustentam essas saídas.

Isso ajuda a modelar melhor os nós anteriores.

---

## MÉTODO PARA PAPER DESIGN

Quando a fase exigir paper design, trabalhar nesta sequência:

1. identificar os blocos clínicos principais;
2. definir o objetivo de cada nó;
3. listar perguntas ou variáveis centrais por nó;
4. mapear condicionais de navegação;
5. prever `clinicalExpressions` necessárias;
6. desenhar a estrutura da conduta;
7. validar se o fluxo ficou coerente antes de codificar.

O paper design deve reduzir improviso na codificação.
Se ele estiver mal resolvido, o JSON tende a sair instável.

---

## MÉTODO PARA CODIFICAÇÃO JSON

Quando a fase ativa for codificação JSON:

1. confirmar que o playbook foi liberado;
2. revisar padrões arquiteturais já consolidados;
3. verificar benchmark estrutural aplicável;
4. transformar paper design em estrutura de nós;
5. modelar variáveis, expressões e edges com disciplina;
6. revisar consistência da conduta;
7. validar o JSON com ferramentas disponíveis.

Não começar codificação no escuro.
Não usar JSON final como lugar de descobrir a arquitetura.

---

## MÉTODO PARA EDIÇÃO DE ARTEFATOS MADUROS

Quando o arquivo já estiver avançado ou consolidado:

- localizar o trecho exato que precisa mudar;
- entender dependências ao redor;
- editar o mínimo necessário;
- revisar efeitos colaterais;
- validar após a mudança.

Evitar grandes reescritas sem necessidade.
Quanto mais maduro o artefato, mais importante a edição precisa ser.

---

## MÉTODO PARA SESSÕES COMPLEXAS

Em sessões com muitos documentos, muitas dependências ou muita ambiguidade:

1. localizar o estado primeiro;
2. definir a fase ativa;
3. separar documentos centrais de documentos auxiliares;
4. identificar o entregável exato da sessão;
5. só então abrir leitura complementar.

Não reagir à complexidade lendo tudo.
Responder à complexidade com melhor ordenação.

---

## ERROS RECORRENTES A EVITAR

- começar implementação sem arquitetura mínima;
- abrir leitura indiscriminada do repositório;
- usar benchmark como cópia clínica;
- modelar `clinicalExpressions` sem necessidade clara;
- tratar `summary` como nó trivial;
- construir conduta tarde demais;
- misturar decisão clínica com improviso estrutural;
- editar artefato maduro de forma ampla demais;
- validar só no fim;
- esquecer de registrar continuidade ao encerrar a sessão.

---

## COMO ESTE DOCUMENTO SE RELACIONA COM OS DEMAIS

- `AGENTE.md` define o boot e a ordem de autoridade.
- `HANDOFF.md` informa o estado operacional curto.
- `ESTADO.md` informa o snapshot canônico.
- `SKILL.md` informa as fases do pipeline.
- a sub-skill ativa informa a execução da fase.
- este documento informa como operar melhor dentro desse contexto.

---

## REGRA FINAL

Use este documento para trabalhar com mais precisão.

Não use este documento para substituir:
- o estado do ambiente;
- a fase atual;
- o gate do pipeline;
- a instrução principal da sub-skill ativa.

Método vem depois do boot.
Heurística vem depois do estado.
Implementação vem depois da fase correta.