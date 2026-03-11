#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_v061_to_v070.py -- Onda 5: Reforma Sindrômica
v0.6.1 -> v0.7.0

Problema: protocolo pensa sindromicamente mas prescreve baseado em diagnostico_ativo.
Pacientes sem rótulo CID mas com síndrome bem caracterizada ficam sem conduta.

Solução: camada de expressões derivadas de fenótipo no summary node +
expansão OR conservadora em medicamentos/exames/perguntas.

GRUPO X  — Fixes residuais de v0.6.0 não aplicados em v0.6.1
  X2: Adicionar tdah_abuso_substancias_ativo derivado (ausente do v0.6.1)
  (X1 risco_baixo: já correto em v0.6.1; X3 causa_organica: já correto)

GRUPO A  — 20 expressões derivadas de fenótipo e candidatura terapêutica
  A1: 12 fenótipos base (sem dependência cruzada entre si)
  A2: 7 candidatos terapêuticos (referenciam A1)
  A3: 1 agregador sindrome_em_investigacao

GRUPO B  — Expansão da condição de entrada node-psiq-04→node-psiq-05

GRUPO C  — Reforma OR conservador nos medicamentos (node-psiq-06-conduta)
  C1: 11 antidepressivos ISRS/SNRI/outros (OR append)
  C2: 7 medicamentos TDAH (estimulantes: replace; lisdex/atomox: append)
  C3: 3 estabilizadores e antipsicótico (OR append)

GRUPO D  — Exames e perguntas de node-psiq-05-farmacos
  D1: TSH (condição litio/tdm) + depressao_unipolar_provavel / burnout
  D2: Beta-HCG + candidato_estabilizador_mania
  D3: ecg_indicado_psico + candidato_estimulante / isrs
  D4: sintomas_psicoticos_humor + primeiro_episodio / psicose_paranoia
  D5: causa_organica_investigada + candidato_antipsicotico_psicose

GRUPO E  — Reforma de orientações ao paciente (node-psiq-06-conduta)
  E1: Sobre seu diagnóstico → condição expandida
  E2: Sono e rotina → condição expandida
  E3: orient-tab-episodio-001 → condição expandida
  E4: NOVA orient-investigacao-001

GRUPO F  — Varredura abrangente de acentos (campos de display)
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
INPUT_FILE  = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.6.1.json"
OUTPUT_FILE = REPO_ROOT / "especialidades" / "psiquiatria" / "jsons" / "amil-ficha_psiquiatria-v0.7.0.json"

NODE_DIAGNOSTICO  = "node-psiq-04-diagnostico"
NODE_05           = "node-psiq-05-farmacos"
NODE_CONDUTA      = "node-psiq-06-conduta"
SUMMARY_NODE_ID   = "summary-6e3e3703-1337-46f0-8b08-55e814f0f8ef"
EDGE_LINK_NODE05  = "node-psiq-05-farmacos"   # linkId dentro de condicionais


# ===================================================================
# GRUPO X — Fixes residuais
# ===================================================================
TDAH_ABUSO_DERIVED = {
    "id": "expr-tdah-abuso-derivado-001",
    "name": "tdah_abuso_substancias_ativo",
    "expressao": "not('nenhum' in substancias_uso)",
}


# ===================================================================
# GRUPO A — 20 novas expressões derivadas
# Ordenação: folhas primeiro (sem dependência cruzada),
#            derivadas depois (referenciam folhas),
#            agregador por último.
# ===================================================================
NEW_EXPRESSIONS = [
    # ---- A1: Fenótipos base ----
    {
        "id": "expr-bipolar-nd-001",
        "name": "bipolaridade_nao_descartada",
        "expressao": (
            "selected_any(bipolar_rastreio, 'elevacao_humor_previa', 'reducao_sono_sem_fadiga', "
            "'grandiosidade_episodica', 'tab_documentado') or "
            "'reducao_necessidade_sem_fadiga' in perfil_sono"
        ),
    },
    {
        "id": "expr-burnout-tdm-001",
        "name": "burnout_com_tdm_provavel",
        "expressao": (
            "selected_any(burnout_tdm_discriminador, 'anedonia_universal', "
            "'sem_melhora_fora_trabalho', 'culpa_desvalia', "
            "'sem_contexto_ocupacional', 'duracao_criterio_tdm')"
        ),
    },
    {
        "id": "expr-tag-provavel-001",
        "name": "tag_provavel",
        "expressao": "'preocupacao_difusa_persistente' in subtipo_ansioso",
    },
    {
        "id": "expr-panico-provavel-001",
        "name": "panico_provavel",
        "expressao": "'crises_abruptas_esquiva' in subtipo_ansioso",
    },
    {
        "id": "expr-toc-provavel-001",
        "name": "toc_provavel",
        "expressao": "'obsessoes_compulsoes' in subtipo_ansioso",
    },
    {
        "id": "expr-tept-provavel-001",
        "name": "tept_provavel",
        "expressao": "'trauma_intrusao_evitacao' in subtipo_ansioso",
    },
    {
        "id": "expr-fobia-social-001",
        "name": "fobia_social_provavel",
        "expressao": "'medo_avaliacao_social' in subtipo_ansioso",
    },
    {
        "id": "expr-tdah-confirmado-001",
        "name": "tdah_confirmado_operacional",
        "expressao": (
            "selected_any(tdah_discriminador, 'inicio_infancia_confirmado') and "
            "selected_any(tdah_discriminador, 'multiplos_contextos') and "
            "selected_any(tdah_discriminador, 'prejuizo_funcional_claro') and "
            "selected_any(tdah_discriminador, 'sem_explicacao_alternativa') and "
            "selected_any(tdah_discriminador, 'curso_continuo_sem_episodios')"
        ),
    },
    {
        "id": "expr-anorexia-provavel-001",
        "name": "anorexia_provavel",
        "expressao": "'restricao_medo_engordar' in ta_fenotipo",
    },
    {
        "id": "expr-bulimia-provavel-001",
        "name": "bulimia_provavel",
        "expressao": "'compulsao_purgacao' in ta_fenotipo",
    },
    {
        "id": "expr-tcap-provavel-001",
        "name": "tcap_provavel",
        "expressao": "'compulsao_sem_compensacao' in ta_fenotipo",
    },
    # ---- A1 (late leaf — referencia bipolaridade_nao_descartada) ----
    {
        "id": "expr-dep-unipolar-001",
        "name": "depressao_unipolar_provavel",
        "expressao": (
            "selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada', 'depressao_grave') and "
            "not(bipolaridade_nao_descartada is True) and "
            "not('causa_primaria' in substancia_relacao_quadro)"
        ),
    },
    # ---- A2: Candidatos terapêuticos (referenciam A1) ----
    {
        "id": "expr-cand-isrs-dep-001",
        "name": "candidato_isrs_depressao",
        "expressao": (
            "selected_any(diagnostico_ativo, 'tdm', 'distimia') or "
            "(depressao_unipolar_provavel is True) or "
            "(burnout_com_tdm_provavel is True)"
        ),
    },
    {
        "id": "expr-cand-isrs-ans-001",
        "name": "candidato_isrs_ansiedade",
        "expressao": (
            "selected_any(diagnostico_ativo, 'tag', 'panico', 'fobia_social', 'toc', 'tept') or "
            "(tag_provavel is True) or (panico_provavel is True) or "
            "(fobia_social_provavel is True) or (toc_provavel is True) or (tept_provavel is True)"
        ),
    },
    {
        "id": "expr-cand-estab-001",
        "name": "candidato_estabilizador_mania",
        "expressao": (
            "('tab' in diagnostico_ativo) or "
            "selected_any(episodio_atual_humor, 'mania', 'hipomania')"
        ),
    },
    {
        "id": "expr-cand-estimulante-001",
        "name": "candidato_estimulante",
        "expressao": (
            "(('tdah' in diagnostico_ativo) or (tdah_confirmado_operacional is True)) and "
            "('nenhum' in substancias_uso) and "
            "not(bipolaridade_nao_descartada is True)"
        ),
    },
    {
        "id": "expr-cand-atomoxetina-001",
        "name": "candidato_atomoxetina",
        "expressao": "('tdah' in diagnostico_ativo) or (tdah_confirmado_operacional is True)",
    },
    {
        "id": "expr-cand-lisdex-001",
        "name": "candidato_lisdex_tcap",
        "expressao": "('ta_tcap' in diagnostico_ativo) or (tcap_provavel is True)",
    },
    {
        "id": "expr-cand-ap-psicose-001",
        "name": "candidato_antipsicotico_psicose",
        "expressao": (
            "(primeiro_episodio_psicotico is True) or "
            "selected_any(contexto_agressividade, 'psicose_paranoia')"
        ),
    },
    # ---- A3: Agregador (último — múltiplas referências) ----
    {
        "id": "expr-sind-invest-001",
        "name": "sindrome_em_investigacao",
        "expressao": (
            "('sem_diagnostico' in diagnostico_ativo) and "
            "((candidato_isrs_depressao is True) or (candidato_isrs_ansiedade is True) or "
            "(candidato_estimulante is True) or (candidato_estabilizador_mania is True) or "
            "(candidato_antipsicotico_psicose is True))"
        ),
    },
]


# ===================================================================
# GRUPO B — Expansão condição node-04 → node-05
# ===================================================================
EDGE_04_05_APPEND = (
    " or (candidato_isrs_depressao is True)"
    " or (candidato_isrs_ansiedade is True)"
    " or (candidato_estimulante is True)"
    " or (candidato_estabilizador_mania is True)"
    " or (candidato_antipsicotico_psicose is True)"
)
EDGE_04_05_MARKER = "candidato_isrs_depressao"   # idempotência


# ===================================================================
# GRUPO C — Medicamentos
# Formato: nomeMed -> ("replace"|"append", nova_cond | clausula_or)
# ===================================================================
MED_UPDATES = {
    # ---- C1: ISRs/SNRI/outros (OR append) ----
    "Escitalopram 10mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))"
        " or (tag_provavel is True) or (panico_provavel is True)",
    ),
    "Sertralina 50mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))"
        " or (candidato_isrs_ansiedade is True)",
    ),
    "Fluoxetina 20mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))"
        " or (bulimia_provavel is True) or (toc_provavel is True)",
    ),
    "Venlafaxina XR 37,5mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))"
        " or (tag_provavel is True) or (tept_provavel is True)",
    ),
    "Venlafaxina XR 75mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))"
        " or (tag_provavel is True) or (tept_provavel is True)",
    ),
    "Duloxetina 60mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))"
        " or (tag_provavel is True)",
    ),
    "Bupropiona 150mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True)"
        " and not(anorexia_provavel is True) and not(bulimia_provavel is True))",
    ),
    "Bupropiona 300mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True)"
        " and not(anorexia_provavel is True) and not(bulimia_provavel is True))",
    ),
    "Mirtazapina 15mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))",
    ),
    "Mirtazapina 30mg": (
        "append",
        " or ((candidato_isrs_depressao is True) and not(bipolaridade_nao_descartada is True))",
    ),
    "Paroxetina 20mg": (
        "append",
        " or (tept_provavel is True) or (panico_provavel is True) or (fobia_social_provavel is True)",
    ),
    # ---- C2: TDAH (estimulantes: replace; lisdex/atomox: append) ----
    "Metilfenidato 10mg": (
        "replace",
        "('tdah' in diagnostico_ativo or tdah_confirmado_operacional is True)"
        " and 'nenhum' in substancias_uso and not(bipolaridade_nao_descartada is True)",
    ),
    "Concerta LP 18mg": (
        "replace",
        "('tdah' in diagnostico_ativo or tdah_confirmado_operacional is True)"
        " and 'nenhum' in substancias_uso and not(bipolaridade_nao_descartada is True)",
    ),
    "Ritalina LA 10mg": (
        "replace",
        "('tdah' in diagnostico_ativo or tdah_confirmado_operacional is True)"
        " and 'nenhum' in substancias_uso and not(bipolaridade_nao_descartada is True)",
    ),
    "Lisdexanfetamina 30mg": (
        "append",
        " or (tdah_confirmado_operacional is True) or (tcap_provavel is True)",
    ),
    "Lisdexanfetamina 70mg": (
        "append",
        " or (tdah_confirmado_operacional is True) or (tcap_provavel is True)",
    ),
    "Atomoxetina 40mg": (
        "append",
        " or (tdah_confirmado_operacional is True)",
    ),
    "Atomoxetina 80mg": (
        "append",
        " or (tdah_confirmado_operacional is True)",
    ),
    # ---- C3: Estabilizadores e antipsicótico (OR append) ----
    "L\u00edtio 300mg": (
        "append",
        " or (candidato_estabilizador_mania is True)",
    ),
    "Valproato de s\u00f3dio 500mg": (
        "append",
        " or (candidato_estabilizador_mania is True)",
    ),
    "Haloperidol 5mg": (
        "append",
        " or (candidato_antipsicotico_psicose is True)",
    ),
}


# ===================================================================
# GRUPO D — Exames e perguntas
# ===================================================================
TSH_TUSS         = "40316521"
TSH_LITIO_MARKER = "litio"       # distingue o TSH litio/tdm do TSH psicótico
TSH_MARKER_IDMP  = "depressao_unipolar_provavel"  # idempotência
TSH_APPEND       = " or (depressao_unipolar_provavel is True) or (burnout_com_tdm_provavel is True)"

BETAHCG_TUSS     = "40305759"
BETAHCG_MARKER   = "candidato_estabilizador_mania"  # idempotência
BETAHCG_APPEND   = " or (candidato_estabilizador_mania is True)"

# perguntas em node-psiq-05-farmacos: uid -> (marker_idempotencia, clausula_append)
QUESTION_UPDATES = {
    "ecg_indicado_psico": (
        "candidato_estimulante",
        " or (candidato_estimulante is True)"
        " or (candidato_isrs_depressao is True)"
        " or (candidato_isrs_ansiedade is True)",
    ),
    "sintomas_psicoticos_humor": (
        "primeiro_episodio_psicotico",
        " or (primeiro_episodio_psicotico is True)"
        " or selected_any(contexto_agressividade, 'psicose_paranoia')",
    ),
    "causa_organica_investigada": (
        "candidato_antipsicotico_psicose",
        " or (candidato_antipsicotico_psicose is True)",
    ),
}


# ===================================================================
# GRUPO E — Orientações
# Formato: id -> (condicao_antiga, condicao_nova)
# ===================================================================
ORIENT_UPDATES = {
    "047563fa-1333-45d9-9d95-173d5d6e8179": (     # Sobre seu diagnóstico
        "not('sem_diagnostico' in diagnostico_ativo)",
        "not('sem_diagnostico' in diagnostico_ativo) or (sindrome_em_investigacao is True)",
    ),
    "6912d79d-8b00-4283-8d63-a3759f91c734": (     # Sono e rotina
        "not('sem_diagnostico' in diagnostico_ativo)",
        "not('sem_diagnostico' in diagnostico_ativo) or (sindrome_em_investigacao is True)",
    ),
    "orient-tab-episodio-001": (
        "'tab' in diagnostico_ativo",
        "('tab' in diagnostico_ativo) or (bipolaridade_nao_descartada is True)",
    ),
}

NEW_ORIENT_INVESTIGACAO = {
    "id": "orient-investigacao-001",
    "nome": "Quadro em avalia\u00e7\u00e3o \u2014 o que esperar",
    "descricao": "",
    "condicao": "sindrome_em_investigacao is True",
    "conteudo": (
        "<p><strong>Seu quadro est\u00e1 sendo avaliado:</strong></p>"
        "<ul>"
        "<li>H\u00e1 uma s\u00edndrome cl\u00ednica identificada que est\u00e1 sendo investigada. "
        "O m\u00e9dico pode solicitar exames ou iniciar um tratamento enquanto o diagn\u00f3stico "
        "\u00e9 refinado.</li>"
        "<li><strong>N\u00e3o ajuste nem interrompa nenhuma medica\u00e7\u00e3o por conta pr\u00f3pria</strong> "
        "\u2014 mudan\u00e7as sem orienta\u00e7\u00e3o podem mascarar sintomas ou causar efeitos indesejados.</li>"
        "<li>Anote qualquer mudan\u00e7a nos sintomas (melhora, piora ou sintomas novos) "
        "para relatar no pr\u00f3ximo retorno.</li>"
        "<li><strong>Sinais de alerta \u2014 busque atendimento antes do retorno:</strong> "
        "piora s\u00fabita do humor, pensamentos de se machucar, agita\u00e7\u00e3o intensa "
        "ou confus\u00e3o mental.</li>"
        "</ul>"
    ),
}


# ===================================================================
# GRUPO F — Accent substitutions (campos de display apenas)
# Aplicar F1 (específico) antes de F2 (geral) para evitar double-replace
# ===================================================================
TARGET_DISPLAY_FIELDS = {"titulo", "descricao", "label", "nome", "conteudo", "narrativa"}

ACCENT_FIXES = [
    # ---- F1: contextos específicos primeiro ----
    ("feicoes presentes",                          "fei\u00e7\u00f5es presentes"),
    ("Risco de heteroagressao",                    "Risco de heteroagressa\u00e3o"),
    ("Relacao entre",                              "Rela\u00e7\u00e3o entre"),
    ("sem relacao causal",                         "sem rela\u00e7\u00e3o causal"),
    ("sem relacao clara",                          "sem rela\u00e7\u00e3o clara"),
    ("Automedicacao \u2014",                       "Automedica\u00e7\u00e3o \u2014"),
    ("a substancia para",                          "a subst\u00e2ncia para"),
    ("idealizacao / desvalorizacao",               "idealiza\u00e7\u00e3o / desvaloriza\u00e7\u00e3o"),
    ("instaveis (idealizacao",                     "inst\u00e1veis (idealiza\u00e7\u00e3o"),
    ("Validacao de criterios",                     "Valida\u00e7\u00e3o de crit\u00e9rios"),
    ("desde a infancia (antes",                    "desde a inf\u00e2ncia (antes"),
    ("Nao explicados por",                         "N\u00e3o explicados por"),
    ("privacao de sono",                           "priva\u00e7\u00e3o de sono"),
    ("continuos desde a infancia",                 "cont\u00ednuos desde a inf\u00e2ncia"),
    ("periodos de aceleracao",                     "per\u00edodos de acelera\u00e7\u00e3o"),
    ("Prejuizo funcional",                         "Preju\u00edzo funcional"),
    ("nivel de suporte necessario",                "n\u00edvel de suporte necess\u00e1rio"),
    ("Nivel 1 \u2014",                             "N\u00edvel 1 \u2014"),
    ("Nivel 2 \u2014",                             "N\u00edvel 2 \u2014"),
    ("Nivel 3 \u2014",                             "N\u00edvel 3 \u2014"),
    ("dificuldade em interacoes",                  "dificuldade em intera\u00e7\u00f5es"),
    ("deficits graves em comunicacao",             "d\u00e9ficits graves em comunica\u00e7\u00e3o"),
    ("Aplicavel quando TEA nao esta",              "Aplic\u00e1vel quando TEA n\u00e3o est\u00e1"),
    ("hipotese a investigar",                      "hip\u00f3tese a investigar"),
    ("inferir intencoes, emocoes",                 "inferir inten\u00e7\u00f5es, emo\u00e7\u00f5es"),
    ("Comunicacao predominantemente",              "Comunica\u00e7\u00e3o predominantemente"),
    ("angustia frente a mudancas",                 "ang\u00fastia frente a mudan\u00e7as"),
    (
        "padrao predominante. Permite construcao diagnostica antes do rotulo formal",
        "padr\u00e3o predominante. Permite constru\u00e7\u00e3o diagn\u00f3stica antes do r\u00f3tulo formal",
    ),
    (
        "Restricao alimentar / baixo peso com medo intenso de engordar ou distorcao corporal",
        "Restri\u00e7\u00e3o alimentar / baixo peso com medo intenso de engordar ou distor\u00e7\u00e3o corporal",
    ),
    (
        "compulsao seguidos de vomito, laxantes ou exercicio compensatorio",
        "compuls\u00e3o seguidos de v\u00f4mito, laxantes ou exerc\u00edcio compensat\u00f3rio",
    ),
    (
        "Inapetencia ou perda de peso sem medo de engordar nem distorcao corporal",
        "Inapet\u00eancia ou perda de peso sem medo de engordar nem distor\u00e7\u00e3o corporal",
    ),
    (
        "Confusao mental / torpor / sonolencia desproporcional",
        "Confus\u00e3o mental / torpor / son\u00f4lencia desproporcional",
    ),
    ("Nausea / vomito / dor abdominal",            "N\u00e1usea / v\u00f4mito / dor abdominal"),
    ("Sedacao excessiva",                          "Seda\u00e7\u00e3o excessiva"),
    ("Nao dispensar",                              "N\u00e3o dispensar"),
    ("Nao manejar",                                "N\u00e3o manejar"),
    ("Causa primaria \u2014",                      "Causa prim\u00e1ria \u2014"),
    ("areas com potencial",                        "\u00e1reas com potencial"),
    ("ansiedade intensa e episodica",              "ansiedade intensa e epis\u00f3dica"),
    # ---- F2: substituições mais gerais (após F1) ----
    ("feicoes",          "fei\u00e7\u00f5es"),
    ("relacao",          "rela\u00e7\u00e3o"),
    ("abstinencia",      "absti\u00eancia"),
    ("automedicacao",    "automedica\u00e7\u00e3o"),
    ("instaveis",        "inst\u00e1veis"),
    ("infancia",         "inf\u00e2ncia"),
    ("continuos",        "cont\u00ednuos"),
    ("aceleracao",       "acelera\u00e7\u00e3o"),
    ("periodos",         "per\u00edodos"),
    ("necessario",       "necess\u00e1rio"),
    ("interacoes",       "intera\u00e7\u00f5es"),
    ("deficits",         "d\u00e9ficits"),
    ("comunicacao",      "comunica\u00e7\u00e3o"),
    ("hipotese",         "hip\u00f3tese"),
    ("intencoes",        "inten\u00e7\u00f5es"),
    ("emocoes",          "emo\u00e7\u00f5es"),
    ("mudancas",         "mudan\u00e7as"),
    ("angustia",         "ang\u00fastia"),
    ("heteroagressao",   "heteroagressa\u00e3o"),
    ("padrao",           "padr\u00e3o"),
    ("construcao",       "constru\u00e7\u00e3o"),
    ("rotulo",           "r\u00f3tulo"),
    ("distorcao",        "distor\u00e7\u00e3o"),
    ("compulsao",        "compuls\u00e3o"),
    ("vomito",           "v\u00f4mito"),
    ("exercicio",        "exerc\u00edcio"),
    ("compensatorio",    "compensat\u00f3rio"),
    ("inapetencia",      "inapet\u00eancia"),
    ("sonolencia",       "son\u00f4lencia"),
    ("sedacao",          "seda\u00e7\u00e3o"),
    ("direcao",          "dire\u00e7\u00e3o"),
    ("Validacao",        "Valida\u00e7\u00e3o"),
    ("Prejuizo",         "Preju\u00edzo"),
    ("Aplicavel",        "Aplic\u00e1vel"),
    ("Restricao",        "Restri\u00e7\u00e3o"),
    ("Episodios",        "Epis\u00f3dios"),
    ("idealizacao",      "idealiza\u00e7\u00e3o"),
    ("desvalorizacao",   "desvaloriza\u00e7\u00e3o"),
    ("Nivel ",           "N\u00edvel "),
    ("Nao ",             "N\u00e3o "),
]


# ===================================================================
# Helpers
# ===================================================================

def get_data(node):
    """Retorna o dict 'data' de um nó (todo conteúdo está em node['data'])."""
    return node.get("data") or {}


def find_node(data, node_id):
    for nd in data.get("nodes", []):
        if nd.get("id") == node_id:
            return nd
    return None


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
    # GRUPO X — Fixes residuais (X2: tdah_abuso derivado)
    # -------------------------------------------------------------------
    summary_node = find_node(data, SUMMARY_NODE_ID)
    summary_data = get_data(summary_node) if summary_node else {}

    if not summary_node:
        print(f"AVISO: no summary nao encontrado: {SUMMARY_NODE_ID}")
    else:
        exprs = summary_data.get("clinicalExpressions")
        if exprs is None:
            summary_data["clinicalExpressions"] = []
            exprs = summary_data["clinicalExpressions"]

        existing_names = {e.get("name") for e in exprs}

        x2_done = False
        if TDAH_ABUSO_DERIVED["name"] not in existing_names:
            exprs.append(TDAH_ABUSO_DERIVED)
            existing_names.add(TDAH_ABUSO_DERIVED["name"])
            changes.append("[X2] tdah_abuso_substancias_ativo: expressao derivada adicionada")
            x2_done = True

    print(f"GRUPO X2: tdah_abuso_derivado {'adicionado' if x2_done else 'ja existia (ignorado)'}")

    # -------------------------------------------------------------------
    # GRUPO A — 20 novas expressões derivadas
    # -------------------------------------------------------------------
    a_count = 0
    if summary_node and summary_data:
        exprs = summary_data.get("clinicalExpressions", [])
        existing_names = {e.get("name") for e in exprs}
        for expr in NEW_EXPRESSIONS:
            if expr["name"] not in existing_names:
                exprs.append(expr)
                existing_names.add(expr["name"])
                changes.append(f"[A] expr {expr['name']}: adicionada")
                a_count += 1
            else:
                print(f"  AVISO GRUPO A: {expr['name']} ja existe, ignorado")

    print(f"GRUPO A: {a_count}/{len(NEW_EXPRESSIONS)} expressoes adicionadas")

    # -------------------------------------------------------------------
    # GRUPO B — Expansão condição node-04 → node-05
    # -------------------------------------------------------------------
    b_done = False
    diag_node = find_node(data, NODE_DIAGNOSTICO)
    if diag_node:
        conds = get_data(diag_node).get("condicionais", [])
        for cond_obj in conds:
            if cond_obj.get("linkId") == EDGE_LINK_NODE05:
                old_cond = cond_obj.get("condicao", "")
                if EDGE_04_05_MARKER not in old_cond:
                    cond_obj["condicao"] = old_cond + EDGE_04_05_APPEND
                    changes.append("[B] condicao node-04->node-05: 5 clausulas OR adicionadas")
                    b_done = True
                else:
                    print("GRUPO B: condicao ja atualizada (ignorado)")
                break
    else:
        print(f"AVISO GRUPO B: {NODE_DIAGNOSTICO} nao encontrado")

    print(f"GRUPO B: {'condicao expandida' if b_done else 'nao alterada'}")

    # -------------------------------------------------------------------
    # GRUPO C — Medicamentos (node-psiq-06-conduta)
    # -------------------------------------------------------------------
    c_count = 0
    conduta_node = find_node(data, NODE_CONDUTA)
    if not conduta_node:
        print(f"AVISO GRUPO C: {NODE_CONDUTA} nao encontrado")
    else:
        cd = get_data(conduta_node).get("condutaDataNode") or {}
        for med in cd.get("medicamento", []):
            nome = med.get("nomeMed", "")
            if nome not in MED_UPDATES:
                continue
            action, value = MED_UPDATES[nome]
            old_cond = med.get("condicao", "")

            if action == "replace":
                if old_cond != value:
                    med["condicao"] = value
                    changes.append(f"[C] {nome}: condicao substituida")
                    c_count += 1

            elif action == "append":
                marker = value.strip()[:40]
                if marker not in old_cond:
                    med["condicao"] = old_cond + value
                    changes.append(f"[C] {nome}: OR clinico adicionado")
                    c_count += 1

    print(f"GRUPO C: {c_count} medicamentos atualizados (esperado ~22 contando Lisdex 2x)")

    # -------------------------------------------------------------------
    # GRUPO D — Exames e perguntas
    # -------------------------------------------------------------------
    d_count = 0

    # D1: TSH com condição litio/tdm (distinguir dos 2 TSH pelo marcador)
    if conduta_node:
        cd = get_data(conduta_node).get("condutaDataNode") or {}
        for exam in cd.get("exame", []):
            cod_list = exam.get("codigo", [])
            if not cod_list or cod_list[0].get("codigo") != TSH_TUSS:
                continue
            cond = exam.get("condicao", "")
            if TSH_LITIO_MARKER in cond and TSH_MARKER_IDMP not in cond:
                exam["condicao"] = cond + TSH_APPEND
                changes.append("[D1] TSH (litio/tdm): condicao expandida com depressao_unipolar")
                d_count += 1

    # D2: Beta-HCG
    if conduta_node:
        cd = get_data(conduta_node).get("condutaDataNode") or {}
        for exam in cd.get("exame", []):
            cod_list = exam.get("codigo", [])
            if not cod_list or cod_list[0].get("codigo") != BETAHCG_TUSS:
                continue
            cond = exam.get("condicao", "")
            if BETAHCG_MARKER not in cond:
                exam["condicao"] = cond + BETAHCG_APPEND
                changes.append("[D2] Beta-HCG: condicao expandida com candidato_estabilizador")
                d_count += 1

    # D3–D5: Perguntas em node-psiq-05-farmacos
    node05 = find_node(data, NODE_05)
    if not node05:
        print(f"AVISO GRUPO D: {NODE_05} nao encontrado")
    else:
        for q in get_data(node05).get("questions", []):
            uid = q.get("uid", "")
            if uid not in QUESTION_UPDATES:
                continue
            marker, append_clause = QUESTION_UPDATES[uid]
            old_expr = q.get("expressao", "")
            if marker not in old_expr:
                q["expressao"] = old_expr + append_clause
                changes.append(f"[D] pergunta uid={uid}: expressao expandida")
                d_count += 1

    print(f"GRUPO D: {d_count}/5 exames e perguntas atualizados")

    # -------------------------------------------------------------------
    # GRUPO E — Orientações
    # -------------------------------------------------------------------
    e_count = 0
    if not conduta_node:
        print(f"AVISO GRUPO E: {NODE_CONDUTA} nao encontrado")
    else:
        cd = get_data(conduta_node).get("condutaDataNode") or {}
        orients = cd.get("orientacao", [])
        existing_ids = {o.get("id") for o in orients}

        # E1–E3: atualizar condições existentes
        for orient in orients:
            oid = orient.get("id", "")
            if oid not in ORIENT_UPDATES:
                continue
            old_cond, new_cond = ORIENT_UPDATES[oid]
            current = orient.get("condicao", "")
            if current == old_cond:
                orient["condicao"] = new_cond
                changes.append(f"[E] orient {oid}: condicao expandida")
                e_count += 1
            elif new_cond in current:
                print(f"  AVISO E: orient {oid} ja tem condicao atualizada")
            else:
                print(f"  AVISO E: orient {oid} com condicao inesperada: {current[:60]}")

        # E4: nova orientação
        if NEW_ORIENT_INVESTIGACAO["id"] not in existing_ids:
            orients.append(NEW_ORIENT_INVESTIGACAO)
            changes.append(f"[E] orientacao {NEW_ORIENT_INVESTIGACAO['id']}: adicionada")
            e_count += 1

    print(f"GRUPO E: {e_count}/4 orientacoes atualizadas/adicionadas")

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
        data["metadata"]["version"] = "0.7.0"
    changes.append("[META] version -> 0.7.0")

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
