#!/usr/bin/env python3
"""
patch_vdraft3_to_v023.py
Origem: amil-ficha_psiquiatria-vdraft(3).json
Destino: especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.3.json

Mudanças implementadas (sessão_023 — fechamento de hiatos do briefing):
  1. motivo_consulta: +3 opções (irritabilidade, agressividade_comportamento, sonolencia_hipersonia)
  2. diagnostico_ativo: +1 opção (agressividade / TEI)
  3. node-psiq-03-anamnese: nova pergunta historico_familiar_psiq
  4. node-psiq-04-diagnostico: nova pergunta sintomas_depressivos_presentes
  5. Encaminhamento Neuropsicólogo: condição expandida (TDAH + TEA + 1º psicótico)
  6. conduta: +1 mensagem alerta agressividade
  7. conduta: +1 orientação atividade física / sedentarismo
  8. metadata.version → "0.2.3"
"""
import json
import uuid
import sys
from pathlib import Path

INPUT_FILE  = Path(r"C:\Users\daanm\Downloads\amil-ficha_psiquiatria-vdraft(3).json")
REPO_ROOT   = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.2.3.json"

def uid() -> str:
    return str(uuid.uuid4())


# ── 1. Novas opções de motivo_consulta ──────────────────────────────────────
NEW_MOTIVO_OPTIONS = [
    {
        "iid": uid(), "id": "irritabilidade",
        "label": "Irritabilidade / explosividade",
        "preselected": False, "exclusive": False
    },
    {
        "iid": uid(), "id": "agressividade_comportamento",
        "label": "Comportamento agressivo / heteroagressividade",
        "preselected": False, "exclusive": False
    },
    {
        "iid": uid(), "id": "sonolencia_hipersonia",
        "label": "Sonolência excessiva / hipersonia",
        "preselected": False, "exclusive": False
    },
]

# ── 2. Nova opção em diagnostico_ativo ──────────────────────────────────────
NEW_DIAG_OPTION = {
    "iid": uid(), "id": "agressividade",
    "label": "Agressividade / Transtorno explosivo intermitente (F63.8)",
    "preselected": False, "exclusive": False
}

# ── 3. Nova pergunta: historico_familiar_psiq ───────────────────────────────
Q_HISTORICO_FAMILIAR = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-03-anamnese",
    "uid": "historico_familiar_psiq",
    "titulo": "<p><strong>Histórico familiar psiquiátrico relevante?</strong></p>",
    "descricao": "<p>Familiar de 1º grau (pais, irmãos, filhos)</p>",
    "condicional": "visivel",
    "expressao": "",
    "select": "multiChoice",
    "options": [
        {"iid": uid(), "id": "nenhum_familiar", "label": "Nenhum conhecido",
         "preselected": False, "exclusive": True},
        {"iid": uid(), "id": "tab_familiar",
         "label": "TAB / Depressão maior em familiar de 1º grau",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "esquizofrenia_familiar",
         "label": "Esquizofrenia / Transtorno psicótico em familiar de 1º grau",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "tdah_familiar",
         "label": "TDAH / TEA em familiar de 1º grau",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "suicidio_familiar",
         "label": "Tentativa de suicídio ou suicídio em familiar",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "outros_familiar",
         "label": "Outro transtorno psiquiátrico em familiar",
         "preselected": False, "exclusive": False},
    ]
}

# ── 4. Nova pergunta: sintomas_depressivos_presentes ────────────────────────
Q_SINTOMAS_DEPRESSIVOS = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "sintomas_depressivos_presentes",
    "titulo": "<p><strong>Sintomas depressivos / afetivos presentes</strong></p>",
    "descricao": "<p>Selecione os sintomas que o paciente refere ou que foram observados na consulta</p>",
    "condicional": "visivel",
    "expressao": "selected_any(diagnostico_ativo, 'tdm', 'distimia', 'burnout', 'tpb', 'tab') or 'humor_deprimido' in motivo_consulta",
    "select": "multiChoice",
    "options": [
        {"iid": uid(), "id": "anedonia",
         "label": "Anedonia / falta de prazer em atividades antes agradáveis",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "apatia",
         "label": "Apatia / embotamento afetivo / falta de motivação",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "astenia",
         "label": "Astenia / fadiga persistente",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "isolamento_social",
         "label": "Isolamento social / retraimento",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "choro_frequente",
         "label": "Choro frequente / labilidade emocional",
         "preselected": False, "exclusive": False},
        {"iid": uid(), "id": "inapetencia",
         "label": "Inapetência / perda de apetite",
         "preselected": False, "exclusive": False},
    ]
}

# ── 5. Alerta — agressividade (mensagem ao médico) ───────────────────────────
MSG_AGRESSIVIDADE = {
    "id": uid(),
    "nome": "Alerta — Agressividade / Risco para terceiros",
    "descricao": "",
    "narrativa": "",
    "condicional": "visivel",
    "condicao": "'agressividade' in diagnostico_ativo or 'agressividade_comportamento' in motivo_consulta",
    "conteudo": (
        "<p>⚠️ <strong>Risco para terceiros identificado.</strong><br>"
        "• Avaliar gravidade e plano de manejo do comportamento agressivo.<br>"
        "• Documentar detalhadamente no prontuário (possível implicação legal).<br>"
        "• Comunicar responsável legal se houver risco iminente a terceiros (CFM, CEM Art. 46).<br>"
        "• Considerar encaminhamento ao CAPS II para casos refratários ou de alta complexidade.<br>"
        "• Farmacoterapia: antipsicóticos e/ou estabilizadores de humor conforme conduta abaixo.</p>"
    ),
    "observacao": ""
}

# ── 6. Orientação — atividade física / sedentarismo ─────────────────────────
ORI_ATIVIDADE_FISICA = {
    "id": uid(),
    "nome": "Atividade física e estilo de vida",
    "descricao": "",
    "titulo": "<p><strong>Sobre atividade física</strong></p>",
    "narrativa": (
        "<p><strong>Movimento como parte do tratamento:</strong></p>"
        "<ul>"
        "<li>A atividade física regular (pelo menos <strong>150 minutos/semana</strong> de exercício moderado) "
        "melhora humor, ansiedade e qualidade do sono.</li>"
        "<li>Comece devagar: uma caminhada de 20–30 minutos ao dia já faz diferença.</li>"
        "<li>Atividades em grupo (academia, dança, esportes coletivos) também ajudam o isolamento social.</li>"
        "<li>Converse com seu médico antes de iniciar atividades intensas se tiver condições físicas associadas.</li>"
        "</ul>"
    ),
    "condicional": "visivel",
    "condicao": (
        "selected_any(diagnostico_ativo, 'tdm', 'distimia', 'burnout', 'tag', 'tab', 'tpb') "
        "or 'humor_deprimido' in motivo_consulta"
    ),
    "observacao": "",
    "categorias": []
}


def patch(data: dict) -> dict:
    nodes = data["nodes"]
    changed = []

    for node in nodes:
        nid = node["id"]
        questions = node["data"].get("questions", [])
        cd = node["data"].get("condutaDataNode", {})

        # ── motivo_consulta: add 3 options ──────────────────────────────────
        for q in questions:
            if q.get("uid") == "motivo_consulta":
                existing_ids = {o["id"] for o in q["options"]}
                added = []
                for opt in NEW_MOTIVO_OPTIONS:
                    if opt["id"] not in existing_ids:
                        # Insert before "outra_queixa" for better ordering
                        outra_idx = next(
                            (i for i, o in enumerate(q["options"]) if o["id"] == "outra_queixa"),
                            len(q["options"])
                        )
                        q["options"].insert(outra_idx, opt)
                        added.append(opt["id"])
                if added:
                    changed.append(f"motivo_consulta +{len(added)} opções: {added}")

            # ── diagnostico_ativo: add agressividade ─────────────────────────
            if q.get("uid") == "diagnostico_ativo":
                existing_ids = {o["id"] for o in q["options"]}
                if NEW_DIAG_OPTION["id"] not in existing_ids:
                    q["options"].append(NEW_DIAG_OPTION)
                    changed.append("diagnostico_ativo +1 opção: agressividade")

        # ── historico_familiar_psiq: add to anamnese ────────────────────────
        if nid == "node-psiq-03-anamnese":
            existing_uids = {q.get("uid") for q in questions}
            if "historico_familiar_psiq" not in existing_uids:
                questions.append(Q_HISTORICO_FAMILIAR)
                node["data"]["questions"] = questions
                changed.append("node-psiq-03-anamnese +1 pergunta: historico_familiar_psiq")

        # ── sintomas_depressivos_presentes: add to diagnostico ───────────────
        if nid == "node-psiq-04-diagnostico":
            existing_uids = {q.get("uid") for q in questions}
            if "sintomas_depressivos_presentes" not in existing_uids:
                # Insert after tea_irritabilidade_grave
                tea_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "tea_irritabilidade_grave"),
                    len(questions)
                )
                questions.insert(tea_idx + 1, Q_SINTOMAS_DEPRESSIVOS)
                node["data"]["questions"] = questions
                changed.append("node-psiq-04-diagnostico +1 pergunta: sintomas_depressivos_presentes")

        # ── Conduta (node-psiq-06) ───────────────────────────────────────────
        if nid == "node-psiq-06-conduta" and cd:
            # Fix Neuropsicólogo condition
            for enc in cd.get("encaminhamento", []):
                if "Neuropsicól" in enc.get("nome", ""):
                    old_cond = enc.get("condicao", "")
                    new_cond = "selected_any(diagnostico_ativo, 'tdah', 'tea') or primeiro_episodio_psicotico is True"
                    if old_cond != new_cond:
                        enc["condicao"] = new_cond
                        changed.append(f"Neuropsicólogo condição: '{old_cond}' → '{new_cond}'")

            # Add mensagem agressividade
            msg_ids = {m.get("nome", "") for m in cd.get("mensagem", [])}
            if MSG_AGRESSIVIDADE["nome"] not in msg_ids:
                cd.setdefault("mensagem", []).append(MSG_AGRESSIVIDADE)
                changed.append("conduta +1 mensagem: Alerta agressividade")

            # Add orientação atividade física
            ori_ids = {o.get("nome", "") for o in cd.get("orientacao", [])}
            if ORI_ATIVIDADE_FISICA["nome"] not in ori_ids:
                cd.setdefault("orientacao", []).append(ORI_ATIVIDADE_FISICA)
                changed.append("conduta +1 orientação: Atividade física")

    # ── metadata.version ────────────────────────────────────────────────────
    data["metadata"]["version"] = "0.2.3"
    changed.append("metadata.version → 0.2.3")

    return data, changed


def main():
    print(f"Lendo: {INPUT_FILE}")
    with open(INPUT_FILE, encoding="utf-8") as f:
        data = json.load(f)

    data, changes = patch(data)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nSalvo em: {OUTPUT_FILE}")
    print(f"\n{len(changes)} mudanças aplicadas:")
    for c in changes:
        print(f"  ✓ {c}")

    # Quick count
    for node in data["nodes"]:
        if node["id"] == "node-psiq-06-conduta":
            cd = node["data"].get("condutaDataNode", {})
            if cd:
                print("\nConduta final:")
                for k in ("medicamento", "exame", "encaminhamento", "mensagem", "orientacao"):
                    print(f"  {k}: {len(cd.get(k, []))}")

    # Count all questions
    total_q = 0
    for node in data["nodes"]:
        total_q += len(node["data"].get("questions", []))
    print(f"  Total perguntas no protocolo: {total_q}")


if __name__ == "__main__":
    main()
