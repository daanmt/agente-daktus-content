"""
Sessões C-F: Injeta Nós 4 (Módulo Diagnóstico — 30 questões) e
             Nó 5 (Monitoramento Farmacológico — 18 questões)
"""
import json, uuid

def u(): return str(uuid.uuid4())

filepath = 'especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json'
d = json.load(open(filepath, encoding='utf-8'))

# ─────────────────────────────────────────────────────────────
# NÓ 4 — MÓDULO DIAGNÓSTICO ATIVO (30 questões, todas condicionais)
# ─────────────────────────────────────────────────────────────

no4_questions = [

  # ── BLOCO HUMOR ──────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'episodio_atual_humor',
    'titulo': '<p><strong>Episódio atual de humor</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "('tdm' in diagnostico_ativo) or ('distimia' in diagnostico_ativo) or ('tab' in diagnostico_ativo)",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'eutimia', 'label': 'Eutimia / sem episódio ativo', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'depressao_leve', 'label': 'Depressão leve (PHQ-9: 7–13 / MADRS: 7–19)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'depressao_moderada', 'label': 'Depressão moderada (PHQ-9: 14–19 / MADRS: 20–34)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'depressao_grave', 'label': 'Depressão grave (PHQ-9 ≥20 / MADRS ≥35)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'hipomania', 'label': 'Hipomania (≥4 dias, sem prejuízo marcado)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'mania', 'label': 'Mania (≥7 dias + prejuízo / hospitalização)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'misto', 'label': 'Episódio misto (≥3 sx do polo oposto)', 'preselected': False, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tab_fase_diagnostica',
    'titulo': '<p><strong>TAB — confirmação de subtipo</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tab' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'tab1', 'label': 'TAB I (mania plena documentada)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'tab2', 'label': 'TAB II (hipomania + depressão, sem mania)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'ciclotimia', 'label': 'Ciclotimia', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_definido', 'label': 'Subtipo ainda não definido', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'ciclagem_rapida',
    'titulo': '<p><strong>Ciclagem rápida (≥4 episódios / ano)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tab' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'especificador_misto',
    'titulo': '<p><strong>Especificador misto presente (≥3 sx polo oposto)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'depressao_grave', 'mania', 'hipomania')",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'sintomas_psicoticos_humor',
    'titulo': '<p><strong>Sintomas psicóticos durante episódio de humor?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "episodio_atual_humor in ('depressao_grave', 'mania')",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'madrs_score',
    'titulo': '<p><strong>MADRS score (se aplicado)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "episodio_atual_humor in ('depressao_leve', 'depressao_moderada', 'depressao_grave')",
    'select': 'number', 'options': [], 'opcional': True
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'ymrs_score',
    'titulo': '<p><strong>YMRS score (se aplicado)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "episodio_atual_humor in ('mania', 'hipomania')",
    'select': 'number', 'options': [], 'opcional': True
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'ad_sem_estabilizador',
    'titulo': '<p><strong>⚠️ ALERTA: Antidepressivo em uso SEM estabilizador em TAB — confirmar conduta:</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "('tab' in diagnostico_ativo) and ('isrs' in medicamentos_em_uso) and not selected_any(medicamentos_em_uso, 'litio', 'valproato', 'lamotrigina', 'carbamazepina')",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'confirmado_risco_documentado', 'label': 'Risco documentado — manter com monitoramento intensivo', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'trocar_conduta', 'label': 'Suspender AD / adicionar estabilizador', 'preselected': False, 'exclusive': True},
    ]
  },

  # ── BLOCO ANSIEDADE ───────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'ansiedade_subtipo',
    'titulo': '<p><strong>Subtipo de transtorno de ansiedade presente</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "selected_any(diagnostico_ativo, 'tag', 'panico', 'fobia_social', 'toc', 'tept', 'burnout')",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'tag', 'label': 'TAG — ansiedade generalizada', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'panico', 'label': 'Transtorno do pânico', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'fobia_social', 'label': 'Fobia social / Transtorno de ansiedade social', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'toc', 'label': 'TOC', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'tept', 'label': 'TEPT', 'preselected': False, 'exclusive': False},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'ybocs_score',
    'titulo': '<p><strong>Y-BOCS score (se aplicado)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'toc' in diagnostico_ativo",
    'select': 'number', 'options': [], 'opcional': True
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tept_psicoterapia_indicada',
    'titulo': '<p><strong>Paciente em psicoterapia focada em trauma (TF-CBT / EMDR / CPT)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tept' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — em andamento', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_encaminhar', 'label': 'Não — encaminhar para psicologia (TF-CBT/EMDR)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'em_lista_espera', 'label': 'Em lista de espera', 'preselected': False, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'burnout_criterios_tdm',
    'titulo': '<p><strong>Critérios de TDM preenchidos concomitantemente ao Burnout?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'burnout' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — TDM concomitante confirmado', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não — burnout sem critérios de TDM', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'pcl5_score',
    'titulo': '<p><strong>PCL-5 score (se aplicado)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tept' in diagnostico_ativo",
    'select': 'number', 'options': [], 'opcional': True
  },

  # ── BLOCO PSICOSE ─────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'primeiro_episodio_psicotico',
    'titulo': '<p><strong>Primeiro episódio psicótico?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'esquizofrenia' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'causa_organica_investigada',
    'titulo': '<p><strong>Causa orgânica investigada (neuroimagem + labs)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "primeiro_episodio_psicotico == 'sim'",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — investigação completa sem causa orgânica', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_pendente', 'label': 'Não — pendente (solicitar nesta consulta)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não — primeiro episódio recente, não aplicável ainda', 'preselected': False, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'eps_presente',
    'titulo': '<p><strong>EPS presente</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'esquizofrenia' in diagnostico_ativo",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'sem_eps', 'label': 'Sem EPS', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'parkinsonismo', 'label': 'Parkinsonismo (rigidez, bradicinesia, tremor)', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'acatisia', 'label': 'Acatisia', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'distonia_aguda', 'label': 'Distonia aguda', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'discinesia_tardia', 'label': 'Discinesia tardia', 'preselected': False, 'exclusive': False},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'esquizofrenia_refrataria',
    'titulo': '<p><strong>Esquizofrenia refratária (≥2 antipsicóticos falhados em dose e tempo adequados)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'esquizofrenia' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — indicação de clozapina', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'comportamento_suicida_recorrente',
    'titulo': '<p><strong>Comportamento suicida recorrente (critério adicional para clozapina)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'esquizofrenia' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },

  # ── BLOCO TDAH ────────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tdah_apresentacao',
    'titulo': '<p><strong>Apresentação do TDAH (DSM-5)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tdah' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'desatenta', 'label': 'Predominantemente desatenta', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'hiperativa_impulsiva', 'label': 'Predominantemente hiperativa-impulsiva', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'combinada', 'label': 'Combinada', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tdah_abuso_substancias_ativo',
    'titulo': '<p><strong>Abuso de substâncias ativo concomitante?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tdah' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — precaução com estimulantes', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'sintomas_cardiacos_tdah',
    'titulo': '<p><strong>Sintomas cardíacos ou suspeita de cardiopatia?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tdah' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — solicitar ECG antes de estimulante', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'neuropsicologica_indicada',
    'titulo': '<p><strong>Avaliação neuropsicológica indicada?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tdah' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim_solicitada', 'label': 'Sim — solicitada nesta consulta', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'sim_pendente', 'label': 'Sim — pendente (em agenda)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_diagnostico_clinico_claro', 'label': 'Não — diagnóstico clínico suficientemente claro', 'preselected': True, 'exclusive': True},
    ]
  },

  # ── BLOCO TEA ─────────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tea_nivel_suporte',
    'titulo': '<p><strong>Nível de suporte necessário (DSM-5 / ICD-11)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tea' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'nivel1', 'label': 'Nível 1 — requer suporte', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nivel2', 'label': 'Nível 2 — requer suporte substancial', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nivel3', 'label': 'Nível 3 — requer suporte muito substancial', 'preselected': False, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tea_irritabilidade_grave',
    'titulo': '<p><strong>Irritabilidade grave (critério para considerar AP)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tea' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — considerar risperidona ou aripiprazol', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tea_comorbidades',
    'titulo': '<p><strong>Comorbidades psiquiátricas associadas ao TEA</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tea' in diagnostico_ativo",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'nenhuma', 'label': 'Nenhuma', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'ansiedade', 'label': 'Ansiedade', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'depressao', 'label': 'Depressão', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'tdah_comorbido', 'label': 'TDAH', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'toc_comorbido', 'label': 'TOC', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'psicose_comorbida', 'label': 'Psicose', 'preselected': False, 'exclusive': False},
    ]
  },

  # ── BLOCO TPB ─────────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tpb_autolesao_ativa',
    'titulo': '<p><strong>Autolesão ativa (não suicida)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tpb' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — ativa nas últimas 4 semanas', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tpb_em_tcd',
    'titulo': '<p><strong>Paciente em TCD (Terapia Comportamental Dialética)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tpb' in diagnostico_ativo",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — em TCD', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_encaminhar', 'label': 'Não — encaminhar para TCD', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'aguardando_vaga', 'label': 'Aguardando vaga em TCD', 'preselected': False, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'tpb_sintoma_alvo',
    'titulo': '<p><strong>Sintoma-alvo para farmacoterapia (se indicada)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'tpb' in diagnostico_ativo",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'nenhum', 'label': 'Nenhum — farmacoterapia não indicada no momento', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'impulsividade_grave', 'label': 'Impulsividade grave', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'instabilidade_humor', 'label': 'Instabilidade de humor', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'mini_psicose_transitoria', 'label': 'Mini-psicose transitória / ideação paranoide', 'preselected': False, 'exclusive': False},
    ]
  },

  # ── BLOCO TRANSTORNOS ALIMENTARES ────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'an_sinais_alarme',
    'titulo': '<p><strong>Sinais de alarme para AN (critérios de internação)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'ta_anorexia' in diagnostico_ativo",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'sem_sinais_alarme', 'label': 'Sem sinais de alarme', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'imc_menor_15', 'label': 'IMC <15', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'fc_menor_50', 'label': 'FC <50 bpm', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'pa_menor_90_60', 'label': 'PA <90/60 mmHg', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'sincope', 'label': 'Síncope', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'eletrólitos_criticos', 'label': 'Eletrólitos críticos (K+ <3,0 ou Na+ <130)', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'instabilidade_clinica', 'label': 'Instabilidade clínica geral', 'preselected': False, 'exclusive': False},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-04-diagnostico',
    'uid': 'nutri_encaminhada',
    'titulo': '<p><strong>Nutricionista encaminhada?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "selected_any(diagnostico_ativo, 'ta_anorexia', 'ta_bulimia', 'ta_tcap')",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim_encaminhada', 'label': 'Sim — encaminhada nesta consulta', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'ja_acompanha', 'label': 'Já em acompanhamento nutricional', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_encaminhar', 'label': 'Não — encaminhar', 'preselected': False, 'exclusive': True},
    ]
  },
]

# ─────────────────────────────────────────────────────────────
# NÓ 5 — MONITORAMENTO FARMACOLÓGICO (18 questões)
# ─────────────────────────────────────────────────────────────

no5_questions = [

  # ── LÍTIO ─────────────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'litio_fase',
    'titulo': '<p><strong>Fase do uso de lítio</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'litio' in medicamentos_em_uso",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'iniciando_baseline', 'label': 'Iniciando — aguardando baseline laboratorial', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'ajuste_dose', 'label': 'Ajuste de dose (litemia fora da faixa alvo)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'manutencao_menos_1ano', 'label': 'Manutenção estável < 1 ano', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'manutencao_mais_1ano', 'label': 'Manutenção estável ≥ 1 ano', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'litemia_valor',
    'titulo': '<p><strong>Litemia mais recente (mEq/L) — coletar 12h após última dose</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'litio' in medicamentos_em_uso",
    'select': 'number', 'options': [], 'opcional': True
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'litemia_dentro_faixa',
    'titulo': '<p><strong>Litemia dentro da faixa terapêutica?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'litio' in medicamentos_em_uso",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim', 'label': 'Sim — dentro da faixa (0,6–1,0 mEq/L manutenção / 0,8–1,2 aguda)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'baixo', 'label': 'Abaixo da faixa — considerar ajuste de dose', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'alto_risco_toxicidade', 'label': '⛔ Acima de 1,2 mEq/L — risco de toxicidade', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_coletada', 'label': 'Não coletada — solicitar', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'sintomas_toxicidade_litio',
    'titulo': '<p><strong>Sinais de toxicidade ao lítio?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'litio' in medicamentos_em_uso",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'nenhum', 'label': 'Nenhum', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'tremor_novo', 'label': 'Tremor novo ou agravado', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'nausea_diarreia', 'label': 'Náusea / vômito / diarreia', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'ataxia', 'label': 'Ataxia / disartria', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'confusao', 'label': 'Confusão mental / obnubilação', 'preselected': False, 'exclusive': False},
    ]
  },

  # ── VALPROATO ─────────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'vpa_fase',
    'titulo': '<p><strong>Fase do uso de valproato</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'valproato' in medicamentos_em_uso",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'iniciando', 'label': 'Iniciando', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'ajuste', 'label': 'Ajuste de dose', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'manutencao', 'label': 'Manutenção estável', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'vpa_nivel',
    'titulo': '<p><strong>Nível sérico de VPA (µg/mL) — faixa terapêutica: 50–125</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'valproato' in medicamentos_em_uso",
    'select': 'number', 'options': [], 'opcional': True
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'vpa_labs_recentes',
    'titulo': '<p><strong>Monitoramento laboratorial VPA nos últimos 3 meses</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'valproato' in medicamentos_em_uso",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'tgo_tgp', 'label': 'TGO / TGP', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'hemograma_plaquetas', 'label': 'Hemograma + plaquetas', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'amonia', 'label': 'Amônia sérica', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'nenhum_pendente', 'label': 'Nenhum — solicitar monitoramento', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'vpa_mie_consentimento',
    'titulo': '<p><strong>⚠️ Aconselhamento de teratogenicidade VPA documentado + contracepção eficaz?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "('valproato' in medicamentos_em_uso) and (sexo_feminino_ie == 'sim')",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim_documentado', 'label': 'Sim — documentado em prontuário + contracepção dupla confirmada', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_pendente_hoje', 'label': '⛔ Não — obrigatório realizar e documentar HOJE (AAN/AES/SMFM 2024)', 'preselected': False, 'exclusive': True},
    ]
  },

  # ── CARBAMAZEPINA ─────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'cbz_nivel',
    'titulo': '<p><strong>Nível sérico de carbamazepina (µg/mL) — faixa: 4–12</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'carbamazepina' in medicamentos_em_uso",
    'select': 'number', 'options': [], 'opcional': True
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'cbz_hla_realizado',
    'titulo': '<p><strong>HLA-B*1502 realizado (risco de Stevens-Johnson em descendentes asiáticos)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'carbamazepina' in medicamentos_em_uso",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'sim_negativo', 'label': 'Sim — negativo (seguro prosseguir)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'sim_positivo_evitar', 'label': '⛔ Sim — positivo (EVITAR carbamazepina)', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'nao_nao_asiatico', 'label': 'Não realizado — sem descendência asiática relevante', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'nao_pendente', 'label': 'Não realizado — solicitar (descendência asiática)', 'preselected': False, 'exclusive': True},
    ]
  },

  # ── CLOZAPINA ─────────────────────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'clozapina_semana',
    'titulo': '<p><strong>Semana atual de uso de clozapina</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'clozapina' in medicamentos_em_uso",
    'select': 'number', 'options': []
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'anc_valor',
    'titulo': '<p><strong>ANC mais recente (/µL)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'clozapina' in medicamentos_em_uso",
    'select': 'number', 'options': []
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'anc_dentro_limite',
    'titulo': '<p><strong>ANC status</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'clozapina' in medicamentos_em_uso",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'normal_maior_1500', 'label': 'Normal (>1.500/µL)', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'alerta_1000_1500', 'label': '⚠️ Alerta (1.000–1.500/µL) — aumentar frequência do monitoramento', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'suspender_menor_1000', 'label': '⛔ SUSPENDER CLOZAPINA (<1.000/µL)', 'preselected': False, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'sintomas_miocardite',
    'titulo': '<p><strong>Sintomas sugestivos de miocardite (monitorar no 1º mês)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "('clozapina' in medicamentos_em_uso) and (clozapina_semana <= 4)",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'nenhum', 'label': 'Nenhum', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'dor_toracica_dispneia_febre', 'label': '⛔ Dor torácica / dispneia / febre — encaminhar urgência', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'taquicardia_inexplicada', 'label': '⚠️ Taquicardia inexplicada — solicitar troponina + ECG', 'preselected': False, 'exclusive': True},
    ]
  },

  # ── ANTIPSICÓTICOS ATÍPICOS ───────────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'ap_tempo_uso',
    'titulo': '<p><strong>Tempo de uso do antipsicótico atípico</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "selected_any(medicamentos_em_uso, 'ap_atipico_olanzapina', 'ap_atipico_quetiapina', 'ap_atipico_risperidona', 'ap_atipico_aripiprazol', 'ap_atipico_ziprasidona')",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'iniciando_baseline', 'label': 'Iniciando — baseline metabólico pendente', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'um_a_tres_meses', 'label': '1–3 meses de uso', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'mais_de_tres_meses', 'label': '>3 meses de uso estável', 'preselected': True, 'exclusive': True},
    ]
  },
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'metabolico_monitorado',
    'titulo': '<p><strong>Monitoramento metabólico realizado (últimos 3 meses)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "selected_any(medicamentos_em_uso, 'ap_atipico_olanzapina', 'ap_atipico_quetiapina', 'ap_atipico_risperidona', 'ap_atipico_aripiprazol', 'ap_atipico_ziprasidona')",
    'select': 'multiChoice',
    'options': [
      {'iid': u(), 'id': 'glicemia_hba1c', 'label': 'Glicemia / HbA1c', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'lipidios', 'label': 'Lipídios (CT, LDL, HDL, TG)', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'peso_imc_cc', 'label': 'Peso / IMC / circunferência abdominal', 'preselected': False, 'exclusive': False},
      {'iid': u(), 'id': 'nenhum_pendente', 'label': 'Nenhum — solicitar monitoramento completo', 'preselected': True, 'exclusive': True},
    ]
  },

  # ── ISRS / TCA / ESTIMULANTE — ECG ────────────────────────────
  {
    'id': 'P' + u(), 'nodeId': 'node-psiq-05-farmacos',
    'uid': 'ecg_indicado_psico',
    'titulo': '<p><strong>ECG indicado por psicofármaco?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "('isrs' in medicamentos_em_uso) or ('antidepressivo_tca' in medicamentos_em_uso) or ('estimulante' in medicamentos_em_uso) or ('clozapina' in medicamentos_em_uso)",
    'select': 'choice',
    'options': [
      {'iid': u(), 'id': 'nao_indicado', 'label': 'Não indicado no momento', 'preselected': True, 'exclusive': True},
      {'iid': u(), 'id': 'isrs_dose_alta_qt', 'label': 'ISRS em dose alta (escitalopram >20mg / citalopram >20mg) — QTc', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'tca_obrigatorio', 'label': 'TCA em uso — ECG obrigatório antes de iniciar', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'estimulante_cardiopatia', 'label': 'Estimulante + suspeita de cardiopatia', 'preselected': False, 'exclusive': True},
      {'iid': u(), 'id': 'qt_multiplas_drogas', 'label': 'Múltiplos fármacos QT-prolongantes', 'preselected': False, 'exclusive': True},
    ]
  },
]

# ── Injetar Nó 4 e Nó 5 ──────────────────────────────────────
for node in d['nodes']:
    if node['id'] == 'node-psiq-04-diagnostico':
        node['data']['questions'] = no4_questions
        node['data']['label'] = 'Avaliação Diagnóstica — Condição Ativa'
        node['data']['descricao'] = '<p>Perguntas específicas por diagnóstico ativo. Apenas os blocos relevantes para o paciente serão exibidos.</p>'
    elif node['id'] == 'node-psiq-05-farmacos':
        node['data']['questions'] = no5_questions
        node['data']['label'] = 'Monitoramento Farmacológico'
        node['data']['descricao'] = '<p>Perguntas condicionadas pelos psicofármacos em uso. Apenas itens relevantes serão exibidos.</p>'

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('Nó 4: ' + str(len(no4_questions)) + ' questoes')
print('Nó 5: ' + str(len(no5_questions)) + ' questoes')
