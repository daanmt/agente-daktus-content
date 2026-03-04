#!/usr/bin/env python3
"""Valida estrutura do JSON Daktus: edges, linkIds, iids duplicados."""
import json, sys
from collections import Counter

def validate(filepath):
    d = json.load(open(filepath, encoding='utf-8'))
    nodes = {n['id'] for n in d['nodes']}
    errors = []
    
    for e in d['edges']:
        if e['source'] not in nodes:
            errors.append(f"Edge source inexistente: {e['source']}")
        if e['target'] not in nodes:
            errors.append(f"Edge target inexistente: {e['target']}")
        expected_id = f"e-{e['source']}-{e['target']}"
        if e['id'] != expected_id:
            errors.append(f"Edge ID inválido: {e['id']} (esperado: {expected_id})")
    
    for node in d['nodes']:
        for cond in node['data'].get('condicionais', []):
            if cond['linkId'] not in nodes:
                errors.append(f"linkId inexistente: {cond['linkId']} em {node['id']}")
    
    # Verificar unicidade de iid no catálogo de condutas
    iids = []
    for node in d['nodes']:
        if node.get('type') == 'conduct':
            cnd = node['data'].get('condutaDataNode') or {}
            for section in ['exame', 'medicamento', 'encaminhamento', 'mensagem', 'orientacao']:
                for item in cnd.get(section, []):
                    iid = item.get('iid') or item.get('id', '')
                    if iid:
                        iids.append(iid)
    dups = {iid: c for iid, c in Counter(iids).items() if c > 1}
    if dups:
        errors.append(f"IIDs duplicados no catálogo: {dups}")
    
    if errors:
        print("ERROS ENCONTRADOS:")
        for e in errors:
            print(f"  ✗ {e}")
    else:
        print(f"✓ JSON válido — {len(d['nodes'])} nodes, {len(d['edges'])} edges")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_json.py <ficha.json>")
        sys.exit(1)
    validate(sys.argv[1])
