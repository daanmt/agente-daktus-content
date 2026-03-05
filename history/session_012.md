# Sessao 012 — Varredura End-to-End + Novas Orientacoes

**Data:** 2026-03-04
**Ferramenta:** Claude Code Opus 4.6
**Duracao estimada:** ~1h
**Repo:** agente-daktus-content

---

## Objetivo

Varredura end-to-end completa da ficha ginecologia v1.0.0 exportada por Dan (com correcoes aplicadas no Spider), seguida de criacao das orientacoes clinicas faltantes.

---

## Metodologia da Varredura

1. Busca automatizada por expressoes bare (clinicalExpressions sem `is True`) — resultado vazio ✓
2. Busca por typo `seletec_any` — resultado vazio ✓
3. Verificacao de CIDs criticos (creatinina) — Z13.6 confirmado ✓
4. Leitura de todos os condicionais de roteamento (8 no-a-no)
5. Leitura de todas as 7 clinicalExpressions do summary
6. Auditoria de todas as 20 mensagens, 16 encaminhamentos, 39 exames
7. Mapeamento de gaps em orientacoes (cross-referencia conduct x orientacao)

---

## Confirmacoes: Achados Sessao 011 Resolvidos

| Achado | Verificacao linha a linha |
|--------|--------------------------|
| C2 — `espessamento_endometrial_significativo` bare (2x) | Busca bare retornou vazio. Confirmado. |
| C3 — `trh_indicada` bare (4x) | Busca bare retornou vazio. Confirmado. |
| C4 — `alto_risco_mama` bare (orientacao) | `is True` presente. Confirmado. |
| NEW-C1 — typo `seletec_any` DXA | Busca `seletec_any` retornou vazio. `selected_any` correto. |
| NEW-C2 — 3 bare orientacao cervical | `is True` em todas as tres. Confirmado. |
| NEW-I2 — CID creatinina E78.5 | CID Z13.6 confirmado. |

---

## Achados da Varredura (novos)

### Falsos positivos descartados

- **M1 (T4L sem trouxe_lab guard):** Descartado por Dan — campo numerico so aparece quando trouxe_lab e True. Logica correta.
- **M2 (Ferritina sem trouxe_lab guard):** Idem. Descartado.

### Pendentes (sem alteracao desde s011)

- **I3:** `hpv_resultado_nd` — questao coletada, sem conduta. Aguarda decisao clinica.
- **I4:** `diu_contraindicacao` — questao coletada (gestacao, DIP ativa, distorcao, ca_mama), sem conduta. Aguarda decisao clinica.

---

## Novas Orientacoes Adicionadas

Gap identificado: 5 topicos com exames/encaminhamentos/mensagens mas sem orientacao dedicada.

| ID | Nome | Condicao | Insercao |
|----|------|----------|---------|
| `2130cb40` | Infertilidade e investigacao da fertilidade | `infertilidade_associada is True` | Antes de "Orientacao geral" |
| `3c8161e7` | Incontinencia urinaria | `incontinencia_urinaria is True` | Antes de "Orientacao geral" |
| `786fe125` | Insuficiencia ovariana prematura (POI) | `poi_suspeita is True` | Antes de "Orientacao geral" |
| `d57bef31` | Hepatites virais e HIV: sorologias alteradas | `hiv_reagente or hbsag_reagente or hcv_reagente` | Antes de "Orientacao geral" |
| `1538f488` | Hiperandrogenismo e virilizacao | `not 'sem_sinais' in hiperandrogenismo_sinais` | Antes de "Orientacao geral" |

**Total de orientacoes:** 11 → 16

---

## Topicos COM cobertura adequada (nao precisam de nova orientacao)

| Topico | Cobertura existente |
|--------|-------------------|
| Lesao vulvar / vulvoscopia | Parcialmente via "Corrimento vaginal e ISTs" (ulcera genital → VDRL) |
| Hiperprolactinemia | Encaminhamento existe; orientacao verbal suficiente |
| Lynch / CA endometrio previo | Encaminhamento existe; historia oncologica registrada em N5 |

---

## Arquivos Modificados

| Arquivo | Alteracao |
|---------|----------|
| `especialidades/ginecologia/jsons/amil-ficha-ginecologia-v1.0.0.json` | +5 orientacoes (11→16) |
| `especialidades/ginecologia/research/AUDITORIA_JSON_GINECOLOGIA.md` | Status atualizado; secao novas orientacoes adicionada |
| `ESTADO.md` | Fase ginecologia atualizada; s012 adicionada ao log |
| `scripts/insert_orientacoes.py` | Script temporario (pode ser removido) |

---

## Commit

`feat: adiciona 5 orientacoes clinicas faltantes — ficha ginecologia sessao 012`

---

## Proxima Sessao

1. Dan decide I3 e I4 (decisao clinica)
2. Avaliar inclusao de `historia_familiar_ca` / `lynch_suspeita` (melhoria futura)
3. Iniciar gravacao dos Loom videos com Gabriel
