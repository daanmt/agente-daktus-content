"""Sessao 013: fixes de formatacao + re-insercao das 5 orientacoes da sessao 012
no JSON final da ficha ginecologia.

Fixes aplicados:
  FIX-1: MSG-21 (DIU contraindicado) — HTML duplamente escapado -> HTML correto
  FIX-2: MSG-18 (hrHPV nao-16/18 + cito negativa) — adicionar conteudo
  FIX-3: MSG-19 (NIC1 em colposcopia) — adicionar conteudo
  FIX-4: MSG-20 (citologia reflexa nao realizada) — adicionar conteudo
  FIX-5: ORI-1 (Rastreamento cervical) — remover emojis
  FIX-6: ORI-2 (Rastreamento de mama) — remover emojis
  FIX-7: ORI-3 (Climaterio e terapia hormonal) — remover emoji
  ORI-12..16: Re-inserir 5 orientacoes da sessao 012 (ausentes do JSON final)
"""

import json, sys

# ── Setup encoding para Windows cp1252 ──
def p(s):
    print(s.encode('utf-8', errors='replace').decode('utf-8', errors='replace'))

PATH = r'C:\Users\daanm\Daktus\agente-daktus-content\especialidades\ginecologia\jsons\amil-ficha_ginecologia-v1.0.0-final.json'

with open(PATH, encoding='utf-8') as f:
    data = json.load(f)

conduct_node = None
for node in data.get('nodes', []):
    if node.get('type') == 'conduct' and 'dico' in node.get('data', {}).get('label', ''):
        conduct_node = node
        break

if not conduct_node:
    print('ERRO: no conduct nao encontrado', file=sys.stderr)
    sys.exit(1)

cdata = conduct_node['data']['condutaDataNode']
mensagens = cdata['mensagem']
orientacoes = cdata['orientacao']

print(f'Estado inicial: {len(mensagens)} mensagens, {len(orientacoes)} orientacoes')

# ═══════════════════════════════════════════════════════════
# FIXES DE MENSAGENS (medico)
# ═══════════════════════════════════════════════════════════

MSG21_ID = '365cc93f-3518-41c8-b7b2-4c8eabf16e6f'
MSG21_HTML = (
    '<p><strong>Inser\u00e7\u00e3o de DIU contraindicada no momento.</strong> '
    'Revisar antes de agendar procedimento:</p>'
    '<ul>'
    '<li><strong>Gesta\u00e7\u00e3o:</strong> contraindica\u00e7\u00e3o absoluta. '
    'Confirmar com beta-HCG se d\u00favida.</li>'
    '<li><strong>DIP ativa:</strong> tratar infec\u00e7\u00e3o e reavaliar ap\u00f3s '
    'cura cl\u00ednica (m\u00ednimo 3 meses).</li>'
    '<li><strong>Sangramento n\u00e3o investigado:</strong> investigar causa '
    '(ultrassom \u00b1 histeroscopia) antes da inser\u00e7\u00e3o.</li>'
    '<li><strong>Distor\u00e7\u00e3o da cavidade:</strong> histeroscopia diagn\u00f3stica '
    'para avalia\u00e7\u00e3o e poss\u00edvel corre\u00e7\u00e3o.</li>'
    '<li><strong>C\u00e2ncer de mama atual:</strong> DIU de cobre (n\u00e3o hormonal) '
    'pode ser considerado \u2014 discutir com oncologista.</li>'
    '</ul>'
)

MSG18_ID = '876612d6-3eca-412c-9846-9ce779187a21'
MSG18_HTML = (
    '<p>hrHPV n\u00e3o-16/18 com citologia reflexa negativa. Risco baixo de les\u00e3o '
    'de alto grau. Co-teste (HPV + citologia) em 1 ano. N\u00e3o solicitar colposcopia '
    'neste momento.</p>'
)

MSG19_ID = '0ae591fa-24b2-424e-80d7-d07e017db569'
MSG19_HTML = (
    '<p>NIC1 confirmado \u00e0 bi\u00f3psia \u2014 les\u00e3o de baixo grau. Tratamento '
    'imediato n\u00e3o indicado: regress\u00e3o espont\u00e2nea em 60\u201380% dos casos. '
    'Seguimento: colposcopia em 6 e 12 meses. Tratar apenas se persist\u00eancia superior '
    'a 2 anos ou progress\u00e3o histol\u00f3gica documentada.</p>'
)

MSG20_ID = '11bbb9f5-25d2-44de-9899-f013c373813d'
MSG20_HTML = (
    '<p>hrHPV n\u00e3o-16/18 sem citologia reflexa. Pend\u00eancia ativa: coletar '
    'citologia cervical convencional nesta consulta. N\u00e3o encerrar sem coleta. '
    'Registrar resultado para ativar a conduta correta '
    '(ver alerta \u201cConduta: citologia reflexa \u2014 resultado\u201d).</p>'
)

MSG_FIXES = {
    MSG21_ID: MSG21_HTML,
    MSG18_ID: MSG18_HTML,
    MSG19_ID: MSG19_HTML,
    MSG20_ID: MSG20_HTML,
}

fixes_msg = 0
for msg in mensagens:
    if msg['id'] in MSG_FIXES:
        msg['conteudo'] = MSG_FIXES[msg['id']]
        print(f'  MSG fix: {msg["nome"][:55]}')
        fixes_msg += 1

print(f'Mensagens corrigidas: {fixes_msg}/4')

# ═══════════════════════════════════════════════════════════
# FIXES DE ORIENTACOES — remover emojis
# ═══════════════════════════════════════════════════════════

# Emojis representados como Unicode para evitar problemas de encoding no Windows
EMOJI_MAP = {
    'd41b6155-1644-43c6-a4cb-7a13aab649ec': [  # ORI-1 cervical
        ('\U0001f4c5 Com que freq', 'Com que freq'),
        ('\U0001f52c O que significa HPV', 'O que significa HPV'),
    ],
    '1ad6c1c9-bc1d-428e-8d99-81b2b9f03bc1': [  # ORI-2 mama
        ('\U0001f440 O que observar', 'O que observar'),
        ('\U0001f4c5 Mamografia', 'Mamografia'),
    ],
    'a67d96a8-8cb9-4bd7-ac3c-2b37a87b24a1': [  # ORI-3 climaterio
        ('\U0001f48a Terapia Hormonal', 'Terapia Hormonal'),
    ],
}

fixes_ori = 0
for ori in orientacoes:
    if ori['id'] in EMOJI_MAP:
        for (old_suffix, new_suffix) in EMOJI_MAP[ori['id']]:
            # Busca generica por prefixo de emoji
            narrativa = ori['narrativa']
            # Percorre e faz replace manual para evitar problemas de encoding
            import re
            # Pattern: emoji seguido de espaco e texto
            old_emoji = old_suffix[0]  # primeiro char e o emoji
            old_rest = old_suffix[1:]  # resto do padrao
            new_text = new_suffix

            # Verificar se narrativa contem o padrao
            if old_suffix in narrativa:
                ori['narrativa'] = narrativa.replace(old_suffix, new_suffix)
                fixes_ori += 1
                print(f'  ORI emoji fix: "{new_suffix[:30]}" em {ori["nome"][:30]}')

print(f'Substituicoes emoji: {fixes_ori}/5 esperadas')

# ═══════════════════════════════════════════════════════════
# RE-INSERIR 5 ORIENTACOES DA SESSAO 012
# (ausentes do JSON final exportado pelo Gabriel)
# ═══════════════════════════════════════════════════════════

NOVAS_ORI = [
    {
        "id": "2130cb40-af9d-4083-aa72-a4714e62a4f6",
        "nome": "Infertilidade e investiga\u00e7\u00e3o da fertilidade",
        "descricao": "",
        "condicional": "visivel",
        "condicao": "infertilidade_associada is True",
        "narrativa": (
            "<p>A <strong>dificuldade para engravidar</strong> \u00e9 definida como aus\u00eancia "
            "de gesta\u00e7\u00e3o ap\u00f3s 12 meses de rela\u00e7\u00f5es sexuais sem "
            "prote\u00e7\u00e3o (ou 6 meses se voc\u00ea tiver mais de 35 anos). Isso \u00e9 "
            "mais comum do que parece \u2014 afeta cerca de 1 em cada 6 casais.</p>"
            "<p><strong>Por onde come\u00e7a a investiga\u00e7\u00e3o?</strong><br>A avalia\u00e7\u00e3o "
            "da fertilidade envolve os dois parceiros. Na mulher, exames hormonais (FSH, LH, "
            "estradiol, progesterona), ultrassom e, quando necess\u00e1rio, histeroscopia para "
            "avaliar o \u00fatero por dentro. No homem, o espermograma \u00e9 o primeiro passo.</p>"
            "<p><strong>O que esperar do encaminhamento?</strong><br>O especialista em reprodu\u00e7\u00e3o "
            "humana vai tra\u00e7ar um plano individualizado. Dependendo da causa, o tratamento pode "
            "ser cl\u00ednico (medicamentos para ovula\u00e7\u00e3o), cir\u00fargico (corre\u00e7\u00e3o "
            "de obstru\u00e7\u00e3o) ou por reprodu\u00e7\u00e3o assistida (insemina\u00e7\u00e3o ou "
            "FIV). A avalia\u00e7\u00e3o n\u00e3o \u00e9 dolorosa na maioria dos casos.</p>"
            "<p><strong>Fatores que ajudam:</strong> manter peso saud\u00e1vel, n\u00e3o fumar, "
            "controlar o estresse e evitar exposi\u00e7\u00e3o a subst\u00e2ncias t\u00f3xicas. "
            "Idade importa \u2014 procure avalia\u00e7\u00e3o sem demora se tiver mais de 35 anos.</p>"
        ),
        "conteudo": ""
    },
    {
        "id": "3c8161e7-c619-4123-957b-c3257ef9792a",
        "nome": "Incontinência urinária",
        "descricao": "",
        "condicional": "visivel",
        "condicao": "incontinencia_urinaria is True",
        "narrativa": (
            "<p>A <strong>incontinência urinária</strong> \u2014 perda involuntária de urina \u2014 "
            "é muito mais comum do que as mulheres falam. Afeta até 1 em cada 3 mulheres em "
            "algum momento da vida e tem tratamento eficaz.</p>"
            "<p><strong>Dois tipos principais:</strong></p>"
            "<ul>"
            "<li><strong>Esforço:</strong> perda de urina ao tossir, espirrar, pular, rir. Causa: "
            "fraqueza do assoalho pélvico (músculos que sustentam a bexiga).</li>"
            "<li><strong>Urgência:</strong> vontade súbita e intensa de urinar, às vezes sem "
            "conseguir chegar ao banheiro a tempo. Causa: bexiga hiperativa.</li>"
            "</ul>"
            "<p><strong>Fisioterapia pélvica:</strong> é o tratamento de primeira escolha para "
            "incontinência de esforço. Exercícios específicos (Kegel) fortalecem o assoalho "
            "pélvico e resolvem ou melhoram significativamente os sintomas em 60\u201370% dos "
            "casos. Resultados aparecem em 6\u201312 semanas de prática regular.</p>"
            "<p><strong>Como fazer o exercício de Kegel:</strong> contraia os músculos que você "
            "usaria para interromper o xixi no meio. Segure por 5 segundos, relaxe por 5. "
            "Repita 10\u201315 vezes, 3 vezes ao dia. Não retenha a respiração.</p>"
            "<p>Para incontinência de urgência, existem medicamentos e técnicas de reeducação "
            "vesical. Converse com seu médico sobre a melhor opção para o seu caso.</p>"
        ),
        "conteudo": ""
    },
    {
        "id": "786fe125-0271-4cd5-82c8-d50ca75f10d7",
        "nome": "Insuficiência ovariana prematura (POI)",
        "descricao": "",
        "condicional": "visivel",
        "condicao": "poi_suspeita is True",
        "narrativa": (
            "<p>A <strong>insuficiência ovariana prematura (POI)</strong> \u2014 também chamada de "
            "menopausa precoce \u2014 é quando os ovários param de funcionar normalmente antes "
            "dos 40 anos. Pode causar menstruação irregular ou ausente, fogachos e dificuldade "
            "para engravidar.</p>"
            "<p><strong>Por que investigar com urgência?</strong><br>Sem estrogênio, os ossos "
            "perdem densidade rapidamente e o risco cardiovascular aumenta. O diagnóstico e o "
            "tratamento precoces protegem a saúde óssea, cardíaca e a qualidade de vida.</p>"
            "<p><strong>Fertilidade:</strong> o diagnóstico de POI não significa infertilidade "
            "absoluta. Em algumas mulheres, os ovários voltam a funcionar esporadicamente. Se há "
            "desejo de gestação, o encaminhamento para reprodução assistida deve ser feito "
            "rapidamente.</p>"
            "<p><strong>Terapia hormonal:</strong> diferente da menopausa natural, na POI a "
            "reposição hormonal é fortemente recomendada até pelo menos os 50 anos \u2014 não "
            "apenas para sintomas, mas para proteção de ossos e coração. Os riscos da TH nesse "
            "contexto são muito menores do que os riscos de não tratar.</p>"
            "<p>O acompanhamento com endocrinologista vai confirmar o diagnóstico, descartar "
            "outras causas e definir o tratamento ideal para você.</p>"
        ),
        "conteudo": ""
    },
    {
        "id": "d57bef31-cb76-4c65-9b39-89d5b3f4bf4a",
        "nome": "Hepatites virais e HIV: sorologias alteradas",
        "descricao": "",
        "condicional": "visivel",
        "condicao": "('hiv_reagente' in hiv_resultado) or ('hbsag_reagente' in hbsag_resultado) or ('hcv_reagente' in hcv_resultado)",
        "narrativa": (
            "<p>Um resultado <strong>reagente ou positivo</strong> nas sorologias para hepatite B, "
            "hepatite C ou HIV não é um diagnóstico definitivo \u2014 é um sinal que precisa de "
            "investigação complementar. Na maioria dos casos, o resultado é confirmado por exames "
            "adicionais antes de qualquer conduta.</p>"
            "<p><strong>Hepatite B (HBsAg reagente):</strong> a hepatite B tem vacina e tratamento "
            "eficaz. Muitas pessoas convivem com o vírus por anos sem sintomas. O acompanhamento "
            "com especialista define se o vírus está ativo e se o tratamento é necessário. "
            "Familiares próximos devem ser vacinados.</p>"
            "<p><strong>Hepatite C (HCV reagente):</strong> hoje existe cura para a hepatite C "
            "\u2014 em mais de 95% dos casos, com medicamentos orais de curta duração "
            "(8\u201312 semanas). O tratamento impede a progressão para cirrose e câncer de "
            "fígado.</p>"
            "<p><strong>HIV reagente:</strong> o HIV é uma infecção crônica controlável. Com "
            "tratamento (TARV), as pessoas vivem décadas com qualidade de vida normal e não "
            "transmitem o vírus. O tratamento é gratuito pelo SUS. Quanto antes iniciado, melhor "
            "o prognóstico.</p>"
            "<p>O encaminhamento ao especialista será feito ainda nessa consulta. Não adie "
            "\u2014 o diagnóstico precoce muda completamente o curso dessas doenças.</p>"
        ),
        "conteudo": ""
    },
    {
        "id": "1538f488-00ea-49a1-a0f0-dafd25b977ec",
        "nome": "Hiperandrogenismo e virilização",
        "descricao": "",
        "condicional": "visivel",
        "condicao": "not 'sem_sinais' in hiperandrogenismo_sinais",
        "narrativa": (
            "<p>O <strong>hiperandrogenismo</strong> é o excesso de hormônios masculinos "
            "(androgênios) na mulher. Pode se manifestar como acne persistente, pelos em excesso "
            "(hirsutismo), queda de cabelo com padrão masculino ou, em casos mais intensos, "
            "engrossamento da voz e aumento do clitóris.</p>"
            "<p><strong>Causas mais comuns:</strong> Síndrome dos Ovários Policísticos (SOP) "
            "\u2014 a mais frequente. Hiperplasia adrenal congênita de início tardio. Em casos "
            "raros, tumor produtor de androgênios (suspeitar quando os sintomas surgem de forma "
            "rápida e intensa).</p>"
            "<p><strong>Quando é urgente:</strong> Virilização de início rápido (semanas a "
            "poucos meses) é um sinal de alerta que requer investigação imediata. Nesse caso, "
            "o encaminhamento ao especialista deve ser prioritário.</p>"
            "<p><strong>Tratamento:</strong> depende da causa. SOP responde bem a "
            "anticoncepcionais hormonais, metformina e mudanças no estilo de vida. Para "
            "hirsutismo, antiandrógenos (como espironolactona) reduzem os pelos ao longo de "
            "meses. Métodos cosméticos (laser, cera) podem ser usados em conjunto com o "
            "tratamento médico.</p>"
            "<p>Os exames solicitados nessa consulta (testosterona, DHEA-S, 17-OHP) ajudarão "
            "o especialista a identificar a origem do problema.</p>"
        ),
        "conteudo": ""
    }
]

# Inserir antes do ultimo item (Orientacao geral de saude)
ids_existentes = {o['id'] for o in orientacoes}
for ori in reversed(NOVAS_ORI):
    if ori['id'] not in ids_existentes:
        orientacoes.insert(-1, ori)
        print(f'  ORI inserida: {ori["nome"][:50]}')
    else:
        print(f'  ORI ja existe: {ori["nome"][:50]}')

# ═══════════════════════════════════════════════════════════
# SALVAR
# ═══════════════════════════════════════════════════════════

with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('\nSalvo. Verificando...')

# ── VERIFICACAO ──
with open(PATH, encoding='utf-8') as f:
    data2 = json.load(f)

for node in data2.get('nodes', []):
    if node.get('type') == 'conduct' and 'dico' in node.get('data', {}).get('label', ''):
        msgs2 = node['data']['condutaDataNode']['mensagem']
        oris2 = node['data']['condutaDataNode']['orientacao']

        # MSG-21 sem escape
        for m in msgs2:
            if m['id'] == MSG21_ID:
                assert '&lt;' not in m.get('conteudo', ''), 'ERRO: HTML ainda escapado!'
                print('  MSG-21 HTML: OK (sem &lt;)')

        # MSG-18, 19, 20 com conteudo
        for m in msgs2:
            if m['id'] in (MSG18_ID, MSG19_ID, MSG20_ID):
                assert m.get('conteudo'), f'ERRO: {m["nome"]} sem conteudo!'
                print(f'  {m["nome"][:50]}: OK')

        # Emojis ausentes nas orientacoes
        EMOJI_CHARS = ['\U0001f4c5', '\U0001f52c', '\U0001f440', '\U0001f48a']
        for ori in oris2:
            for em in EMOJI_CHARS:
                assert em not in ori.get('narrativa', ''), f'ERRO: emoji ainda em {ori["nome"]}'
        print('  Emojis nas orientacoes: nenhum encontrado OK')

        # 5 novas orientacoes presentes
        ids_novos = {o['id'] for o in NOVAS_ORI}
        ids_atuais = {o['id'] for o in oris2}
        faltando = ids_novos - ids_atuais
        assert not faltando, f'ERRO: orientacoes faltando: {faltando}'
        print(f'  5 orientacoes da s012: todas presentes OK')

        print(f'\nResultado final: {len(msgs2)} mensagens, {len(oris2)} orientacoes')
        print('Lista de orientacoes:')
        for i, o in enumerate(oris2, 1):
            print(f'  {i:2}. {o["nome"][:55]}')
        break

print('\nJSON valido e salvo com sucesso.')
