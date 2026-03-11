#!/usr/bin/env python3
"""
patch_v040_to_v050.py
amil-ficha_psiquiatria v0.4.0 -> v0.5.0 — Onda 3: Gap Resolution

7 gaps corrigidos:
  G1 — primeiro_episodio_psicotico gate alargado (sintomas_psicoticos)
  G2 — Urgência não suicida (nova mensagem E1 mania/psicose + SAMU expandido)
  G3 — Iminência de heteroagressão (nova pergunta B3 + mensagem E2)
  G4 — TDAH falso-positivo TAB (nova opção curso_continuo_sem_episodios)
  G5 — TA fenotipagem pré-diagnóstico (nova pergunta B2 + an_sinais_alarme gate)
  G6 — TEA mascarado (nova pergunta B1 + Neuropsicólogo expandido)
  G7a — Bupropiona sem proteção em TA (bug fix H1/H2)
  G7b — Amônia sérica referenciava sintomas_toxicidade_litio (bug fix G2 + nova pergunta D1)
"""
import json
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = (
    REPO_ROOT / "especialidades" / "psiquiatria" / "jsons"
    / "amil-ficha_psiquiatria-v0.4.0.json"
)
OUTPUT_FILE = (
    REPO_ROOT / "especialidades" / "psiquiatria" / "jsons"
    / "amil-ficha_psiquiatria-v0.5.0.json"
)

NODE_DIAGNOSTICO = "node-psiq-04-diagnostico"
NODE_FARMACOS    = "node-psiq-05-farmacos"
NODE_CONDUTA     = "node-psiq-06-conduta"

# IDs fixos de itens existentes (extraídos do JSON v0.4.0)
ID_SAMU          = "a86867c6-ab7b-44c7-a1c8-b958298c42e8"
ID_NEUROPSIC     = "041a7502-ea52-4f38-9aa2-cfd6b2c13d12"
ID_AMONIA        = "8aef2815-1d9b-4e17-8ba4-68b928dd8ff2"
ID_BUPROPIONA_150 = "5fc3c138-22ea-4d56-b17e-9d0829141928"
ID_BUPROPIONA_300 = "dwg5y7sk"


def uid4() -> str:
    return str(uuid.uuid4())


# ─────────────────────────────────────────────────────────────
# GRUPO B — Novas perguntas em node-psiq-04-diagnostico
# ─────────────────────────────────────────────────────────────

Q_TEA_SUSPEITA = {
    "id": f"P{uid4()}",
    "nodeId": NODE_DIAGNOSTICO,
    "uid": "tea_suspeita_clinica",
    "titulo": "<p><strong>Rastreio de TEA — suspeita clinica sem diagnostico formalizado</strong></p>",
    "descricao": (
        "<p>Selecione os elementos presentes. Aplicavel quando TEA nao esta em "
        "diagnostico_ativo mas e hipotese a investigar.</p>"
    ),
    "condicional": "visivel",
    "expressao": (
        "not('tea' in diagnostico_ativo) and "
        "selected_any(motivo_consulta, 'outra_queixa', 'deficit_atencao')"
    ),
    "select": "multiChoice",
    "options": [
        {
            "iid": uid4(),
            "id": "dificuldade_inferir_social",
            "label": (
                "Dificuldade em inferir intencoes, emocoes ou contexto social dos outros"
            ),
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "comunicacao_literal",
            "label": (
                "Comunicacao predominantemente literal — dificuldade com ironia, "
                "subtexto e tom"
            ),
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "rotinas_rigidas",
            "label": (
                "Necessidade intensa de rotinas; grande angustia frente a mudancas "
                "inesperadas"
            ),
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "interesses_restritos_intensos",
            "label": (
                "Interesse muito especifico e intenso que domina conversas/tempo"
            ),
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "sensibilidade_sensorial",
            "label": (
                "Hiper ou hiposensibilidade sensorial marcante (luz, som, textura, toque)"
            ),
            "preselected": False,
            "exclusive": False,
        },
    ],
    "defaultValue": [],
}

Q_AGRESSIVIDADE_IMINENCIA = {
    "id": f"P{uid4()}",
    "nodeId": NODE_DIAGNOSTICO,
    "uid": "agressividade_iminencia",
    "titulo": "<p><strong>Risco de heteroagressao — avaliacao de iminencia</strong></p>",
    "descricao": "<p>Selecione todos os indicadores de iminencia presentes</p>",
    "condicional": "visivel",
    "expressao": (
        "'agressividade' in diagnostico_ativo or "
        "'agressividade_comportamento' in motivo_consulta"
    ),
    "select": "multiChoice",
    "options": [
        {
            "iid": uid4(),
            "id": "sem_risco_iminente",
            "label": "Sem risco iminente identificado",
            "preselected": True,
            "exclusive": True,
        },
        {
            "iid": uid4(),
            "id": "ameaca_atual",
            "label": "Ameaca verbal ou gestual atual a pessoa especifica",
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "vitima_identificada",
            "label": "Alvo ou vitima identificada",
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "acesso_vitima",
            "label": "Acesso fisico a vitima",
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "escalada_recente",
            "label": "Escalada de frequencia ou intensidade nas ultimas 72h",
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "agressao_fisica_recente",
            "label": "Agressao fisica nas ultimas 24-72h",
            "preselected": False,
            "exclusive": False,
        },
    ],
    "defaultValue": ["sem_risco_iminente"],
}

Q_TA_FENOTIPO = {
    "id": f"P{uid4()}",
    "nodeId": NODE_DIAGNOSTICO,
    "uid": "ta_fenotipo",
    "titulo": "<p><strong>Fenotipo do comportamento alimentar</strong></p>",
    "descricao": (
        "<p>Selecione o padrao predominante. Permite construcao diagnostica "
        "antes do rotulo formal.</p>"
    ),
    "condicional": "visivel",
    "expressao": (
        "'comportamento_alimentar' in motivo_consulta or "
        "selected_any(diagnostico_ativo, 'ta_anorexia', 'ta_bulimia', 'ta_tcap')"
    ),
    "select": "choice",
    "options": [
        {
            "iid": uid4(),
            "id": "restricao_medo_engordar",
            "label": (
                "Restricao alimentar / baixo peso com medo intenso de engordar "
                "ou distorcao corporal"
            ),
            "preselected": False,
            "exclusive": True,
        },
        {
            "iid": uid4(),
            "id": "compulsao_purgacao",
            "label": (
                "Episodios de compulsao seguidos de vomito, laxantes ou "
                "exercicio compensatorio"
            ),
            "preselected": False,
            "exclusive": True,
        },
        {
            "iid": uid4(),
            "id": "compulsao_sem_compensacao",
            "label": "Episodios de compulsao sem comportamento compensatorio",
            "preselected": False,
            "exclusive": True,
        },
        {
            "iid": uid4(),
            "id": "inapetencia_sem_distorcao",
            "label": (
                "Inapetencia ou perda de peso sem medo de engordar nem "
                "distorcao corporal"
            ),
            "preselected": False,
            "exclusive": True,
        },
    ],
    "defaultValue": "",
}

# ─────────────────────────────────────────────────────────────
# GRUPO C — Nova opção em tdah_discriminador
# ─────────────────────────────────────────────────────────────

NEW_TDAH_OPTION = {
    "iid": uid4(),
    "id": "curso_continuo_sem_episodios",
    "label": (
        "Sintomas continuos desde a infancia, sem periodos de aceleracao, "
        "hipossonia e euforia/irritabilidade marcante intercalados"
    ),
    "preselected": False,
    "exclusive": False,
}

# ─────────────────────────────────────────────────────────────
# GRUPO D — Nova pergunta em node-psiq-05-farmacos
# ─────────────────────────────────────────────────────────────

Q_SINTOMAS_TOXICIDADE_VPA = {
    "id": f"P{uid4()}",
    "nodeId": NODE_FARMACOS,
    "uid": "sintomas_toxicidade_vpa",
    "titulo": "<p><strong>Sinais de toxicidade ao valproato (VPA)?</strong></p>",
    "descricao": "",
    "condicional": "visivel",
    "expressao": "'valproato' in medicamentos_em_uso",
    "select": "multiChoice",
    "options": [
        {
            "iid": uid4(),
            "id": "nenhum_vpa",
            "label": "Nenhum",
            "preselected": True,
            "exclusive": True,
        },
        {
            "iid": uid4(),
            "id": "confusao_vpa",
            "label": "Confusao mental / torpor / sonolencia desproporcional",
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "nausea_vomito_vpa",
            "label": "Nausea / vomito / dor abdominal",
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "tremor_vpa",
            "label": "Tremor fino",
            "preselected": False,
            "exclusive": False,
        },
        {
            "iid": uid4(),
            "id": "sedacao_excessiva",
            "label": "Sedacao excessiva sem justificativa de dose",
            "preselected": False,
            "exclusive": False,
        },
    ],
    "defaultValue": ["nenhum_vpa"],
}

# ─────────────────────────────────────────────────────────────
# GRUPO E — Novas mensagens em node-psiq-06-conduta
# ─────────────────────────────────────────────────────────────

NEW_MESSAGES = [
    {
        "id": uid4(),
        "nome": "URGENCIA — MANIA GRAVE COM AGITACAO/PSICOSE",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "selected_any(episodio_atual_humor, 'mania') and "
            "selected_any(contexto_agressividade, 'mania_agitacao', 'psicose_paranoia')"
        ),
        "conteudo": (
            "<p><strong>Mania grave com agitacao ou componente psicotico ativo.</strong><br>"
            "Avaliar necessidade urgente de internacao. Contatar SAMU 192 ou encaminhar "
            "a servico de urgencia psiquiatrica. Nao manejar sozinho em ambulatorio sem "
            "suporte de equipe. Considerar haloperidol IM ou lorazepam IM se agitacao "
            "grave impeca manejo clinico seguro.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid4(),
        "nome": "AGRESSIVIDADE — RISCO IMINENTE PARA TERCEIROS",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "selected_any(agressividade_iminencia, 'ameaca_atual', 'vitima_identificada', "
            "'acesso_vitima', 'escalada_recente', 'agressao_fisica_recente')"
        ),
        "conteudo": (
            "<p><strong>Risco iminente de heteroagressao identificado.</strong><br>"
            "Considerar notificacao as autoridades se vitima identificada "
            "(dever de protecao).<br>"
            "Avaliar internacao involuntaria — Lei Federal 10.216/2001.<br>"
            "Acionar SAMU 192 se risco imediato e incontrolavel.<br>"
            "Nao dispensar paciente sem plano de seguranca estruturado documentado.</p>"
        ),
        "observacao": "",
    },
    {
        "id": uid4(),
        "nome": "BULIMIA NERVOSA — Monitorar eletrolitos e risco de hipocalemia",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "ta_fenotipo == 'compulsao_purgacao' or 'ta_bulimia' in diagnostico_ativo"
        ),
        "conteudo": (
            "<p><strong>BN com purgacao — riscos medicos ativos.</strong><br>"
            "Solicitar K+, Na+, Cl-, funcao renal (hipocalemia, alcalose metabolica).<br>"
            "Estigmas fisicos: erosao dentaria, parotidite, sinal de Russell.<br>"
            "<strong>Bupropiona CONTRAINDICADA</strong> em BN — risco aumentado de "
            "convulsoes.<br>"
            "Considerar encaminhamento para nutricionista especializada em "
            "transtornos alimentares.</p>"
        ),
        "observacao": "",
    },
]


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():
    with open(INPUT_FILE, encoding="utf-8") as f:
        data = json.load(f)

    changes = []

    for node in data["nodes"]:
        nid = node["id"]
        nd  = node["data"]
        qs  = nd.get("questions", [])

        # ─────────────────────────────────────────────────────
        # NODE-PSIQ-04-DIAGNOSTICO
        # ─────────────────────────────────────────────────────
        if nid == NODE_DIAGNOSTICO:

            # GRUPO A1 — Alargar gate de primeiro_episodio_psicotico
            for q in qs:
                if q["uid"] == "primeiro_episodio_psicotico":
                    old_expr = q["expressao"]
                    q["expressao"] = (
                        "'esquizofrenia' in diagnostico_ativo or "
                        "'sintomas_psicoticos' in motivo_consulta"
                    )
                    changes.append(
                        f"A1: primeiro_episodio_psicotico.expressao alargado "
                        f"('{old_expr}' -> '{q['expressao']}')"
                    )
                    break

            # GRUPO C1 — Nova opção em tdah_discriminador
            for q in qs:
                if q["uid"] == "tdah_discriminador":
                    q["options"].append(NEW_TDAH_OPTION)
                    changes.append("C1: nova opcao 'curso_continuo_sem_episodios' em tdah_discriminador")
                    break

            # GRUPO F1 — Alargar gate de an_sinais_alarme
            for q in qs:
                if q["uid"] == "an_sinais_alarme":
                    old_expr = q["expressao"]
                    q["expressao"] = (
                        "'ta_anorexia' in diagnostico_ativo or "
                        "ta_fenotipo == 'restricao_medo_engordar'"
                    )
                    changes.append(
                        f"F1: an_sinais_alarme.expressao alargado para ta_fenotipo"
                    )
                    break

            # GRUPO B — Inserir 3 novas perguntas
            # Calcular índices âncora no estado ORIGINAL (antes de qualquer insert)
            idx_tea_nivel  = next((i for i, q in enumerate(qs) if q["uid"] == "tea_nivel_suporte"), -1)
            idx_contexto   = next((i for i, q in enumerate(qs) if q["uid"] == "contexto_agressividade"), -1)
            idx_an_alarme  = next((i for i, q in enumerate(qs) if q["uid"] == "an_sinais_alarme"), -1)

            assert idx_tea_nivel  >= 0, "ERRO: tea_nivel_suporte nao encontrado"
            assert idx_contexto   >= 0, "ERRO: contexto_agressividade nao encontrado"
            assert idx_an_alarme  >= 0, "ERRO: an_sinais_alarme nao encontrado"

            # Inserções: em ordem DECRESCENTE de índice para não deslocar âncoras
            inserts_sorted = sorted(
                [
                    (idx_tea_nivel  + 1, Q_TEA_SUSPEITA,           "B1: tea_suspeita_clinica apos tea_nivel_suporte"),
                    (idx_contexto   + 1, Q_AGRESSIVIDADE_IMINENCIA, "B3: agressividade_iminencia apos contexto_agressividade"),
                    (idx_an_alarme,      Q_TA_FENOTIPO,             "B2: ta_fenotipo antes de an_sinais_alarme"),
                ],
                key=lambda x: x[0],
                reverse=True,
            )
            for insert_idx, q_obj, label in inserts_sorted:
                qs.insert(insert_idx, q_obj)
                changes.append(label)

        # ─────────────────────────────────────────────────────
        # NODE-PSIQ-05-FARMACOS
        # ─────────────────────────────────────────────────────
        elif nid == NODE_FARMACOS:
            idx_litio = next(
                (i for i, q in enumerate(qs) if q["uid"] == "sintomas_toxicidade_litio"),
                -1,
            )
            if idx_litio >= 0:
                qs.insert(idx_litio + 1, Q_SINTOMAS_TOXICIDADE_VPA)
                changes.append("D1: sintomas_toxicidade_vpa inserido apos sintomas_toxicidade_litio")

        # ─────────────────────────────────────────────────────
        # CONDUTA (encaminhamentos, exames, medicamentos, mensagens)
        # ─────────────────────────────────────────────────────
        cd = nd.get("condutaDataNode") or {}

        # GRUPO E — 3 novas mensagens (apenas no nodo de conduta principal)
        if nid == NODE_CONDUTA and "mensagem" in cd:
            for msg in NEW_MESSAGES:
                cd["mensagem"].append(msg)
            changes.append("E1-E3: 3 novas mensagens adicionadas (urgencia mania, risco iminente, BN)")

        # GRUPO G1 — SAMU expandido
        for enc in cd.get("encaminhamento", []):
            if enc["id"] == ID_SAMU:
                enc["condicao"] = (
                    "risco_suicidio_alto is True or "
                    "selected_any(agressividade_iminencia, 'ameaca_atual', "
                    "'agressao_fisica_recente', 'vitima_identificada')"
                )
                changes.append("G1: SAMU condicao expandida para risco iminente de heteroagressao")

        # GRUPO G2 — Amônia sérica: corrigir campo de referência
        for exam in cd.get("exame", []):
            if exam["id"] == ID_AMONIA:
                old = exam["condicao"]
                exam["condicao"] = (
                    "'valproato' in medicamentos_em_uso and "
                    "selected_any(sintomas_toxicidade_vpa, 'confusao_vpa')"
                )
                changes.append(
                    f"G2: Amonia serica condicao corrigida "
                    f"(sintomas_toxicidade_litio -> sintomas_toxicidade_vpa)"
                )

        # GRUPO G3 — Neuropsicólogo: expandir para TEA suspeito
        for enc in cd.get("encaminhamento", []):
            if enc["id"] == ID_NEUROPSIC:
                enc["condicao"] = (
                    "selected_any(diagnostico_ativo, 'tdah', 'tea') or "
                    "selected_any(tea_suspeita_clinica, 'dificuldade_inferir_social', "
                    "'comunicacao_literal', 'rotinas_rigidas', "
                    "'interesses_restritos_intensos', 'sensibilidade_sensorial')"
                )
                changes.append("G3: Neuropsicólogo expandido para TEA suspeito")

        # GRUPO H1/H2 — Bupropiona: proteção contra TA
        for med in cd.get("medicamento", []):
            if med["id"] in (ID_BUPROPIONA_150, ID_BUPROPIONA_300):
                old = med["condicao"]
                med["condicao"] = (
                    old
                    + " and not selected_any(diagnostico_ativo, 'ta_bulimia', 'ta_anorexia')"
                )
                changes.append(
                    f"H: Bupropiona '{med['nome']}' — protecao TA adicionada"
                )

    # Version bump
    data["metadata"]["version"] = "0.5.0"
    changes.append("version -> 0.5.0")

    # Salvar
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Output: {OUTPUT_FILE}")
    print(f"Total changes: {len(changes)}")
    for i, c in enumerate(changes, 1):
        try:
            print(f"  {i:02d}. {c}")
        except UnicodeEncodeError:
            print(f"  {i:02d}. [unicode label — ok]")


if __name__ == "__main__":
    main()
