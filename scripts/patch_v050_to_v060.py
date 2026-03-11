#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_v050_to_v060.py -- Onda 4: Quality & Precision Reform
v0.5.0 -> v0.6.0

NOTA ESTRUTURAL: conteudo dos nos esta em node["data"], nao diretamente em node.
NOTA TUSS: exam["codigo"] e uma lista de objetos {iid, sistema, codigo, nome}.

GRUPO A: Recalibrar formulas de risco suicida (3 clinicalExpressions)
GRUPO B: Bug fixes DSL e conteudo (causa_organica_investigada + DEPRESSAO LEVE)
GRUPO C: Eliminar redundancia tdah_abuso_substancias_ativo
GRUPO D: Auditoria TUSS (18 codigos + 1 nome ECG)
GRUPO E: 6 novas orientacoes ao paciente
GRUPO F: Restauracao de acentos em campos de display
"""

import json
import io
import sys
from pathlib import Path

# Fix Windows console encoding
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass

REPO_ROOT   = Path(__file__).resolve().parent.parent
INPUT_FILE  = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.5.0.json"
OUTPUT_FILE = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.6.0.json"

NODE_DIAGNOSTICO = "node-psiq-04-diagnostico"
NODE_CONDUTA     = "node-psiq-06-conduta"
SUMMARY_NODE_ID  = "summary-6e3e3703-1337-46f0-8b08-55e814f0f8ef"

# ===================================================================
# GRUPO A — Formulas de risco suicida
# ===================================================================
RISK_FORMULA_UPDATES = {
    "expr-9edcd193-55e2-430b-9f20-d327272eff34": (
        "risco_suicidio_baixo",
        "(ideacao_passiva is True) and (ideacao_ativa is False) and (tentativa_previa is False) "
        "and not('sem_fatores_protetores' in suporte_social)",
    ),
    "expr-6fec4094-976b-4b23-babf-2db922d614d1": (
        "risco_suicidio_intermediario",
        "((ideacao_ativa is True) and (ideacao_com_plano is False) and (ideacao_com_intencao is False) "
        "and (acesso_meios_letais is False)) or ((tentativa_previa is True) and (ideacao_ativa is False) "
        "and (ideacao_com_plano is False) and (ideacao_com_intencao is False))",
    ),
    "expr-8cc38fa1-af89-4c04-841c-3a4f6d5017a8": (
        "risco_suicidio_alto",
        "((ideacao_com_plano is True) and (ideacao_com_intencao is True) and (acesso_meios_letais is True)) "
        "or ((tentativa_previa is True) and ((ideacao_ativa is True) or (ideacao_com_intencao is True) "
        "or (ideacao_com_plano is True)))",
    ),
}

# ===================================================================
# GRUPO B1 — causa_organica_investigada DSL bug (4 exames)
# ===================================================================
CAUSA_ORGANICA_EXAM_IDS = {
    "a1b3e931-a1fd-4025-b87d-eba52377d1eb",
    "9a4f2983-2eeb-4635-beed-624d33264e2f",
    "6cbec494-910d-41fa-9739-de889c98b219",
    "1e350367-a25d-4550-88b0-43e99f381cb1",
}

# ===================================================================
# GRUPO B2 — Mensagem DEPRESSAO LEVE
# ===================================================================
DEPRESSAO_LEVE_ID       = "d9c2f119-1f59-4402-8d8a-37d786c6a09f"
DEPRESSAO_LEVE_NOME     = "DEPRESS\u00c3O LEVE \u2014 Monitorar evolu\u00e7\u00e3o e reavaliar em 2\u20134 semanas"
DEPRESSAO_LEVE_CONTEUDO = (
    "<p><strong>Depress\u00e3o leve (PHQ-9 &lt; 10 ou MADRS &lt; 20).</strong></p>"
    "<p>Priorizar interven\u00e7\u00f5es psicossociais: psicoeducação, atividade f\u00edsica, "
    "higiene do sono e suporte interpessoal. Farmacoterapia pode ser iniciada se sem melhora "
    "em 4\u20136 semanas ou se prefer\u00eancia do paciente. Reavaliar em 2\u20134 semanas.</p>"
)

# ===================================================================
# GRUPO C — tdah_abuso_substancias_ativo
# ===================================================================
TDAH_ABUSO_QUESTION_ID = "P51a70f03-660e-434b-96f3-ea9f6d956cee"
TDAH_ABUSO_DERIVED = {
    "id": "expr-tdah-abuso-derivado-001",
    "name": "tdah_abuso_substancias_ativo",
    "expressao": "not('nenhum' in substancias_uso)",
}

# ===================================================================
# GRUPO D — TUSS corrections
# Maps current TUSS code -> (new_code, new_exam_nome_display)
# exam["codigo"][0]["codigo"] = TUSS code
# exam["nome"] = display name used in UI
# ===================================================================
TUSS_CORRECTIONS = {
    "40320094": ("40316521", "Tireoestimulante, horm\u00f4nio (TSH) - pesquisa e/ou dosagem"),
    "40302130": ("40301400", "C\u00e1lcio - pesquisa e/ou dosagem"),
    "40302415": ("40302580", "Ur\u00e9ia - pesquisa e/ou dosagem"),
    "40302555": ("40301168", "\u00c1cido valproico - pesquisa e/ou dosagem"),
    "40302180": ("40302512", "Transaminase pir\u00favica (amino transferase de alanina) - pesquisa e/ou dosagem"),
    "40302172": ("40302504", "Transaminase oxalac\u00e9tica (amino transferase aspartato) - pesquisa e/ou dosagem"),
    "40302082": ("40301320", "Am\u00f4nia - pesquisa e/ou dosagem"),
    "40302490": ("40301435", "Carbamazepina - pesquisa e/ou dosagem"),
    "40302350": ("40302423", "S\u00f3dio - pesquisa e/ou dosagem"),
    "40302058": ("40304361", "Hemograma com contagem de plaquetas ou fra\u00e7\u00f5es (eritrograma, leucograma, plaquetas)"),
    "40302148": ("40302040", "Glicose - pesquisa e/ou dosagem"),
    "40307252": ("40302733", "Hemoglobina glicada (Fra\u00e7\u00e3o A1c) - pesquisa e/ou dosagem"),
    "40302121": ("40302750", "Perfil lip\u00eddico / lipidograma (colesterol total, HDL, LDL, VLDL, triglicer\u00eddeos)"),
    "40302407": ("40302547", "Triglicer\u00eddeos - pesquisa e/ou dosagem"),
    "40302326": ("40316416", "Prolactina - pesquisa e/ou dosagem"),
    "40306045": ("40305759", "Beta-HCG (gonadotrofina cori\u00f4nica humana) - pesquisa qualitativa"),
    "40314098": ("40307760", "S\u00edfilis - VDRL"),
    "40312003": ("40307182", "HIV1 + HIV2, (determina\u00e7\u00e3o conjunta), pesquisa de anticorpos"),
}

# ===================================================================
# GRUPO E — Novas orientacoes ao paciente (6)
# ===================================================================
NEW_ORIENTACOES = [
    {
        "id": "orient-litio-001",
        "nome": "L\u00edtio \u2014 uso seguro e monitoramento",
        "descricao": "",
        "condicao": "'litio' in medicamentos_em_uso",
        "conteudo": (
            "<p><strong>Sobre o seu tratamento com l\u00edtio:</strong></p>"
            "<ul>"
            "<li>Tome a medica\u00e7\u00e3o sempre no mesmo hor\u00e1rio. A regularidade \u00e9 essencial.</li>"
            "<li>Mantenha boa hidrata\u00e7\u00e3o \u2014 pelo menos 2 litros de \u00e1gua por dia.</li>"
            "<li>N\u00e3o reduza drasticamente a ingest\u00e3o de sal (s\u00f3dio) \u2014 pode elevar o n\u00edvel de l\u00edtio no sangue.</li>"
            "<li>Os exames de sangue (litemia) s\u00e3o parte do tratamento \u2014 n\u00e3o pule as coletas.</li>"
            "<li><strong>Sinais de toxicidade \u2014 procure emerg\u00eancia:</strong> tremor grosseiro, confus\u00e3o mental, n\u00e1usea/v\u00f4mito intensos ou tonteira/desequil\u00edbrio.</li>"
            "</ul>"
        ),
    },
    {
        "id": "orient-tab-episodio-001",
        "nome": "Transtorno Bipolar \u2014 reconhecer sinais de um novo epis\u00f3dio",
        "descricao": "",
        "condicao": "'tab' in diagnostico_ativo",
        "conteudo": (
            "<p><strong>Fique atento a sinais precoces de um novo epis\u00f3dio:</strong></p>"
            "<ul>"
            "<li><strong>Mania/hipomania:</strong> precisar de menos horas de sono sem sentir cans\u00e1\u00e7o, pensamentos muito r\u00e1pidos, euforia intensa, irritabilidade ou gastos impulsivos.</li>"
            "<li><strong>Depress\u00e3o:</strong> tristeza persistente, perda de prazer, cans\u00e1\u00e7o extremo, dificuldade de concentra\u00e7\u00e3o.</li>"
            "<li>Quanto antes voc\u00ea contatar sua equipe, maior a chance de evitar uma interna\u00e7\u00e3o.</li>"
            "<li>Nunca suspenda a medica\u00e7\u00e3o sem orienta\u00e7\u00e3o m\u00e9dica \u2014 pode precipitar um novo epis\u00f3dio.</li>"
            "</ul>"
        ),
    },
    {
        "id": "orient-substancias-001",
        "nome": "Subst\u00e2ncias e tratamento psiqui\u00e1trico",
        "descricao": "",
        "condicao": "not('nenhum' in substancias_uso)",
        "conteudo": (
            "<p><strong>O impacto do \u00e1lcool e de outras drogas no tratamento:</strong></p>"
            "<ul>"
            "<li>\u00c1lcool e drogas podem <strong>reduzir a efic\u00e1cia da medica\u00e7\u00e3o</strong> e precipitar crises ou reca\u00eddas.</li>"
            "<li>O uso de subst\u00e2ncias pode mascarar sintomas e dificultar o ajuste do tratamento.</li>"
            "<li>Se tiver dificuldade para reduzir o uso, converse com seu m\u00e9dico \u2014 h\u00e1 tratamentos eficazes para depend\u00eancia.</li>"
            "<li>N\u00e3o interrompa o uso de subst\u00e2ncias abruptamente sem orienta\u00e7\u00e3o \u2014 pode haver risco de s\u00edndrome de absti\u00eancia.</li>"
            "</ul>"
        ),
    },
    {
        "id": "orient-tdah-001",
        "nome": "TDAH \u2014 estrat\u00e9gias pr\u00e1ticas do dia a dia",
        "descricao": "",
        "condicao": "'tdah' in diagnostico_ativo or 'deficit_atencao' in motivo_consulta",
        "conteudo": (
            "<p><strong>Ferramentas para o dia a dia com TDAH:</strong></p>"
            "<ul>"
            "<li>Use <strong>listas e alarmes</strong> para tarefas e compromissos \u2014 n\u00e3o confie apenas na mem\u00f3ria.</li>"
            "<li>Divida tarefas grandes em etapas menores e conclua uma de cada vez.</li>"
            "<li>Minimize distra\u00e7\u00f5es no trabalho ou estudo (celular no silencioso, ambiente tranquilo).</li>"
            "<li>Tome a medica\u00e7\u00e3o sempre no mesmo hor\u00e1rio \u2014 um alarme ajuda.</li>"
            "<li>Se sentir que a medica\u00e7\u00e3o perdeu efeito ou causou efeito colateral, comunique ao m\u00e9dico antes de alterar a dose.</li>"
            "</ul>"
        ),
    },
    {
        "id": "orient-ta-001",
        "nome": "Transtornos alimentares \u2014 recupera\u00e7\u00e3o e suporte",
        "descricao": "",
        "condicao": (
            "selected_any(diagnostico_ativo, 'ta_anorexia', 'ta_bulimia', 'ta_tcap') or "
            "selected_any(ta_fenotipo, 'restricao_medo_engordar', 'compulsao_purgacao', 'compulsao_sem_compensacao')"
        ),
        "conteudo": (
            "<p><strong>Sobre a sua recupera\u00e7\u00e3o:</strong></p>"
            "<ul>"
            "<li>O tratamento dos transtornos alimentares \u00e9 mais eficaz com uma <strong>equipe multidisciplinar</strong>: m\u00e9dico, nutricionista e psic\u00f3logo/psicoterapeuta.</li>"
            "<li>Evite dietas restritivas por conta pr\u00f3pria \u2014 podem piorar o quadro.</li>"
            "<li>Reduzir a frequ\u00eancia de se pesar pode ajudar a diminuir a ansiedade com o corpo.</li>"
            "<li>Reca\u00eddas fazem parte do processo \u2014 comunique ao seu m\u00e9dico sem culpa.</li>"
            "<li>O apoio de pessoas pr\u00f3ximas \u00e9 um fator protetor importante na recupera\u00e7\u00e3o.</li>"
            "</ul>"
        ),
    },
    {
        "id": "orient-clozapina-001",
        "nome": "Clozapina \u2014 vigil\u00e2ncia e seguran\u00e7a hematol\u00f3gica",
        "descricao": "",
        "condicao": "selected_any(medicamentos_em_uso, 'clozapina')",
        "conteudo": (
            "<p><strong>Sobre o uso de clozapina:</strong></p>"
            "<ul>"
            "<li>A clozapina \u00e9 eficaz, mas exige <strong>exames de sangue regulares</strong> \u2014 os resultados determinam se o uso pode continuar com seguran\u00e7a.</li>"
            "<li><strong>Sinais de alerta \u2014 busque emerg\u00eancia imediatamente:</strong> febre sem causa aparente, infec\u00e7\u00f5es frequentes, feridas na boca ou garganta.</li>"
            "<li>Nunca interrompa a clozapina por conta pr\u00f3pria \u2014 a suspens\u00e3o abrupta pode causar reca\u00edda grave.</li>"
            "<li>Em emerg\u00eancia: informe ao m\u00e9dico de plant\u00e3o que voc\u00ea usa clozapina e a dose atual.</li>"
            "</ul>"
        ),
    },
]

# ===================================================================
# GRUPO F — Accent substitutions (display fields only)
# ===================================================================
TARGET_DISPLAY_FIELDS = {"titulo", "descricao", "label", "nome", "conteudo", "narrativa"}

# Apply most specific first to avoid partial replacement
ACCENT_FIXES = [
    ("Reavaliacao clinica", "Reavalia\u00e7\u00e3o cl\u00ednica"),
    ("avaliacao inicial",   "avalia\u00e7\u00e3o inicial"),
    ("feicoes de",          "fei\u00e7\u00f5es de"),
    ("com intencao",        "com inten\u00e7\u00e3o"),
    ("da substancia",       "da subst\u00e2ncia"),
    ("das substancias",     "das subst\u00e2ncias"),
    ("uso de substancia",   "uso de subst\u00e2ncia"),
    ("automedicacao",       "automedica\u00e7\u00e3o"),
    ("com agitacao",        "com agita\u00e7\u00e3o"),
    ("DEPRESSAO",           "DEPRESS\u00c3O"),
    ("evolucao e",          "evolu\u00e7\u00e3o e"),
    ("caracteristicas",     "caracter\u00edsticas"),
    ("criterios",           "crit\u00e9rios"),
    ("diagnosticos",        "diagn\u00f3sticos"),
    ("psiquiatrico",        "psiqui\u00e1trico"),
    ("psiquiatricos",       "psiqui\u00e1tricos"),
    ("iminencia",           "iminência"),
    ("suicidio",            "suic\u00eddio"),
    ("avaliacao",           "avalia\u00e7\u00e3o"),
    ("atencao",             "aten\u00e7\u00e3o"),
    ("nao ha",              "n\u00e3o h\u00e1"),
]


# ===================================================================
# Helpers
# ===================================================================

def get_data(node):
    """Return the 'data' dict of a node (all content is nested inside data)."""
    return node.get("data") or {}


def find_node(data, node_id):
    for nd in data.get("nodes", []):
        if nd.get("id") == node_id:
            return nd
    return None


def apply_accent_fixes(obj, changes_log):
    """Recursively apply accent fixes ONLY to TARGET_DISPLAY_FIELDS string values."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in TARGET_DISPLAY_FIELDS and isinstance(value, str):
                new_value = value
                for old, new in ACCENT_FIXES:
                    new_value = new_value.replace(old, new)
                if new_value != value:
                    obj[key] = new_value
                    changes_log.append(f"[F] campo={key}: acento corrigido")
            elif isinstance(value, (dict, list)):
                apply_accent_fixes(value, changes_log)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                apply_accent_fixes(item, changes_log)


# ===================================================================
# Main
# ===================================================================

def main():
    if not INPUT_FILE.exists():
        print(f"ERRO: arquivo nao encontrado: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    changes = []

    # ---------------------------------------------------------------
    # GRUPO A — Risk formulas (in summary node's data.clinicalExpressions)
    # ---------------------------------------------------------------
    summary_node = find_node(data, SUMMARY_NODE_ID)
    summary_data = get_data(summary_node) if summary_node else {}

    if not summary_node:
        print(f"AVISO: no summary nao encontrado: {SUMMARY_NODE_ID}")
    else:
        exprs = summary_data.get("clinicalExpressions") or []
        updated = 0
        for expr in exprs:
            expr_id = expr.get("id")
            if expr_id in RISK_FORMULA_UPDATES:
                name, new_formula = RISK_FORMULA_UPDATES[expr_id]
                expr["expressao"] = new_formula
                changes.append(f"[A] formula {name}: atualizada")
                updated += 1
        print(f"GRUPO A: {updated}/3 formulas de risco atualizadas")

    # ---------------------------------------------------------------
    # GRUPO B1 — causa_organica_investigada DSL fix
    # ---------------------------------------------------------------
    b1_count = 0
    for nd in data.get("nodes", []):
        cd = get_data(nd).get("condutaDataNode") or {}
        for exam in cd.get("exame", []):
            if exam.get("id") in CAUSA_ORGANICA_EXAM_IDS:
                old_cond = exam.get("condicao", "")
                if "!= 'sim'" in old_cond:
                    exam["condicao"] = old_cond.replace(
                        "causa_organica_investigada != 'sim'",
                        "causa_organica_investigada is False"
                    )
                    changes.append(f"[B1] exame {exam.get('id')[:20]}: causa_organica DSL fix")
                    b1_count += 1
    print(f"GRUPO B1: {b1_count}/4 exames corrigidos (causa_organica_investigada)")

    # ---------------------------------------------------------------
    # GRUPO B2 — Mensagem DEPRESSAO LEVE
    # ---------------------------------------------------------------
    b2_done = False
    for nd in data.get("nodes", []):
        cd = get_data(nd).get("condutaDataNode") or {}
        for msg in cd.get("mensagem", []):
            if msg.get("id") == DEPRESSAO_LEVE_ID:
                msg["nome"]     = DEPRESSAO_LEVE_NOME
                msg["conteudo"] = DEPRESSAO_LEVE_CONTEUDO
                changes.append("[B2] DEPRESSAO LEVE: nome e conteudo corrigidos")
                b2_done = True
    print(f"GRUPO B2: mensagem DEPRESSAO LEVE {'corrigida' if b2_done else 'NAO ENCONTRADA'}")

    # ---------------------------------------------------------------
    # GRUPO C1 — Remove tdah_abuso_substancias_ativo question
    # ---------------------------------------------------------------
    diag_node = find_node(data, NODE_DIAGNOSTICO)
    diag_data = get_data(diag_node) if diag_node else {}
    c1_done = False
    if diag_node:
        qs = diag_data.get("questions", [])
        before = len(qs)
        diag_data["questions"] = [q for q in qs if q.get("id") != TDAH_ABUSO_QUESTION_ID]
        after = len(diag_data["questions"])
        if before != after:
            changes.append(f"[C1] tdah_abuso_substancias_ativo removido ({before} -> {after} perguntas)")
            c1_done = True
    print(f"GRUPO C1: pergunta tdah_abuso {'removida' if c1_done else 'NAO ENCONTRADA'}")

    # ---------------------------------------------------------------
    # GRUPO C2 — Add derived expression to summary node data
    # ---------------------------------------------------------------
    c2_done = False
    if summary_node and summary_data:
        if summary_data.get("clinicalExpressions") is None:
            summary_data["clinicalExpressions"] = []
        existing_names = {e.get("name") for e in summary_data["clinicalExpressions"]}
        if TDAH_ABUSO_DERIVED["name"] not in existing_names:
            summary_data["clinicalExpressions"].append(TDAH_ABUSO_DERIVED)
            changes.append("[C2] tdah_abuso_substancias_ativo: expressao derivada adicionada")
            c2_done = True
        else:
            print("GRUPO C2: expressao derivada ja existe (ignorado)")
    print(f"GRUPO C2: expressao derivada {'adicionada' if c2_done else 'nao necessaria'}")

    # ---------------------------------------------------------------
    # GRUPO C3 — Update medication conditions
    # ---------------------------------------------------------------
    c3_count = 0
    for nd in data.get("nodes", []):
        cd = get_data(nd).get("condutaDataNode") or {}
        for med in cd.get("medicamento", []):
            cond = med.get("condicao", "")
            if "tdah_abuso_substancias_ativo is False" in cond:
                med["condicao"] = cond.replace(
                    "tdah_abuso_substancias_ativo is False",
                    "'nenhum' in substancias_uso"
                )
                changes.append(f"[C3] {med.get('nomeMed', '')[:30]}: condicao atualizada")
                c3_count += 1
    print(f"GRUPO C3: {c3_count}/3 condicoes de medicamento atualizadas")

    # ---------------------------------------------------------------
    # GRUPO D — TUSS corrections
    # exam["codigo"] is a list: [{"iid":..., "sistema":"TUSS", "codigo":"...", "nome":""}]
    # We update: codigo[0]["codigo"] and exam["nome"]
    # ---------------------------------------------------------------
    d_count = 0
    ecg_fixed = False
    for nd in data.get("nodes", []):
        cd = get_data(nd).get("condutaDataNode") or {}
        for exam in cd.get("exame", []):
            codigo_list = exam.get("codigo", [])
            if isinstance(codigo_list, list) and codigo_list:
                current_code = codigo_list[0].get("codigo", "")
                if current_code in TUSS_CORRECTIONS:
                    new_code, new_nome = TUSS_CORRECTIONS[current_code]
                    codigo_list[0]["codigo"] = new_code
                    exam["nome"] = new_nome
                    changes.append(f"[D] TUSS {current_code} -> {new_code}")
                    d_count += 1
            # ECG nome fix (code 40101010 already correct)
            nome = exam.get("nome", "")
            if "ECG" in nome and "derivações" in nome and "até" not in nome:
                exam["nome"] = "ECG convencional de at\u00e9 12 deriva\u00e7\u00f5es"
                changes.append("[D] ECG nome: 'de ate' adicionado")
                ecg_fixed = True
    print(f"GRUPO D: {d_count}/18 codigos TUSS corrigidos; ECG: {'corrigido' if ecg_fixed else 'nao alterado'}")

    # ---------------------------------------------------------------
    # GRUPO E — New orientacoes (always target NODE_CONDUTA explicitly)
    # ---------------------------------------------------------------
    e_count = 0
    conduta_node = find_node(data, NODE_CONDUTA)
    if conduta_node:
        cd = get_data(conduta_node).get("condutaDataNode") or {}
        if "orientacao" in cd:
            existing_ids = {o.get("id") for o in cd["orientacao"]}
            for orient in NEW_ORIENTACOES:
                if orient["id"] not in existing_ids:
                    cd["orientacao"].append(orient)
                    changes.append(f"[E] orientacao: {orient['id']}")
                    e_count += 1
        else:
            print("AVISO GRUPO E: condutaDataNode sem campo 'orientacao' em NODE_CONDUTA")
    else:
        print(f"AVISO GRUPO E: {NODE_CONDUTA} nao encontrado")
    print(f"GRUPO E: {e_count}/6 orientacoes adicionadas")

    # ---------------------------------------------------------------
    # GRUPO F — Accent fixes (traverses entire tree)
    # ---------------------------------------------------------------
    f_log = []
    apply_accent_fixes(data, f_log)
    changes.extend(f_log)
    print(f"GRUPO F: {len(f_log)} correcoes de acento aplicadas")

    # ---------------------------------------------------------------
    # Version
    # ---------------------------------------------------------------
    if "metadata" in data:
        data["metadata"]["version"] = "0.6.0"
    changes.append("[META] version -> 0.6.0")

    # ---------------------------------------------------------------
    # Write output
    # ---------------------------------------------------------------
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"Total de mudancas aplicadas: {len(changes)}")
    print(f"Output: {OUTPUT_FILE.name}")
    print(f"{'='*60}\n")
    for c in changes:
        try:
            print(f"  {c}")
        except Exception:
            print("  [mudanca com caracteres especiais]")


if __name__ == "__main__":
    main()
