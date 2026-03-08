"""
patch_v011_to_v012.py — Patch v0.1.1 → v0.1.2
Conecta uids de alta prioridade à conduta, corrige condições quebradas
pós-conversão boolean, e adiciona alertas baseados em scores clínicos.

Grupos:
  A — Corrigir expressoes de perguntas com referencias a boolean fields
  B — Corrigir condições da conduta com padrões == 'sim' em campos boolean
  C — Adicionar 10 novos itens mensagem na conduta médica
  D — Atualizar condições de 2 encaminhamentos existentes
  E — Atualizar metadata.version para 0.1.2
"""

import json
import uuid
import sys
import copy

sys.stdout.reconfigure(encoding="utf-8")

SRC = "especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.1.json"
DST = "especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json"


def uid():
    return str(uuid.uuid4())


d = json.load(open(SRC, encoding="utf-8"))
d = copy.deepcopy(d)

nodes_by_id = {n["id"]: n for n in d["nodes"]}
changes = []


def find_node(node_id):
    n = nodes_by_id.get(node_id)
    if n is None:
        raise KeyError(f"Nó não encontrado: {node_id}")
    return n


def find_question(node, target_uid):
    for q in node["data"].get("questions", []) or []:
        if q.get("uid") == target_uid:
            return q
    return None


# Campos que foram convertidos para boolean nas fases anteriores
# Qualquer referência a {campo} == 'sim' ou {campo} != 'sim' está quebrada
BOOLEAN_FIELDS = [
    "ideacao_ativa", "ideacao_com_intencao", "ideacao_com_plano",
    "ideacao_com_metodo", "acesso_meios_letais", "tentativa_previa",
    "sexo_feminino_ie", "gestante", "internacao_psiq_previa",
    "primeira_consulta_vida", "encaminhamento_urgencia_necessario",
    "ideacao_passiva",
    "ciclagem_rapida", "especificador_misto", "sintomas_psicoticos_humor",
    "burnout_criterios_tdm", "primeiro_episodio_psicotico",
    "esquizofrenia_refrataria", "comportamento_suicida_recorrente",
    "tdah_abuso_substancias_ativo", "sintomas_cardiacos_tdah",
    "tea_irritabilidade_grave", "tpb_autolesao_ativa",
]


def fix_boolean_refs(text):
    """Substitui padroes == 'sim' e != 'sim' em campos boolean."""
    original = text
    for field in BOOLEAN_FIELDS:
        text = text.replace(f"{field} == 'sim'", f"{field} is True")
        text = text.replace(f"{field} != 'sim'", f"{field} is False")
        text = text.replace(f"{field} == 'nao'", f"{field} is False")
        text = text.replace(f"{field} != 'nao'", f"{field} is True")
    return text, original != text


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO A — Corrigir expressoes de perguntas
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO A — Corrigir expressoes de perguntas (refs a boolean fields)")
print("=" * 70)

for node in d["nodes"]:
    for q in node["data"].get("questions", []) or []:
        expr = q.get("expressao", "") or ""
        if not expr:
            continue
        new_expr, changed = fix_boolean_refs(expr)
        if changed:
            q["expressao"] = new_expr
            nome = f"[{node['id'][:30]}] uid={q.get('uid', '?')}"
            print(f"  [CORRIGIDO] {nome}")
            print(f"    ANTES:  {expr}")
            print(f"    DEPOIS: {new_expr}")
            changes.append(f"A: expressao corrigida — {q.get('uid', '?')}")

if not any(c.startswith("A:") for c in changes):
    print("  Nenhuma expressao de pergunta precisou de correção.")
print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO B — Corrigir condições da conduta
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO B — Corrigir condições da conduta (padrões == 'sim' em boolean)")
print("=" * 70)

CONDUTA_ID = "node-psiq-06-conduta"
conduta_node = find_node(CONDUTA_ID)
conduta_data = conduta_node["data"].get("condutaDataNode") or {}

for section in ["mensagem", "exame", "encaminhamento", "medicamento", "orientacao"]:
    for item in conduta_data.get(section, []) or []:
        cond = item.get("condicao", "") or ""
        new_cond, changed = fix_boolean_refs(cond)
        if changed:
            item["condicao"] = new_cond
            nome = item.get("nome", item.get("id", "?"))[:50]
            print(f"  [CORRIGIDO] {section}: {nome}")
            print(f"    ANTES:  {cond}")
            print(f"    DEPOIS: {new_cond}")
            changes.append(f"B: condicao da conduta corrigida — {nome}")

if not any(c.startswith("B:") for c in changes):
    print("  Nenhuma condição da conduta precisou de correção.")
print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO C — Adicionar novos itens mensagem na conduta médica
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO C — Adicionar 10 novos alertas (mensagem) na conduta médica")
print("=" * 70)

NOVAS_MENSAGENS = [
    {
        "id": uid(),
        "nome": "⚠️ ACESSO A MEIOS LETAIS — Lethal means counseling obrigatório",
        "condicao": "acesso_meios_letais is True",
        "conteudo": (
            "<p><strong>Realizar lethal means counseling hoje.</strong></p>"
            "<p>Orientar armazenamento seguro de medicamentos, armas de fogo e outros meios letais. "
            "Envolver familiar ou responsável de confiança. Registrar aconselhamento no prontuário.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "⚠️ ESQUIZOFRENIA REFRATÁRIA — Clozapina como próximo passo",
        "condicao": "esquizofrenia_refrataria is True",
        "conteudo": (
            "<p><strong>Esquizofrenia refratária: indicar clozapina.</strong></p>"
            "<p>Critério: falha em ≥2 antipsicóticos em dose e duração adequadas. "
            "Registrar no PGRM/ANVISA antes de iniciar. Solicitar hemograma basal (ANC ≥1.500/mm³). "
            "Iniciar com 12,5–25 mg/dia com titulação lenta.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "⚠️ COMPORTAMENTO SUICIDA RECORRENTE — TCD prioritária",
        "condicao": "comportamento_suicida_recorrente is True",
        "conteudo": (
            "<p><strong>Comportamento suicida recorrente: TCD (Terapia Comportamental Dialética) indicada.</strong></p>"
            "<p>Encaminhar para serviço com TCD disponível. "
            "TCD é o tratamento de primeira linha para padrão de autolesão e comportamento suicida recorrente. "
            "Considerar CAPS-II se sem recursos ambulatoriais.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "⛔ GESTANTE + VALPROATO — Contraindicação absoluta: substituir hoje",
        "condicao": "gestante is True and 'valproato' in medicamentos_em_uso",
        "conteudo": (
            "<p><strong>Valproato contraindicado na gestação — substituir imediatamente.</strong></p>"
            "<p>Risco de malformações maiores ~9% (espinha bífida, cardiopatia congênita) e prejuízo "
            "neurocognitivo fetal. Considerar lamotrigina ou lítio após avaliação risco-benefício. "
            "Encaminhar para psiquiatria de ligação com obstetrícia.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "⚠️ GESTANTE + LÍTIO — Revisão urgente de prescrição",
        "condicao": "gestante is True and 'litio' in medicamentos_em_uso",
        "conteudo": (
            "<p><strong>Lítio na gestação: avaliar risco-benefício com urgência.</strong></p>"
            "<p>Risco de anomalia de Ebstein (~0,1%). Ajustar dose para litemia mínima eficaz "
            "(volumes hídricos alterados). Solicitar ecocardiograma fetal. "
            "Encaminhar para psiquiatria de ligação com obstetrícia.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "⚠️ PSICOSE EM EPISÓDIO DE HUMOR — Antipsicótico indicado",
        "condicao": "sintomas_psicoticos_humor is True",
        "conteudo": (
            "<p><strong>Episódio de humor com psicose: adicionar antipsicótico.</strong></p>"
            "<p>Considerar quetiapina, olanzapina ou aripiprazol como add-on ao estabilizador de humor. "
            "Manter antipsicótico até remissão completa dos sintomas psicóticos antes de iniciar redução.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "⚠️ DEPRESSÃO GRAVE — MADRS ≥20: Revisar conduta",
        "condicao": "madrs_score >= 20",
        "conteudo": (
            "<p><strong>MADRS ≥20: depressão moderada a grave.</strong></p>"
            "<p>Revisar adequação de dose do antidepressivo atual. "
            "Considerar potencialização (lítio, quetiapina ou aripiprazol em dose baixa) "
            "se sem resposta após 4–6 semanas em dose adequada. "
            "MADRS ≥30: ponderar hospitalização psiquiátrica.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "⛔ MANIA GRAVE — YMRS ≥20: Avaliar internação",
        "condicao": "ymrs_score >= 20",
        "conteudo": (
            "<p><strong>YMRS ≥20: mania grave.</strong></p>"
            "<p>Avaliar internação psiquiátrica imediata se risco para si ou terceiros. "
            "Garantir estabilizador de humor em dose terapêutica + antipsicótico. "
            "Suspender estimulantes ou antidepressivos em monoterapia.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "ℹ️ TOC MODERADO-GRAVE — Y-BOCS ≥16: TCC/ERP indicada",
        "condicao": "ybocs_score >= 16",
        "conteudo": (
            "<p><strong>Y-BOCS ≥16: TOC moderado a grave.</strong></p>"
            "<p>Encaminhar para TCC com ERP (Exposição e Prevenção de Resposta) — padrão ouro. "
            "Y-BOCS ≥32: considerar potencialização com antipsicótico atípico em baixa dose "
            "(risperidona 0,5–2 mg ou aripiprazol 2,5–15 mg).</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "ℹ️ TEPT CLÍNICO — PCL-5 ≥33: EMDR/TF-CBT indicado",
        "condicao": "pcl5_score >= 33",
        "conteudo": (
            "<p><strong>PCL-5 ≥33: critérios de TEPT preenchidos.</strong></p>"
            "<p>Encaminhar para EMDR (Eye Movement Desensitization and Reprocessing) "
            "ou TF-CBT (Terapia Cognitivo-Comportamental focada em Trauma) — "
            "tratamentos de primeira linha (OMS, APA). "
            "Evitar benzodiazepínicos a longo prazo (risco de cronicidade).</p>"
        ),
        "observacao": "",
    },
]

mensagens = conduta_data.get("mensagem", []) or []
for msg in NOVAS_MENSAGENS:
    mensagens.append(msg)
    print(f"  [ADICIONADO] {msg['nome']}")
    print(f"    condicao: {msg['condicao']}")
    changes.append(f"C: nova mensagem — {msg['nome'][:50]}")

conduta_data["mensagem"] = mensagens
print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO D — Atualizar condições de encaminhamentos existentes
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO D — Atualizar condições de encaminhamentos existentes")
print("=" * 70)

# Mapeamento: id do item → nova condicao
ENCAMINHAMENTOS_UPDATE = {
    # CAPS-II: adicionar comportamento_suicida_recorrente como gate adicional
    "260889e2-fa7b-405f-9e28-3d6c6237bc1a": (
        "('esquizofrenia' in diagnostico_ativo) or (comportamento_suicida_recorrente is True)"
    ),
    # SAMU 192: adicionar encaminhamento_urgencia_necessario como gate adicional
    "a86867c6-ab7b-44c7-a1c8-b958298c42e8": (
        "(risco_suicidio_alto is True) or (encaminhamento_urgencia_necessario is True)"
    ),
}

encaminhamentos = conduta_data.get("encaminhamento", []) or []
for item in encaminhamentos:
    item_id = item.get("id", "")
    if item_id in ENCAMINHAMENTOS_UPDATE:
        old_cond = item.get("condicao", "")
        new_cond = ENCAMINHAMENTOS_UPDATE[item_id]
        item["condicao"] = new_cond
        nome = item.get("nome", item_id)[:50]
        print(f"  [ATUALIZADO] encaminhamento: {nome}")
        print(f"    ANTES:  {old_cond}")
        print(f"    DEPOIS: {new_cond}")
        changes.append(f"D: encaminhamento atualizado — {nome}")

if not any(c.startswith("D:") for c in changes):
    print("  Nenhum encaminhamento atualizado (IDs não encontrados — verificar).")
print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO E — Atualizar metadata
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO E — Atualizar metadata.version")
print("=" * 70)

if "metadata" in d:
    old_v = d["metadata"].get("version", "N/A")
    d["metadata"]["version"] = "0.1.2"
    print(f"  [ATUALIZADO] metadata.version: {old_v!r} → '0.1.2'")
    changes.append("E: metadata.version → 0.1.2")
elif "meta" in d:
    old_v = d["meta"].get("version", "N/A")
    d["meta"]["version"] = "0.1.2"
    print(f"  [ATUALIZADO] meta.version: {old_v!r} → '0.1.2'")
    changes.append("E: meta.version → 0.1.2")
else:
    print("  [AVISO] Nenhum campo metadata/meta encontrado.")
print()


# ──────────────────────────────────────────────────────────────────────────────
# SALVAR
# ──────────────────────────────────────────────────────────────────────────────

with open(DST, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("=" * 70)
print("RESUMO DO PATCH v0.1.2")
print("=" * 70)
print(f"  Arquivo de saída: {DST}")
print(f"  Total de modificações: {len(changes)}")
print()
for i, c in enumerate(changes, 1):
    print(f"  {i:2d}. {c}")
print()
print("OK — v0.1.2 gerado com sucesso.")
