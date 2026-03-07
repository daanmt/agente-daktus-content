import json

filepath = 'especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v1.0.0.json'
d = json.load(open(filepath, encoding='utf-8'))

no3_questions = [
  {
    'id': 'P6cfba8d8-1419-40f6-9596-755a5eb62556',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'tipo_consulta_confirmacao',
    'titulo': '<p><strong>Esta consulta é:</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'choice',
    'options': [
      {'iid': 'c5c824ca-e71c-4b3c-9106-f7f64752f306', 'id': 'primeira_consulta', 'label': 'Primeira consulta', 'preselected': False, 'exclusive': True},
      {'iid': '0c6d8b3a-e7ad-45c6-a63e-e1cb005b6c92', 'id': 'retorno_eletivo', 'label': 'Retorno eletivo', 'preselected': True, 'exclusive': True},
      {'iid': '36965bd3-bcdf-4908-b3d5-665fc6ca88ce', 'id': 'retorno_urgente', 'label': 'Retorno urgente / intercorrência', 'preselected': False, 'exclusive': True},
      {'iid': 'da64811b-2863-49c5-bd2a-f85c093e8d74', 'id': 'alta_hospitalar', 'label': 'Alta hospitalar — primeira consulta ambulatorial', 'preselected': False, 'exclusive': True}
    ]
  },
  {
    'id': 'Pcdcbde88-e1d4-4a61-8c08-0088773de093',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'diagnostico_ativo',
    'titulo': '<p><strong>Diagnóstico(s) ativo(s) do paciente (CID-10)</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'multiChoice',
    'options': [
      {'iid': '4c05ef0c-8be7-4cfb-b5cb-e71c6c905a03', 'id': 'sem_diagnostico', 'label': 'Sem diagnóstico definido / avaliação inicial', 'preselected': False, 'exclusive': True},
      {'iid': 'b404124a-8417-4bdf-aedd-474b16feb2e8', 'id': 'tdm', 'label': 'TDM / Depressão maior (F32–F33)', 'preselected': False, 'exclusive': False},
      {'iid': 'c6316fe6-97ae-4ad8-91fb-3d69afe92ec4', 'id': 'distimia', 'label': 'Distimia / TDP (F34.1)', 'preselected': False, 'exclusive': False},
      {'iid': '5e3dbaf0-4b37-43e5-b287-2ca5d9103f38', 'id': 'tab', 'label': 'TAB I ou II (F31)', 'preselected': False, 'exclusive': False},
      {'iid': '76ff2f30-66ec-4ee0-9cb8-2e7abce6bb8d', 'id': 'tag', 'label': 'TAG (F41.1)', 'preselected': False, 'exclusive': False},
      {'iid': '3b572347-d5ac-49c6-8fa0-d9bf04517be4', 'id': 'panico', 'label': 'Transtorno do pânico (F41.0)', 'preselected': False, 'exclusive': False},
      {'iid': 'b2d2ea6b-5d74-4ddb-b74b-9b98ac2d4500', 'id': 'fobia_social', 'label': 'Fobia social (F40.1)', 'preselected': False, 'exclusive': False},
      {'iid': '407c55f6-af4d-480e-9b8e-7d219758dc3c', 'id': 'toc', 'label': 'TOC (F42)', 'preselected': False, 'exclusive': False},
      {'iid': 'a09ed6f8-bc7b-45cc-b94f-41fde578c7cc', 'id': 'tept', 'label': 'TEPT (F43.1)', 'preselected': False, 'exclusive': False},
      {'iid': 'd00f96e5-629b-4583-9115-166a51ae4dc4', 'id': 'burnout', 'label': 'Burnout (Z73.0)', 'preselected': False, 'exclusive': False},
      {'iid': '8290d80b-4175-495c-a3fa-1b01e10f4486', 'id': 'esquizofrenia', 'label': 'Esquizofrenia / esq. afetivo (F20–F25)', 'preselected': False, 'exclusive': False},
      {'iid': '9b54ad92-6709-4140-a1ef-a316ef28021a', 'id': 'tdah', 'label': 'TDAH (F90.0)', 'preselected': False, 'exclusive': False},
      {'iid': '44c0b441-21ee-4b19-996a-abca6f201c2d', 'id': 'tea', 'label': 'TEA (F84)', 'preselected': False, 'exclusive': False},
      {'iid': '7b01836e-5259-4449-bb5b-f3ee2911c834', 'id': 'tpb', 'label': 'TPB / Borderline (F60.3)', 'preselected': False, 'exclusive': False},
      {'iid': 'eb471af7-665e-42cd-ba75-58735c590dfe', 'id': 'ta_anorexia', 'label': 'Anorexia nervosa (F50.0)', 'preselected': False, 'exclusive': False},
      {'iid': '7b9c8f9c-bbda-45e8-9f49-253f5ee12060', 'id': 'ta_bulimia', 'label': 'Bulimia nervosa (F50.2)', 'preselected': False, 'exclusive': False},
      {'iid': 'e0582489-cee3-48c8-b22d-18982a174ad1', 'id': 'ta_tcap', 'label': 'TCAP (F50.8)', 'preselected': False, 'exclusive': False},
      {'iid': '5bbaef1a-4506-4893-bdae-d673f99aeabe', 'id': 'uso_substancias', 'label': 'Transtorno por uso de substâncias (F10–F19)', 'preselected': False, 'exclusive': False}
    ]
  },
  {
    'id': 'P4f8e8427-8530-49d4-93fe-6efac9115ab8',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'medicamentos_em_uso',
    'titulo': '<p><strong>Psicofármacos em uso atual</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'multiChoice',
    'options': [
      {'iid': '011bd37f-86a3-4886-ba71-8839036567e4', 'id': 'sem_psicofarmacos', 'label': 'Sem psicofármacos', 'preselected': False, 'exclusive': True},
      {'iid': '7fd743ce-fbd2-4a9f-bc7f-088dd800d6aa', 'id': 'litio', 'label': 'Lítio (carbonato)', 'preselected': False, 'exclusive': False},
      {'iid': '7c39ba81-70c2-4a79-ac35-198565d6c08b', 'id': 'valproato', 'label': 'Valproato / ácido valpróico', 'preselected': False, 'exclusive': False},
      {'iid': 'c67aa1cf-efac-4ec7-a356-02a0e7bd6766', 'id': 'lamotrigina', 'label': 'Lamotrigina', 'preselected': False, 'exclusive': False},
      {'iid': 'ee20eba6-9f12-4c35-aa8e-abaace8351a3', 'id': 'carbamazepina', 'label': 'Carbamazepina', 'preselected': False, 'exclusive': False},
      {'iid': 'b973cc3b-5ffc-482d-bf87-38e1154fdda8', 'id': 'clozapina', 'label': 'Clozapina', 'preselected': False, 'exclusive': False},
      {'iid': '6fcdda56-936e-4b9e-a9a1-f2d1acfcf824', 'id': 'ap_atipico_olanzapina', 'label': 'Olanzapina', 'preselected': False, 'exclusive': False},
      {'iid': '1d049ff8-5edd-42b5-97b7-b855e2ef0aca', 'id': 'ap_atipico_quetiapina', 'label': 'Quetiapina', 'preselected': False, 'exclusive': False},
      {'iid': 'a63b6089-545f-412f-9e13-de7c9fe991e5', 'id': 'ap_atipico_risperidona', 'label': 'Risperidona / Paliperidona', 'preselected': False, 'exclusive': False},
      {'iid': 'b61a497c-43c0-47e2-8f1b-5224cddf1c5b', 'id': 'ap_atipico_aripiprazol', 'label': 'Aripiprazol', 'preselected': False, 'exclusive': False},
      {'iid': '554cf279-e822-45e2-9592-a11cf9ec26b1', 'id': 'ap_atipico_ziprasidona', 'label': 'Ziprasidona', 'preselected': False, 'exclusive': False},
      {'iid': '1af4837a-7c86-414c-9cf8-1c9ccafc83ee', 'id': 'ap_tipico', 'label': 'Antipsicótico típico (haloperidol, clorpromazina)', 'preselected': False, 'exclusive': False},
      {'iid': '804ddf14-b462-4261-8138-a6e7d3c5734e', 'id': 'isrs', 'label': 'ISRS (fluoxetina, sertralina, escitalopram, paroxetina, fluvoxamina)', 'preselected': False, 'exclusive': False},
      {'iid': '03bb54dd-7179-4eb7-a63c-9fdf56c9e581', 'id': 'irsn', 'label': 'IRSN (venlafaxina, duloxetina)', 'preselected': False, 'exclusive': False},
      {'iid': '92d1157b-eb47-4f4b-818a-1213f3531086', 'id': 'bupropiona', 'label': 'Bupropiona', 'preselected': False, 'exclusive': False},
      {'iid': '77ac1648-a65a-40eb-a07b-74937d140c4e', 'id': 'mirtazapina', 'label': 'Mirtazapina', 'preselected': False, 'exclusive': False},
      {'iid': '43203425-08cc-4644-917c-016271ad98bb', 'id': 'antidepressivo_tca', 'label': 'Antidepressivo tricíclico (clomipramina, amitriptilina)', 'preselected': False, 'exclusive': False},
      {'iid': '2c6dbc35-6a82-479d-b1de-a8e3de6276da', 'id': 'estimulante', 'label': 'Estimulante (metilfenidato, lisdexanfetamina)', 'preselected': False, 'exclusive': False},
      {'iid': '6d9bd8a4-26c4-453f-93a5-31cea26c76a8', 'id': 'atomoxetina', 'label': 'Atomoxetina / Guanfacina', 'preselected': False, 'exclusive': False},
      {'iid': '7d60b0b2-8a0f-4665-aafb-062876f9d716', 'id': 'bzd', 'label': 'Benzodiazepínico (clonazepam, lorazepam)', 'preselected': False, 'exclusive': False},
      {'iid': '905c9b14-57a5-41da-a111-bb83cf527634', 'id': 'outro_psicofarmacos', 'label': 'Outro psicofármaco', 'preselected': False, 'exclusive': False}
    ]
  },
  {
    'id': 'P8574364a-3130-4734-88bc-0de237b24da2',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'outros_medicamentos_relevantes',
    'titulo': '<p><strong>Outros medicamentos em uso com potencial de interação</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'multiChoice',
    'options': [
      {'iid': 'd7ed8aa6-8558-467c-b61f-af232515e370', 'id': 'nenhum', 'label': 'Nenhum relevante', 'preselected': True, 'exclusive': True},
      {'iid': '5ae06a49-d84b-4263-87d5-b7e306728f6b', 'id': 'aineis', 'label': 'AINEs (ibuprofeno, naproxeno)', 'preselected': False, 'exclusive': False},
      {'iid': '93386da8-575d-4825-b045-3102be581a2e', 'id': 'ieca_diuretico', 'label': 'IECA / Diuréticos', 'preselected': False, 'exclusive': False},
      {'iid': 'df5fb9f3-80a9-43c3-ac6a-6316a31e62f3', 'id': 'anticonvulsivantes', 'label': 'Anticonvulsivantes (não psiquiátricos)', 'preselected': False, 'exclusive': False},
      {'iid': '6d22bcc2-8171-4766-bf01-fc2cfbdbc193', 'id': 'contraceptivo_hormonal', 'label': 'Contraceptivo hormonal', 'preselected': False, 'exclusive': False},
      {'iid': '02ac6fb7-9c34-462e-b007-b782fc813538', 'id': 'tramadol', 'label': 'Tramadol / opioides', 'preselected': False, 'exclusive': False},
      {'iid': '336da1a7-c494-4327-ab21-1780c5434faa', 'id': 'ritonavir_ip', 'label': 'Ritonavir / inibidores de protease (HIV)', 'preselected': False, 'exclusive': False},
      {'iid': '56f0f1ca-3315-4220-831a-b11f9ac50a9a', 'id': 'amiodarona', 'label': 'Amiodarona', 'preselected': False, 'exclusive': False},
      {'iid': 'd95a9e8c-7e1d-4c4b-a2a5-50c7e9b79f13', 'id': 'qt_prolongante', 'label': 'Outros fármacos QT-prolongantes', 'preselected': False, 'exclusive': False}
    ]
  },
  {
    'id': 'P59a3f99f-e5c5-4c8f-a7a6-e70532e094d8',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'comorbidades_clinicas',
    'titulo': '<p><strong>Comorbidades clínicas relevantes</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'multiChoice',
    'options': [
      {'iid': '6fecd64e-cf3e-48ca-890a-a0d237b71d27', 'id': 'nenhuma', 'label': 'Nenhuma', 'preselected': True, 'exclusive': True},
      {'iid': '51832071-6a8c-4b5d-9aab-d8ad36cfc8b3', 'id': 'hipotireoidismo', 'label': 'Hipotireoidismo', 'preselected': False, 'exclusive': False},
      {'iid': 'cae2f641-773c-4d27-980b-bb3f7dba1733', 'id': 'drc', 'label': 'DRC / insuficiência renal', 'preselected': False, 'exclusive': False},
      {'iid': '23ff567e-d6b7-4d8c-84e2-c2cebae10bac', 'id': 'diabetes', 'label': 'Diabetes mellitus', 'preselected': False, 'exclusive': False},
      {'iid': '777f63f3-9799-4670-ac41-0c7313a2e1c1', 'id': 'dislipidemia', 'label': 'Dislipidemia / síndrome metabólica', 'preselected': False, 'exclusive': False},
      {'iid': 'cb215290-2d77-4cec-82c1-3ed2ef391416', 'id': 'epilepsia', 'label': 'Epilepsia', 'preselected': False, 'exclusive': False},
      {'iid': 'ac15197c-620b-4735-a950-72d6971b7534', 'id': 'cardiopatia', 'label': 'Cardiopatia estrutural / arritmia', 'preselected': False, 'exclusive': False},
      {'iid': 'd8fd1b3b-54e1-49ed-99cc-6733436970ac', 'id': 'hiv', 'label': 'HIV', 'preselected': False, 'exclusive': False},
      {'iid': '51d325ac-f3fd-4bba-9788-da69fc47f5ab', 'id': 'obesidade', 'label': 'Obesidade (IMC ≥30)', 'preselected': False, 'exclusive': False}
    ]
  },
  {
    'id': 'P9379161a-c76c-4ed7-9f90-f21478133524',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'sexo_feminino_ie',
    'titulo': '<p><strong>Mulher em idade fértil (12–55 anos)?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "sex == 'female' and age >= 12 and age <= 55",
    'select': 'choice',
    'options': [
      {'iid': '1ab278f3-8fb5-468d-b8be-16584ebf87d6', 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': '92687061-5caa-4149-9e4e-153a8526ad4a', 'id': 'nao', 'label': 'Não', 'preselected': False, 'exclusive': True}
    ]
  },
  {
    'id': 'P290063fe-e887-4069-afd2-6599965042ad',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'gestante',
    'titulo': '<p><strong>Gestante atual?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "sexo_feminino_ie == 'sim'",
    'select': 'choice',
    'options': [
      {'iid': 'bbef6588-e07b-4b57-81fc-2b60613d3681', 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': '6389eae7-55f7-48ca-9a50-f6dab9fe407b', 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True}
    ]
  },
  {
    'id': 'P04955ba5-dc89-458b-a533-7980a4721d56',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'substancias_uso',
    'titulo': '<p><strong>Uso de substâncias psicoativas</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'multiChoice',
    'options': [
      {'iid': 'a89be55e-65b1-499e-8796-b362d3e6cd83', 'id': 'nenhum', 'label': 'Nenhum', 'preselected': True, 'exclusive': True},
      {'iid': '1eb03690-eb25-4809-ae02-5dc9fb461862', 'id': 'alcool_uso_problematico', 'label': 'Álcool (uso problemático / dependência)', 'preselected': False, 'exclusive': False},
      {'iid': '53b9bb51-164c-4f35-93b3-1adcb5bc56a3', 'id': 'cannabis', 'label': 'Cannabis', 'preselected': False, 'exclusive': False},
      {'iid': 'dde8387d-ccdc-40c0-a310-85b7a10826a5', 'id': 'cocaina_crack', 'label': 'Cocaína / crack', 'preselected': False, 'exclusive': False},
      {'iid': 'a93b7150-d5d4-4fa6-89f5-d5552919f7ef', 'id': 'outras_drogas', 'label': 'Outras drogas', 'preselected': False, 'exclusive': False},
      {'iid': '165e2978-d176-4049-b745-8f4d6de4a4c1', 'id': 'tabaco', 'label': 'Tabagismo', 'preselected': False, 'exclusive': False}
    ]
  },
  {
    'id': 'P2cd97e60-6cd1-4743-8a83-f43c31e1bf05',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'internacao_psiq_previa',
    'titulo': '<p><strong>Internação psiquiátrica prévia?</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'choice',
    'options': [
      {'iid': 'c9364380-7472-4bd0-86e3-01e7804c0bf1', 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': '77b9ab98-cc34-494b-b138-b7325b27124c', 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True}
    ]
  },
  {
    'id': 'P7db33f7c-c4d1-4ba1-8391-88819b3e5657',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'phq9_score',
    'titulo': '<p><strong>PHQ-9 score (se aplicado nesta consulta)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "('tdm' in diagnostico_ativo) or ('distimia' in diagnostico_ativo) or ('burnout' in diagnostico_ativo)",
    'select': 'number',
    'options': [],
    'opcional': True
  },
  {
    'id': 'Pf48216db-9552-4c5f-8bae-40a4894a6c0e',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'mdq_aplicado',
    'titulo': '<p><strong>MDQ aplicado?</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "('tdm' in diagnostico_ativo) or ('distimia' in diagnostico_ativo)",
    'select': 'choice',
    'options': [
      {'iid': '1853936c-6acc-4068-b9bb-94c9ff9de831', 'id': 'sim_positivo', 'label': 'Sim — MDQ positivo (suspeita de TAB)', 'preselected': False, 'exclusive': True},
      {'iid': 'e3158cea-d3a2-432b-84f4-37f9e4b36dbe', 'id': 'sim_negativo', 'label': 'Sim — MDQ negativo', 'preselected': False, 'exclusive': True},
      {'iid': 'c774044d-a994-4017-9850-0e80ba04bc62', 'id': 'nao_aplicado', 'label': 'Não aplicado nesta consulta', 'preselected': True, 'exclusive': True}
    ]
  },
  {
    'id': 'Pcd73d00b-8e4a-4085-a3a5-22576db598f7',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'audit_score',
    'titulo': '<p><strong>AUDIT score (se aplicado)</strong></p>',
    'descricao': '',
    'condicional': 'condicional',
    'expressao': "'alcool_uso_problematico' in substancias_uso",
    'select': 'number',
    'options': [],
    'opcional': True
  },
  {
    'id': 'Pa69635de-0d0c-4655-b273-d3fd9c3912d8',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'primeira_consulta_vida',
    'titulo': '<p><strong>Primeira consulta psiquiátrica em vida?</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'choice',
    'options': [
      {'iid': '800e8a74-415e-44b9-8a38-821e950299e0', 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': '1b7414ee-efe7-4992-9623-22f07558ac38', 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True}
    ]
  },
  {
    'id': 'P72a1098d-416e-46a5-be84-7e2c116ae102',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'encaminhamento_urgencia_necessario',
    'titulo': '<p><strong>Encaminhamento de urgência necessário (além de Gate P0)?</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'choice',
    'options': [
      {'iid': '505ebb16-dcc0-4bdd-bca8-3733aad0d331', 'id': 'sim', 'label': 'Sim', 'preselected': False, 'exclusive': True},
      {'iid': 'be6d5ba4-5059-49de-8693-05209e0a3202', 'id': 'nao', 'label': 'Não', 'preselected': True, 'exclusive': True}
    ]
  },
  {
    'id': 'P684f542b-6b14-4a4c-96e3-4cf6983673b6',
    'nodeId': 'node-psiq-03-anamnese',
    'uid': 'observacoes_livres',
    'titulo': '<p><strong>Observações complementares (opcional)</strong></p>',
    'descricao': '',
    'condicional': 'visivel',
    'expressao': '',
    'select': 'string',
    'options': [],
    'opcional': True
  }
]

# Atualizar o nó 3
for node in d['nodes']:
    if node['id'] == 'node-psiq-03-anamnese':
        node['data']['questions'] = no3_questions
        node['data']['label'] = 'Anamnese Psiquiátrica'
        break

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('No 3 injetado com ' + str(len(no3_questions)) + ' questoes.')
