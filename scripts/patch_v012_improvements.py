"""
patch_v012_improvements.py — Quality Improvement Patch for v0.1.2
Input/Output: especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json

Groups:
  A — Move questions between nodes (same-node violation fix)
      A1: phq9_score, mdq_aplicado, audit_score — Nó 3 → Nó 4
      A2: madrs_score, ymrs_score — Nó 4 → Nó 5
  B — Remove ansiedade_subtipo (redundant with diagnostico_ativo)
  C — Connect orphaned scores to conduta
      C1: phq9_score >= 15 → alert (complemento ao MADRS)
      C2: audit_score >= 8 → alert + update CAPS-AD referral condition
  D — Remove emojis from alert names and question option labels
  E — Add exam categories (all currently empty)
  F — Add handoff messages to nursing pause conduct node
  G — Add 4 essential antipsychotics to medical conduct
  H — Add patient-facing orientacoes (rewritten in 2nd person)
  I — Cohesion fixes: nodeId mismatch, typo, anglicism, metadata.version
"""

import json
import uuid
import sys
import copy
import re

sys.stdout.reconfigure(encoding="utf-8")

PATH = "especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json"


def uid():
    return str(uuid.uuid4())


# ─────────────────────────────────────────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────────────────────────────────────────

d = json.load(open(PATH, encoding="utf-8"))
d = copy.deepcopy(d)
nodes_by_id = {n["id"]: n for n in d["nodes"]}
changes = []


def find_node(node_id):
    n = nodes_by_id.get(node_id)
    if n is None:
        raise KeyError(f"Nó não encontrado: {node_id}")
    return n


def find_and_remove_question(node, target_uid):
    """Remove and return question with given uid from node. Returns None if not found."""
    questions = node["data"].get("questions", []) or []
    for i, q in enumerate(questions):
        if q.get("uid") == target_uid:
            node["data"]["questions"] = questions[:i] + questions[i + 1:]
            return q
    return None


def insert_question_after(node, question, after_uid):
    """Insert question into node after the question with after_uid.
    If after_uid not found, appends to end."""
    questions = node["data"].get("questions", []) or []
    idx = next((i for i, q in enumerate(questions) if q.get("uid") == after_uid), -1)
    if idx >= 0:
        questions.insert(idx + 1, question)
    else:
        questions.append(question)
    node["data"]["questions"] = questions


def append_question(node, question):
    questions = node["data"].get("questions", []) or []
    questions.append(question)
    node["data"]["questions"] = questions


def strip_emoji_prefix(text):
    """Remove leading emoji prefix (⛔, ⚠️, ℹ️) from a string."""
    prefixes = ["⛔ ", "⚠️ ", "ℹ️ ", "⛔", "⚠️", "ℹ️"]
    for p in prefixes:
        if text.startswith(p):
            return text[len(p):]
    return text


# Node references
NO3_ID = "node-psiq-03-anamnese"
NO4_ID = "node-psiq-04-diagnostico"
NO5_ID = "node-psiq-05-farmacos"
NO6_ID = "node-psiq-06-conduta"
PAUSE_ID = "conduta-a9ccd9ee-4962-4bf2-ae6a-a0f4fef7d7d9"

no3 = find_node(NO3_ID)
no4 = find_node(NO4_ID)
no5 = find_node(NO5_ID)
no6 = find_node(NO6_ID)
pause_node = find_node(PAUSE_ID)

conduta6 = no6["data"].get("condutaDataNode") or {}


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO A1 — Mover phq9_score, mdq_aplicado, audit_score: Nó 3 → Nó 4
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO A1 — Mover phq9_score, mdq_aplicado, audit_score: Nó 3 → Nó 4")
print("=" * 70)

MOVER_NO3_NO4 = ["phq9_score", "mdq_aplicado", "audit_score"]

for uid_to_move in MOVER_NO3_NO4:
    q = find_and_remove_question(no3, uid_to_move)
    if q:
        q["nodeId"] = NO4_ID
        # Insert after ciclagem_rapida (episode characterization section)
        insert_question_after(no4, q, after_uid="ciclagem_rapida")
        print(f"  [MOVIDO] {uid_to_move}: Nó 3 → Nó 4 (após ciclagem_rapida)")
        changes.append(f"A1: {uid_to_move} movido Nó 3 → Nó 4")
    else:
        print(f"  [AVISO] {uid_to_move} não encontrado no Nó 3")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO A2 — Mover madrs_score, ymrs_score: Nó 4 → Nó 5
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO A2 — Mover madrs_score, ymrs_score: Nó 4 → Nó 5")
print("=" * 70)

MOVER_NO4_NO5 = ["madrs_score", "ymrs_score"]

for uid_to_move in MOVER_NO4_NO5:
    q = find_and_remove_question(no4, uid_to_move)
    if q:
        q["nodeId"] = NO5_ID
        # Fix: madrs_score incorrectly has condicional="visivel" — expressao should be active
        if uid_to_move == "madrs_score" and q.get("condicional") == "visivel":
            q["condicional"] = "condicional"
            print(f"  [CORRIGIDO] {uid_to_move}: condicional 'visivel' → 'condicional'")
        # Insert at beginning of Nó 5 (before pharmacological monitoring questions)
        no5_questions = no5["data"].get("questions", []) or []
        no5_questions.insert(0, q)
        no5["data"]["questions"] = no5_questions
        print(f"  [MOVIDO] {uid_to_move}: Nó 4 → Nó 5 (início do nó)")
        changes.append(f"A2: {uid_to_move} movido Nó 4 → Nó 5")
    else:
        print(f"  [AVISO] {uid_to_move} não encontrado no Nó 4")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO B — Remover ansiedade_subtipo (redundante)
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO B — Remover ansiedade_subtipo")
print("=" * 70)

removed = find_and_remove_question(no4, "ansiedade_subtipo")
if removed:
    print("  [REMOVIDO] ansiedade_subtipo do Nó 4")
    changes.append("B: ansiedade_subtipo removido (redundante com diagnostico_ativo)")
else:
    print("  [AVISO] ansiedade_subtipo não encontrado no Nó 4")

# Verificar se ansiedade_subtipo é referenciado em alguma expressao ou condicao
refs_found = []
for node in d["nodes"]:
    for q in node["data"].get("questions", []) or []:
        for field in ["expressao", "condicao"]:
            val = q.get(field, "") or ""
            if "ansiedade_subtipo" in val:
                refs_found.append(f"[{node['id'][:30]}] uid={q.get('uid')} campo={field}")
    # Verificar conduta
    cond_data = node["data"].get("condutaDataNode") or {}
    for section in ["mensagem", "exame", "encaminhamento", "medicamento", "orientacao"]:
        for item in cond_data.get(section, []) or []:
            cond = item.get("condicao", "") or ""
            if "ansiedade_subtipo" in cond:
                refs_found.append(f"CONDUTA [{node['id'][:30]}] section={section} item={item.get('nome','?')[:30]}")

if refs_found:
    print(f"  [ATENÇÃO] ansiedade_subtipo ainda referenciado em {len(refs_found)} locais:")
    for r in refs_found:
        print(f"    - {r}")
else:
    print("  [OK] ansiedade_subtipo sem referências externas — remoção limpa")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO C1 — Conectar phq9_score à conduta (alerta complementar ao MADRS)
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO C1 — Adicionar alerta PHQ-9 ≥15 à conduta")
print("=" * 70)

alerta_phq9 = {
    "id": uid(),
    "nome": "DEPRESSÃO GRAVE — PHQ-9 ≥15: Revisar tratamento",
    "descricao": "",
    "narrativa": "",
    "condicional": "visivel",
    "condicao": "(phq9_score >= 15) and not(madrs_score >= 20)",
    "conteudo": (
        "<p><strong>PHQ-9 ≥15: depressão moderada a grave.</strong></p>"
        "<p>MADRS não aplicado. Revisar adequação do antidepressivo atual ou iniciar farmacoterapia "
        "se ainda não prescrita. Considerar potencialização com lítio, quetiapina ou aripiprazol "
        "em dose baixa se sem resposta após 4–6 semanas em dose adequada.</p>"
    ),
    "observacao": "",
}

mensagens = conduta6.get("mensagem", []) or []
mensagens.append(alerta_phq9)
conduta6["mensagem"] = mensagens
print(f"  [ADICIONADO] {alerta_phq9['nome']}")
print(f"    condicao: {alerta_phq9['condicao']}")
changes.append("C1: alerta PHQ-9 ≥15 adicionado à conduta")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO C2 — Conectar audit_score à conduta + atualizar CAPS-AD
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO C2 — Adicionar alerta AUDIT ≥8 e atualizar encaminhamento CAPS-AD")
print("=" * 70)

alerta_audit = {
    "id": uid(),
    "nome": "USO PROBLEMÁTICO DE ÁLCOOL — AUDIT: Intervenção indicada",
    "descricao": "",
    "narrativa": "",
    "condicional": "visivel",
    "condicao": "audit_score >= 8",
    "conteudo": (
        "<p><strong>AUDIT ≥8: uso de risco de álcool.</strong></p>"
        "<p>Aplicar intervenção breve (5–15 min) na consulta. "
        "AUDIT ≥16: provável dependência — encaminhar para CAPS-AD. "
        "Atenção à síndrome de abstinência em uso intenso diário "
        "(risco nas primeiras 48–72h após cessar uso).</p>"
    ),
    "observacao": "",
}

mensagens = conduta6.get("mensagem", []) or []
mensagens.append(alerta_audit)
conduta6["mensagem"] = mensagens
print(f"  [ADICIONADO] {alerta_audit['nome']}")
changes.append("C2: alerta AUDIT ≥8 adicionado à conduta")

# Atualizar condição do CAPS-AD para incluir audit_score >= 16
encaminhamentos = conduta6.get("encaminhamento", []) or []
caps_ad_updated = False
for item in encaminhamentos:
    nome = item.get("nome", "")
    if "CAPS-AD" in nome or "CAPS AD" in nome or "caps-ad" in nome.lower():
        old_cond = item.get("condicao", "")
        if "audit_score >= 16" not in old_cond:
            if old_cond:
                new_cond = f"({old_cond}) or (audit_score >= 16)"
            else:
                new_cond = "audit_score >= 16"
            item["condicao"] = new_cond
            print(f"  [ATUALIZADO] encaminhamento CAPS-AD:")
            print(f"    ANTES:  {old_cond}")
            print(f"    DEPOIS: {new_cond}")
            caps_ad_updated = True
            changes.append("C2: condição encaminhamento CAPS-AD atualizada (+ audit_score >= 16)")

if not caps_ad_updated:
    print("  [AVISO] Encaminhamento CAPS-AD não encontrado — não atualizado")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO D — Remover emojis de nomes de alertas e labels de perguntas
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO D — Remover emojis de alertas e labels de perguntas")
print("=" * 70)

# D1 — Nomes de alertas
EMOJI_CHARS = ["⛔", "⚠️", "ℹ️", "🚨", "📋"]

def has_emoji(text):
    return any(text.startswith(e) for e in EMOJI_CHARS)

for section in ["mensagem", "exame", "encaminhamento", "medicamento", "orientacao"]:
    for item in conduta6.get(section, []) or []:
        nome = item.get("nome", "") or ""
        new_nome = strip_emoji_prefix(nome)
        if new_nome != nome:
            item["nome"] = new_nome
            print(f"  [EMOJI REMOVIDO] {section}: '{nome}' → '{new_nome}'")
            changes.append(f"D: emoji removido de {section}: {new_nome[:40]}")

# D2 — Labels de opções de perguntas (scan completo)
emoji_labels_removed = 0
for node in d["nodes"]:
    for q in node["data"].get("questions", []) or []:
        for opt in q.get("options", []) or []:
            label = opt.get("label", "") or ""
            new_label = strip_emoji_prefix(label)
            if new_label != label:
                opt["label"] = new_label
                print(f"  [EMOJI REMOVIDO] label opção [{q.get('uid')}]: '{label}' → '{new_label}'")
                changes.append(f"D: emoji removido de label de opção [{q.get('uid')}]")
                emoji_labels_removed += 1

if emoji_labels_removed == 0:
    print("  Nenhum emoji encontrado em labels de opções de perguntas.")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO E — Adicionar categorias aos exames
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO E — Adicionar categorias aos exames")
print("=" * 70)

# Mapeamento: substring do nome → categoria (case-insensitive)
EXAM_CATEGORY_MAP = [
    # Monitoramento Farmacológico
    ("litemia", "Monitoramento Farmacológico"),
    ("lítio sérico", "Monitoramento Farmacológico"),
    ("creatinina", "Monitoramento Farmacológico"),
    ("egfr", "Monitoramento Farmacológico"),
    ("valpróico", "Monitoramento Farmacológico"),
    ("valproico", "Monitoramento Farmacológico"),
    ("hla-b", "Monitoramento Farmacológico"),
    ("hla b", "Monitoramento Farmacológico"),
    ("carbamazepina", "Monitoramento Farmacológico"),
    ("anc", "Monitoramento Farmacológico"),
    ("troponina", "Monitoramento Farmacológico"),
    ("pcr", "Monitoramento Farmacológico"),
    ("ck-mb", "Monitoramento Farmacológico"),
    ("clozapina", "Monitoramento Farmacológico"),
    # Investigação Orgânica
    ("tsh", "Investigação Orgânica"),
    ("tireoide", "Investigação Orgânica"),
    ("vitamina b12", "Investigação Orgânica"),
    ("ácido fólico", "Investigação Orgânica"),
    ("acido folico", "Investigação Orgânica"),
    ("vdrl", "Investigação Orgânica"),
    ("hiv", "Investigação Orgânica"),
    ("neuroimagem", "Investigação Orgânica"),
    ("tomografia", "Investigação Orgânica"),
    ("ressonância", "Investigação Orgânica"),
    ("eeg", "Investigação Orgânica"),
    ("cálcio", "Investigação Orgânica"),  # Hipercalcemia por lítio = investigação
    ("calcio", "Investigação Orgânica"),
    ("fator reumatoide", "Investigação Orgânica"),
    ("anca", "Investigação Orgânica"),
    # Cardiometabólico
    ("glicemia", "Cardiometabólico"),
    ("glicada", "Cardiometabólico"),
    ("hba1c", "Cardiometabólico"),
    ("lipídios", "Cardiometabólico"),
    ("colesterol", "Cardiometabólico"),
    ("triglicérides", "Cardiometabólico"),
    ("ecg", "Cardiometabólico"),
    ("eletrocardiograma", "Cardiometabólico"),
    ("peso", "Cardiometabólico"),
    ("imc", "Cardiometabólico"),
    # Avaliação Laboratorial (fallback para hemograma, hepatograma, etc.)
    ("hemograma", "Avaliação Laboratorial"),
    ("hepatograma", "Avaliação Laboratorial"),
    ("transaminases", "Avaliação Laboratorial"),
    ("sódio", "Avaliação Laboratorial"),
    ("potássio", "Avaliação Laboratorial"),
    ("magnésio", "Avaliação Laboratorial"),
    ("urina", "Avaliação Laboratorial"),
    ("metabolico", "Avaliação Laboratorial"),
    ("metabólico", "Avaliação Laboratorial"),
    ("prolactina", "Avaliação Laboratorial"),
]


def classify_exam(nome):
    nome_lower = nome.lower()
    for keyword, categoria in EXAM_CATEGORY_MAP:
        if keyword.lower() in nome_lower:
            return categoria
    return "Avaliação Laboratorial"  # fallback


exames = conduta6.get("exame", []) or []
categorias_adicionadas = 0
for exame in exames:
    if not exame.get("categorias"):
        categoria = classify_exam(exame.get("nome", ""))
        exame["categorias"] = [
            {
                "iid": uid(),
                "sistema": "",
                "codigo": "",
                "nome": categoria,
                "texto": "",
            }
        ]
        print(f"  [CATEGORIA] '{exame['nome'][:45]}' → '{categoria}'")
        categorias_adicionadas += 1

print(f"  Total de exames com categoria adicionada: {categorias_adicionadas}")
if categorias_adicionadas > 0:
    changes.append(f"E: categorias adicionadas a {categorias_adicionadas} exames")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO F — Adicionar mensagens de handoff no nó de pausa de enfermagem
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO F — Adicionar mensagens de handoff no nó de pausa de enfermagem")
print("=" * 70)

CONDUTA_DATA_PAUSA = {
    "mensagem": [
        {
            "id": uid(),
            "nome": "HANDOFF — Risco alto: encaminhar para médico imediatamente",
            "descricao": "",
            "narrativa": "",
            "condicional": "visivel",
            "condicao": "risco_suicidio_alto is True",
            "conteudo": (
                "<p><strong>Triagem de suicídio concluída — risco ALTO identificado.</strong></p>"
                "<p>Chamar o médico imediatamente. "
                "Não deixar o paciente desacompanhado. "
                "Registrar horário da triagem e notificar o plantonista ou responsável.</p>"
            ),
            "observacao": "",
        },
        {
            "id": uid(),
            "nome": "HANDOFF — Risco intermediário: comunicar ao médico",
            "descricao": "",
            "narrativa": "",
            "condicional": "visivel",
            "condicao": "risco_suicidio_intermediario is True",
            "conteudo": (
                "<p><strong>Triagem de suicídio concluída — risco INTERMEDIÁRIO identificado.</strong></p>"
                "<p>Comunicar ao médico antes de prosseguir. "
                "SPI (Safety Planning Intervention) deve ser realizado pelo médico nesta consulta.</p>"
            ),
            "observacao": "",
        },
        {
            "id": uid(),
            "nome": "HANDOFF — Triagem concluída: aguardar avaliação médica",
            "descricao": "",
            "narrativa": "",
            "condicional": "visivel",
            "condicao": "risco_suicidio_baixo is True",
            "conteudo": (
                "<p>Triagem de suicídio concluída — risco baixo. "
                "Anamnese registrada. Aguardar avaliação médica para prosseguir.</p>"
            ),
            "observacao": "",
        },
    ],
    "exame": [],
    "encaminhamento": [],
    "medicamento": [],
    "orientacao": [],
}

if "condutaDataNode" not in pause_node["data"]:
    pause_node["data"]["condutaDataNode"] = CONDUTA_DATA_PAUSA
    print("  [ADICIONADO] condutaDataNode ao nó de pausa de enfermagem (3 mensagens de handoff)")
    changes.append("F: condutaDataNode com 3 mensagens de handoff adicionado ao nó de pausa")
else:
    print("  [INFO] condutaDataNode já existe no nó de pausa — verificar manualmente")

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO G — Adicionar 4 antipsicóticos essenciais à conduta médica
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO G — Adicionar 4 antipsicóticos à conduta médica")
print("=" * 70)

NOVOS_MEDICAMENTOS = [
    {
        "id": uid(),
        "nome": "Quetiapina 25 mg / 50 mg / 100 mg",
        "descricao": "",
        "condicional": "visivel",
        "condicao": (
            "(sintomas_psicoticos_humor is True) or "
            "selected_any(diagnostico_ativo, 'tab', 'esquizofrenia', 'tdm') or "
            "(madrs_score >= 20)"
        ),
        "conteudo": (
            "<p><strong>Quetiapina:</strong> estabilizador de humor / antipsicótico atípico. "
            "Iniciar 25–50 mg/noite; dose-alvo 100–300 mg/dia (humor), 300–800 mg/dia (psicose). "
            "Monitorar glicemia, lipídios e peso. Titulação lenta reduz sedação diurna.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "Olanzapina 5 mg / 10 mg",
        "descricao": "",
        "condicional": "visivel",
        "condicao": (
            "(sintomas_psicoticos_humor is True) or "
            "selected_any(diagnostico_ativo, 'tab', 'esquizofrenia')"
        ),
        "conteudo": (
            "<p><strong>Olanzapina:</strong> antipsicótico atípico. "
            "Iniciar 5–10 mg/dia; dose-alvo 10–20 mg/dia. "
            "Alto risco metabólico — monitorar glicemia, peso e lipídios a cada 3 meses. "
            "Evitar em diabetes ou síndrome metabólica estabelecida.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "Risperidona 1 mg / 2 mg",
        "descricao": "",
        "condicional": "visivel",
        "condicao": (
            "selected_any(diagnostico_ativo, 'esquizofrenia', 'tea') or "
            "(primeiro_episodio_psicotico is True) or "
            "(tea_irritabilidade_grave is True)"
        ),
        "conteudo": (
            "<p><strong>Risperidona:</strong> antipsicótico atípico. "
            "Iniciar 1–2 mg/dia; dose-alvo 2–6 mg/dia (psicose), 0,5–2 mg/dia (TEA). "
            "Monitorar EPS e hiperprolactinemia. "
            "Indicação ANVISA para irritabilidade grave no TEA.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "Aripiprazol 10 mg / 15 mg",
        "descricao": "",
        "condicional": "visivel",
        "condicao": (
            "(esquizofrenia_refrataria is True) or "
            "selected_any(diagnostico_ativo, 'tab', 'tdm') or "
            "(madrs_score >= 20)"
        ),
        "conteudo": (
            "<p><strong>Aripiprazol:</strong> agonista parcial D2 — baixo risco metabólico e de EPS. "
            "Iniciar 10–15 mg/dia; dose-alvo 15–30 mg/dia (psicose), 5–15 mg/dia (potencialização). "
            "Preferência quando há risco de síndrome metabólica ou ganho de peso.</p>"
        ),
        "observacao": "",
    },
]

medicamentos = conduta6.get("medicamento", []) or []
for med in NOVOS_MEDICAMENTOS:
    medicamentos.append(med)
    print(f"  [ADICIONADO] {med['nome']}")
    print(f"    condicao: {med['condicao'][:60]}...")
    changes.append(f"G: medicamento adicionado — {med['nome']}")
conduta6["medicamento"] = medicamentos

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO H — Adicionar orientações ao paciente (voz do paciente, 2ª pessoa)
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO H — Adicionar orientações ao paciente (voz do paciente)")
print("=" * 70)

NOVAS_ORIENTACOES = [
    {
        "id": uid(),
        "nome": "Sobre seu diagnóstico",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "",
        "conteudo": (
            "<p><strong>Seu diagnóstico é uma condição de saúde — e tem tratamento.</strong></p>"
            "<ul>"
            "<li>Transtornos mentais são tão reais quanto diabetes ou hipertensão.</li>"
            "<li>Com acompanhamento adequado, a maioria das pessoas melhora significativamente.</li>"
            "<li>Tire suas dúvidas com a equipe de saúde — não há perguntas erradas.</li>"
            "<li>Busque informações em fontes confiáveis (médico, psicólogo, CFM, CFP).</li>"
            "</ul>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "Sobre seus medicamentos",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "",
        "conteudo": (
            "<p><strong>Sobre o seu tratamento com medicamentos:</strong></p>"
            "<ul>"
            "<li><strong>Não interrompa</strong> a medicação por conta própria — converse com seu médico antes.</li>"
            "<li>Os efeitos do remédio costumam aparecer em <strong>2 a 6 semanas</strong>. Tenha paciência.</li>"
            "<li>Se sentir efeitos colaterais, <strong>comunique ao médico antes de parar</strong>.</li>"
            "<li>Usar um alarme no celular ajuda a não esquecer o horário da medicação.</li>"
            "</ul>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "Plano de segurança em crise",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "(risco_suicidio_intermediario is True) or (risco_suicidio_alto is True)",
        "conteudo": (
            "<p><strong>Plano para momentos difíceis:</strong></p>"
            "<ul>"
            "<li>Identifique os sinais de que uma crise está chegando (pensamentos, sentimentos, comportamentos).</li>"
            "<li>Tenha em mente <strong>2 ou 3 pessoas de confiança</strong> para ligar quando precisar.</li>"
            "<li>Anote o contato do seu serviço de saúde mental.</li>"
            "<li><strong>SAMU: 192</strong> — emergências médicas, incluindo crises de saúde mental.</li>"
            "<li><strong>CVV: 188</strong> — apoio emocional, gratuito, 24 horas.</li>"
            "</ul>"
        ),
        "observacao": "",
    },
    {
        "id": uid(),
        "nome": "Sono e rotina",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "",
        "conteudo": (
            "<p><strong>Cuidados com o sono:</strong></p>"
            "<ul>"
            "<li>Tente dormir e acordar <strong>sempre no mesmo horário</strong>, inclusive nos fins de semana.</li>"
            "<li>Evite telas (celular, televisão) nas <strong>2 horas antes de dormir</strong>.</li>"
            "<li>Quarto escuro, silencioso e fresco ajuda a dormir melhor.</li>"
            "<li>Evite cafeína após as 14h e álcool à noite — ambos pioram a qualidade do sono.</li>"
            "<li>Atividade física regular melhora o sono. Evite exercícios intensos nas 3h antes de dormir.</li>"
            "</ul>"
        ),
        "observacao": "",
    },
]

orientacoes = conduta6.get("orientacao", []) or []
for ori in NOVAS_ORIENTACOES:
    orientacoes.append(ori)
    cond_display = ori["condicao"][:40] + "..." if len(ori["condicao"]) > 40 else (ori["condicao"] or "(sempre)")
    print(f"  [ADICIONADO] '{ori['nome']}' | condicao: {cond_display}")
    changes.append(f"H: orientação adicionada — {ori['nome']}")
conduta6["orientacao"] = orientacoes

print()


# ─────────────────────────────────────────────────────────────────────────────
# GRUPO I — Correções de coesão
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("GRUPO I — Correções de coesão (nodeId, typo, anglicismo, metadata)")
print("=" * 70)

# I1 — Typo em nome de alerta: EPÍSODIO → EPISÓDIO
mensagens = conduta6.get("mensagem", []) or []
for msg in mensagens:
    nome = msg.get("nome", "")
    if "EPÍSODIO" in nome:
        new_nome = nome.replace("EPÍSODIO", "EPISÓDIO")
        msg["nome"] = new_nome
        print(f"  [TYPO CORRIGIDO] '{nome}' → '{new_nome}'")
        changes.append("I1: typo EPÍSODIO → EPISÓDIO corrigido")

# I2 — Anglicismo: "Lethal means counseling" → português (no nome do alerta)
for msg in mensagens:
    nome = msg.get("nome", "")
    if "Lethal means counseling" in nome:
        new_nome = nome.replace("Lethal means counseling obrigatório", "Restrição de meios letais obrigatória")
        new_nome = new_nome.replace("Lethal means counseling", "Restrição de meios letais")
        msg["nome"] = new_nome
        print(f"  [ANGLICISMO] '{nome}' → '{new_nome}'")
        changes.append("I2: 'Lethal means counseling' → 'Restrição de meios letais' no nome do alerta")

# I3 — NodeId mismatch: 3 perguntas com nodeId errado
NODEID_FIXES = {
    "tipo_consulta": "20e05d57-3dfa-43cb-b039-74279162a73a",
    "motivo_consulta": "20e05d57-3dfa-43cb-b039-74279162a73a",
    "exames_recentes": "20e05d57-3dfa-43cb-b039-74279162a73a",
}

for node in d["nodes"]:
    for q in node["data"].get("questions", []) or []:
        uid_q = q.get("uid")
        if uid_q in NODEID_FIXES:
            correct_id = NODEID_FIXES[uid_q]
            if q.get("nodeId") != correct_id:
                old_node_id = q.get("nodeId", "?")
                q["nodeId"] = correct_id
                print(f"  [NODEID] uid={uid_q}: '{old_node_id}' → '{correct_id}'")
                changes.append(f"I3: nodeId corrigido para {uid_q}")

# I4 — metadata.version
if "metadata" in d:
    old_v = d["metadata"].get("version", "N/A")
    d["metadata"]["version"] = "0.1.2"
    print(f"  [VERSION] metadata.version: '{old_v}' → '0.1.2'")
    changes.append("I4: metadata.version → '0.1.2'")
elif "meta" in d:
    old_v = d["meta"].get("version", "N/A")
    d["meta"]["version"] = "0.1.2"
    print(f"  [VERSION] meta.version: '{old_v}' → '0.1.2'")
    changes.append("I4: meta.version → '0.1.2'")
else:
    print("  [AVISO] Nenhum campo metadata/meta encontrado.")

print()


# ─────────────────────────────────────────────────────────────────────────────
# SALVAR
# ─────────────────────────────────────────────────────────────────────────────

# Ensure conduta6 changes are reflected in the node structure
no6["data"]["condutaDataNode"] = conduta6

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("=" * 70)
print("RESUMO DO PATCH v0.1.2 IMPROVEMENTS")
print("=" * 70)
print(f"  Arquivo: {PATH}")
print(f"  Total de modificações: {len(changes)}")
print()
for i, c in enumerate(changes, 1):
    print(f"  {i:2d}. {c}")
print()
print("OK — v0.1.2 melhorado com sucesso.")
