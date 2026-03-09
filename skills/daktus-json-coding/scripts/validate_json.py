"""
validate_json.py — Validação estrutural de JSON Daktus
Verifica integridade de edges, linkIds, iids e posicionamento.
Não modifica o JSON. Apenas relata problemas.

Uso:
  python validate_json.py <caminho_do_json>
"""
import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

def validate(filepath):
    with open(filepath, encoding="utf-8") as f:
        d = json.load(f)

    nodes = {n["id"] for n in d["nodes"]}
    errors = []
    warnings = []

    # 1. Verificar edges
    for e in d.get("edges", []):
        if e["source"] not in nodes:
            errors.append(f"Edge source inexistente: {e['source']}")
        if e["target"] not in nodes:
            errors.append(f"Edge target inexistente: {e['target']}")
        expected_id = f"e-{e['source']}-{e['target']}"
        if e["id"] != expected_id:
            errors.append(f"Edge ID invalido: {e['id']} (esperado: {expected_id})")

    # 2. Verificar linkIds em condicionais
    for node in d["nodes"]:
        for cond in node["data"].get("condicionais", []):
            link_id = cond.get("linkId", "")
            if link_id and link_id not in nodes:
                errors.append(f"linkId inexistente: {link_id} em {node['id']}")

    # 3. Verificar unicidade de iids
    iids = []
    for node in d["nodes"]:
        cdn = node["data"].get("condutaDataNode") or node["data"].get("conduta") or {}
        for section in ["exame", "exames", "orientacao", "encaminhamento", "encaminhamentos", "medicamento", "mensagem"]:
            for item in cdn.get(section, []):
                iid = item.get("iid") or item.get("id", "")
                if iid:
                    iids.append(iid)

    dups = {i: c for i, c in Counter(iids).items() if c > 1}
    if dups:
        errors.append(f"IIDs duplicados: {dups}")

    # 4. Verificar posicionamento
    for node in d["nodes"]:
        pos = node.get("position", {})
        x = pos.get("x", 0)
        if x > 0 and x % 900 != 0:
            warnings.append(f"Posicao x={x} nao e multiplo de 900: {node['id']}")

    # 5. Verificar conduta sem condicao
    conduta_sem_cond = 0
    for node in d["nodes"]:
        cdn = node["data"].get("condutaDataNode") or node["data"].get("conduta") or {}
        for section in ["exame", "exames", "orientacao", "encaminhamento", "encaminhamentos", "medicamento", "mensagem"]:
            for item in cdn.get(section, []):
                cond = item.get("condicao", "") or item.get("condicional", "")
                if not cond or not str(cond).strip():
                    conduta_sem_cond += 1

    if conduta_sem_cond:
        warnings.append(f"Itens de conduta sem condicao: {conduta_sem_cond}")

    # Resultado
    print(f"Arquivo: {filepath}")
    print(f"Nodes: {len(d['nodes'])}  |  Edges: {len(d.get('edges', []))}  |  IIDs: {len(iids)}")
    print()

    if errors:
        print(f"ERROS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    else:
        print("Erros: 0")

    if warnings:
        print(f"\nAVISOS ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")

    print()
    if not errors:
        print("✓ JSON estruturalmente valido")
    else:
        print("✗ JSON com erros estruturais")

    return len(errors) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_json.py <caminho_do_json>")
        sys.exit(1)

    filepath = sys.argv[1]
    success = validate(filepath)
    sys.exit(0 if success else 1)
