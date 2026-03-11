#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_v070_to_v080.py -- session_029: Merge do Gestor
v0.7.0 -> v0.8.0

Aplica mudanças arquiteturais e de enxugamento do gestor sobre a base v0.7.0.
Preserva 100% da camada sindrômica (clinicalExpressions, OR conservador em medicamentos).

GRUPO A  — Reforma arquitetural (fluxo único médico)
  A1: Remover nó conduta-a9ccd9ee (Conduta — Enfermagem)
  A2: Remover 2 edges conectadas ao nó removido
  A3: Criar nova edge node-03 → node-04 (passagem direta)
  A4: Atualizar condicionais de node-psiq-03-anamnese (linkId)
  A5: Renomear 6 labels de nós

GRUPO B  — Enxugamento da conduta
  B1: Remover 3 orientações ao paciente
  B2: Remover 4 encaminhamentos (CAPS II, CAPS-AD, SAMU, Medicina do Trabalho)
  B3: Remover 1 mensagem (GATE P0 — RISCO INTERMEDIÁRIO: SPI)

GRUPO C  — Atualizar título pergunta exames_recentes

GRUPO D  — Merge mensagens de gravidez (GESTANTE valproato + lítio → 1 mensagem)

GRUPO E  — Limpeza de mensagens
  E1: Renomear nomes com acentos incorretos/faltantes
  E2: Remover/substituir referências CAPS/SAMU no conteúdo

GRUPO F  — Nova varredura de acentos (v0.8.0)
"""

import json
import io
import sys
from pathlib import Path

# Fix Windows console encoding
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass

REPO_ROOT   = Path(__file__).resolve().parent.parent
INPUT_FILE  = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.7.0.json"
OUTPUT_FILE = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.8.0.json"


# ===================================================================
# GRUPO A — Constantes de arquitetura
# ===================================================================

NODE_CONDUTA_ENFERMA = "conduta-a9ccd9ee-4962-4bf2-ae6a-a0f4fef7d7d9"
NODE_TRIAGEM_INIT    = "20e05d57-3dfa-43cb-b039-74279162a73a"
NODE_GATE_P0         = "node-psiq-02-gate-p0"
NODE_ANAMNESE        = "node-psiq-03-anamnese"
NODE_DIAGNOSTICO     = "node-psiq-04-diagnostico"
NODE_FARMACOS        = "node-psiq-05-farmacos"
NODE_CONDUTA         = "node-psiq-06-conduta"

EDGES_TO_REMOVE = {
    "e-node-psiq-03-anamnese-conduta-a9ccd9ee-4962-4bf2-ae6a-a0f4fef7d7d9",
    "e-conduta-a9ccd9ee-4962-4bf2-ae6a-a0f4fef7d7d9-node-psiq-04-diagnostico",
}

NEW_EDGE = {
    "id": "e-node-psiq-03-anamnese-node-psiq-04-diagnostico",
    "source": "node-psiq-03-anamnese",
    "target": "node-psiq-04-diagnostico",
    "data": {},
}

NODE_LABEL_UPDATES = {
    NODE_TRIAGEM_INIT: "Avalia\u00e7\u00e3o inicial",
    NODE_GATE_P0:      "Avalia\u00e7\u00e3o de risco de auto exterm\u00ednio",
    NODE_ANAMNESE:     "Antecedentes",
    NODE_DIAGNOSTICO:  "Fluxo de seguimento",
    NODE_FARMACOS:     "Contexto adicional e f\u00e1rmacos",
    NODE_CONDUTA:      "Conduta",
}


# ===================================================================
# GRUPO B — Remoções
# ===================================================================

ORIENTS_TO_REMOVE = {
    "047563fa-1333-45d9-9d95-173d5d6e8179",   # Sobre seu diagnóstico
    "a38db3ca-2767-49bd-bb7f-f9e4e33c8515",   # Sobre seus medicamentos
    "orient-investigacao-001",                  # Quadro em avaliação
}

ENCAMINHAMENTOS_TO_REMOVE = {
    "260889e2-fa7b-405f-9e28-3d6c6237bc1a",   # CAPS II
    "cd8fa3e9-8df4-424e-a196-a0297df74155",   # CAPS-AD
    "a86867c6-ab7b-44c7-a1c8-b958298c42e8",   # Emergência / SAMU 192
    "8806bb9f-9057-49a4-ac43-fb9ee7dffb8e",   # Medicina do Trabalho
}

MSG_TO_REMOVE_PREFIX = "3f15ec15"   # GATE P0 — RISCO INTERMEDIÁRIO: SPI


# ===================================================================
# GRUPO C — exames_recentes
# ===================================================================

EXAMES_RECENTES_UID = "exames_recentes"
EXAMES_RECENTES_TITULO_OLD = "<p><strong>Exames laboratoriais recentes:</strong></p>"
EXAMES_RECENTES_TITULO_NEW = "<p><strong>Trouxe exames para avalia\u00e7\u00e3o?</strong></p>"


# ===================================================================
# GRUPO D — Merge GESTANTE
# ===================================================================

MSG_GESTANTE_VALP_PREFIX  = "8911c614"
MSG_GESTANTE_LITIO_PREFIX = "977efeee"
GESTANTE_MERGED_NOME  = "GESTANTE + PSICOTR\u00d3PICO \u2014 Revis\u00e3o urgente"
GESTANTE_MERGED_COND  = "gestante is True and selected_any(medicamentos_em_uso, 'valproato', 'litio')"


# ===================================================================
# GRUPO E — Limpeza de mensagens
# ===================================================================

MSG_NOME_UPDATES = {
    "fa6a2d13": "URG\u00caNCIA \u2014 MANIA GRAVE COM AGITA\u00c7\u00c3O/PSICOSE",
    "6a2c7758": "MANIA / HIPOMANIA \u2014 Avaliar interna\u00e7\u00e3o se epis\u00f3dio man\u00edaco grave",
    "9245499b": "SUBST\u00c2NCIA COMO CAUSA PRIM\u00c1RIA \u2014 tratar depend\u00eancia antes de psicof\u00e1rmaco",
}

# Substituições específicas de CAPS/SAMU no conteúdo (por ID-prefix)
MSG_CONTENT_FIXES = {
    "72743c14": [
        # Remove sentença "Considerar CAPS-II se sem recursos ambulatoriais."
        (" Considerar CAPS-II se sem recursos ambulatoriais.", ""),
        ("Considerar CAPS-II se sem recursos ambulatoriais.", ""),
    ],
    "fa6a2d13": [
        # Substituir SAMU 192 por encaminhar genérico
        (
            "Contatar SAMU 192 ou encaminhar a servico de urgencia psiquiatrica.",
            "Encaminhar para servi\u00e7o de urg\u00eancia psiqui\u00e1trica.",
        ),
    ],
    "9245499b": [
        # Substituir CAPS-AD + "ou programa especializado" por serviço único
        (
            "CAPS-AD ou programa especializado de depend\u00eancia",
            "servi\u00e7o especializado em depend\u00eancia qu\u00edmica",
        ),
        # fallback: substituição simples caso a frase acima não bata exatamente
        ("CAPS-AD", "servi\u00e7o especializado em depend\u00eancia qu\u00edmica"),
    ],
    "837ff5cb": [
        # Remover bullet CAPS II (texto exato do v0.7.0)
        (
            "<br>\u2022 Considerar CAPS II para manejo ambulatorial intensivo se quadro complexo.",
            "",
        ),
        # fallback sem bullet unicode
        (
            "<br>• Considerar CAPS II para manejo ambulatorial intensivo se quadro complexo.",
            "",
        ),
        # fallback sem tag <br>
        (
            " Considerar CAPS II para manejo ambulatorial intensivo se quadro complexo.",
            "",
        ),
    ],
    "960df136": [
        # Substituir "Acionar SAMU 192 se risco..." (texto exato do v0.7.0, sem acentos)
        (
            "Acionar SAMU 192 se risco imediato e incontrolavel.",
            "Contatar servi\u00e7o de emerg\u00eancia se risco imediato e incontrol\u00e1vel.",
        ),
    ],
    "264c5116": [
        # Substituir cabeçalho SAMU/UPA
        (
            "Acionar SAMU 192 / encaminhar UPA imediatamente.",
            "Encaminhar para urg\u00eancia psiqui\u00e1trica imediatamente.",
        ),
    ],
    "03f6c30b": [
        # Substituir CAPS-AD
        ("encaminhar para CAPS-AD.", "encaminhar para servi\u00e7o especializado em depend\u00eancia qu\u00edmica."),
        ("CAPS-AD", "servi\u00e7o especializado em depend\u00eancia qu\u00edmica"),
    ],
}


# ===================================================================
# GRUPO F — Accent substitutions (campos de display apenas)
# Aplicar F1 (específico) antes de F2 (geral) para evitar double-replace
# ===================================================================

TARGET_DISPLAY_FIELDS = {"titulo", "descricao", "label", "nome", "conteudo", "narrativa"}

ACCENT_FIXES = [
    # ---- F1: typos / posição errada de acento ----
    ("cans\u00e1\u00e7o",       "cansa\u00e7o"),         # cansáço → cansaço
    ("heteroagressa\u00e3o",   "heteroagress\u00e3o"),   # heteroagressaão → heteroagressão (extra 'a' antes de ã)
    ("absti\u00eancia",         "abstin\u00eancia"),      # "abstiência" (typo s/ 'n') → "abstinência"
    ("abstinencia",             "abstin\u00eancia"),      # "abstinencia" (s/ acento) → "abstinência"
    ("Esforcxos",               "Esfor\u00e7os"),         # typo
    ("freneticos",              "fren\u00e9ticos"),
    # ---- F2: palavras sem acento novas em v0.8.0 ----
    ("internacao",              "interna\u00e7\u00e3o"),
    ("Internacao",              "Interna\u00e7\u00e3o"),
    ("psicotico",               "psic\u00f3tico"),
    ("Psicotico",               "Psic\u00f3tico"),
    ("maniaco",                 "man\u00edaco"),
    ("Maniaco",                 "Man\u00edaco"),
    ("agitacao",                "agita\u00e7\u00e3o"),
    ("Agitacao",                "Agita\u00e7\u00e3o"),
    ("dependencia",             "depend\u00eancia"),
    ("Dependencia",             "Depend\u00eancia"),
    ("funcao",                  "fun\u00e7\u00e3o"),
    ("erosao",                  "eros\u00e3o"),
    ("dentaria",                "dent\u00e1ria"),
    ("convulsoes",              "convuls\u00f5es"),
    ("notificacao",             "notifica\u00e7\u00e3o"),
    ("Notificacao",             "Notifica\u00e7\u00e3o"),
    ("involuntaria",            "involunt\u00e1ria"),
    ("incontrolavel",           "incontrol\u00e1vel"),
    ("seguranca",               "seguran\u00e7a"),
    ("servico",                 "servi\u00e7o"),
    ("Servico",                 "Servi\u00e7o"),
    ("fisicos",                 "f\u00edsicos"),
    ("psicofarmaco",            "psicof\u00e1rmaco"),
    ("Psicofarmaco",            "Psicof\u00e1rmaco"),
    ("diagnostico",             "diagn\u00f3stico"),
    ("Diagnostico",             "Diagn\u00f3stico"),
    ("ambulatorio",             "ambulat\u00f3rio"),
    ("Ambulatorio",             "Ambulat\u00f3rio"),
    ("apos ",                   "ap\u00f3s "),
    ("intervencao",             "interven\u00e7\u00e3o"),
    ("criterio",                "crit\u00e9rio"),
    ("urgencia",                "urg\u00eancia"),
    ("Urgencia",                "Urg\u00eancia"),
    ("clinico",                 "cl\u00ednico"),
    ("Clinico",                 "Cl\u00ednico"),
    ("policia",                 "pol\u00edcia"),
    ("Policia",                 "Pol\u00edcia"),
    ("obrigatorio",             "obrigat\u00f3rio"),
    ("Obrigatorio",             "Obrigat\u00f3rio"),
    ("prontuario",              "prontu\u00e1rio"),
    ("Prontuario",              "Prontu\u00e1rio"),
    ("vitima",                  "v\u00edtima"),
    ("Vitima",                  "V\u00edtima"),
    ("protecao",                "prote\u00e7\u00e3o"),
    ("Protecao",                "Prote\u00e7\u00e3o"),
    ("emerg\u00eancia",         "emerg\u00eancia"),  # idempotência
    ("emergencia",              "emerg\u00eancia"),
    ("Emergencia",              "Emerg\u00eancia"),
]


# ===================================================================
# Helpers
# ===================================================================

def get_data(node):
    """Retorna o dict 'data' de um nó."""
    return node.get("data") or {}


def find_node(data, node_id):
    for nd in data.get("nodes", []):
        if nd.get("id") == node_id:
            return nd
    return None


def find_msg_and_container(data, id_prefix):
    """
    Encontra mensagem por prefixo de ID e seu array container.
    Busca em data.condutaDataNode.mensagem (campo singular) e data.mensagem de cada nó.
    """
    for nd in data.get("nodes", []):
        nd_data = get_data(nd)
        # Path 1: data.condutaDataNode.mensagem (campo principal em nós de conduta)
        cdn = nd_data.get("condutaDataNode")
        if isinstance(cdn, dict):
            msgs = cdn.get("mensagem", [])
            if isinstance(msgs, list):
                for msg in msgs:
                    if msg.get("id", "").startswith(id_prefix):
                        return msg, msgs
        # Path 2: data.mensagem direto (fallback para outros tipos de nó)
        msgs2 = nd_data.get("mensagem")
        if isinstance(msgs2, list):
            for msg in msgs2:
                if msg.get("id", "").startswith(id_prefix):
                    return msg, msgs2
        # Path 3: data.mensagens (fallback plural)
        msgs3 = nd_data.get("mensagens")
        if isinstance(msgs3, list):
            for msg in msgs3:
                if msg.get("id", "").startswith(id_prefix):
                    return msg, msgs3
    return None, None


def apply_accent_fixes(obj, changes_log):
    """Aplica correções de acento APENAS em campos TARGET_DISPLAY_FIELDS."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in TARGET_DISPLAY_FIELDS and isinstance(value, str):
                new_value = value
                for old, new in ACCENT_FIXES:
                    new_value = new_value.replace(old, new)
                if new_value != value:
                    obj[key] = new_value
                    changes_log.append(f"[F] campo={key}: acento corrigido")
            elif isinstance(value, (dict, list)):
                apply_accent_fixes(value, changes_log)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                apply_accent_fixes(item, changes_log)


# ===================================================================
# Main
# ===================================================================

def main():
    if not INPUT_FILE.exists():
        print(f"ERRO: arquivo nao encontrado: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    changes = []

    # -------------------------------------------------------------------
    # GRUPO A — Reforma arquitetural
    # -------------------------------------------------------------------

    # A1: Remover nó conduta-a9ccd9ee
    original_nodes = data.get("nodes", [])
    data["nodes"] = [nd for nd in original_nodes if nd.get("id") != NODE_CONDUTA_ENFERMA]
    removed_nodes = len(original_nodes) - len(data["nodes"])
    if removed_nodes > 0:
        changes.append(f"[A1] No {NODE_CONDUTA_ENFERMA} removido")
        print(f"GRUPO A1: no conduta-enfermagem removido ({removed_nodes} no(s))")
    else:
        print(f"AVISO A1: no {NODE_CONDUTA_ENFERMA} nao encontrado (ja removido?)")

    # A2: Remover edges da conduta-enfermagem
    original_edges = data.get("edges", [])
    data["edges"] = [e for e in original_edges if e.get("id") not in EDGES_TO_REMOVE]
    removed_edges = len(original_edges) - len(data["edges"])
    changes.append(f"[A2] {removed_edges} edge(s) removida(s)")
    print(f"GRUPO A2: {removed_edges} edges removidas (esperado 2)")

    # A3: Adicionar nova edge node-03 → node-04
    existing_edge_ids = {e.get("id") for e in data["edges"]}
    if NEW_EDGE["id"] not in existing_edge_ids:
        data["edges"].append(NEW_EDGE)
        changes.append(f"[A3] Edge {NEW_EDGE['id']}: adicionada")
        print("GRUPO A3: nova edge node-03→node-04 adicionada")
    else:
        print("GRUPO A3: edge ja existe (idempotente)")

    # A4: Atualizar condicionais de node-psiq-03-anamnese
    anamnese_node = find_node(data, NODE_ANAMNESE)
    a4_count = 0
    if anamnese_node:
        conds = get_data(anamnese_node).get("condicionais", [])
        for cond in conds:
            if cond.get("linkId") == NODE_CONDUTA_ENFERMA:
                cond["linkId"] = NODE_DIAGNOSTICO
                changes.append(
                    f"[A4] condicionais.linkId: '{NODE_CONDUTA_ENFERMA}' -> '{NODE_DIAGNOSTICO}'"
                )
                a4_count += 1
    print(f"GRUPO A4: {a4_count} condicionais atualizados")

    # A5: Renomear labels dos nós
    a5_count = 0
    for nd in data.get("nodes", []):
        nd_id = nd.get("id")
        if nd_id not in NODE_LABEL_UPDATES:
            continue
        new_label = NODE_LABEL_UPDATES[nd_id]
        nd_data = get_data(nd)
        old_label = nd_data.get("label", "")
        if old_label != new_label:
            nd_data["label"] = new_label
            changes.append(f"[A5] {nd_id} label: '{old_label}' -> '{new_label}'")
            a5_count += 1
        # else: já está correto (idempotente)
    print(f"GRUPO A5: {a5_count}/{len(NODE_LABEL_UPDATES)} labels renomeados")

    # -------------------------------------------------------------------
    # GRUPO B — Enxugamento da conduta
    # -------------------------------------------------------------------
    conduta_node = find_node(data, NODE_CONDUTA)
    if not conduta_node:
        print(f"AVISO GRUPO B: {NODE_CONDUTA} nao encontrado")
    else:
        cd = get_data(conduta_node).get("condutaDataNode") or {}

        # B1: Remover orientações
        orients = cd.get("orientacao", [])
        orig_len_o = len(orients)
        cd["orientacao"] = [o for o in orients if o.get("id") not in ORIENTS_TO_REMOVE]
        removed_o = orig_len_o - len(cd["orientacao"])
        changes.append(f"[B1] {removed_o} orientacao(oes) removida(s)")
        print(f"GRUPO B1: {removed_o} orientacoes removidas (esperado 3, pode ser menos se orient-investigacao-001 nao existia)")

        # B2: Remover encaminhamentos (campo singular: encaminhamento)
        encams = cd.get("encaminhamento", [])
        orig_len_e = len(encams)
        cd["encaminhamento"] = [e for e in encams if e.get("id") not in ENCAMINHAMENTOS_TO_REMOVE]
        removed_enc = orig_len_e - len(cd["encaminhamento"])
        changes.append(f"[B2] {removed_enc} encaminhamento(s) removido(s)")
        print(f"GRUPO B2: {removed_enc} encaminhamentos removidos (esperado 4)")

    # B3: Remover mensagem SPI intermediário
    msg_spi, container_spi = find_msg_and_container(data, MSG_TO_REMOVE_PREFIX)
    if msg_spi and container_spi:
        container_spi.remove(msg_spi)
        changes.append(f"[B3] Mensagem {MSG_TO_REMOVE_PREFIX} (RISCO INTERMEDIARIO SPI) removida")
        print("GRUPO B3: mensagem SPI intermediario removida")
    else:
        print(f"AVISO B3: mensagem {MSG_TO_REMOVE_PREFIX} nao encontrada")

    # -------------------------------------------------------------------
    # GRUPO C — Pergunta exames_recentes
    # -------------------------------------------------------------------
    c_done = False
    for nd in data.get("nodes", []):
        for q in get_data(nd).get("questions", []):
            if q.get("uid") == EXAMES_RECENTES_UID:
                old_titulo = q.get("titulo", "")
                if old_titulo == EXAMES_RECENTES_TITULO_OLD:
                    q["titulo"] = EXAMES_RECENTES_TITULO_NEW
                    changes.append("[C] exames_recentes titulo: atualizado")
                    c_done = True
                elif EXAMES_RECENTES_TITULO_NEW in old_titulo:
                    print("GRUPO C: titulo ja atualizado (idempotente)")
                else:
                    print(f"AVISO C: titulo inesperado: {old_titulo[:80]}")
                break
        if c_done:
            break
    print(f"GRUPO C: exames_recentes titulo {'atualizado' if c_done else 'nao alterado'}")

    # -------------------------------------------------------------------
    # GRUPO D — Merge mensagens de gravidez
    # -------------------------------------------------------------------
    msg_valp, container_valp = find_msg_and_container(data, MSG_GESTANTE_VALP_PREFIX)
    msg_litio, container_litio = find_msg_and_container(data, MSG_GESTANTE_LITIO_PREFIX)

    if msg_valp and msg_litio:
        # D1: Atualizar valproato → mensagem unificada
        old_nome_v = msg_valp.get("nome", "")
        old_cond_v = msg_valp.get("condicao", "")

        if old_nome_v != GESTANTE_MERGED_NOME:
            msg_valp["nome"] = GESTANTE_MERGED_NOME
            changes.append(f"[D1] Mensagem {MSG_GESTANTE_VALP_PREFIX} nome: atualizado para PSICOTRÓPICO unificado")

        if "selected_any" not in old_cond_v:
            msg_valp["condicao"] = GESTANTE_MERGED_COND
            changes.append(f"[D1] Mensagem {MSG_GESTANTE_VALP_PREFIX} condicao: expandida para valproato+litio")

        # Merge conteúdo
        litio_conteudo = msg_litio.get("conteudo", "")
        valp_conteudo  = msg_valp.get("conteudo", "")
        if litio_conteudo and "<hr/>" not in valp_conteudo:
            msg_valp["conteudo"] = valp_conteudo + "<hr/>" + litio_conteudo
            changes.append(f"[D1] Mensagem {MSG_GESTANTE_VALP_PREFIX} conteudo: secao lítio mergeada")

        # D2: Remover mensagem lítio standalone
        if msg_litio in container_litio:
            container_litio.remove(msg_litio)
            changes.append(f"[D2] Mensagem {MSG_GESTANTE_LITIO_PREFIX} (lítio standalone) removida")
            print("GRUPO D: GESTANTE messages mergeadas; lítio standalone removido")
        else:
            print("AVISO D2: msg litio nao estava no container esperado")
    elif msg_valp and not msg_litio:
        print(f"AVISO D: mensagem lítio ({MSG_GESTANTE_LITIO_PREFIX}) nao encontrada — sem merge")
    elif not msg_valp:
        print(f"AVISO D: mensagem valproato ({MSG_GESTANTE_VALP_PREFIX}) nao encontrada")

    # -------------------------------------------------------------------
    # GRUPO E — Limpeza de mensagens
    # -------------------------------------------------------------------

    # E1: Renomear nomes
    e_nome_count = 0
    for id_prefix, new_nome in MSG_NOME_UPDATES.items():
        msg, _ = find_msg_and_container(data, id_prefix)
        if msg:
            old_nome = msg.get("nome", "")
            if old_nome != new_nome:
                msg["nome"] = new_nome
                changes.append(f"[E1] Mensagem {id_prefix} nome: atualizado")
                e_nome_count += 1
        else:
            print(f"AVISO E1: mensagem {id_prefix} nao encontrada")
    print(f"GRUPO E1: {e_nome_count}/{len(MSG_NOME_UPDATES)} nomes atualizados")

    # E2: Remoção/substituição de CAPS/SAMU em conteúdo
    e_content_count = 0
    for id_prefix, replacements in MSG_CONTENT_FIXES.items():
        msg, _ = find_msg_and_container(data, id_prefix)
        if msg:
            conteudo = msg.get("conteudo", "")
            new_conteudo = conteudo
            for old_text, new_text in replacements:
                new_conteudo = new_conteudo.replace(old_text, new_text)
            if new_conteudo != conteudo:
                msg["conteudo"] = new_conteudo
                changes.append(f"[E2] Mensagem {id_prefix} conteudo: CAPS/SAMU substituido")
                e_content_count += 1
            else:
                print(f"  INFO E2: mensagem {id_prefix} — nenhuma substituicao necessaria (ja correto ou texto nao encontrado)")
        else:
            print(f"AVISO E2: mensagem {id_prefix} nao encontrada")
    print(f"GRUPO E2: {e_content_count}/{len(MSG_CONTENT_FIXES)} mensagens com conteudo atualizado")

    # -------------------------------------------------------------------
    # GRUPO F — Accent fixes (traversal completo da árvore)
    # -------------------------------------------------------------------
    f_log = []
    apply_accent_fixes(data, f_log)
    changes.extend(f_log)
    print(f"GRUPO F: {len(f_log)} correcoes de acento aplicadas")

    # -------------------------------------------------------------------
    # Version
    # -------------------------------------------------------------------
    if "metadata" in data:
        data["metadata"]["version"] = "0.8.0"
    changes.append("[META] version -> 0.8.0")

    # -------------------------------------------------------------------
    # Write output
    # -------------------------------------------------------------------
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"Total de mudancas aplicadas: {len(changes)}")
    print(f"Output: {OUTPUT_FILE.name}")
    print(f"{'='*60}\n")
    for c in changes:
        try:
            print(f"  {c}")
        except Exception:
            print("  [mudanca com caracteres especiais]")


if __name__ == "__main__":
    main()
