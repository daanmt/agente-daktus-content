"""patch_v021_fixes.py
=====================
Produz amil-ficha_psiquiatria-v0.2.1.json (versao final) a partir do draft do usuario.

OPERACOES:
  A. metadata.version "draft" -> "0.2.1"
  B. 5 alertas com UIDs de escores removidos -> substituicao por condicoes diagnostico-driven
  C. Remove duplicata do alerta PHQ-9 (mesmo item aparece 2x no array mensagem)

Sessao: session_021 -- 2026-03-09

FUNDAMENTO DAS SUBSTITUICOES:
  Os escores PHQ-9, MADRS, YMRS, Y-BOCS, PCL-5 foram removidos como perguntas pelo usuario
  pois "provavelmente nao serao tao utilizados". Os alertas correspondentes nao disparam pois
  referenciam UIDs inexistentes. Substituicao por condicoes baseadas em episodio_atual_humor
  (choice: eutimia / depressao_leve / depressao_moderada / depressao_grave / hipomania / mania
  / misto) e diagnostico_ativo (multiChoice). A logica clinica e preservada sem escores.
"""

import json
import os
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = os.path.join(os.path.dirname(__file__), "..", "especialidades", "psiquiatria", "jsons")
JSON_PATH = os.path.join(BASE, "amil-ficha_psiquiatria-v0.2.1.json")

# ---------------------------------------------------------------------------
# B. MAPA DE CORRECAO DE ALERTAS
# ---------------------------------------------------------------------------
# chave = substring unica na condicao antiga
# valor = (cond_nova, nome_novo)
ALERT_MAP = {
    "madrs_score >= 20": (
        "selected_any(episodio_atual_humor, 'depressao_moderada', 'depressao_grave')",
        "DEPRESSAO MODERADA/GRAVE — Revisar conduta e tratamento",
    ),
    "ymrs_score >= 20": (
        "selected_any(episodio_atual_humor, 'mania', 'hipomania')",
        "MANIA / HIPOMANIA — Avaliar internacao se episodio maniaco grave",
    ),
    "ybocs_score >= 16": (
        "'toc' in diagnostico_ativo",
        "TOC — TCC/ERP indicada (intensidade moderada-grave)",
    ),
    "pcl5_score >= 33": (
        "'tept' in diagnostico_ativo",
        "TEPT — EMDR / TF-CBT indicado",
    ),
    "phq9_score": (  # captura a condicao com phq9_score (qualquer forma)
        "selected_any(episodio_atual_humor, 'depressao_leve')",
        "DEPRESSAO LEVE — Monitorar evolucao e iniciar tratamento",
    ),
}


def patch_mensagens(cdn: dict) -> tuple[int, int]:
    """
    Corrige alertas no condutaDataNode.
    Retorna (n_corrigidos, n_duplicatas_removidas).
    """
    mensagens = cdn.get("mensagem", [])
    resultado = []
    corrigidos = 0
    dups_removidas = 0
    phq9_corrigido = False  # controle de duplicata

    for item in mensagens:
        cond = item.get("condicao", "")
        fix_key = None

        # Encontrar qual chave do mapa bate nesta condicao
        for key in ALERT_MAP:
            if key in cond:
                fix_key = key
                break

        if fix_key is None:
            # Nenhuma correcao necessaria — manter item intacto
            resultado.append(item)
            continue

        if fix_key == "phq9_score":
            if phq9_corrigido:
                # Segunda ocorrencia do mesmo alerta — remover duplicata
                print(f"  [REMOVE_DUP] Duplicata PHQ-9 removida: '{item.get('nome', '?')}'")
                dups_removidas += 1
                continue
            phq9_corrigido = True

        cond_nova, nome_novo = ALERT_MAP[fix_key]
        nome_antigo = item.get("nome", "?")
        item = dict(item)  # copia para nao mutar original
        item["condicao"] = cond_nova
        item["nome"] = nome_novo
        print(
            f"  [ALERT_FIX] '{nome_antigo}'\n"
            f"    cond: '{cond[:70]}'\n"
            f"       -> '{cond_nova}'\n"
            f"    nome: '{nome_antigo}'\n"
            f"       -> '{nome_novo}'"
        )
        corrigidos += 1
        resultado.append(item)

    cdn["mensagem"] = resultado
    return corrigidos, dups_removidas


def main():
    path = os.path.abspath(JSON_PATH)
    print(f"Arquivo: {path}")

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    total_corrigidos = 0
    total_dups = 0

    for node in data["nodes"]:
        nd = node.get("data", {})
        cdn = nd.get("condutaDataNode") or {}
        if not cdn.get("mensagem"):
            continue
        node_id = nd.get("nodeId", node.get("id", "?"))
        print(f"\nProcessando no: {node_id}")
        n_c, n_d = patch_mensagens(cdn)
        total_corrigidos += n_c
        total_dups += n_d

    # A. Atualizar metadata.version
    if "metadata" in data:
        old = data["metadata"].get("version", "?")
        data["metadata"]["version"] = "0.2.1"
        print(f"\n[METADATA] version: '{old}' -> '0.2.1'")

    # Salvar
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"ALERTAS CORRIGIDOS : {total_corrigidos}  (esperado: 5)")
    print(f"DUPLICATAS REMOVIDAS: {total_dups}  (esperado: 1)")

    # ---- Verificacao pos-patch ----
    print("\nVerificando UIDs de escores residuais...")
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    score_uids = ["phq9_score", "madrs_score", "ymrs_score", "ybocs_score", "pcl5_score"]
    erros = 0
    for uid in score_uids:
        # Ignorar se aparecer apenas em comentarios/nomes historicos (nao em "condicao")
        if f'"{uid}"' in raw or f"'{uid}'" in raw or f" {uid} " in raw or f"({uid}" in raw:
            print(f"  RESIDUAL em condicao: {uid!r}")
            erros += 1
    if erros == 0:
        print("  OK -- 0 UIDs de escores em condicoes")
    else:
        print(f"  ATENCAO: {erros} UIDs residuais (verificar manualmente)")

    with open(path, encoding="utf-8") as f:
        data2 = json.load(f)

    total_msg = 0
    for node in data2["nodes"]:
        cdn2 = node.get("data", {}).get("condutaDataNode") or {}
        total_msg += len(cdn2.get("mensagem", []))

    print(f"\nTotal alertas pos-patch : {total_msg}  (era 21, esperado: 20 apos remover duplicata)")
    print(f"metadata.version        : {data2.get('metadata', {}).get('version')}")
    print(f"Output                  : {path}")


if __name__ == "__main__":
    main()
