"""
inject_no6.py — Sessões G-H
Injeta Nó 6 (Conduta) no JSON de psiquiatria.
Conteúdo: 9 alertas, 25 exames, 13 encaminhamentos, 9 medicamentos.
Referência de estrutura: amil-ficha_cardiologia-v2.0.9.json
"""
import json
import uuid

def u():
    return str(uuid.uuid4())

filepath = "especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json"
d = json.load(open(filepath, encoding="utf-8"))


# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────

def mk_exame(nome, condicao, tuss_codigo, cid, indicacao,
             tipo_amostra="Sangue", detalhes="", instrucoes=""):
    codigo = []
    if tuss_codigo:
        codigo = [{"iid": u(), "sistema": "TUSS", "codigo": tuss_codigo, "nome": ""}]
    return {
        "id": u(),
        "nome": nome,
        "descricao": "",
        "condicional": "visivel",
        "condicao": condicao,
        "codigo": codigo,
        "cid": cid,
        "indicacao": indicacao,
        "narrativa": "",
        "codigoTexto": "",
        "categorias": [],
        "detalhesPedido": detalhes,
        "quantidade": 1,
        "tipoAmostra": {"sistema": "", "codigo": "", "nome": "", "texto": tipo_amostra},
        "instrucoesPaciente": instrucoes,
        "guiaSeparada": False,
        "programacaoDosagem": {
            "codigoProgramacao": {"sistema": "", "codigo": "", "nome": "", "texto": ""},
            "numRepeticoes": 0,
            "numRepeticoesMax": 0,
            "duracao": 0,
            "duracaoMax": 0,
            "unidadeTempoDuracao": ""
        },
        "comentarios": ""
    }


def mk_encaminhamento(nome, condicao, indicacao, especialidade_texto, cid=""):
    return {
        "id": u(),
        "nome": nome,
        "descricao": "",
        "condicional": "visivel",
        "condicao": condicao,
        "indicacao": indicacao,
        "cid": cid,
        "narrativa": "",
        "especialidade": [],
        "especialidadeTexto": especialidade_texto,
        "detalhesPedido": "",
        "categorias": []
    }


def mk_medicamento(nome, condicao, posologia, categoria_nome, via="oral", cod_mevo=""):
    codigo = []
    if cod_mevo:
        codigo = [{"iid": u(), "sistema": "MEVO", "codigo": cod_mevo, "nome": ""}]
    return {
        "id": u(),
        "nome": nome,
        "descricao": "",
        "condicional": "visivel",
        "condicao": condicao,
        "condicionalMedicamento": "domiciliar",
        "quantidade": 1,
        "codigo": codigo,
        "nomeMed": nome,
        "posologia": f"<p>{posologia}</p>",
        "mensagemMedico": "",
        "via": via,
        "narrativa": "",
        "categorias": [{"iid": u(), "sistema": "", "codigo": "", "nome": categoria_nome, "texto": ""}]
    }


def mk_alerta(nome, condicao, conteudo):
    return {
        "id": u(),
        "nome": nome,
        "descricao": "",
        "narrativa": "",
        "condicional": "visivel",
        "condicao": condicao,
        "conteudo": conteudo,
        "observacao": ""
    }


# ──────────────────────────────────────────────────────────────────────────────
# 4.1 ALERTAS (mensagem) — 9 itens, em ordem de prioridade clínica
# ──────────────────────────────────────────────────────────────────────────────

alertas = [
    mk_alerta(
        "\u26d4 GATE P0 \u2014 RISCO ALTO: Interna\u00e7\u00e3o indicada",
        "nivel_risco_p0 == 'alto' and internacao_indicada_p0 in ('sim_involuntaria', 'sim_voluntaria')",
        "<p><strong>Acionar SAMU 192 / encaminhar UPA imediatamente.</strong><br>"
        "N\u00e3o deixar paciente sozinho. Notificar familiar (CFM Art. 46). "
        "Iniciar SPI antes do encaminhamento quando poss\u00edvel. "
        "Completar laudo para interna\u00e7\u00e3o involunt\u00e1ria (Lei 10.216/2001, Art. 6). "
        "Notificar MP em 72h (Art. 9).</p>"
    ),
    mk_alerta(
        "\u26a0\ufe0f GATE P0 \u2014 RISCO INTERMEDI\u00c1RIO: SPI obrigat\u00f3rio",
        "nivel_risco_p0 == 'intermediario' and spi_realizado != 'sim'",
        "<p><strong>SPI obrigat\u00f3rio antes de encerrar a consulta.</strong><br>"
        "Retorno intensificado &lt;2 semanas. Acionar suporte familiar. "
        "Documentar n\u00edvel de risco e conduta no prontu\u00e1rio.</p>"
    ),
    mk_alerta(
        "\u26d4 CLOZAPINA \u2014 ANC &lt;1.000: SUSPENDER IMEDIATAMENTE",
        "anc_dentro_limite == 'suspender_menor_1000'",
        "<p><strong>Suspender clozapina imediatamente.</strong><br>"
        "Encaminhar urg\u00eancia hematol\u00f3gica. "
        "Registrar na monitora\u00e7\u00e3o do PGRM (ANVISA). "
        "N\u00e3o reiniciar sem avalia\u00e7\u00e3o especializada.</p>"
    ),
    mk_alerta(
        "\u26a0\ufe0f VPA + MIE \u2014 Aconselhamento pendente",
        "vpa_mie_consentimento == 'nao_pendente_hoje'",
        "<p><strong>Realizar aconselhamento hoje:</strong><br>"
        "Risco de malforma\u00e7\u00f5es maiores ~9% (espinha b\u00edfida, cardiopatia). "
        "Contracep\u00e7\u00e3o eficaz obrigat\u00f3ria. "
        "\u00c1cido f\u00f3lico \u22650,4 mg/dia. "
        "Documentar no prontu\u00e1rio. (AAN/AES/SMFM 2024)</p>"
    ),
    mk_alerta(
        "\u26a0\ufe0f TAB + Antidepressivo sem estabilizador de humor",
        "ad_sem_estabilizador == 'confirmado_risco_documentado'",
        "<p><strong>Antidepressivo sem estabilizador em TAB: contraindicado.</strong><br>"
        "Risco de viragem man\u00edaca e ciclagem r\u00e1pida. "
        "Revisar prescri\u00e7\u00e3o. "
        "Associar estabilizador (l\u00edtio, lamotrigina ou VPA) antes de manter AD.</p>"
    ),
    mk_alerta(
        "\u26d4 ANOREXIA NERVOSA \u2014 Sinais de alarme: Interna\u00e7\u00e3o urgente",
        "selected_any(an_sinais_alarme, 'imc_menor_15', 'fc_menor_50', 'pa_menor_90_60', 'eletr\u00f3litos_criticos', 'instabilidade_clinica')",
        "<p><strong>AN com instabilidade cl\u00ednica \u2014 interna\u00e7\u00e3o urgente.</strong><br>"
        "FC &lt;50 bpm, PA &lt;90/60 mmHg ou eletr\u00f3litos cr\u00edticos "
        "(K+ &lt;3,0 mEq/L ou Na+ &lt;130 mEq/L): emerg\u00eancia m\u00e9dica. "
        "Encaminhar UPA/hospital com suporte nutricional.</p>"
    ),
    mk_alerta(
        "\u26a0\ufe0f CLOZAPINA \u2014 Sintomas de miocardite",
        "sintomas_miocardite in ('dor_toracica_dispneia_febre', 'taquicardia_inexplicada')",
        "<p><strong>Suspeita de miocardite associada \u00e0 clozapina.</strong><br>"
        "Solicitar troponina + PCR urgente. "
        "Encaminhar cardiologia/emerg\u00eancia. "
        "Suspender clozapina se confirmada. Monitorar CK-MB e ECG.</p>"
    ),
    mk_alerta(
        "\u26a0\ufe0f TOXICIDADE DE L\u00cdTIO",
        "selected_any(sintomas_toxicidade_litio, 'ataxia', 'confusao')",
        "<p><strong>Sintomas de toxicidade ao l\u00edtio.</strong><br>"
        "Solicitar n\u00edvel s\u00e9rico urgente. "
        "Suspender AINEs, IECA e diur\u00e9ticos. Hidrata\u00e7\u00e3o vigorosa. "
        "Hemodi\u00e1lise indicada se litemia &gt;2,5 mEq/L ou toxicidade grave. "
        "Encaminhar urg\u00eancia.</p>"
    ),
    mk_alerta(
        "\u2139\ufe0f PRIMEIRO EP\u00cdSODIO PSIC\u00d3TICO \u2014 Investiga\u00e7\u00e3o org\u00e2nica obrigat\u00f3ria",
        "primeiro_episodio_psicotico == 'sim' and causa_organica_investigada != 'sim'",
        "<p><strong>Descartar causa org\u00e2nica antes de estabelecer diagn\u00f3stico prim\u00e1rio.</strong><br>"
        "Hemograma, metab\u00f3lico completo, TSH, B12, VDRL, HIV. "
        "Neuroimagem (TC ou RM) obrigat\u00f3ria. "
        "Encaminhar neurologia para avalia\u00e7\u00e3o.</p>"
    ),
]


# ──────────────────────────────────────────────────────────────────────────────
# 4.2 EXAMES LABORATORIAIS — 25 itens
# ──────────────────────────────────────────────────────────────────────────────

exames = [
    # ── Grupo: Monitoramento de Lítio (5 exames) ──
    mk_exame(
        "Litemia (l\u00edtio s\u00e9rico)",
        "'litio' in medicamentos_em_uso",
        "40302440", "F31",
        "Monitoramento de l\u00edtio \u2014 estabilizador do humor. Faixa mania: 0,8\u20131,2 mEq/L; manuten\u00e7\u00e3o: 0,6\u20131,0 mEq/L.",
        instrucoes="Coletar 12h ap\u00f3s \u00faltima dose, em jejum. N\u00e3o tomar comprimido antes da coleta."
    ),
    mk_exame(
        "Creatinina s\u00e9rica + eGFR",
        "'litio' in medicamentos_em_uso",
        "40302253", "F31",
        "L\u00edtio \u2014 monitoramento de fun\u00e7\u00e3o renal. Nefropatia cr\u00f4nica em uso prolongado."
    ),
    mk_exame(
        "TSH (horm\u00f4nio estimulante da tireoide)",
        "('litio' in medicamentos_em_uso) or selected_any(diagnostico_ativo, 'tdm', 'distimia')",
        "40320094", "F31",
        "L\u00edtio / depress\u00e3o refrat\u00e1ria \u2014 hipotireoidismo subcl\u00ednico como causa secund\u00e1ria."
    ),
    mk_exame(
        "C\u00e1lcio total",
        "'litio' in medicamentos_em_uso",
        "40302130", "F31",
        "L\u00edtio \u2014 hipercalcemia e hiperparatireoidismo (efeito adverso cr\u00f4nico)."
    ),
    mk_exame(
        "Ureia s\u00e9rica",
        "'litio' in medicamentos_em_uso",
        "40302415", "F31",
        "L\u00edtio \u2014 fun\u00e7\u00e3o renal complementar (junto com creatinina)."
    ),
    # ── Grupo: Monitoramento de Valproato (4 exames) ──
    mk_exame(
        "N\u00edvel s\u00e9rico de \u00e1cido valpr\u00f3ico (VPA)",
        "'valproato' in medicamentos_em_uso",
        "40302555", "F31",
        "Valproato \u2014 faixa terap\u00eautica: 50\u2013100 \u00b5g/mL.",
        instrucoes="Coletar antes da dose matinal (vale de concentra\u00e7\u00e3o)."
    ),
    mk_exame(
        "ALT/TGP (alanina aminotransferase)",
        "selected_any(medicamentos_em_uso, 'valproato', 'carbamazepina', 'ap_atipico_olanzapina')",
        "40302180", "F31",
        "Hepatotoxicidade por VPA / CBZ / olanzapina. Suspender se ALT/TGP >3\u00d7 LSN com sintomas."
    ),
    mk_exame(
        "AST/TGO (aspartato aminotransferase)",
        "selected_any(medicamentos_em_uso, 'valproato', 'carbamazepina', 'ap_atipico_olanzapina')",
        "40302172", "F31",
        "Hepatotoxicidade por VPA / CBZ / olanzapina."
    ),
    mk_exame(
        "Am\u00f4nia s\u00e9rica",
        "'valproato' in medicamentos_em_uso and selected_any(sintomas_toxicidade_litio, 'confusao')",
        "40302082", "F31",
        "VPA \u2014 hiperamonemia (encefalopatia valproica). Suspeitar se confus\u00e3o mental em uso de VPA."
    ),
    # ── Grupo: Monitoramento de Carbamazepina (3 exames) ──
    mk_exame(
        "N\u00edvel s\u00e9rico de carbamazepina (CBZ)",
        "'carbamazepina' in medicamentos_em_uso",
        "40302490", "F31",
        "CBZ \u2014 faixa terap\u00eautica: 4\u201312 \u00b5g/mL.",
        instrucoes="Coletar antes da dose matinal."
    ),
    mk_exame(
        "S\u00f3dio s\u00e9rico",
        "'carbamazepina' in medicamentos_em_uso",
        "40302350", "F31",
        "CBZ \u2014 hiponatremia por SIADH (s\u00edndrome de secre\u00e7\u00e3o inapropriada de ADH)."
    ),
    mk_exame(
        "HLA-B*1502 (genotipagem)",
        "'carbamazepina' in medicamentos_em_uso and cbz_hla_realizado == 'nao_pendente'",
        "", "F31",
        "CBZ \u2014 risco de S\u00edndrome de Stevens-Johnson em pacientes de descendência asi\u00e1tica. TUSS a confirmar."
    ),
    # ── Grupo: Hemograma (1 exame — cobre CBZ + Clozapina + VPA) ──
    mk_exame(
        "Hemograma completo com plaquetas",
        "selected_any(medicamentos_em_uso, 'clozapina', 'carbamazepina', 'valproato')",
        "40302058", "F31",
        "Clozapina / CBZ / VPA \u2014 mielossupresso. Anemia aplstica (CBZ), agranulocitose (clozapina), trombocitopenia (VPA)."
    ),
    # ── Grupo: Monitoramento Metabólico — AP Atípicos (5 exames) ──
    mk_exame(
        "Glicemia de jejum",
        "selected_any(medicamentos_em_uso, 'clozapina', 'ap_atipico_olanzapina', 'ap_atipico_quetiapina', 'ap_atipico_risperidona', 'ap_atipico_aripiprazol') and 'glicemia_hba1c' not in metabolico_monitorado",
        "40302148", "F32",
        "AP at\u00edpico \u2014 s\u00edndrome metab\u00f3lica / DM2. Maior risco: olanzapina, clozapina, quetiapina.",
        instrucoes="Jejum de 8h."
    ),
    mk_exame(
        "Hemoglobina glicada (HbA1c)",
        "selected_any(medicamentos_em_uso, 'clozapina', 'ap_atipico_olanzapina', 'ap_atipico_quetiapina', 'ap_atipico_risperidona', 'ap_atipico_aripiprazol') and 'glicemia_hba1c' not in metabolico_monitorado",
        "40307252", "F32",
        "AP at\u00edpico \u2014 controle glic\u00eamico e rastreio de DM2."
    ),
    mk_exame(
        "Colesterol total e fra\u00e7\u00f5es (LDL, HDL, VLDL)",
        "selected_any(medicamentos_em_uso, 'clozapina', 'ap_atipico_olanzapina', 'ap_atipico_quetiapina', 'ap_atipico_risperidona', 'ap_atipico_aripiprazol') and 'lipidios' not in metabolico_monitorado",
        "40302121", "F32",
        "AP at\u00edpico \u2014 dislipidemia. Clozapina e olanzapina com maior impacto lip\u00eddico.",
        instrucoes="Jejum de 12h."
    ),
    mk_exame(
        "Triglicer\u00eddeos",
        "selected_any(medicamentos_em_uso, 'clozapina', 'ap_atipico_olanzapina', 'ap_atipico_quetiapina', 'ap_atipico_risperidona', 'ap_atipico_aripiprazol') and 'lipidios' not in metabolico_monitorado",
        "40302407", "F32",
        "AP at\u00edpico \u2014 hipertrigliceridemia.",
        instrucoes="Jejum de 12h."
    ),
    mk_exame(
        "Prolactina",
        "'ap_atipico_risperidona' in medicamentos_em_uso and prolactina_sintomatic != 'nenhum'",
        "40302326", "F32",
        "Risperidona \u2014 hiperprolactinemia sintom\u00e1tica (galactorreia, amenorreia, disfun\u00e7\u00e3o sexual)."
    ),
    # ── Grupo: Baseline — MIE + Lítio/VPA (1 exame) ──
    mk_exame(
        "Beta-HCG (gonadotrofina cori\u00f4nica)",
        "sexo_feminino_ie == 'sim' and selected_any(medicamentos_em_uso, 'litio', 'valproato')",
        "40306045", "F31",
        "L\u00edtio/VPA em mulher em idade f\u00e9rtil \u2014 excluir gravidez antes de iniciar/manter f\u00e1rmaco teratog\u00eanico.",
        tipo_amostra="Sangue ou urina"
    ),
    # ── Grupo: ECG (1 exame) ──
    mk_exame(
        "ECG convencional 12 deriva\u00e7\u00f5es",
        "ecg_indicado_psico != 'nao_indicado'",
        "40101010", "F31",
        "Psicof\u00e1rmaco QT-prolongante \u2014 rastreio de arritmia / QTc prolongado. TCA: ECG obrigat\u00f3rio.",
        tipo_amostra=""
    ),
    # ── Grupo: Primeiro episódio psicótico (5 exames) ──
    mk_exame(
        "Hemograma com diferencial (1\u00ba epis\u00f3dio)",
        "primeiro_episodio_psicotico == 'sim' and causa_organica_investigada != 'sim'",
        "40302058", "F29",
        "Primeiro epis\u00f3dio psic\u00f3tico \u2014 exclus\u00e3o de causa org\u00e2nica infecciosa/inflamat\u00f3ria."
    ),
    mk_exame(
        "TSH (1\u00ba epis\u00f3dio)",
        "primeiro_episodio_psicotico == 'sim' and causa_organica_investigada != 'sim'",
        "40320094", "F29",
        "Primeiro epis\u00f3dio \u2014 hipotireoidismo ou hipertireoidismo como causa org\u00e2nica."
    ),
    mk_exame(
        "VDRL / RPR (s\u00edfilis)",
        "primeiro_episodio_psicotico == 'sim' and causa_organica_investigada != 'sim'",
        "40314098", "F29",
        "Primeiro epis\u00f3dio \u2014 neuross\u00edfilis (treponema pallidum)."
    ),
    mk_exame(
        "Sorologia HIV (anti-HIV 1 e 2)",
        "primeiro_episodio_psicotico == 'sim' and causa_organica_investigada != 'sim'",
        "40312003", "F29",
        "Primeiro epis\u00f3dio \u2014 encefalite ou complica\u00e7\u00f5es neurol\u00f3gicas por HIV."
    ),
    mk_exame(
        "Troponina + Prote\u00edna C-reativa (PCR)",
        "sintomas_miocardite in ('dor_toracica_dispneia_febre', 'taquicardia_inexplicada')",
        "", "F29",
        "Clozapina \u2014 suspeita de miocardite. TUSS a confirmar com codifica\u00e7\u00e3o espec\u00edfica da institui\u00e7\u00e3o."
    ),
]


# ──────────────────────────────────────────────────────────────────────────────
# 4.3 ENCAMINHAMENTOS — 13 itens
# ──────────────────────────────────────────────────────────────────────────────

encaminhamentos = [
    mk_encaminhamento(
        "Psic\u00f3logo \u2014 ERP (TOC)",
        "'toc' in diagnostico_ativo",
        "ERP (Exposi\u00e7\u00e3o com Preven\u00e7\u00e3o de Resposta) \u2014 tratamento obrigat\u00f3rio para TOC. "
        "Psic\u00f3logo com treinamento espec\u00edfico. Resposta esperada: redu\u00e7\u00e3o \u226535% no Y-BOCS ap\u00f3s 12\u201320 sess\u00f5es.",
        "Psic\u00f3logo", "F42"
    ),
    mk_encaminhamento(
        "Psic\u00f3logo \u2014 TF-CBT/EMDR (TEPT)",
        "'tept' in diagnostico_ativo and tept_psicoterapia_indicada != 'sim'",
        "Psicoterapia focada em trauma obrigat\u00f3ria: TF-CBT, CPT, PE ou EMDR. "
        "1\u00aa linha com maior n\u00edvel de evid\u00eancia para TEPT (APA/NICE 2024).",
        "Psic\u00f3logo", "F43.1"
    ),
    mk_encaminhamento(
        "Psic\u00f3logo \u2014 TCD (TPB)",
        "'tpb' in diagnostico_ativo and tpb_em_tcd != 'sim'",
        "TCD (Terapia Comportamental Dial\u00e9tica) \u2014 \u00fanico tratamento de 1\u00aa linha para TPB com RCT confirmat\u00f3rio. "
        "M\u00ednimo 1 ano de tratamento.",
        "Psic\u00f3logo", "F60.3"
    ),
    mk_encaminhamento(
        "Psic\u00f3logo \u2014 TCC",
        "selected_any(diagnostico_ativo, 'tdm', 'tag', 'panico', 'fobia_social', 'burnout')",
        "TCC como adjuvante \u00e0 farmacoterapia. "
        "1\u00aa linha em combina\u00e7\u00e3o com ISRS para TDM / TAG / P\u00e2nico / Fobia Social.",
        "Psic\u00f3logo", "F32"
    ),
    mk_encaminhamento(
        "Neuropsic\u00f3logo",
        "neuropsicologica_indicada in ('sim_solicitada', 'sim_pendente')",
        "Avalia\u00e7\u00e3o neuropsicol\u00f3gica: TDAH com diagn\u00f3stico incerto / TEA adulto para confirma\u00e7\u00e3o. "
        "Relat\u00f3rio diagn\u00f3stico completo.",
        "Neuropsic\u00f3logo", "F90"
    ),
    mk_encaminhamento(
        "Nutricionista",
        "selected_any(diagnostico_ativo, 'ta_anorexia', 'ta_bulimia', 'ta_tcap') and nutri_encaminhada != 'ja_acompanha'",
        "Avalia\u00e7\u00e3o e acompanhamento nutricional obrigat\u00f3rio em transtornos alimentares. "
        "Avaliar risco de s\u00edndrome de realimenta\u00e7\u00e3o (AN).",
        "Nutricionista", "F50"
    ),
    mk_encaminhamento(
        "Emerg\u00eancia / SAMU 192",
        "nivel_risco_p0 == 'alto'",
        "SAMU 192. Encaminhamento de urg\u00eancia por risco suicida alto classificado no C-SSRS. "
        "N\u00e3o deixar paciente sem acompanhante.",
        "Emerg\u00eancia", "Z91.5"
    ),
    mk_encaminhamento(
        "CAPS II",
        "'esquizofrenia' in diagnostico_ativo",
        "Acompanhamento psicossocial complementar \u2014 esquizofrenia est\u00e1vel. "
        "Reabilita\u00e7\u00e3o e reinser\u00e7\u00e3o social (Lei 10.216/2001).",
        "CAPS II", "F20"
    ),
    mk_encaminhamento(
        "CAPS-AD",
        "selected_any(diagnostico_ativo, 'uso_substancias')",
        "Depend\u00eancia de subst\u00e2ncias \u2014 CAPS-AD. Tratamento especializado em rede p\u00fablica.",
        "CAPS-AD", "F19"
    ),
    mk_encaminhamento(
        "Neurologia",
        "primeiro_episodio_psicotico == 'sim' or selected_any(comorbidades_clinicas, 'epilepsia')",
        "Primeiro epis\u00f3dio psic\u00f3tico / epilepsia \u2014 exclus\u00e3o de causa org\u00e2nica. "
        "Solicitar neuroimagem (TC ou RM de cr\u00e2nio).",
        "Neurologista", "F29"
    ),
    mk_encaminhamento(
        "Cardiologia",
        "selected_any(an_sinais_alarme, 'fc_menor_50') or ecg_indicado_psico in ('estimulante_cardiopatia') or (anc_dentro_limite == 'suspender_menor_1000' and sintomas_miocardite != 'nenhum')",
        "QTc >500ms / cardiopatia estrutural / miocardite por clozapina. Avalia\u00e7\u00e3o urgente.",
        "Cardiologista", "I49"
    ),
    mk_encaminhamento(
        "Medicina do Trabalho",
        "'burnout' in diagnostico_ativo",
        "Burnout grave \u2014 an\u00e1lise do ambiente organizacional e afastamento quando indicado.",
        "M\u00e9dico do Trabalho", "F43.8"
    ),
    mk_encaminhamento(
        "Endocrinologia",
        "('litio' in medicamentos_em_uso) and ('hipotireoidismo' in comorbidades_clinicas)",
        "Hipotireoidismo em uso de l\u00edtio. "
        "L\u00edtio inibe s\u00edntese e libera\u00e7\u00e3o de horm\u00f4nios tireoidianos. Ajuste de levotiroxina.",
        "Endocrinologista", "E03"
    ),
]


# ──────────────────────────────────────────────────────────────────────────────
# 4.4 MEDICAMENTOS — 9 lembretes de prescrição
# ──────────────────────────────────────────────────────────────────────────────

medicamentos = [
    mk_medicamento(
        "Escitalopram 10mg",
        "selected_any(diagnostico_ativo, 'tdm', 'tag', 'panico') and episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'depressao_grave')",
        "10 mg/dia pela manh\u00e3. Aumentar para 20 mg ap\u00f3s 4 semanas se resposta parcial. M\u00e1x 20 mg/dia.",
        "ISRS"
    ),
    mk_medicamento(
        "Sertralina 50mg",
        "selected_any(diagnostico_ativo, 'tdm', 'tag', 'panico', 'tept', 'toc') and episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'depressao_grave')",
        "50 mg/dia com alimento. Titular at\u00e9 100\u2013200 mg/dia. TOC: dose alvo 150\u2013200 mg.",
        "ISRS"
    ),
    mk_medicamento(
        "Fluoxetina 20mg",
        "selected_any(diagnostico_ativo, 'tdm', 'toc', 'ta_bulimia')",
        "TDM: 20 mg/dia. TOC: 60\u201380 mg/dia (titular lentamente). BN: 60 mg/dia alvo.",
        "ISRS"
    ),
    mk_medicamento(
        "L\u00edtio 300mg",
        "('tab' in diagnostico_ativo) and episodio_atual_humor in ('mania', 'hipomania', 'eutimia')",
        "300 mg 3\u00d7/dia (in\u00edcio). N\u00edvel-alvo: mania aguda 0,8\u20131,2 mEq/L; manuten\u00e7\u00e3o 0,6\u20131,0 mEq/L. "
        "Coletar litemia 12h ap\u00f3s \u00faltima dose.",
        "Estabilizador de humor"
    ),
    mk_medicamento(
        "Lamotrigina 25mg",
        "('tab' in diagnostico_ativo) and episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'eutimia')",
        "Iniciar 25 mg/dia \u00d7 2 semanas \u2192 50 mg/dia \u00d7 2 semanas \u2192 100 mg/dia. "
        "Tita\u00e7\u00e3o lenta obrigat\u00f3ria (risco Stevens-Johnson).",
        "Estabilizador de humor"
    ),
    mk_medicamento(
        "Metilfenidato LP 18mg",
        "'tdah' in diagnostico_ativo and tdah_abuso_substancias_ativo != 'sim'",
        "18 mg/dia pela manh\u00e3 (in\u00edcio). Titular at\u00e9 36\u201354 mg/dia. M\u00e1x 72 mg/dia.",
        "Estimulante \u2014 TDAH"
    ),
    mk_medicamento(
        "Lisdexanfetamina 20mg",
        "('tdah' in diagnostico_ativo) or ('ta_tcap' in diagnostico_ativo)",
        "TDAH: 20\u201330 mg/dia (in\u00edcio) \u2192 30\u201370 mg/dia. TCAP: 30\u201370 mg/dia. Tomar pela manh\u00e3.",
        "Estimulante \u2014 TDAH / TCAP"
    ),
    mk_medicamento(
        "Biperideno 2mg",
        "selected_any(eps_presente, 'parkinsonismo', 'distonia_aguda')",
        "EPS/parkinsonismo: 2\u20134 mg/dia VO. Distonia aguda: 5 mg IM (repetir se necess\u00e1rio em 30 min).",
        "Anticolinerg\u00edco \u2014 EPS"
    ),
    mk_medicamento(
        "Propranolol 20mg",
        "'acatisia' in eps_presente",
        "20\u201340 mg/dia, dividido 2\u00d7/dia. "
        "Verificar contraindica\u00e7\u00f5es (asma, bloqueio AV, bradicardia).",
        "\u03b2-bloqueador \u2014 Acatisia"
    ),
]


# ──────────────────────────────────────────────────────────────────────────────
# INJEÇÃO NO NÓ 6
# ──────────────────────────────────────────────────────────────────────────────

for node in d["nodes"]:
    if node["id"] == "node-psiq-06-conduta":
        node["type"] = "conduct"
        node["data"]["label"] = "Conduta \u2014 Exames, Alertas, Encaminhamentos"
        node["data"]["descricao"] = (
            "<p>Conduta gerada automaticamente com base nas respostas cl\u00ednicas. "
            "Exames, alertas de seguran\u00e7a, encaminhamentos e lembretes de prescri\u00e7\u00e3o "
            "s\u00e3o exibidos de acordo com os dados coletados.</p>"
        )
        node["data"]["condutaDataNode"] = {
            "orientacao": [],
            "exame": exames,
            "medicamento": medicamentos,
            "encaminhamento": encaminhamentos,
            "mensagem": alertas,
        }
        print(f"N\u00f3 6 atualizado:")
        print(f"  type: {node['type']}")
        print(f"  Alertas (mensagem): {len(alertas)}")
        print(f"  Exames: {len(exames)}")
        print(f"  Encaminhamentos: {len(encaminhamentos)}")
        print(f"  Medicamentos: {len(medicamentos)}")
        break

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("JSON gravado com sucesso.")
