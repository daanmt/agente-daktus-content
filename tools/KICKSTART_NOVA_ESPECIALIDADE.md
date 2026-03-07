# KICKSTART_NOVA_ESPECIALIDADE.md — ABERTURA DE NOVA FRENTE NO AMBIENTE DAKTUS

## PAPEL DESTE DOCUMENTO

Este documento orienta a abertura de uma nova especialidade ou nova frente de produção dentro do ambiente daktus.

Ele não é o ponto de entrada do ambiente.
O ponto de entrada é `AGENTE.md`.

Use este documento apenas quando a frente ainda estiver em fase inicial e for necessário estruturar o começo do trabalho.

---

## QUANDO USAR

Ative este documento quando:

- uma nova especialidade for iniciada;
- um novo protocolo precisar ser aberto do zero;
- ainda não existir frente estruturada para o tema;
- for necessário organizar o início da produção antes do pipeline normal seguir.

Não use este documento quando:
- a especialidade já estiver em andamento;
- a sessão for continuação de frente já aberta;
- o estado atual já estiver definido em `HANDOFF.md` e `ESTADO.md`;
- a fase ativa já for posterior ao kickstart.

---

## PRÉ-REQUISITO

Antes de usar este documento, o agente já deve ter lido:

1. `AGENTE.md`
2. `HANDOFF.md`, se existir
3. `ESTADO.md`
4. `SKILL.md`

Só depois disso decidir se realmente se trata da abertura de uma nova frente.

---

## OBJETIVO DO KICKSTART

Ao iniciar uma nova especialidade, o objetivo não é “produzir tudo”.
O objetivo é deixar a frente pronta para entrar no pipeline de forma clara, rastreável e sustentável.

Uma boa sessão de kickstart deve:

- enquadrar o problema;
- definir o escopo inicial;
- localizar ou criar a frente correta no repositório;
- identificar a fase inicial real;
- listar os artefatos mínimos necessários;
- registrar o próximo passo executável.

---

## PRINCÍPIO CENTRAL

Nova frente não significa leitura total do repositório.

Mesmo em kickstart, vale a lógica de progressive disclosure:
- ler primeiro o estado do ambiente;
- entender o pipeline;
- localizar os documentos auxiliares relevantes;
- criar apenas o mínimo necessário para a frente começar bem.

---

## PERGUNTAS QUE O AGENTE DEVE RESPONDER

Antes de iniciar o trabalho, o agente deve responder internamente:

- Qual é a especialidade ou frente nova?
- Essa frente realmente não existe ainda?
- Já há materiais prévios no ambiente que sirvam de base?
- Existe benchmark maduro que possa orientar a estrutura?
- Qual é a fase inicial correta?
- Quais artefatos mínimos precisam existir após esta sessão?
- O que ainda não deve ser produzido agora?

---

## REGRA DE NÃO DUPLICAÇÃO

Antes de abrir uma nova frente, verificar se já existe:

- diretório da especialidade;
- material preliminar em `especialidades/`;
- artefatos relacionados em `referencia/`;
- sessão anterior em `history/`;
- menção no `HANDOFF.md` ou `ESTADO.md`.

Não criar frente duplicada.
Não reiniciar trabalho já existente com outro nome.
Não abrir estrutura paralela sem necessidade clara.

---

## FONTE DE VERDADE PARA O INÍCIO

Na abertura de nova frente, a ordem de autoridade continua sendo:

1. instrução explícita do usuário nesta sessão;
2. `HANDOFF.md`;
3. `ESTADO.md`;
4. `SKILL.md`;
5. documentos auxiliares aplicáveis;
6. histórico.

Se o usuário disser que a frente é nova, mas houver evidência de trabalho prévio no repositório, o agente deve registrar a divergência e propor a interpretação mais consistente.

---

## SAÍDA ESPERADA DE UM KICKSTART

Ao final da sessão, a nova frente deve ter pelo menos:

- nome definido da especialidade ou tema;
- localização correta no repositório;
- fase inicial identificada;
- escopo inicial descrito;
- artefatos mínimos listados;
- benchmark estrutural identificado, se houver;
- próximo passo recomendado;
- registro de continuidade preparado.

---

## ARTEFATOS MÍNIMOS ESPERADOS

Dependendo do caso, o kickstart pode resultar em:

- criação ou confirmação de diretório da frente em `especialidades/{nome}/`;
- documento inicial de briefing ou enquadramento;
- definição dos documentos-base que serão usados;
- registro no `HANDOFF.md`;
- atualização do `ESTADO.md`, se a nova frente alterar o snapshot do ambiente;
- registro da sessão em `history/session_NNN.md`.

Criar apenas o que for necessário.
Não materializar estruturas vazias sem utilidade imediata.

---

## ESTRUTURA RECOMENDADA PARA NOVA FRENTE

Quando realmente necessário abrir uma nova frente ativa, a convenção preferencial é:

```text
especialidades/{nome-da-especialidade}/
````

Dentro dela, os artefatos devem surgir de forma incremental, conforme a fase:

* briefing / arquitetura
* base de evidências
* auditorias
* playbook
* JSON
* QA

Não criar todos os arquivos de uma vez.
A estrutura deve acompanhar a evolução real da frente.

---

## BENCHMARKS

Sempre que possível, identificar uma frente madura ou artefato consolidado como benchmark estrutural.

Benchmark serve para:

* arquitetura;
* modelagem;
* organização de artefatos;
* estilo de transição entre fases;
* padrões técnicos reutilizáveis.

Benchmark não serve para:

* copiar lógica clínica;
* presumir condutas;
* transplantar perguntas entre especialidades;
* justificar salto de fase.

---

## RELAÇÃO COM O PIPELINE

Após o kickstart, a frente deve entrar no pipeline normal do ambiente.

Via de regra:

* nova frente começa em `briefing-arquitetura`;
* em seguida evolui para evidências, auditoria, playbook e demais fases;
* só avança se os gates forem sendo cumpridos.

O kickstart não substitui as sub-skills do pipeline.
Ele apenas prepara a entrada correta da frente.

---

## ERROS A EVITAR

* começar pela produção final;
* abrir múltiplas frentes para o mesmo tema;
* ler todos os documentos do repositório sem necessidade;
* criar estrutura de pastas excessiva logo no início;
* ignorar benchmarks já disponíveis;
* confundir benchmark estrutural com autorização clínica;
* deixar a nova frente sem registro em `HANDOFF.md` e `ESTADO.md` quando aplicável.

---

## CHECKLIST OPERACIONAL

Ao usar este documento, verificar:

* a frente realmente é nova;
* a fase inicial foi identificada corretamente;
* não há duplicação com materiais existentes;
* o diretório correto foi localizado ou criado;
* os artefatos mínimos foram definidos;
* o próximo passo ficou claro;
* a continuidade foi registrada.

---

## MODELO DE ENTREGA DA SESSÃO DE KICKSTART

Ao final, o agente deve entregar algo neste formato:

### 1. Frente aberta

* nome da especialidade ou tema
* localização no repositório

### 2. Estado inicial identificado

* fase inicial
* materiais prévios encontrados
* benchmark estrutural, se houver

### 3. Escopo inicial

* o que esta frente pretende produzir
* o que ainda não será feito agora

### 4. Artefatos mínimos da abertura

* o que foi criado, confirmado ou mapeado

### 5. Próximo passo recomendado

* próxima ação executável no pipeline

---

## REGRA FINAL

Este documento só deve ser usado para abrir corretamente uma nova frente.

Ele não substitui:

* `AGENTE.md` como boot;
* `HANDOFF.md` como estado operacional curto;
* `ESTADO.md` como snapshot canônico;
* `SKILL.md` como orchestrator do pipeline;
* a sub-skill específica da fase ativa.

Use este documento para começar bem.
Depois, volte ao pipeline normal do ambiente.