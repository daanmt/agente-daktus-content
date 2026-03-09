"""patch_v021_to_v03_codigos.py
================================
Popula codigos TUSS e MEVO em amil-ficha_psiquiatria-v0.2.1.json.

OPERACOES:
  A. 2 exames com TUSS vazio -> popular com codigos do TUSS.xlsx / confirmados
  B. 13 medicamentos sem codigo MEVO -> popular com codigos do Mevo..xlsx

Sessao: session_021 -- 2026-03-09

FONTES DE REFERENCIA:
  - referencia/TUSS.xlsx (Planilha 1_TUSS-SIP: ~5971 registros, versao TUSS 202405)
  - referencia/Mevo..xlsx (aba Medicamentos: ~978 registros; aba Exames: ~89 registros)

NOTAS:
  - Metilfenidato LP, Lisdexanfetamina, Biperideno, Propranolol: NAO encontrados no Mevo..xlsx.
    Medicamentos nao cobertos pela operadora Amil ou nao cadastrados no periodo de referencia.
    codigo mantido como [].
  - Escitalopram 10mg: Mevo lista apenas 20mg (MEVO=35779).
    Dose de inicio recomendada (10mg) nao esta no catalogo; codigo mantido como [] para nao
    induzir erro de cobertura. Revisar com equipe de saude/Amil.
  - Quetiapina: Mevo tem 50mg LP (MEVO=15067) e 100mg (MEVO=29137). Sem 25mg.
  - Para exames com item unico representando dois procedimentos (Troponina + PCR),
    sao listados dois codigos TUSS no array codigo[].
"""

import json
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = os.path.join(os.path.dirname(__file__), "..", "especialidades", "psiquiatria", "jsons")
JSON_PATH = os.path.join(BASE, "amil-ficha_psiquiatria-v0.2.1.json")


# ---------------------------------------------------------------------------
# A. TUSS PARA EXAMES VAZIOS
# ---------------------------------------------------------------------------
# Chave = substring unica do nome do exame no JSON
# Valor = lista de {"sistema": "TUSS", "codigo": "XXXXXXXX"}
TUSS_FIXES = {
    "HLA-B*1502": [
        {"sistema": "TUSS", "codigo": "40306887"},  # Genotipagem do sistema HLA (TUSS 202405)
    ],
    "Troponina + Proteína C-reativa": [
        {"sistema": "TUSS", "codigo": "40302571"},  # Troponina - pesquisa e/ou dosagem
        {"sistema": "TUSS", "codigo": "40308391"},  # Proteina C reativa, quantitativa
    ],
}


# ---------------------------------------------------------------------------
# B. MEVO PARA MEDICAMENTOS
# ---------------------------------------------------------------------------
# Chave = substring unica do nome do medicamento no JSON
# Valor = lista de {"sistema": "MEVO", "codigo": "XXXXX"}
# Mevo..xlsx -- aba Medicamentos, campo "ID Mevo" (5 digitos, zero-padded)
MEVO_FIXES = {
    # Antidepressivos (ISRS)
    "Sertralina 50mg": [
        {"sistema": "MEVO", "codigo": "08994"},  # Cloridrato de Sertralina 50mg
    ],
    "Fluoxetina 20mg": [
        {"sistema": "MEVO", "codigo": "42541"},  # Fluoxetina 20mg Comprimido Revestido
    ],
    # Estabilizadores de humor
    "Litio 300mg": [
        {"sistema": "MEVO", "codigo": "42533"},  # Carbonato de Litio 300mg
    ],
    "Lamotrigina 25mg": [
        {"sistema": "MEVO", "codigo": "35451"},  # Lamotrigina 25mg Comprimido
    ],
    # Antipsicóticos atipicos
    "Quetiapina 25 mg / 50 mg / 100 mg": [
        {"sistema": "MEVO", "codigo": "15067"},  # Hemifumarato de Quetiapina 50mg LP
        {"sistema": "MEVO", "codigo": "29137"},  # Quetiapina 100mg Comprimido Revestido
    ],
    "Olanzapina 5 mg / 10 mg": [
        {"sistema": "MEVO", "codigo": "31921"},  # Olanzapina 5mg
        {"sistema": "MEVO", "codigo": "34587"},  # Olanzapina 10mg
    ],
    "Risperidona 1 mg / 2 mg": [
        {"sistema": "MEVO", "codigo": "35806"},  # Risperidona 1mg Comprimido Revestido
        {"sistema": "MEVO", "codigo": "35807"},  # Risperidona 2mg Comprimido Revestido
    ],
    "Aripiprazol 10 mg / 15 mg": [
        {"sistema": "MEVO", "codigo": "35461"},  # Aripiprazol 10mg
        {"sistema": "MEVO", "codigo": "32613"},  # Aripiprazol 15mg
    ],
    # NOTA: Escitalopram, Metilfenidato LP, Lisdexanfetamina, Biperideno, Propranolol
    # nao foram encontrados no Mevo..xlsx com o dosagem/forma correspondente ao JSON.
    # Mantidos como [] ate confirmacao com equipe Amil.
}


def patch_exames(cdn: dict) -> int:
    """Popula codigos TUSS em exames vazios. Retorna n exames corrigidos."""
    count = 0
    for exa in cdn.get("exame", []):
        nome = exa.get("nome", "")
        for key, codigos in TUSS_FIXES.items():
            if key in nome:
                if not exa.get("codigo"):
                    exa["codigo"] = codigos
                    print(f"  [TUSS] '{nome}'")
                    for c in codigos:
                        print(f"    -> {c}")
                    count += 1
                else:
                    print(f"  [SKIP] '{nome}' ja tem codigos: {exa['codigo']}")
    return count


def patch_medicamentos(cdn: dict) -> int:
    """Popula codigos MEVO em medicamentos. Retorna n medicamentos corrigidos."""
    count = 0
    for med in cdn.get("medicamento", []):
        nome = med.get("nome", "")
        for key, codigos in MEVO_FIXES.items():
            if key in nome or nome in key:
                if not med.get("codigo"):
                    med["codigo"] = codigos
                    print(f"  [MEVO] '{nome}'")
                    for c in codigos:
                        print(f"    -> {c}")
                    count += 1
                else:
                    print(f"  [SKIP] '{nome}' ja tem codigos: {med['codigo']}")
    return count


def main():
    path = os.path.abspath(JSON_PATH)
    print(f"Arquivo: {path}")

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    total_tuss = 0
    total_mevo = 0

    for node in data["nodes"]:
        nd = node.get("data", {})
        cdn = nd.get("condutaDataNode") or {}
        if not cdn:
            continue
        node_id = nd.get("nodeId", node.get("id", "?"))

        n_t = patch_exames(cdn)
        n_m = patch_medicamentos(cdn)

        if n_t + n_m:
            print(f"No {node_id}: {n_t} TUSS + {n_m} MEVO preenchidos")

        total_tuss += n_t
        total_mevo += n_m

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"TUSS populados : {total_tuss}  (esperado: 2)")
    print(f"MEVO populados : {total_mevo}  (esperado: 8)")
    print(f"Output         : {path}")

    # Verificacao final de exames/meds sem codigo
    print("\nItens sem codigo apos patch:")
    with open(path, encoding="utf-8") as f:
        data2 = json.load(f)
    sem_codigo = []
    for node in data2["nodes"]:
        nd = node.get("data", {})
        cdn = nd.get("condutaDataNode") or {}
        for exa in cdn.get("exame", []):
            if not exa.get("codigo"):
                sem_codigo.append(f"  [EXAME] {exa.get('nome')}")
        for med in cdn.get("medicamento", []):
            if not med.get("codigo"):
                sem_codigo.append(f"  [MED]   {med.get('nome')}")
    if sem_codigo:
        for s in sem_codigo:
            print(s)
        print(f"Total sem codigo: {len(sem_codigo)}")
        print("NOTA: medicamentos sem codigo MEVO nao estao no catalogo Mevo (Amil) atual.")
    else:
        print("  OK -- todos os itens tem codigos")


if __name__ == "__main__":
    main()
