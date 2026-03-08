"""
patch_vdraft_to_v011.py — Patch estrutural: vdraft → v0.1.1
Aplica 6 grupos de correções no JSON de psiquiatria (vdraft do usuário).
Não modifica o arquivo de entrada. Gera novo arquivo v0.1.1.

Grupos:
  A — Corrigir fórmulas do nó summary (risco_suicidio_alto/intermediario/baixo)
  B — Reescrever condicoes da conduta de nivel_risco_p0 → expressoes booleanas
  C — Mover spi_realizado e internacao_indicada_p0 para Nó 4 (Medicina)
  D — Corrigir expressao de ideacao_com_plano (ideacao_suicida → ideacao_ativa)
  E — Converter ciclagem_rapida e especificador_misto para boolean
  F — Corrigir expressao de vpa_mie_consentimento (== 'sim' → is True)
"""

import json
import sys
import copy

sys.stdout.reconfigure(encoding="utf-8")

SRC = "especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-vdraft.json"
DST = "especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.1.json"

d = json.load(open(SRC, encoding="utf-8"))
d = copy.deepcopy(d)

# Índice de nós por id para acesso rápido
nodes_by_id = {n["id"]: n for n in d["nodes"]}

changes = []


# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────

def find_node(node_id):
    n = nodes_by_id.get(node_id)
    if n is None:
        raise KeyError(f"Nó não encontrado: {node_id}")
    return n

def find_question(node, uid):
    for q in node["data"].get("questions", []) or []:
        if q.get("uid") == uid:
            return q
    return None

def find_question_index(node, uid):
    qs = node["data"].get("questions", []) or []
    for i, q in enumerate(qs):
        if q.get("uid") == uid:
            return i
    return -1

def find_summary_expr(node, name):
    for expr in node["data"].get("clinicalExpressions", []) or []:
        if expr.get("name") == name:
            return expr
    return None


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO A — Corrigir fórmulas do nó summary
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO A — Fórmulas do nó summary (processamento clínico)")
print("=" * 70)

SUMMARY_ID = "summary-6e3e3703-1337-46f0-8b08-55e814f0f8ef"
summary_node = find_node(SUMMARY_ID)

FORMULAS = {
    "risco_suicidio_alto": (
        "(ideacao_ativa is True) and ("
        "(ideacao_com_plano is True) or "
        "(ideacao_com_intencao is True) or "
        "(ideacao_com_metodo is True) or "
        "(tentativa_previa is True) or "
        "(acesso_meios_letais is True)"
        ")"
    ),
    "risco_suicidio_intermediario": (
        "(ideacao_ativa is True) and "
        "(ideacao_com_plano is False) and "
        "(ideacao_com_intencao is False) and "
        "(tentativa_previa is True)"
    ),
    "risco_suicidio_baixo": (
        "(ideacao_ativa is True) and "
        "(ideacao_com_plano is False) and "
        "(ideacao_com_intencao is False) and "
        "(tentativa_previa is False) and "
        "(not('sem_fatores_protetores' in suporte_social))"
    ),
}

for expr_name, new_formula in FORMULAS.items():
    expr = find_summary_expr(summary_node, expr_name)
    if expr is not None:
        old_formula = expr.get("formula", "")
        expr["formula"] = new_formula
        print(f"  [CORRIGIDO] {expr_name}")
        print(f"    ANTES: {old_formula}")
        print(f"    DEPOIS: {new_formula}")
        changes.append(f"A: fórmula corrigida — {expr_name}")
    else:
        print(f"  [AVISO] expressão '{expr_name}' não encontrada no nó summary")

print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO B — Reescrever condições da conduta (mensagens) de nivel_risco_p0
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO B — Condições da conduta: nivel_risco_p0 → expressões booleanas")
print("=" * 70)

CONDUTA_ID = "node-psiq-06-conduta"
conduta_node = find_node(CONDUTA_ID)
conduta_data = conduta_node["data"].get("condutaDataNode") or {}

# Mapeamento de substituições de strings dentro do campo condicao
SUBSTITUICOES = [
    (
        "nivel_risco_p0 == 'alto'",
        "risco_suicidio_alto is True"
    ),
    (
        "nivel_risco_p0 == 'intermediario'",
        "risco_suicidio_intermediario is True"
    ),
    (
        "selected_any(nivel_risco_p0, 'intermediario', 'alto')",
        "(risco_suicidio_alto is True) or (risco_suicidio_intermediario is True)"
    ),
    (
        "'alto' in nivel_risco_p0",
        "risco_suicidio_alto is True"
    ),
    # Variantes sem aspas simples específicas (fallback)
    (
        "nivel_risco_p0",
        "risco_suicidio_alto"  # fallback genérico — alerta manual se isso disparar
    ),
]

for section_name in ["mensagem", "exame", "encaminhamento", "medicamento", "orientacao"]:
    items = conduta_data.get(section_name, []) or []
    for item in items:
        cond = item.get("condicao", "") or ""
        if "nivel_risco_p0" not in cond:
            continue
        old_cond = cond
        for old_pat, new_pat in SUBSTITUICOES:
            cond = cond.replace(old_pat, new_pat)
        if cond != old_cond:
            item["condicao"] = cond
            nome = item.get("nome", item.get("id", "?"))[:50]
            print(f"  [CORRIGIDO] {section_name}: {nome}")
            print(f"    ANTES:  {old_cond}")
            print(f"    DEPOIS: {cond}")
            changes.append(f"B: condicao da conduta corrigida — {nome}")

print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO C — Mover spi_realizado e internacao_indicada_p0 para Nó 4
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO C — Mover spi_realizado e internacao_indicada_p0 para Medicina")
print("=" * 70)

GATE_P0_ID = "node-psiq-02-gate-p0"
NO4_ID = "node-psiq-04-diagnostico"

gate_p0 = find_node(GATE_P0_ID)
no4 = find_node(NO4_ID)

UIDS_MOVER = {
    "spi_realizado": {
        "condicional": "oculto",
        "expressao": "(risco_suicidio_alto is True) or (risco_suicidio_intermediario is True)",
    },
    "internacao_indicada_p0": {
        "condicional": "oculto",
        "expressao": "risco_suicidio_alto is True",
    },
}

perguntas_para_inserir = []

for uid, updates in UIDS_MOVER.items():
    idx = find_question_index(gate_p0, uid)
    if idx == -1:
        print(f"  [AVISO] '{uid}' não encontrado em {GATE_P0_ID}")
        continue
    q = gate_p0["data"]["questions"].pop(idx)
    # Aplicar updates de condicional e expressao
    q["condicional"] = updates["condicional"]
    q["expressao"] = updates["expressao"]
    perguntas_para_inserir.append(q)
    print(f"  [REMOVIDO de gate-p0] uid={uid}")
    changes.append(f"C: '{uid}' removido de gate-p0")

# Inserir no início do Nó 4
if perguntas_para_inserir:
    no4_questions = no4["data"].get("questions") or []
    # Inserir em ordem: internacao_indicada_p0 primeiro, depois spi_realizado
    # (internacao aparece quando risco alto; spi quando risco intermediario ou alto)
    # Manter a ordem original de retirada para inserção no início
    for q in reversed(perguntas_para_inserir):
        no4_questions.insert(0, q)
        print(f"  [INSERIDO em nó-4 início] uid={q['uid']}")
        changes.append(f"C: '{q['uid']}' inserido em início do nó-4")
    no4["data"]["questions"] = no4_questions

print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO D — Corrigir expressao de ideacao_com_plano
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO D — Corrigir expressao de ideacao_com_plano")
print("=" * 70)

gate_p0 = find_node(GATE_P0_ID)
q_plano = find_question(gate_p0, "ideacao_com_plano")

if q_plano is not None:
    old_expr = q_plano.get("expressao", "")
    if "ideacao_suicida" in old_expr:
        new_expr = old_expr.replace("ideacao_suicida", "ideacao_ativa")
        q_plano["expressao"] = new_expr
        print(f"  [CORRIGIDO] ideacao_com_plano.expressao")
        print(f"    ANTES:  {old_expr}")
        print(f"    DEPOIS: {new_expr}")
        changes.append("D: expressao de ideacao_com_plano corrigida (ideacao_suicida → ideacao_ativa)")
    else:
        print(f"  [OK] ideacao_com_plano.expressao não contém 'ideacao_suicida': {old_expr!r}")
else:
    print(f"  [AVISO] 'ideacao_com_plano' não encontrado em gate-p0")

print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO E — Converter ciclagem_rapida e especificador_misto para boolean
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO E — Converter choice(sim/nao) para boolean no Nó 4")
print("=" * 70)

no4 = find_node(NO4_ID)
UIDS_BOOLEAN = ["ciclagem_rapida", "especificador_misto"]

for uid in UIDS_BOOLEAN:
    q = find_question(no4, uid)
    if q is None:
        print(f"  [AVISO] '{uid}' não encontrado em nó-4")
        continue
    old_select = q.get("select", "")
    old_options = q.get("options", [])
    # Verificar se é choice com 2 opções sim/nao
    opt_ids = [o.get("id", "") for o in old_options] if old_options else []
    is_sim_nao = set(opt_ids) == {"sim", "nao"} or set(opt_ids) == {"yes", "no"}
    if old_select == "choice" and len(opt_ids) == 2 and is_sim_nao:
        q["select"] = "boolean"
        q["options"] = []
        q["defaultValue"] = "false"
        print(f"  [CORRIGIDO] uid={uid}: choice({opt_ids}) → boolean")
        changes.append(f"E: '{uid}' convertido de choice(sim/nao) para boolean")
    elif old_select == "boolean":
        print(f"  [JÁ OK] uid={uid} já é boolean")
    else:
        print(f"  [AVISO] uid={uid}: select={old_select!r}, opcoes={opt_ids} — verificar manualmente")

print()


# ──────────────────────────────────────────────────────────────────────────────
# GRUPO F — Corrigir expressao de vpa_mie_consentimento
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO F — Corrigir expressao de vpa_mie_consentimento")
print("=" * 70)

NO5_ID = "node-psiq-05-farmacos"
no5 = find_node(NO5_ID)
q_vpa = find_question(no5, "vpa_mie_consentimento")

if q_vpa is not None:
    old_expr = q_vpa.get("expressao", "")
    if "sexo_feminino_ie == 'sim'" in old_expr:
        new_expr = old_expr.replace("sexo_feminino_ie == 'sim'", "sexo_feminino_ie is True")
        q_vpa["expressao"] = new_expr
        print(f"  [CORRIGIDO] vpa_mie_consentimento.expressao")
        print(f"    ANTES:  {old_expr}")
        print(f"    DEPOIS: {new_expr}")
        changes.append("F: expressao de vpa_mie_consentimento corrigida (== 'sim' → is True)")
    else:
        print(f"  [OK] vpa_mie_consentimento.expressao não contém padrão a corrigir: {old_expr!r}")
else:
    print(f"  [AVISO] 'vpa_mie_consentimento' não encontrado em nó-5")

print()


# ──────────────────────────────────────────────────────────────────────────────
# METADATA — Atualizar versão
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("METADATA — Atualizar versão")
print("=" * 70)

meta = d.get("metadata") or d.get("meta") or {}
old_version = meta.get("version", "N/A")

if "metadata" in d:
    d["metadata"]["version"] = "0.1.1"
    print(f"  [ATUALIZADO] metadata.version: {old_version!r} → '0.1.1'")
    changes.append("metadata.version atualizado para 0.1.1")
elif "meta" in d:
    d["meta"]["version"] = "0.1.1"
    print(f"  [ATUALIZADO] meta.version: {old_version!r} → '0.1.1'")
    changes.append("meta.version atualizado para 0.1.1")
else:
    print(f"  [AVISO] Nenhum campo 'metadata' ou 'meta' encontrado na raiz do JSON")

print()


# ──────────────────────────────────────────────────────────────────────────────
# SALVAR
# ──────────────────────────────────────────────────────────────────────────────

with open(DST, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("=" * 70)
print("RESUMO DO PATCH")
print("=" * 70)
print(f"  Arquivo de saída: {DST}")
print(f"  Total de modificações aplicadas: {len(changes)}")
print()
for i, c in enumerate(changes, 1):
    print(f"  {i:2d}. {c}")
print()
print("OK — v0.1.1 gerado com sucesso.")


# ──────────────────────────────────────────────────────────────────────────────
# SEGUNDA PASSAGEM: recarregar v0.1.1 e aplicar Grupo G
# (conversoes boolean residuais em Nos 3 e 4 identificadas pela auditoria)
# ──────────────────────────────────────────────────────────────────────────────

print()
print("=" * 70)
print("GRUPO G — Converter choice(sim/nao) residuais em Nos 3 e 4 para boolean")
print("=" * 70)

d2 = json.load(open(DST, encoding="utf-8"))
nodes_by_id2 = {n["id"]: n for n in d2["nodes"]}

def find_node2(node_id):
    return nodes_by_id2[node_id]

def find_question2(node, uid):
    for q in node["data"].get("questions", []) or []:
        if q.get("uid") == uid:
            return q
    return None

NODES_G = [
    ("node-psiq-03-anamnese", ["sexo_feminino_ie", "gestante"]),
    ("node-psiq-04-diagnostico", [
        "burnout_criterios_tdm",
        "primeiro_episodio_psicotico",
        "esquizofrenia_refrataria",
        "comportamento_suicida_recorrente",
        "tdah_abuso_substancias_ativo",
        "sintomas_cardiacos_tdah",
        "tea_irritabilidade_grave",
        "tpb_autolesao_ativa",
    ]),
]

changes_g = []
for node_id, uids in NODES_G:
    node = find_node2(node_id)
    for uid in uids:
        q = find_question2(node, uid)
        if q is None:
            print(f"  [AVISO] '{uid}' não encontrado em {node_id}")
            continue
        old_select = q.get("select", "")
        old_options = q.get("options", []) or []
        opt_ids = [o.get("id", "") for o in old_options]
        is_sim_nao = set(opt_ids) <= {"sim", "nao", "yes", "no"} and len(opt_ids) == 2
        if old_select == "choice" and is_sim_nao:
            q["select"] = "boolean"
            q["options"] = []
            q["defaultValue"] = "false"
            print(f"  [CORRIGIDO] [{node_id}] uid={uid}: choice({opt_ids}) → boolean")
            changes_g.append(f"G: '{uid}' convertido para boolean")
        elif old_select == "boolean":
            print(f"  [JÁ OK] uid={uid} já é boolean")
        else:
            print(f"  [AVISO] uid={uid}: select={old_select!r}, opcoes={opt_ids} — verificar")

print()
if changes_g:
    with open(DST, "w", encoding="utf-8") as f:
        json.dump(d2, f, ensure_ascii=False, indent=2)
    print(f"  v0.1.1 atualizado com {len(changes_g)} conversoes adicionais do Grupo G.")
else:
    print("  Nenhuma conversao adicional necessária.")

print()
print("=" * 70)
print(f"TOTAL FINAL DE MODIFICAÇÕES: {len(changes) + len(changes_g)}")
print("=" * 70)
