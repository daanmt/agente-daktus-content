# session_027 — Onda 4: Quality & Precision Reform → v0.6.0

**Data:** 2026-03-11
**Branch:** main
**Input:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.5.0.json`
**Output:** `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.6.0.json`
**Script:** `scripts/patch_v050_to_v060.py`
**Resultado da auditoria:** ✅ 0 BLOQUEANTES

---

## Contexto

Após a Onda 3 (v0.5.0), revisão clínica aprofundada via GPT (Kaplan & Sadock + Dalgalarrondo) identificou 6 áreas de melhoria sistêmica — **nenhuma adiciona perguntas novas ao tronco universal**, todas corrigem precisão, completude e segurança do protocolo:

| Área | Problema | Grupo |
|------|----------|-------|
| Fórmulas de risco suicida | `risco_suicidio_baixo` exigia `ideacao_ativa is True` (contradição conceitual); `risco_suicidio_intermediario` cobria apenas ativa+tentativa sem plano; `risco_suicidio_alto` classificava como alto cenários que seriam intermediários | A |
| Bug DSL `causa_organica_investigada` | 4 condições de exame usavam `!= 'sim'` para campo boolean — operador inválido para DSL | B1 |
| Bug de conteúdo DEPRESSÃO LEVE | Mensagem citava "PHQ-9 ≥15" (moderada/grave) quando condição era `depressao_leve` | B2 |
| Redundância `tdah_abuso_substancias_ativo` | Pergunta boolean replicava informação já coletada em `substancias_uso` | C |
| Códigos TUSS incorretos | ~19 exames com código ou nomenclatura não canônica | D |
| Orientações ao paciente | 5 orientações genéricas; 6 novas condicionais clinicamente necessárias | E |
| Acentos ausentes | ~22 instâncias em campos de display afetavam UX | F |

---

## Mudanças implementadas (63 total)

### GRUPO A — Recalibrar 3 fórmulas de risco suicida

**Nó:** `summary-6e3e3703-1337-46f0-8b08-55e814f0f8ef` → `clinicalExpressions`

| Expressão | Problema corrigido | Nova fórmula |
|-----------|-------------------|--------------|
| `risco_suicidio_baixo` | Exigia `ideacao_ativa is True` (contradição: risco baixo = ideação passiva) | `(ideacao_passiva is True) and (ideacao_ativa is False) and (tentativa_previa is False) and not('sem_fatores_protetores' in suporte_social)` |
| `risco_suicidio_intermediario` | Restrito demais — não cobria ativa-sem-tentativa nem tentativa-sem-ideação-atual | `((ideacao_ativa is True) and (ideacao_com_plano is False) and (ideacao_com_intencao is False) and (acesso_meios_letais is False)) or ((tentativa_previa is True) and (ideacao_ativa is False) and (ideacao_com_plano is False) and (ideacao_com_intencao is False))` |
| `risco_suicidio_alto` | Incluía ativa+tentativa_prévia (sem plano/intenção atual) como ALTO — pode ser intermediário | `((ideacao_com_plano is True) and (ideacao_com_intencao is True) and (acesso_meios_letais is True)) or ((tentativa_previa is True) and ((ideacao_ativa is True) or (ideacao_com_intencao is True) or (ideacao_com_plano is True)))` |

---

### GRUPO B — Bug fixes DSL e conteúdo

#### B1 — `causa_organica_investigada` (4 exames)

**Problema:** `causa_organica_investigada != 'sim'` usa comparação de string em campo boolean — DSL inválida.
**Correção:** substituído por `causa_organica_investigada is False`

| ID do exame | Nome |
|-------------|------|
| `a1b3e931-a1fd-4025-b87d-eba52377d1eb` | Hemograma com diferencial (1º episódio psicótico) |
| `9a4f2983-2eeb-4635-beed-624d33264e2f` | TSH (1º episódio psicótico) |
| `6cbec494-910d-41fa-9739-de889c98b219` | VDRL / RPR (sífilis) |
| `1e350367-a25d-4550-88b0-43e99f381cb1` | Sorologia HIV (anti-HIV 1 e 2) |

#### B2 — Mensagem DEPRESSÃO LEVE

**ID:** `d9c2f119-1f59-4402-8d8a-37d786c6a09f`

- **Nome anterior:** `"DEPRESSAO LEVE — Monitorar evolucao e iniciar tratamento"`
- **Nome novo:** `"DEPRESSÃO LEVE — Monitorar evolução e reavaliar em 2–4 semanas"`
- **Conteúdo corrigido:** de PHQ-9 ≥15 (moderada/grave) para PHQ-9 < 10 (leve), com orientação para intervenções psicossociais e reavaliação em 2–4 semanas

---

### GRUPO C — Eliminar redundância `tdah_abuso_substancias_ativo`

#### C1 — Remoção da pergunta
- **ID removido:** `P51a70f03-660e-434b-96f3-ea9f6d956cee`
- **Nó:** `node-psiq-04-diagnostico` (24 → **23 perguntas**)

#### C2 — Expressão derivada no nó summary
```json
{
  "id": "expr-tdah-abuso-derivado-001",
  "name": "tdah_abuso_substancias_ativo",
  "expressao": "not('nenhum' in substancias_uso)"
}
```
> `nenhum` é a opção exclusiva de ausência em `substancias_uso`. Qualquer outra seleção implica uso ativo.

#### C3 — Atualização de condições dos estimulantes (3 medicamentos)

| Medicamento | Condição anterior | Condição nova |
|-------------|-------------------|---------------|
| Metilfenidato 10mg | `... and tdah_abuso_substancias_ativo is False` | `... and 'nenhum' in substancias_uso` |
| Concerta LP 18mg | `... and tdah_abuso_substancias_ativo is False` | `... and 'nenhum' in substancias_uso` |
| Ritalina LA 10mg | `... and tdah_abuso_substancias_ativo is False` | `... and 'nenhum' in substancias_uso` |

---

### GRUPO D — Auditoria e correção TUSS (19 códigos + 1 nome)

| Código anterior | Código correto | Nome TUSS canônico |
|-----------------|----------------|--------------------|
| `40320094` | `40316521` | Tireoestimulante, hormônio (TSH) |
| `40302130` | `40301400` | Cálcio |
| `40302415` | `40302580` | Uréia |
| `40302555` | `40301168` | Ácido valpróico |
| `40302180` | `40302512` | Transaminase pirúvica (ALT) |
| `40302172` | `40302504` | Transaminase oxalacética (AST) |
| `40302082` | `40301320` | Amônia |
| `40302490` | `40301435` | Carbamazepina |
| `40302350` | `40302423` | Sódio |
| `40302058` | `40304361` | Hemograma com contagem de plaquetas (×2 itens) |
| `40302148` | `40302040` | Glicose |
| `40307252` | `40302733` | Hemoglobina glicada (A1c) |
| `40302121` | `40302750` | Perfil lipídico / lipidograma |
| `40302407` | `40302547` | Triglicerídeos |
| `40302326` | `40316416` | Prolactina |
| `40306045` | `40305759` | Beta-HCG |
| `40314098` | `40307760` | Sífilis - VDRL |
| `40312003` | `40307182` | HIV1 + HIV2 |
| ECG `40101010` (inalterado) | — | Nome: `"ECG convencional de até 12 derivações"` |

**Códigos mantidos:** Lítio `40302229` ✓ | Creatinina `40301630` ✓ | Troponina `40302571` ✓ | PCR `40308391` ✓ | HLA-B*1502 `40306887` ✓

---

### GRUPO E — 6 novas orientações ao paciente

| ID | Nome | Condição |
|----|------|----------|
| `orient-litio-001` | Lítio — uso seguro e monitoramento | `'litio' in medicamentos_em_uso` |
| `orient-tab-episodio-001` | Transtorno Bipolar — reconhecer sinais de um novo episódio | `'tab' in diagnostico_ativo` |
| `orient-substancias-001` | Substâncias e tratamento psiquiátrico | `not('nenhum' in substancias_uso)` |
| `orient-tdah-001` | TDAH — estratégias práticas do dia a dia | `'tdah' in diagnostico_ativo or 'deficit_atencao' in motivo_consulta` |
| `orient-ta-001` | Transtornos alimentares — recuperação e suporte | `selected_any(diagnostico_ativo, ...) or selected_any(ta_fenotipo, ...)` |
| `orient-clozapina-001` | Clozapina — vigilância e segurança hematológica | `selected_any(medicamentos_em_uso, 'clozapina')` |

---

### GRUPO F — Restauração de acentos em campos de display

**22 correções** aplicadas recursivamente a campos `titulo`, `descricao`, `label`, `nome`, `conteudo`, `narrativa`. Campos técnicos (UIDs, expressões DSL, condições) inalterados.

Principais correções:
- `DEPRESSAO` → `DEPRESSÃO`
- `avaliacao` → `avaliação` | `avaliacao inicial` → `avaliação inicial`
- `Reavaliacao clinica` → `Reavaliação clínica`
- `suicidio` → `suicídio` | `iminencia` → `iminência`
- `criterios` → `critérios` | `caracteristicas` → `características`
- `psiquiatrico` → `psiquiátrico` | `psiquiatricos` → `psiquiátricos`
- `automedicacao` → `automedicação` | `atencao` → `atenção`

---

## Notas de implementação

- **Bug estrutural corrigido no script**: GRUPO E usava loop genérico com `break` que poderia atingir `conduta-a9ccd9ee-...` antes de `node-psiq-06-conduta`. Corrigido para usar `find_node(data, NODE_CONDUTA)` diretamente.
- **Estrutura JSON**: todo conteúdo dos nós está em `node["data"]` (não no nível raiz). `exam["codigo"]` é lista de objetos `{iid, sistema, codigo, nome}`.
- **clinicalExpressions**: campo com `expressao: ''` em v0.5.0 para 4 expressões — agora 3 preenchidas, 1 derivada adicionada (`tdah_abuso_substancias_ativo`), 1 mantida vazia (`sexo_feminino_ie`).

---

## Ordem final das perguntas em node-psiq-04-diagnostico (v0.6.0)

| # | UID | Status |
|---|-----|--------|
| 1 | `internacao_indicada_p0` | existente |
| 2 | `episodio_atual_humor` | existente |
| 3 | `bipolar_rastreio` | existente |
| 4 | `burnout_tdm_discriminador` | existente (Onda 2) |
| 5 | `subtipo_ansioso` | existente |
| 6 | `audit_score` | existente |
| 7 | `substancia_relacao_quadro` | existente (Onda 2) |
| 8 | `primeiro_episodio_psicotico` | existente |
| 9 | `eps_presente` | existente |
| 10 | `esquizofrenia_refrataria` | existente |
| 11 | `comportamento_suicida_recorrente` | existente |
| 12 | `tpb_rastreio` | existente (Onda 2) |
| 13 | `tdah_discriminador` | existente |
| 14 | `tea_irritabilidade_grave` | existente |
| 15 | `tea_nivel_suporte` | existente (Onda 2) |
| 16 | `tea_suspeita_clinica` | existente (Onda 3) |
| 17 | `contexto_agressividade` | existente |
| 18 | `agressividade_iminencia` | existente (Onda 3) |
| 19 | `perfil_sono` | existente |
| 20 | `sintomas_depressivos_presentes` | existente |
| 21 | `ta_fenotipo` | existente (Onda 3) |
| 22 | `an_sinais_alarme` | existente |
| 23 | `clozapina_semana` | existente |

> `tdah_abuso_substancias_ativo` removido (era posição 13 em v0.5.0) → substituído por expressão derivada em `clinicalExpressions`.

---

## Métricas comparativas

| Métrica | v0.5.0 | v0.6.0 |
|---------|--------|--------|
| Perguntas (node-psiq-04-diagnostico) | 24 | **23** (-1: tdah_abuso removido) |
| Perguntas (node-psiq-05-farmacos) | 7 | **7** (inalterado) |
| Mensagens de conduta | 37 | **37** (inalterado) |
| Orientações ao paciente | 5 | **11** (+6: E1–E6) |
| Expressões derivadas (clinicalExpressions) | 4 | **5** (+1: tdah_abuso derivado) |
| Fórmulas de risco recalibradas | — | **3** (baixo, intermediário, alto) |
| Bugs DSL corrigidos | — | **4** (causa_organica_investigada) |
| Bugs de conteúdo corrigidos | — | **1** (DEPRESSÃO LEVE) |
| Exames com TUSS corrigido | — | **19** (códigos) + **1** (nome ECG) |
| Medicamentos estimulantes atualizados | — | **3** (condição simplificada) |
| Acentos restaurados | — | **22** instâncias |
| IIDs totais | 120 | **126** (+6 orientações) |
| Erros de validação | 0 | **0** ✅ |

---

## Artefatos produzidos

- `especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.6.0.json`
- `scripts/patch_v050_to_v060.py`

---

## Próximo passo recomendado

1. **QA clínico de v0.6.0 no preview Daktus** — 10 perfis críticos (herdados de v0.5.0):
   - Alto risco suicida com acesso a meios → restrição de meios letais + fórmula risco_alto recalibrada
   - Mulher grávida em uso de valproato → alerta gestante+VPA
   - Esquizofrenia refratária → clozapina + hemograma + orientação clozapina nova
   - TDAH com TDM → Metilfenidato + Bupropiona (condição `'nenhum' in substancias_uso`)
   - Depressão com rastreio bipolar positivo → alerta BIPOLAR NÃO DESCARTADO
   - Agressividade com red flags orgânicos → Neurologia + alerta
   - Retorno medicamentoso → shortcut (sem internacao_psiq_previa e historico_familiar)
   - Autolesão sem TPB → rastreio TPB + alerta TCD
   - **[Onda 3]** Primeiro episódio psicótico via motivo_consulta → alerta investigação orgânica
   - **[Onda 3]** Mania grave com psicose/agitação → mensagem urgência + SAMU
2. **Confirmar MEVOs** com equipe Amil (ver `history/session_022_report_farmacologia.md`)
3. **Confirmar Escitalopram MEVO 20945** — inserido manualmente, não verificado no Mevo..xlsx
4. **v0.7.0 / Onda 5** — fármacos de 2ª linha (Fluvoxamina, Clomipramina, Guanfacina XR, Prazosina, Buspirona) + limpeza de perguntas sem conduta direta (32 UIDs A3)
5. Promover para v1.0.0 após QA clínico completo
