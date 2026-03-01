#!/usr/bin/env python3
"""
Cria cópia versionada de um arquivo antes de editá-lo.
Uso: python scripts/versionar.py <arquivo_fonte> <pasta_versions>
"""
import sys
import shutil
import os
from datetime import datetime

def versionar(arquivo_fonte, pasta_versions):
    if not os.path.exists(arquivo_fonte):
        print(f"Arquivo não encontrado: {arquivo_fonte}")
        return None
    
    os.makedirs(pasta_versions, exist_ok=True)
    
    # Contar versões existentes deste arquivo
    nome_base = os.path.splitext(os.path.basename(arquivo_fonte))[0]
    ext = os.path.splitext(arquivo_fonte)[1]
    versoes = [f for f in os.listdir(pasta_versions) if f.startswith(nome_base)]
    num_versao = str(len(versoes) + 1).zfill(3)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    nome_versao = f"{nome_base}_v{num_versao}_{timestamp}{ext}"
    destino = os.path.join(pasta_versions, nome_versao)
    
    shutil.copy2(arquivo_fonte, destino)
    print(f"Versão criada: {destino}")
    return destino

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python versionar.py <arquivo> <pasta_versions>")
        sys.exit(1)
    versionar(sys.argv[1], sys.argv[2])
