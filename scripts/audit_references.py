#!/usr/bin/env python3
"""Verifica phantom citations e orphaned references no playbook."""
import re, sys

def audit(filepath):
    text = open(filepath, encoding='utf-8').read()
    parts = re.split(r'^#{1,3}\s*Referências', text, flags=re.MULTILINE)
    body = parts[0]
    refs = parts[1] if len(parts) > 1 else ''
    cited = set(int(x) for x in re.findall(r'\[(\d+)\]', body))
    listed = set(int(x) for x in re.findall(r'^(\d+)\.', refs, re.MULTILINE))
    phantom = cited - listed
    orphaned = listed - cited
    holes = set(range(1, max(listed)+1)) - listed if listed else set()
    print(f"Citadas no corpo:  {sorted(cited)}")
    print(f"Listadas:          {sorted(listed)}")
    print(f"PHANTOM:           {sorted(phantom) or 'nenhuma'}")
    print(f"ORPHANED:          {sorted(orphaned) or 'nenhuma'}")
    print(f"BURACOS NA SEQUÊNCIA: {sorted(holes) or 'nenhum'}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audit_references.py <playbook.md>")
        sys.exit(1)
    audit(sys.argv[1])
