"""patch_v012_to_v02.py
=====================
Produz amil-ficha_psiquiatria-v0.2.json a partir de v0.1.2.

OPERACOES:
  A. Remove 24 perguntas (6 vdraft + 10 orphans + 8 monitoramento)
  B. Simplifica 5 condicionais de conduta (gates removidos)
  C. Corrige 7 condicionais de conduta com UIDs nao definidos
  D. Atualiza metadata.version para "0.2"

Sessao: session_019 — 2026-03-09
"""

import json
import os
import sys

INPUT_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "especialidades",
    "psiquiatria",
    "jsons",
    "amil-ficha_psiquiatria-v0.1.2.json",
)
OUTPUT_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "especialidades",
    "psiquiatria",
    "jsons",
    "amil-ficha_psiquiatria-v0.2.json",
)

# ---------------------------------------------------------------------------
# A. PERGUNTAS A REMOVER
# ---------------------------------------------------------------------------
REMOVE_UIDS = {
    # Grupo A — Re-adicionadas pelo agente (user deletou no vdraft)
    "spi_realizado",
    "neuropsicologica_indicada",
    "tept_psicoterapia_indicada",
    "nutri_encaminhada",
    "tpb_em_tcd",
    "tea_comorbidades",
    # Grupo B — Orphans diagnosticas (0 conduta, 0 referencias)
    "tab_fase_diagnostica",
    "mdq_aplicado",
    "burnout_criterios_tdm",
    "especificador_misto",
    "tdah_apresentacao",
    "sintomas_cardiacos_tdah",
    "tea_nivel_suporte",
    "tpb_autolesao_ativa",
    "tpb_sintoma_alvo",
    "ciclagem_rapida",
    # Grupo C — Monitoramento farmacologico (0 conduta, user confirmou remocao)
    "litio_fase",
    "litemia_valor",
    "vpa_fase",
    "vpa_nivel",
    "vpa_labs_recentes",
    "cbz_nivel",
    "anc_valor",
    "ap_tempo_uso",
}

# ---------------------------------------------------------------------------
# B + C. SUBSTITUICOES EM CONDICIONAIS DE CONDUTA
# ---------------------------------------------------------------------------
# Formato: (trecho_errado, trecho_correto)
# Mais especificas primeiro para evitar substituicao parcial
COND_SUBSTITUICOES = [
    # --- Grupo B: simplificar gates de perguntas removidas ---
    # spi_realizado
    (
        "risco_suicidio_intermediario is True and spi_realizado != 'sim'",
        "risco_suicidio_intermediario is True",
    ),
    # neuropsicologica_indicada -> encaminhamento Neuropsicólogo
    (
        "selected_any(neuropsicologica_indicada, 'sim_solicitada', 'sim_pendente')",
        "'tdah' in diagnostico_ativo",
    ),
    # tept_psicoterapia_indicada -> encaminhamento TF-CBT/EMDR
    (
        "'tept' in diagnostico_ativo and tept_psicoterapia_indicada != 'sim'",
        "'tept' in diagnostico_ativo",
    ),
    # nutri_encaminhada -> encaminhamento Nutricionista
    (
        "selected_any(diagnostico_ativo, 'ta_anorexia', 'ta_bulimia', 'ta_tcap') and nutri_encaminhada != 'ja_acompanha'",
        "selected_any(diagnostico_ativo, 'ta_anorexia', 'ta_bulimia', 'ta_tcap')",
    ),
    # tpb_em_tcd -> encaminhamento TCD
    (
        "'tpb' in diagnostico_ativo and tpb_em_tcd != 'sim'",
        "'tpb' in diagnostico_ativo",
    ),
    # --- Grupo D: corrigir UIDs nao definidos ---
    # CLOZAPINA ANC: anc_dentro_limite inexistente -> lembrete permanente para clozapina
    (
        "anc_dentro_limite == 'suspender_menor_1000'",
        "'clozapina' in medicamentos_em_uso",
    ),
    # Cardiologia: remover clausula anc_dentro_limite (uid morto)
    (
        " or (anc_dentro_limite == 'suspender_menor_1000' and not ('nenhum' in sintomas_miocardite))",
        "",
    ),
    # VPA + MIE: vpa_mie_consentimento inexistente -> mulher em idade fertil + VPA
    (
        "vpa_mie_consentimento == 'nao_pendente_hoje'",
        "sexo_feminino_ie is True and 'valproato' in medicamentos_em_uso",
    ),
    # TAB + AD sem estabilizador: ad_sem_estabilizador inexistente -> condicao direta
    (
        "ad_sem_estabilizador == 'confirmado_risco_documentado'",
        (
            "'tab' in diagnostico_ativo"
            " and selected_any(medicamentos_em_uso, 'isrs', 'irsn', 'antidepressivo_tca', 'bupropiona_snri')"
            " and not selected_any(medicamentos_em_uso, 'litio', 'valproato', 'carbamazepina', 'lamotrigina')"
        ),
    ),
    # Emergencia/SAMU: remover clausula encaminhamento_urgencia_necessario
    (
        "(risco_suicidio_alto is True) or (encaminhamento_urgencia_necessario is True)",
        "risco_suicidio_alto is True",
    ),
    # HLA-B*1502: remover gate cbz_hla_realizado
    (
        "'carbamazepina' in medicamentos_em_uso and cbz_hla_realizado == 'nao_pendente'",
        "'carbamazepina' in medicamentos_em_uso",
    ),
    # Prolactina: remover gate prolactina_sintomatic
    (
        "'ap_atipico_risperidona' in medicamentos_em_uso and prolactina_sintomatic != 'nenhum'",
        "'ap_atipico_risperidona' in medicamentos_em_uso",
    ),
]

# ---------------------------------------------------------------------------
# D. NOME/CONTEUDO DO ALERTA CLOZAPINA ANC (reescrita editorial)
# ---------------------------------------------------------------------------
CLOZAPINA_NOME_ANTIGO = "CLOZAPINA \u2013 ANC &lt;1.000: SUSPENDER IMEDIATAMENTE"
CLOZAPINA_NOME_NOVO = "CLOZAPINA \u2013 Monitoramento ANC obrigat\u00f3rio (risco de agranulocitose)"
CLOZAPINA_CONTEUDO_NOVO = (
    "<p><strong>Paciente em uso de clozapina: monitoramento obrigat\u00f3rio do "
    "hemograma completo (ANC).</strong><br>"
    "Se ANC &lt;1.500/mm\u00b3: intensificar monitoramento.<br>"
    "Se ANC &lt;1.000/mm\u00b3: <strong>suspender imediatamente</strong>, "
    "encaminhar urg\u00eancia hemato-oncol\u00f3gica e registrar no PGRM (ANVISA). "
    "N\u00e3o reiniciar sem avalia\u00e7\u00e3o especializada.</p>"
)


# ---------------------------------------------------------------------------
# Funcoes auxiliares
# ---------------------------------------------------------------------------

def apply_cond_subs(cond: str) -> tuple[str, list[str]]:
    """Aplica substituicoes em uma string de condicao. Retorna (nova, aplicadas)."""
    applied = []
    for old, new in COND_SUBSTITUICOES:
        if old in cond:
            cond = cond.replace(old, new)
            applied.append(old[:60])
    return cond, applied


def patch_questions(nd: dict, log: list) -> int:
    """Remove perguntas da lista de questions do no."""
    qs_antes = nd.get("questions", [])
    qs_depois = [q for q in qs_antes if q.get("uid") not in REMOVE_UIDS]
    removidos = [q.get("uid") for q in qs_antes if q.get("uid") in REMOVE_UIDS]
    if removidos:
        nd["questions"] = qs_depois
        for uid in removidos:
            log.append(f"  [REMOVE_Q] {uid}")
    return len(removidos)


def patch_conduct(cdn: dict, log: list) -> int:
    """Aplica substituicoes de condicoes nos itens de conduta. Retorna n substituicoes."""
    count = 0
    for secao in ["mensagem", "exame", "encaminhamento", "medicamento", "orientacao"]:
        for item in cdn.get(secao, []):
            cond = item.get("condicao", "")
            if not cond:
                continue
            nova, applied = apply_cond_subs(cond)
            if applied:
                item["condicao"] = nova
                nome = item.get("nome", item.get("id", "?"))[:50]
                for a in applied:
                    log.append(f"  [COND_FIX {secao.upper()}] {nome} | {a!r} -> corrigido")
                count += len(applied)
    return count


def patch_clozapina_alerta(cdn: dict, log: list) -> int:
    """Reescreve nome e conteudo do alerta CLOZAPINA ANC."""
    count = 0
    for item in cdn.get("mensagem", []):
        nome = item.get("nome", "")
        if "ANC" in nome and "CLOZAPINA" in nome:
            item["nome"] = CLOZAPINA_NOME_NOVO
            # Tentar diferentes chaves de conteudo
            for chave in ["conteudo", "texto", "mensagem", "content"]:
                if chave in item:
                    item[chave] = CLOZAPINA_CONTEUDO_NOVO
                    break
            log.append(f"  [EDITORIAL] CLOZAPINA ANC alerta nome/conteudo atualizado")
            count += 1
    return count


def main():
    input_path = os.path.abspath(INPUT_PATH)
    output_path = os.path.abspath(OUTPUT_PATH)
    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    total_removed = 0
    total_cond_fixed = 0
    log = []

    for node in data["nodes"]:
        nd = node.get("data", {})
        node_id = nd.get("nodeId", node.get("id", "?"))

        n_q = patch_questions(nd, log)
        cdn = nd.get("condutaDataNode") or {}
        n_c = patch_conduct(cdn, log)
        n_e = patch_clozapina_alerta(cdn, log)

        if n_q + n_c + n_e:
            print(f"\nNo {node_id}: {n_q} perguntas removidas, {n_c} condicionais corrigidas, {n_e} alertas reescritos")
            for entry in log[-(n_q + n_c + n_e):]:
                print(entry)

        total_removed += n_q
        total_cond_fixed += n_c

    # Atualizar metadata.version
    if "metadata" in data:
        data["metadata"]["version"] = "0.2"
        print("\n[METADATA] version -> 0.2")

    # Salvar output
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"PERGUNTAS REMOVIDAS: {total_removed} (esperado: 24)")
    print(f"CONDICIONAIS CORRIGIDAS: {total_cond_fixed} (esperado: ~12)")
    print(f"Output: {output_path}")

    # Verificacao pos-patch: nenhum UID removido deve restar nas perguntas
    print("\nVerificando perguntas residuais...")
    with open(output_path, encoding="utf-8") as f:
        data2 = json.load(f)

    q_residuais = 0
    for node in data2["nodes"]:
        nd = node.get("data", {})
        for q in nd.get("questions", []):
            if q.get("uid") in REMOVE_UIDS:
                print(f"  RESIDUAL: {q.get('uid')}")
                q_residuais += 1
    if q_residuais == 0:
        print("  OK — 0 perguntas residuais dos grupos A/B/C")
    else:
        print(f"  ERRO: {q_residuais} perguntas residuais encontradas")
        sys.exit(1)

    # Verificar UIDs mortos nas condicionais
    print("\nVerificando UIDs mortos residuais...")
    uids_mortos = [
        "anc_dentro_limite", "vpa_mie_consentimento", "ad_sem_estabilizador",
        "encaminhamento_urgencia_necessario", "cbz_hla_realizado", "prolactina_sintomatic",
        "spi_realizado", "neuropsicologica_indicada", "tept_psicoterapia_indicada",
        "nutri_encaminhada", "tpb_em_tcd",
    ]
    with open(output_path, encoding="utf-8") as f:
        conteudo_raw = f.read()

    erros = 0
    for uid in uids_mortos:
        if uid in conteudo_raw:
            print(f"  AINDA PRESENTE: {uid!r}")
            erros += 1
    if erros == 0:
        print("  OK — 0 UIDs mortos residuais")
    else:
        print(f"  ATENCAO: {erros} UIDs encontrados (verificar manualmente se sao residuos ou coincidencias)")

    # Contagem final de perguntas
    total_q = sum(
        len(node.get("data", {}).get("questions", []))
        for node in data2["nodes"]
    )
    print(f"\nPERGUNTAS TOTAIS EM v0.2: {total_q} (era 66 em v0.1.2)")


if __name__ == "__main__":
    main()
