#!/usr/bin/env python3
"""
patch_v023_to_v030.py
Origem: amil-ficha_psiquiatria-v0.2.3.json
Destino: especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.3.0.json

Reforma v0.3.0 — camada intermediária de dissecção sindrômica
(baseada em análise Kaplan & Sadock + Dalgalarrondo)

GRUPO A — 4 perguntas novas em node-psiq-04-diagnostico:
  D1. bipolar_rastreio        — detector bipolar antes de prescrever antidepressivo
  D2. subtipo_ansioso         — discrimina TAG/pânico/fobia/TOC/TEPT/secundário
  D3. contexto_agressividade  — diferencia mania/psicose/substância/orgânico/TPB/TEI
  D4. perfil_sono             — sono como modificador sindrômico (bipolar, TEPT, melancolia)

GRUPO B — 4 correções de `expressao` em perguntas existentes:
  B1. comportamento_suicida_recorrente: adiciona TPB
  B2. episodio_atual_humor: adiciona burnout + tpb
  (B3 Neuropsicólogo e B4 TAB+bupropiona estão nos grupos E e C)

GRUPO C — Bug fix em 1 mensagem de conduta:
  C1. TAB + Antidepressivo: 'bupropiona_snri' → 'bupropiona'

GRUPO D — 6 novas mensagens em conduta:
  D1. BIPOLAR NÃO DESCARTADO
  D2. SONO REDUZIDO SEM FADIGA
  D3. AGRESSIVIDADE — Red flags orgânicos
  D4. AGRESSIVIDADE — Contexto de psicose
  D5. SUBTIPO ANSIOSO: TOC provável
  D6. SUBTIPO ANSIOSO: TEPT provável

GRUPO E — Recalibração de 3 encaminhamentos:
  E1. Neuropsicólogo: remove primeiro_episodio_psicotico (playbook limita a TDAH/TEA)
  E2. Neurologia: adiciona red_flag_organico em contexto_agressividade
  E3. CAPS II: adiciona agressividade + psicose_paranoia em contexto_agressividade

metadata.version → "0.3.0"
"""
import json
import uuid
import sys
from pathlib import Path

REPO_ROOT   = Path(__file__).resolve().parent.parent
INPUT_FILE  = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.2.3.json"
OUTPUT_FILE = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.3.0.json"


def uid() -> str:
    return str(uuid.uuid4())


# ══════════════════════════════════════════════════════════════════════════════
# GRUPO A — Novas perguntas discriminadoras
# ══════════════════════════════════════════════════════════════════════════════

# D1 — Rastreio bipolar (multiChoice)
Q_BIPOLAR_RASTREIO = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "bipolar_rastreio",
    "titulo": (
        "<p><strong>Rastreio para bipolaridade — histórico do paciente</strong></p>"
    ),
    "descricao": (
        "<p>Selecione se o paciente relata ou apresenta histórico de:</p>"
    ),
    "condicional": "visivel",
    "expressao": (
        "selected_any(diagnostico_ativo, 'tdm', 'distimia', 'burnout') "
        "or 'humor_deprimido' in motivo_consulta"
    ),
    "select": "multiChoice",
    "options": [
        {
            "iid": uid(), "id": "sem_historico_bipolar",
            "label": "Sem histórico de episódios maníacos ou hipomaníacos",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "elevacao_humor_previa",
            "label": "Episódios prévios de euforia, expansividade ou irritabilidade marcante",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "reducao_sono_sem_fadiga",
            "label": "Já ficou dias dormindo muito menos sem sentir cansaço",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "grandiosidade_episodica",
            "label": "Episódios de autoconfiança exagerada, impulsividade ou decisões arriscadas",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "tab_documentado",
            "label": "TAB já diagnosticado previamente",
            "preselected": False, "exclusive": False
        },
    ]
}

# D2 — Subtipo ansioso (choice)
Q_SUBTIPO_ANSIOSO = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "subtipo_ansioso",
    "titulo": (
        "<p><strong>Apresentação clínica predominante do quadro ansioso</strong></p>"
    ),
    "descricao": (
        "<p>Selecione o padrão que melhor descreve a queixa ansiosa do paciente</p>"
    ),
    "condicional": "visivel",
    "expressao": (
        "selected_any(motivo_consulta, 'ansiedade_panico') "
        "or selected_any(diagnostico_ativo, 'tag', 'panico', 'fobia_social', 'toc', 'tept')"
    ),
    "select": "choice",
    "options": [
        {
            "iid": uid(), "id": "preocupacao_difusa_persistente",
            "label": "Preocupação difusa, persistente, em múltiplos domínios (compatível com TAG)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "crises_abruptas_esquiva",
            "label": "Crises abruptas e intensas com medo de nova crise ou esquiva (Pânico/Agorafobia)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "medo_avaliacao_social",
            "label": "Medo intenso de situações sociais ou de avaliação (Fobia social)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "obsessoes_compulsoes",
            "label": "Pensamentos intrusivos repetitivos + rituais/compulsões (TOC)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "trauma_intrusao_evitacao",
            "label": "Evento traumático com revivescência, evitação e hipervigilância (TEPT)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "ansiedade_secundaria",
            "label": "Ansiedade claramente relacionada a substância, estimulante ou condição clínica",
            "preselected": False, "exclusive": True
        },
    ]
}

# D3 — Contexto de agressividade (multiChoice)
Q_CONTEXTO_AGRESSIVIDADE = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "contexto_agressividade",
    "titulo": (
        "<p><strong>Contexto do comportamento agressivo — subtipagem sindrômica</strong></p>"
    ),
    "descricao": (
        "<p>Selecione todos os elementos presentes que contextualizam o comportamento agressivo</p>"
    ),
    "condicional": "visivel",
    "expressao": (
        "'agressividade' in diagnostico_ativo "
        "or 'agressividade_comportamento' in motivo_consulta"
    ),
    "select": "multiChoice",
    "options": [
        {
            "iid": uid(), "id": "mania_agitacao",
            "label": "Euforia/irritabilidade intensa + aceleração do pensamento + redução do sono",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "psicose_paranoia",
            "label": "Delírios persecutórios ou alucinatórios associados ao comportamento",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "substancia_intoxicacao",
            "label": "Comportamento claramente associado a intoxicação ou abstinência",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "red_flag_organico",
            "label": "Red flags neuro: confusão, amnésia do episódio, aura, déficit focal ou início tardio",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "desregulacao_tpb",
            "label": "Padrão de desregulação intensa com medo de abandono e impulsividade crônica (TPB)",
            "preselected": False, "exclusive": False
        },
        {
            "iid": uid(), "id": "episodico_tei",
            "label": "Episódico, desproporcional, impulsivo, sem premeditação, com remorso após o ato (TEI)",
            "preselected": False, "exclusive": False
        },
    ]
}

# D4 — Perfil do sono (choice)
Q_PERFIL_SONO = {
    "id": f"P{uid()}",
    "nodeId": "node-psiq-04-diagnostico",
    "uid": "perfil_sono",
    "titulo": (
        "<p><strong>Perfil da alteração do sono</strong></p>"
    ),
    "descricao": (
        "<p>Selecione o padrão predominante da queixa de sono do paciente</p>"
    ),
    "condicional": "visivel",
    "expressao": (
        "selected_any(motivo_consulta, 'insomnia_sono', 'sonolencia_hipersonia')"
    ),
    "select": "choice",
    "options": [
        {
            "iid": uid(), "id": "insonia_iniciacao",
            "label": "Dificuldade para iniciar o sono (latência prolongada)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "insonia_manutencao",
            "label": "Despertares frequentes ou dificuldade para voltar a dormir",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "despertar_precoce",
            "label": "Despertar muito cedo sem conseguir voltar a dormir (sugestivo de melancolia)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "hipersonia_cansaco",
            "label": "Sonolência excessiva com cansaço marcado (hipersonia)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "reducao_necessidade_sem_fadiga",
            "label": "Dormiu muito menos do habitual sem sentir cansaço (rastreio: hipomania/mania)",
            "preselected": False, "exclusive": True
        },
        {
            "iid": uid(), "id": "pesadelos_trauma",
            "label": "Pesadelos recorrentes ou sono perturbado relacionado a evento traumático (TEPT)",
            "preselected": False, "exclusive": True
        },
    ]
}


# ══════════════════════════════════════════════════════════════════════════════
# GRUPO D — Novas mensagens de conduta
# ══════════════════════════════════════════════════════════════════════════════

NEW_MESSAGES = [
    {
        "id": uid(),
        "nome": "BIPOLAR NÃO DESCARTADO — Não iniciar antidepressivo sem estabilizador de humor",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "selected_any(bipolar_rastreio, 'elevacao_humor_previa', 'reducao_sono_sem_fadiga', "
            "'grandiosidade_episodica', 'tab_documentado') and not 'tab' in diagnostico_ativo"
        ),
        "conteudo": (
            "<p><strong>Rastreio positivo para bipolaridade.</strong><br>"
            "• O paciente relata histórico sugestivo de episódios maníacos ou hipomaníacos.<br>"
            "• <strong>Não iniciar antidepressivo em monoterapia</strong> sem avaliar necessidade "
            "de estabilizador de humor (risco de virada maníaca e ciclagem rápida).<br>"
            "• Aplicar MDQ ou entrevista clínica estruturada para TAB antes de fechar diagnóstico.<br>"
            "• Considerar encaminhamento para avaliação especializada se dúvida diagnóstica persistir.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "SONO — Redução da necessidade sem fadiga: rastreio positivo para hipomania/mania",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "perfil_sono == 'reducao_necessidade_sem_fadiga'",
        "conteudo": (
            "<p><strong>Sono reduzido sem fadiga: sinal cardinal de hipomania/mania.</strong><br>"
            "• Diferenciar de insônia simples: na hipomania/mania o paciente não sente cansaço "
            "apesar de dormir menos.<br>"
            "• Investigar outros sintomas maníacos: taquipsiquismo, grandiosidade, impulsividade, "
            "aumento de atividade.<br>"
            "• <strong>Contraindicado iniciar antidepressivo sem estabilizador</strong> neste contexto.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "AGRESSIVIDADE — Red flags orgânicos/neurológicos: investigação obrigatória",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "selected_any(contexto_agressividade, 'red_flag_organico')",
        "conteudo": (
            "<p><strong>Presença de red flags neurológicos no contexto da agressividade.</strong><br>"
            "• Sinais sugestivos de causa orgânica/neurológica: confusão pós-ictal, amnésia do "
            "episódio, aura, déficit focal, início tardio (>40 anos sem psiquiatria prévia).<br>"
            "• Encaminhamento para <strong>Neurologia obrigatório</strong> (ver abaixo).<br>"
            "• Considerar: EEG, neuroimagem, eletrólitos, glicemia, função tireoidiana, toxicológico.<br>"
            "• Diagnóstico de TEI só após exclusão de causa orgânica, epilepsia temporal e psicose.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "AGRESSIVIDADE — Contexto psicótico: avaliar antipsicótico e segurança imediata",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": "selected_any(contexto_agressividade, 'psicose_paranoia')",
        "conteudo": (
            "<p><strong>Agressividade com componente psicótico identificado.</strong><br>"
            "• Delírios persecutórios ou alucinatórios como motivação para o comportamento.<br>"
            "• <strong>Antipsicótico indicado</strong>: considerar iniciar ou ajustar dose (ver "
            "prescrições abaixo).<br>"
            "• Avaliar necessidade de avaliação emergencial se risco imediato persistir.<br>"
            "• Considerar CAPS II para manejo ambulatorial intensivo se quadro complexo.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "SUBTIPO ANSIOSO — TOC provável: avaliar ERP antes de fechar diagnóstico",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "subtipo_ansioso == 'obsessoes_compulsoes' and not 'toc' in diagnostico_ativo"
        ),
        "conteudo": (
            "<p><strong>Padrão de obsessões e compulsões identificado.</strong><br>"
            "• A apresentação clínica é compatível com TOC, embora o diagnóstico ainda não esteja "
            "formalmente registrado.<br>"
            "• Confirmar: pensamentos intrusivos repetitivos + rituais/compulsões mentais ou "
            "comportamentais + insight (ao menos parcial) + prejuízo funcional.<br>"
            "• Encaminhar para <strong>Psicólogo — ERP (Terapia de Exposição e Prevenção de "
            "Resposta)</strong> se confirmado.<br>"
            "• Considerar formalizar diagnóstico de TOC em `diagnostico_ativo`.</p>"
        ),
        "observacao": ""
    },
    {
        "id": uid(),
        "nome": "SUBTIPO ANSIOSO — TEPT provável: avaliar TF-CBT/EMDR antes de fechar diagnóstico",
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": (
            "subtipo_ansioso == 'trauma_intrusao_evitacao' and not 'tept' in diagnostico_ativo"
        ),
        "conteudo": (
            "<p><strong>Padrão de reação ao trauma identificado.</strong><br>"
            "• A apresentação é compatível com TEPT: evento traumático + revivescência/flashbacks + "
            "evitação + hipervigilância.<br>"
            "• Confirmar: exposição a evento qualificante, duração >1 mês, prejuízo funcional.<br>"
            "• Encaminhar para <strong>Psicólogo — TF-CBT ou EMDR</strong> se confirmado.<br>"
            "• Considerar formalizar diagnóstico de TEPT em `diagnostico_ativo`.</p>"
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

    for node in nodes:
        nid = node["id"]
        questions = node["data"].get("questions", [])
        cd = node["data"].get("condutaDataNode", {})

        # ── GRUPO A: inserir novas perguntas em node-psiq-04-diagnostico ────
        if nid == "node-psiq-04-diagnostico":
            existing_uids = {q.get("uid") for q in questions}

            # D1: bipolar_rastreio — inserir após episodio_atual_humor
            if "bipolar_rastreio" not in existing_uids:
                humor_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "episodio_atual_humor"),
                    0
                )
                questions.insert(humor_idx + 1, Q_BIPOLAR_RASTREIO)
                changes.append("D1: bipolar_rastreio inserido em node-psiq-04-diagnostico")

            # D2: subtipo_ansioso — inserir após bipolar_rastreio
            if "subtipo_ansioso" not in existing_uids:
                rastreio_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "bipolar_rastreio"),
                    1
                )
                questions.insert(rastreio_idx + 1, Q_SUBTIPO_ANSIOSO)
                changes.append("D2: subtipo_ansioso inserido em node-psiq-04-diagnostico")

            # D3: contexto_agressividade — inserir após tea_irritabilidade_grave
            if "contexto_agressividade" not in existing_uids:
                tea_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "tea_irritabilidade_grave"),
                    len(questions) - 1
                )
                questions.insert(tea_idx + 1, Q_CONTEXTO_AGRESSIVIDADE)
                changes.append("D3: contexto_agressividade inserido em node-psiq-04-diagnostico")

            # D4: perfil_sono — inserir após contexto_agressividade
            if "perfil_sono" not in existing_uids:
                agr_idx = next(
                    (i for i, q in enumerate(questions) if q.get("uid") == "contexto_agressividade"),
                    len(questions) - 1
                )
                questions.insert(agr_idx + 1, Q_PERFIL_SONO)
                changes.append("D4: perfil_sono inserido em node-psiq-04-diagnostico")

            # ── GRUPO B: corrigir expressao de perguntas existentes ─────────

            for q in questions:
                # B2: comportamento_suicida_recorrente — adicionar TPB
                if q.get("uid") == "comportamento_suicida_recorrente":
                    old = q.get("expressao", "")
                    new_expr = "selected_any(diagnostico_ativo, 'esquizofrenia', 'tpb')"
                    if old != new_expr:
                        q["expressao"] = new_expr
                        changes.append(f"B2: comportamento_suicida_recorrente expressao: '{old}' → '{new_expr}'")

                # B3: episodio_atual_humor — adicionar burnout + tpb
                if q.get("uid") == "episodio_atual_humor":
                    old = q.get("expressao", "")
                    new_expr = "selected_any(diagnostico_ativo, 'tdm', 'distimia', 'tab', 'burnout', 'tpb')"
                    if old != new_expr:
                        q["expressao"] = new_expr
                        changes.append(f"B3: episodio_atual_humor expressao expandida (burnout + tpb)")

            node["data"]["questions"] = questions

        # ── GRUPO C + D + E: conduta ─────────────────────────────────────────
        if nid == "node-psiq-06-conduta" and cd:

            # GRUPO C: bug bupropiona_snri → bupropiona
            for msg in cd.get("mensagem", []):
                if "TAB + Antidepressivo" in msg.get("nome", ""):
                    old_cond = msg.get("condicao", "")
                    if "bupropiona_snri" in old_cond:
                        msg["condicao"] = old_cond.replace("'bupropiona_snri'", "'bupropiona'")
                        changes.append("C1: TAB+Antidepressivo bug corrigido: bupropiona_snri → bupropiona")

            # GRUPO D: novas mensagens
            existing_msg_names = {m.get("nome", "") for m in cd.get("mensagem", [])}
            for new_msg in NEW_MESSAGES:
                if new_msg["nome"] not in existing_msg_names:
                    cd.setdefault("mensagem", []).append(new_msg)
                    changes.append(f"D: mensagem adicionada: {new_msg['nome'][:55]}")

            # GRUPO E: recalibrar encaminhamentos
            for enc in cd.get("encaminhamento", []):
                nome = enc.get("nome", "")

                # E1: Neuropsicólogo — remover primeiro_episodio_psicotico
                if "Neuropsicól" in nome:
                    old = enc.get("condicao", "")
                    new_cond = "selected_any(diagnostico_ativo, 'tdah', 'tea')"
                    if old != new_cond:
                        enc["condicao"] = new_cond
                        changes.append(f"E1: Neuropsicólogo condição recalibrada (removido primeiro_episodio_psicotico)")

                # E2: Neurologia — adicionar red_flag_organico
                if "Neurologia" in nome:
                    old = enc.get("condicao", "")
                    new_cond = (
                        "primeiro_episodio_psicotico is True "
                        "or selected_any(comorbidades_clinicas, 'epilepsia') "
                        "or selected_any(contexto_agressividade, 'red_flag_organico')"
                    )
                    if old != new_cond:
                        enc["condicao"] = new_cond
                        changes.append("E2: Neurologia condição expandida (red_flag_organico em agressividade)")

                # E3: CAPS II — adicionar agressividade + psicose_paranoia
                if "CAPS II" in nome:
                    old = enc.get("condicao", "")
                    new_cond = (
                        "selected_any(diagnostico_ativo, 'esquizofrenia', 'agressividade') "
                        "or (comportamento_suicida_recorrente is True) "
                        "or selected_any(contexto_agressividade, 'psicose_paranoia')"
                    )
                    if old != new_cond:
                        enc["condicao"] = new_cond
                        changes.append("E3: CAPS II condição expandida (agressividade + psicose_paranoia)")

    # ── metadata.version ──────────────────────────────────────────────────────
    data["metadata"]["version"] = "0.3.0"
    changes.append("metadata.version → 0.3.0")

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
    for node in data["nodes"]:
        if node["id"] == "node-psiq-04-diagnostico":
            qs = node["data"].get("questions", [])
            print(f"\nnode-psiq-04-diagnostico: {len(qs)} perguntas")
        if node["id"] == "node-psiq-06-conduta":
            cd = node["data"].get("condutaDataNode", {})
            if cd:
                print("node-psiq-06-conduta:")
                for k in ("medicamento", "exame", "encaminhamento", "mensagem", "orientacao"):
                    print(f"  {k}: {len(cd.get(k, []))}")


if __name__ == "__main__":
    main()
