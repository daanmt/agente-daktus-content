"""
audit_design_v01.py — Auditoria estrutural de design do JSON v0.1
Verifica violacoes do GUIA_DESIGN_UX.md no arquivo de psiquiatria.
Nao modifica o JSON. Apenas relata problemas.
"""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

filepath = "especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json"
d = json.load(open(filepath, encoding="utf-8"))

# ──────────────────────────────────────────────────────────────────────────────
# COLETA — questoes, expressoes, conduta
# ──────────────────────────────────────────────────────────────────────────────

all_questions = []   # (node_id, question_dict)
all_expressoes = []  # strings de expressoes (questions + conduta)
conduta_items = []   # (node_id, section, item_dict)

for node in d["nodes"]:
    # Questoes do node
    for q in node["data"].get("questions", []) or []:
        all_questions.append((node["id"], q))
        expr = q.get("expressao", "") or ""
        if expr:
            all_expressoes.append(expr)

    # Conduta
    cdn = node["data"].get("condutaDataNode") or {}
    for section in ["exame", "encaminhamento", "medicamento", "mensagem", "orientacao"]:
        for item in cdn.get(section, []):
            conduta_items.append((node["id"], section, item))
            cond = item.get("condicao", "") or ""
            if cond:
                all_expressoes.append(cond)

# Texto unificado para busca de uid
all_expr_text = " ".join(all_expressoes)


# ──────────────────────────────────────────────────────────────────────────────
# AUDITORIA 1 — choice com 2 opcoes (candidatos a boolean)
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("AUDITORIA 1 — choice com 2 opcoes [candidato a boolean]")
print("=" * 70)
print("Severidade: BLOQUEANTE para opcoes sim/nao | REVISAO para outros")
print()

a1_results = []
for node_id, q in all_questions:
    if q.get("select") == "choice" and len(q.get("options", [])) == 2:
        opt_ids = [o["id"] for o in q["options"]]
        is_sim_nao = set(opt_ids) == {"sim", "nao"} or set(opt_ids) == {"yes", "no"}
        a1_results.append({
            "node": node_id,
            "uid": q["uid"],
            "opt_ids": opt_ids,
            "sim_nao": is_sim_nao,
        })

sim_nao_count = sum(1 for r in a1_results if r["sim_nao"])
outros_count = len(a1_results) - sim_nao_count

print(f"Total encontradas: {len(a1_results)} ({sim_nao_count} sim/nao BLOQUEANTES, {outros_count} outros)")
print()
print("-- BLOQUEANTES (sim/nao -> converter para boolean): --")
for r in a1_results:
    if r["sim_nao"]:
        print(f"  [{r['node']}]  uid={r['uid']}")
print()
print("-- REVISAO (2 opcoes nao-sim/nao): --")
for r in a1_results:
    if not r["sim_nao"]:
        print(f"  [{r['node']}]  uid={r['uid']}  opcoes={r['opt_ids']}")


# ──────────────────────────────────────────────────────────────────────────────
# AUDITORIA 2 — labels com enumeracao generica (Q1, Q2, Item N)
# ──────────────────────────────────────────────────────────────────────────────

print()
print("=" * 70)
print("AUDITORIA 2 — labels com enumeracao generica [Q1, Q2, Item N]")
print("=" * 70)
print("Severidade: BLOQUEANTE")
print()

pattern_enum = re.compile(r"<strong>Q\d|<strong>Item \d|<strong>Pergunta \d", re.IGNORECASE)
a2_results = []
for node_id, q in all_questions:
    titulo = q.get("titulo", "") or ""
    if pattern_enum.search(titulo):
        label_clean = re.sub(r"<[^>]+>", "", titulo).strip()[:80]
        a2_results.append({
            "node": node_id,
            "uid": q["uid"],
            "label": label_clean,
        })

print(f"Total encontradas: {len(a2_results)}")
print()
for r in a2_results:
    print(f"  [{r['node']}]  uid={r['uid']}")
    print(f"    titulo: \"{r['label']}\"")


# ──────────────────────────────────────────────────────────────────────────────
# AUDITORIA 3 — uid sem referencia em expressoes ou conduta
# ──────────────────────────────────────────────────────────────────────────────

print()
print("=" * 70)
print("AUDITORIA 3 — uid sem impacto em expressoes ou conduta")
print("=" * 70)
print("Severidade: REVISAO (pode ser informacional ou bug de condicional)")
print()

a3_results = []
for node_id, q in all_questions:
    uid = q.get("uid", "")
    if not uid:
        continue
    if uid in all_expr_text:
        continue
    a3_results.append({
        "node": node_id,
        "uid": uid,
        "select": q.get("select", ""),
    })

print(f"Total encontradas: {len(a3_results)}")
print()

# Agrupar por node para clareza
current_node = None
for r in a3_results:
    if r["node"] != current_node:
        current_node = r["node"]
        print(f"  [{current_node}]")
    print(f"    uid={r['uid']}  select={r['select']}")


# ──────────────────────────────────────────────────────────────────────────────
# AUDITORIA 4 — itens de conduta sem condicao (genericos)
# ──────────────────────────────────────────────────────────────────────────────

print()
print("=" * 70)
print("AUDITORIA 4 — itens de conduta sem condicao [generico]")
print("=" * 70)
print("Severidade: BLOQUEANTE")
print()

a4_results = []
for node_id, section, item in conduta_items:
    cond = item.get("condicao", "") or ""
    if not cond.strip():
        a4_results.append({
            "node": node_id,
            "section": section,
            "nome": item.get("nome", "")[:60],
        })

print(f"Total encontradas: {len(a4_results)}")
for r in a4_results:
    print(f"  [{r['node']}]  {r['section']}: \"{r['nome']}\"")

if not a4_results:
    print("  Nenhuma violacao encontrada. OK.")


# ──────────────────────────────────────────────────────────────────────────────
# RESUMO
# ──────────────────────────────────────────────────────────────────────────────

print()
print("=" * 70)
print("RESUMO DA AUDITORIA")
print("=" * 70)
print(f"  A1 choice->boolean BLOQUEANTE:   {sim_nao_count}")
print(f"  A1 choice 2-opcoes (revisao):    {outros_count}")
print(f"  A2 enum labels BLOQUEANTE:       {len(a2_results)}")
print(f"  A3 uid sem impacto (revisao):    {len(a3_results)}")
print(f"  A4 conduta generica BLOQUEANTE:  {len(a4_results)}")
print()
bloqueantes = sim_nao_count + len(a2_results) + len(a4_results)
revisao = outros_count + len(a3_results)
print(f"  TOTAL BLOQUEANTES: {bloqueantes}")
print(f"  TOTAL REVISAO:     {revisao}")
print()
print(f"Total expressoes coletadas: {len(all_expressoes)}")
print(f"Total questoes auditadas:   {len(all_questions)}")
print(f"Total itens de conduta:     {len(conduta_items)}")
