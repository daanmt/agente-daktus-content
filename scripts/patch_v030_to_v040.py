#!/usr/bin/env python3
"""
patch_v030_to_v040.py
Origem: amil-ficha_psiquiatria-v0.3.0.json
Destino: especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.4.0.json

Reforma v0.4.0 -- Onda 2: 4 novos eixos de discriminacao sindrômica + shortcut retorno

GRUPO A -- 6 perguntas novas:
  A1. tipo_consulta           -- Enfermagem: shortcut retorno medicamentoso
  A2. substancia_relacao_quadro -- nodo-diagnostico: relacao causal substancia/quadro
  A3. tpb_rastreio            -- nodo-diagnostico: rastreio TPB por motivo_consulta
  A4. tdah_discriminador      -- nodo-diagnostico: validacao criterios diagnosticos TDAH
  A5. burnout_tdm_discriminador -- nodo-diagnostico: diferencia burnout de TDM sobreposto
  A6. tea_nivel_suporte       -- nodo-diagnostico: nivel de suporte TEA (DSM-5)

GRUPO B -- modificacoes de expressao (shortcut retorno):
  B1. internacao_psiq_previa  -- visivel apenas em primeira_consulta
  B2. historico_familiar_psiq -- visivel apenas em primeira_consulta

GRUPO C+D -- 6 novas mensagens na conduta:
  C1. SUBSTANCIA COMO CAUSA PRIMARIA
  C2. AUTOMEDICACAO
  C3. RASTREIO POSITIVO PARA TPB
  C4. TDAH -- criterios incompletos
  C5. BURNOUT COM FEICOES DE TDM
  D1. TEA Nivel 2/3 -- suporte multidisciplinar

GRUPO E -- recalibracoes de encaminhamentos:
  E1. CAPS-AD: adicionar causa_primaria em substancia_relacao_quadro
  E2. Psicologo TCD: adicionar autolesao_suicidio_recorrente em tpb_rastreio

metadata.version -> "0.4.0"
"""
import json
import uuid
import sys
from pathlib import Path

REPO_ROOT   = Path(__file__).resolve().parent.parent
INPUT_FILE  = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.3.0.json"
OUTPUT_FILE = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.4.0.json"


def uid() -> str:
    return str(uuid.uuid4())


# ══════════════════════════════════════════════════════════════════════════════
# GRUPO A -- Novas perguntas
# ══════════════════════════════════════════════════════════════════════════════

# A1 -- tipo_consulta (Enfermagem)
Q_TIPO_CONSULTA = {
    "id": f"P{uid()}",
    "nodeId": "20e05d57-3dfa-43cb-b039-74279162a73a",
    "uid": "tipo_consulta",
    "titulo": "<p><strong>Tipo de consulta</strong></p>",
    "descricao": "<p>Selecione o tipo de atendimento de hoje</p>",
    "condicional": "visivel",
    "expressao": "",
    "select": "choice",
    "options": [
        {
            "iid": uid(), "id": "primeira_consulta",
            "label": "Primeira consulta / avaliacao inicial",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "retorno_medicamentoso",
            "label": "Retorno — Monitoramento medicamentoso",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "retorno_clinico",
            "label": "Retorno — Reavaliacao clinica geral",
            "preselected": False, "exclusive": True
        },
    ]
}

# A2 -- substancia_relacao_quadro (node-psiq-04-diagnostico)
Q_SUBSTANCIA_RELACAO = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "substancia_relacao_quadro",
    "titulo": (
        "<p><strong>Relacao entre o uso de substancias e o quadro psiquiatrico</strong></p>"
    ),
    "descricao": (
        "<p>Como o uso de substancias se relaciona com os sintomas do paciente?</p>"
    ),
    "condicional": "visivel",
    "expressao": "not('nenhum' in substancias_uso)",
    "select": "choice",
    "options": [
        {
            "iid": uid(), "id": "causa_primaria",
            "label": "Causa primaria — sintomas surgem e melhoram com a abstinencia",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "agravante_descompensador",
            "label": "Agravante — uso descompensa transtorno subjacente pre-existente",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "automedicacao",
            "label": "Automedicacao — paciente usa a substancia para aliviar sintomas psiquiatricos",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "comorbidade_independente",
            "label": "Comorbidade independente — coexistem sem relacao causal clara",
            "preselected": False, "exclusive": True
        },
    ]
}

# A3 -- tpb_rastreio (node-psiq-04-diagnostico)
Q_TPB_RASTREIO = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "tpb_rastreio",
    "titulo": (
        "<p><strong>Rastreio de criterios de Transtorno de Personalidade Borderline (TPB)</strong></p>"
    ),
    "descricao": (
        "<p>Selecione os criterios presentes (condensados do DSM-5)</p>"
    ),
    "condicional": "visivel",
    "expressao": "'autolesao' in motivo_consulta or 'tpb' in diagnostico_ativo",
    "select": "multiChoice",
    "options": [
        {
            "iid": uid(), "id": "medo_abandono_frenetico",
            "label": "Esforcxos freneticos para evitar abandono real ou imaginado",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "relacoes_instaveis_intensas",
            "label": "Relacionamentos intensos e instaveis (idealizacao / desvalorizacao)",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "instabilidade_identidade",
            "label": "Identidade ou autoimagem marcadamente instavel",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "impulsividade_autoprejudicial",
            "label": "Impulsividade em 2 ou mais areas com potencial de dano (gastos, sexo, substancias, direcao)",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "autolesao_suicidio_recorrente",
            "label": "Comportamento de autolesao, ameacas ou gestos suicidas recorrentes",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "afeto_instavel_reativo",
            "label": "Instabilidade afetiva marcada — disforia, irritabilidade ou ansiedade intensa e episodica",
            "preselected": False, "exclusive": False
        },
    ]
}

# A4 -- tdah_discriminador (node-psiq-04-diagnostico)
Q_TDAH_DISCRIMINADOR = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "tdah_discriminador",
    "titulo": (
        "<p><strong>Validacao de criterios diagnosticos para TDAH</strong></p>"
    ),
    "descricao": (
        "<p>Confirme os criterios essenciais presentes para TDAH</p>"
    ),
    "condicional": "visivel",
    "expressao": "'deficit_atencao' in motivo_consulta or 'tdah' in diagnostico_ativo",
    "select": "multiChoice",
    "options": [
        {
            "iid": uid(), "id": "inicio_infancia_confirmado",
            "label": "Sintomas desde a infancia (antes dos 12 anos) — confirmados por relato ou avaliacao",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "multiplos_contextos",
            "label": "Presentes em 2 ou mais contextos (trabalho/escola + casa + vida social)",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "prejuizo_funcional_claro",
            "label": "Prejuizo funcional documentado — rendimento, relacionamentos ou autonomia afetados",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "sem_explicacao_alternativa",
            "label": "Nao explicados por TDM ativo, TAG ou privacao de sono",
            "preselected": False, "exclusive": False
        },
    ]
}

# A5 -- burnout_tdm_discriminador (node-psiq-04-diagnostico)
Q_BURNOUT_TDM = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "burnout_tdm_discriminador",
    "titulo": (
        "<p><strong>Discriminador Burnout vs. TDM — feicoes presentes</strong></p>"
    ),
    "descricao": (
        "<p>Selecione as caracteristicas que apontam para TDM sobreposto ao burnout</p>"
    ),
    "condicional": "visivel",
    "expressao": (
        "'esgotamento_burnout' in motivo_consulta "
        "or selected_any(diagnostico_ativo, 'burnout', 'tdm')"
    ),
    "select": "multiChoice",
    "options": [
        {
            "iid": uid(), "id": "anedonia_universal",
            "label": "Perda de prazer em TODAS as areas — inclusive atividades fora do trabalho",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "sem_melhora_fora_trabalho",
            "label": "Sintomas PERSISTEM mesmo em ferias, fins de semana ou situacoes de descanso",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "culpa_desvalia",
            "label": "Sentimentos proeminentes de culpa, inutilidade ou desvalia (alem do contexto profissional)",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "sem_contexto_ocupacional",
            "label": "Quadro sem relacao clara com sobrecarga ou ambiente de trabalho",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "duracao_criterio_tdm",
            "label": "Sintomas presentes de forma persistente ha mais de 2 semanas",
            "preselected": False, "exclusive": False
        },
    ]
}

# A6 -- tea_nivel_suporte (node-psiq-04-diagnostico)
Q_TEA_NIVEL = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "tea_nivel_suporte",
    "titulo": (
        "<p><strong>Nivel de suporte — TEA (DSM-5)</strong></p>"
    ),
    "descricao": (
        "<p>Selecione o nivel de suporte necessario para o paciente</p>"
    ),
    "condicional": "visivel",
    "expressao": "'tea' in diagnostico_ativo",
    "select": "choice",
    "options": [
        {
            "iid": uid(), "id": "nivel_1_leve",
            "label": "Nivel 1 — Requer suporte (funciona com apoios; dificuldade em interacoes e flexibilidade)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "nivel_2_moderado",
            "label": "Nivel 2 — Requer suporte substancial (dificuldade marcada mesmo com apoios)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "nivel_3_grave",
            "label": "Nivel 3 — Requer suporte muito substancial (deficits graves em comunicacao e flexibilidade)",
            "preselected": False, "exclusive": True
        },
    ]
}


# ══════════════════════════════════════════════════════════════════════════════
# GRUPO C+D -- Novas mensagens de conduta
# ══════════════════════════════════════════════════════════════════════════════

NEW_MESSAGES = [
    {
        "id": uid(),
        "nome": "SUBSTANCIA COMO CAUSA PRIMARIA — tratar dependencia antes de psicofarmaco",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "substancia_relacao_quadro == 'causa_primaria'",
        "conteudo": (
            "<p><strong>Substancia identificada como causa primaria do quadro psiquiatrico.</strong><br>"
            "• Os sintomas surgem e tendem a melhorar com a abstinencia.<br>"
            "• <strong>Priorizar tratamento da dependencia</strong> antes de iniciar psicofarmaco para o "
            "transtorno psiquiatrico secundario.<br>"
            "• Encaminhar para <strong>CAPS-AD</strong> (ver abaixo) como intervencao de primeira linha.<br>"
            "• Reavalie o diagnostico psiquiatrico apos periodo de abstinencia de 4 semanas: muitos "
            "quadros remitem com a sobriedade.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "AUTOMEDICACAO — identificar e tratar sintoma-alvo subjacente",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "substancia_relacao_quadro == 'automedicacao'",
        "conteudo": (
            "<p><strong>Uso de substancia como automedicacao para sintoma psiquiatrico identificado.</strong><br>"
            "• O paciente busca alivio de sintomas (ansiedade, insonia, dor emocional) atraves da substancia.<br>"
            "• <strong>Identificar e tratar o sintoma-alvo subjacente</strong> e a abordagem prioritaria.<br>"
            "• Reduzir a demanda pela substancia ao tratar adequadamente o transtorno de base.<br>"
            "• Abordagem motivacional e psicoeducacao sobre o ciclo de automedicacao sao componentes "
            "essenciais do tratamento.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "RASTREIO POSITIVO PARA TPB — avaliar criterios completos antes de farmacoterapia",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "selected_any(tpb_rastreio, 'medo_abandono_frenetico', 'relacoes_instaveis_intensas', "
            "'instabilidade_identidade', 'impulsividade_autoprejudicial', "
            "'autolesao_suicidio_recorrente', 'afeto_instavel_reativo') "
            "and not 'tpb' in diagnostico_ativo"
        ),
        "conteudo": (
            "<p><strong>Rastreio positivo para Transtorno de Personalidade Borderline (TPB).</strong><br>"
            "• Um ou mais criterios diagnosticos presentes sem diagnostico formal registrado.<br>"
            "• Avaliar criterios completos (DSM-5: 5/9) antes de fechar diagnostico e iniciar farmacoterapia.<br>"
            "• <strong>TCD (Terapia Comportamental Dialetica)</strong> e o tratamento de primeira linha "
            "para TPB — farmacoterapia e adjuvante, nao tratamento principal.<br>"
            "• Considerar formalizar diagnostico de TPB em `diagnostico_ativo` se criterios completos.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "TDAH — Criterios diagnosticos incompletos: confirmar antes de prescrever estimulante",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "('tdah' in diagnostico_ativo or 'deficit_atencao' in motivo_consulta) "
            "and not selected_any(tdah_discriminador, 'inicio_infancia_confirmado', 'multiplos_contextos')"
        ),
        "conteudo": (
            "<p><strong>Criterios diagnosticos essenciais para TDAH nao confirmados.</strong><br>"
            "• <strong>Inicio na infancia</strong> (antes dos 12 anos) e/ou <strong>presenca em multiplos "
            "contextos</strong> nao foram verificados ou estao ausentes.<br>"
            "• TDAH exige ambos os criterios para diagnostico valido (DSM-5).<br>"
            "• TDM ativo, TAG e privacao cronica de sono mimetizam TDAH — considerar diagnostico diferencial.<br>"
            "• <strong>Adiar prescricao de estimulante</strong> ate confirmacao dos criterios: risco de "
            "virada maniaca (TAB nao diagnosticado) e dependencia.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "BURNOUT COM FEICOES DE TDM — considerar TDM comorbido nao diagnosticado",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "selected_any(burnout_tdm_discriminador, 'anedonia_universal', 'sem_melhora_fora_trabalho', "
            "'culpa_desvalia', 'sem_contexto_ocupacional', 'duracao_criterio_tdm') "
            "and not 'tdm' in diagnostico_ativo"
        ),
        "conteudo": (
            "<p><strong>Feicoes de TDM presentes no contexto de burnout.</strong><br>"
            "• Anedonia universal, ausencia de melhora fora do trabalho, culpa/desvalia ou duracao "
            "persistente indicam TDM comorbido nao diagnosticado.<br>"
            "• Burnout puro: anedonia restrita ao trabalho, melhora nas ferias, sem culpa/desvalia "
            "proeminente.<br>"
            "• <strong>Considerar diagnostico de TDM comorbido</strong> e iniciar farmacoterapia "
            "antidepressiva se criterios presentes.<br>"
            "• Afastamento do trabalho sem tratamento do TDM subjacente e insuficiente para remissao.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "TEA Nivel 2/3 — Suporte multidisciplinar substancial indicado",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "selected_any(tea_nivel_suporte, 'nivel_2_moderado', 'nivel_3_grave')",
        "conteudo": (
            "<p><strong>TEA com necessidade de suporte substancial ou muito substancial identificada.</strong><br>"
            "• Nivel 2 ou 3 do DSM-5: dificuldade marcada ou grave na comunicacao social e "
            "comportamentos restritos/repetitivos mesmo com apoios.<br>"
            "• Encaminhar para <strong>equipe multidisciplinar</strong>: Psicologia especializada em TEA, "
            "Fonoaudiologia (comunicacao), Terapia Ocupacional (habilidades adaptativas).<br>"
            "• Envolver familia/cuidadores no plano terapeutico.<br>"
            "• Nivel 3: considerar servico especializado em TEA grave e suporte intensivo.</p>"
        ),
        "observacao": ""
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# PATCH FUNCTION
# ══════════════════════════════════════════════════════════════════════════════

def patch(data: dict) -> tuple[dict, list[str]]:
    changes = []
    nodes = data["nodes"]

    # Identificar nodo de enfermagem pelo ID fixo
    ENFERMAGEM_NODE_ID = "20e05d57-3dfa-43cb-b039-74279162a73a"

    for node in nodes:
        nid = node["id"]
        questions = node["data"].get("questions", [])
        cd = node["data"].get("condutaDataNode", {})

        # ── GRUPO A1: tipo_consulta no nodo de enfermagem ────────────────────
        if nid == ENFERMAGEM_NODE_ID:
            existing_uids = {q.get("uid") for q in questions}
            if "tipo_consulta" not in existing_uids:
                # Inserir antes de motivo_consulta (ou no início se nao encontrar)
                motivo_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "motivo_consulta"),
                    0
                )
                questions.insert(motivo_idx, Q_TIPO_CONSULTA)
                node["data"]["questions"] = questions
                changes.append("A1: tipo_consulta inserido em Triagem Enfermagem (antes de motivo_consulta)")

        # ── GRUPO B: shortcut retorno em anamnese ─────────────────────────────
        if nid == "node-psiq-03-anamnese":
            for q in questions:
                uid_q = q.get("uid", "")
                if uid_q in ("internacao_psiq_previa", "historico_familiar_psiq"):
                    old_expr = q.get("expressao", "")
                    new_expr = "tipo_consulta == 'primeira_consulta' or tipo_consulta == ''"
                    if old_expr != new_expr:
                        q["expressao"] = new_expr
                        changes.append(
                            f"B: {uid_q} expressao atualizada para gate de primeira consulta"
                        )

        # ── GRUPO A2–A6 + C+D + E: nodo de diagnostico ───────────────────────
        if nid == "node-psiq-04-diagnostico":
            existing_uids = {q.get("uid") for q in questions}

            # A5: burnout_tdm_discriminador -- apos bipolar_rastreio
            if "burnout_tdm_discriminador" not in existing_uids:
                rastreio_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "bipolar_rastreio"),
                    2
                )
                questions.insert(rastreio_idx + 1, Q_BURNOUT_TDM)
                changes.append("A5: burnout_tdm_discriminador inserido apos bipolar_rastreio")

            # A2: substancia_relacao_quadro -- apos audit_score
            if "substancia_relacao_quadro" not in existing_uids:
                audit_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "audit_score"),
                    len(questions) - 1
                )
                questions.insert(audit_idx + 1, Q_SUBSTANCIA_RELACAO)
                changes.append("A2: substancia_relacao_quadro inserido apos audit_score")

            # A3: tpb_rastreio -- apos comportamento_suicida_recorrente
            if "tpb_rastreio" not in existing_uids:
                csr_idx = next(
                    (i for i, q in enumerate(questions)
                     if q.get("uid") == "comportamento_suicida_recorrente"),
                    len(questions) - 1
                )
                questions.insert(csr_idx + 1, Q_TPB_RASTREIO)
                changes.append("A3: tpb_rastreio inserido apos comportamento_suicida_recorrente")

            # A4: tdah_discriminador -- apos tdah_abuso_substancias_ativo
            if "tdah_discriminador" not in existing_uids:
                tdah_idx = next(
                    (i for i, q in enumerate(questions)
                     if q.get("uid") == "tdah_abuso_substancias_ativo"),
                    len(questions) - 1
                )
                questions.insert(tdah_idx + 1, Q_TDAH_DISCRIMINADOR)
                changes.append("A4: tdah_discriminador inserido apos tdah_abuso_substancias_ativo")

            # A6: tea_nivel_suporte -- apos tea_irritabilidade_grave
            if "tea_nivel_suporte" not in existing_uids:
                tea_idx = next(
                    (i for i, q in enumerate(questions)
                     if q.get("uid") == "tea_irritabilidade_grave"),
                    len(questions) - 1
                )
                questions.insert(tea_idx + 1, Q_TEA_NIVEL)
                changes.append("A6: tea_nivel_suporte inserido apos tea_irritabilidade_grave")

            node["data"]["questions"] = questions

        # ── GRUPO C+D + E: conduta ────────────────────────────────────────────
        if nid == "node-psiq-06-conduta" and cd:

            # GRUPO C+D: novas mensagens
            existing_msg_names = {m.get("nome", "") for m in cd.get("mensagem", [])}
            for new_msg in NEW_MESSAGES:
                if new_msg["nome"] not in existing_msg_names:
                    cd.setdefault("mensagem", []).append(new_msg)
                    changes.append(f"C/D: mensagem adicionada: {new_msg['nome'][:60]}")

            # GRUPO E: recalibrar encaminhamentos
            for enc in cd.get("encaminhamento", []):
                nome = enc.get("nome", "")

                # E1: CAPS-AD -- adicionar causa_primaria
                if "CAPS-AD" in nome:
                    old = enc.get("condicao", "")
                    if "causa_primaria" not in old:
                        new_cond = old + " or substancia_relacao_quadro == 'causa_primaria'"
                        enc["condicao"] = new_cond
                        changes.append("E1: CAPS-AD condicao expandida (substancia causa primaria)")

                # E2: Psicologo TCD -- adicionar autolesao_suicidio_recorrente
                if "TCD" in nome:
                    old = enc.get("condicao", "")
                    if "tpb_rastreio" not in old:
                        new_cond = (
                            old + " or selected_any(tpb_rastreio, 'autolesao_suicidio_recorrente')"
                        )
                        enc["condicao"] = new_cond
                        changes.append(
                            "E2: Psicologo TCD condicao expandida (tpb_rastreio autolesao)"
                        )

    # ── metadata.version ──────────────────────────────────────────────────────
    data["metadata"]["version"] = "0.4.0"
    changes.append("metadata.version -> 0.4.0")

    return data, changes


def main():
    print(f"Input: {INPUT_FILE}")
    if not INPUT_FILE.exists():
        print("ERRO: arquivo de entrada nao encontrado.")
        sys.exit(1)

    with open(INPUT_FILE, encoding="utf-8") as f:
        data = json.load(f)

    data, changes = patch(data)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Output: {OUTPUT_FILE}")
    print(f"\n{len(changes)} mudancas aplicadas:")
    for i, c in enumerate(changes, 1):
        print(f"  {i:02d}. {c}")

    # Contagem final
    ENFERMAGEM_NODE_ID = "20e05d57-3dfa-43cb-b039-74279162a73a"
    for node in data["nodes"]:
        nid = node["id"]
        if nid == ENFERMAGEM_NODE_ID:
            qs = node["data"].get("questions", [])
            tipo_q = [q for q in qs if q.get("uid") == "tipo_consulta"]
            print(f"\nEnfermagem: tipo_consulta {'PRESENTE' if tipo_q else 'AUSENTE'}")
        if nid == "node-psiq-04-diagnostico":
            qs = node["data"].get("questions", [])
            print(f"node-psiq-04-diagnostico: {len(qs)} perguntas")
            for q in qs:
                print(f"  uid: {q.get('uid', '?')}")
        if nid == "node-psiq-06-conduta":
            cd = node["data"].get("condutaDataNode", {})
            if cd:
                print("node-psiq-06-conduta:")
                for k in ("medicamento", "exame", "encaminhamento", "mensagem", "orientacao"):
                    print(f"  {k}: {len(cd.get(k, []))}")


if __name__ == "__main__":
    main()
