"""patch_v012_conditional_fix.py
=================================
Corrige 13 padrões de condicional incorretos em amil-ficha_psiquiatria-v0.1.2.json.

ERRO:    campo in ('v1', 'v2')
CORRETO: selected_any(campo, 'v1', 'v2')

Todos os campos afetados têm select=choice no JSON.
Para campos choice, o DSL Daktus usa:
  - 'v1' in campo          (verificar 1 valor)
  - selected_any(campo, …) (verificar N valores)
NÃO usa:
  - campo in ('v1', 'v2')  ❌ inverte operandos
  - campo != 'v1'          ❌ inválido para choice (exceto select=single)

Sessão: session_017 — 2026-03-09
Input/Output: especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.1.2.json (in-place)
"""

import json
import os
import sys

FILEPATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "especialidades",
    "psiquiatria",
    "jsons",
    "amil-ficha_psiquiatria-v0.1.2.json",
)

# ---------------------------------------------------------------------------
# Tabela de substituições exatas
# Ordem importa: mais específicas primeiro para evitar substituição parcial
# ---------------------------------------------------------------------------
SUBSTITUICOES = [
    # ---- Grupo 1: expressao em perguntas ----
    # ymrs_score
    (
        "episodio_atual_humor in ('mania', 'hipomania')",
        "selected_any(episodio_atual_humor, 'mania', 'hipomania')",
    ),
    # madrs_score
    (
        "episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'depressao_grave')",
        "selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada', 'depressao_grave')",
    ),
    # sintomas_psicoticos_humor
    (
        "episodio_atual_humor in ('depressao_grave', 'mania')",
        "selected_any(episodio_atual_humor, 'depressao_grave', 'mania')",
    ),
    # ---- Grupo 2: condicao em medicamentos ----
    # litio 300mg
    (
        "episodio_atual_humor in ('mania', 'hipomania', 'eutimia')",
        "selected_any(episodio_atual_humor, 'mania', 'hipomania', 'eutimia')",
    ),
    # lamotrigina 25mg
    (
        "episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'eutimia')",
        "selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada', 'eutimia')",
    ),
    # escitalopram / sertralina (mesma expressão, str.replace substitui todas as ocorrências)
    # já cobertos pelo item do madrs_score acima (same string)
    # ---- Grupo 3: condicao em encaminhamentos ----
    # neurologista / neuropsicólogo
    (
        "neuropsicologica_indicada in ('sim_solicitada', 'sim_pendente')",
        "selected_any(neuropsicologica_indicada, 'sim_solicitada', 'sim_pendente')",
    ),
    # cardiologia — valor único
    (
        "ecg_indicado_psico in ('estimulante_cardiopatia')",
        "selected_any(ecg_indicado_psico, 'estimulante_cardiopatia')",
    ),
    # ---- Grupo 4: condicao em mensagens de alerta ----
    # gate p0 risco alto
    (
        "internacao_indicada_p0 in ('sim_involuntaria', 'sim_voluntaria')",
        "selected_any(internacao_indicada_p0, 'sim_involuntaria', 'sim_voluntaria')",
    ),
    # clozapina — sintomas miocardite (mensagem + exame = 2 ocorrências)
    (
        "sintomas_miocardite in ('dor_toracica_dispneia_febre', 'taquicardia_inexplicada')",
        "selected_any(sintomas_miocardite, 'dor_toracica_dispneia_febre', 'taquicardia_inexplicada')",
    ),
    # ---- Grupo 6: bonus — != 'nenhum' em campo choice ----
    # cardiologia — sintomas_miocardite é select=choice, não single
    (
        "sintomas_miocardite != 'nenhum'",
        "not ('nenhum' in sintomas_miocardite)",
    ),
]


def apply_subs(text: str) -> tuple[str, list[str]]:
    """Aplica todas as substituições. Retorna (texto_corrigido, lista_de_erros_corrigidos)."""
    applied = []
    for wrong, correct in SUBSTITUICOES:
        if wrong in text:
            text = text.replace(wrong, correct)
            applied.append(wrong)
    return text, applied


def patch_node_questions(nd: dict, log: list) -> int:
    """Corrige campo `expressao` em todas as perguntas do nó."""
    count = 0
    node_id = nd.get("nodeId", nd.get("id", "?"))
    for q in nd.get("questions", []):
        expr = q.get("expressao", "")
        if not expr:
            continue
        fixed, applied = apply_subs(expr)
        if applied:
            q["expressao"] = fixed
            for a in applied:
                log.append(f"  [Q:{q.get('uid','?')}] expressao: {a!r} -> corrigido")
            count += len(applied)
    return count


def patch_conduta(cdn: dict, log: list) -> int:
    """Corrige campo `condicao` em todos os itens de conduta."""
    count = 0
    for secao in ["mensagem", "exame", "encaminhamento", "medicamento", "orientacao"]:
        for item in cdn.get(secao, []):
            cond = item.get("condicao", "")
            if not cond:
                continue
            fixed, applied = apply_subs(cond)
            if applied:
                item["condicao"] = fixed
                for a in applied:
                    log.append(
                        f"  [{secao.upper()}:{item.get('nome', item.get('id','?'))[:40]}] "
                        f"condicao: {a!r} -> corrigido"
                    )
                count += len(applied)
    return count


def main():
    filepath = os.path.abspath(FILEPATH)
    print(f"Lendo: {filepath}")

    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    total = 0
    log = []

    for node in data["nodes"]:
        nd = node.get("data", {})
        node_id = nd.get("nodeId", node.get("id", "?"))

        n_q = patch_node_questions(nd, log)
        n_c = patch_conduta(nd.get("condutaDataNode") or {}, log)
        n = n_q + n_c
        if n:
            print(f"\nNó {node_id}: {n} correção(ões)")
            for entry in log[-(n_q + n_c):]:
                print(entry)
        total += n

    # Salvar
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"TOTAL DE SUBSTITUIÇÕES: {total}")
    print(f"Arquivo salvo: {filepath}")

    # Verificação pós-patch: nenhum padrão errado deve restar
    print("\nVerificação: buscando padrões errados residuais...")
    erros = 0
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    patterns_to_check = [w for w, _ in SUBSTITUICOES]
    for p in patterns_to_check:
        if p in content:
            print(f"  ⚠️  AINDA PRESENTE: {p!r}")
            erros += 1
    if erros == 0:
        print("  ✅ Nenhum padrão errado residual encontrado.")
    else:
        print(f"  ❌ {erros} padrão(ões) ainda presente(s).")
        sys.exit(1)


if __name__ == "__main__":
    main()
