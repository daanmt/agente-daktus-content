"""Script temporario: insere 5 novas orientacoes no JSON da ficha ginecologia."""

import json
import sys

path = r'C:\Users\daanm\Daktus\agente-daktus-content\especialidades\ginecologia\jsons\amil-ficha-ginecologia-v1.0.0.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Locate the Medico conduct node
conduct_node = None
for node in data.get('nodes', []):
    if node.get('type') == 'conduct' and 'dico' in node.get('data', {}).get('label', ''):
        conduct_node = node
        break

if not conduct_node:
    print('ERROR: Conduct node not found', file=sys.stderr)
    sys.exit(1)

oris = conduct_node['data']['condutaDataNode']['orientacao']
print(f'Orientacoes atuais: {len(oris)}')
print(f'Ultima: {oris[-1]["nome"]}')

# --- 5 novas orientacoes ---

new_orientacoes = [
    {
        "id": "2130cb40-af9d-4083-aa72-a4714e62a4f6",
        "nome": "Infertilidade e investigação da fertilidade",
        "descricao": "",
        "condicional": "visivel",
        "condicao": "infertilidade_associada is True",
        "narrativa": (
            "<p>A <strong>dificuldade para engravidar</strong> é definida como ausência de gestação após 12 meses de "
            "relações sexuais sem proteção (ou 6 meses se você tiver mais de 35 anos). Isso é mais comum do que parece "
            "\u2014 afeta cerca de 1 em cada 6 casais.</p>"
            "<p><strong>Por onde começa a investigação?</strong><br>A avaliação da fertilidade envolve os dois "
            "parceiros. Na mulher, exames hormonais (FSH, LH, estradiol, progesterona), ultrassom e, quando necessário, "
            "histeroscopia para avaliar o útero por dentro. No homem, o espermograma é o primeiro passo.</p>"
            "<p><strong>O que esperar do encaminhamento?</strong><br>O especialista em reprodução humana vai traçar um "
            "plano individualizado. Dependendo da causa, o tratamento pode ser clínico (medicamentos para ovulação), "
            "cirúrgico (correção de obstrução) ou por reprodução assistida (inseminação ou FIV). A avaliação não é "
            "dolorosa na maioria dos casos.</p>"
            "<p><strong>Fatores que ajudam:</strong> manter peso saudável, não fumar, controlar o estresse e evitar "
            "exposição a substâncias tóxicas. Idade importa \u2014 procure avaliação sem demora se tiver mais de 35 anos.</p>"
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
            "<p>A <strong>incontinência urinária</strong> \u2014 perda involuntária de urina \u2014 é muito mais comum "
            "do que as mulheres falam. Afeta até 1 em cada 3 mulheres em algum momento da vida e tem tratamento eficaz.</p>"
            "<p><strong>Dois tipos principais:</strong></p>"
            "<ul>"
            "<li><strong>Esforço:</strong> perda de urina ao tossir, espirrar, pular, rir. Causa: fraqueza do assoalho "
            "pélvico (músculos que sustentam a bexiga).</li>"
            "<li><strong>Urgência:</strong> vontade súbita e intensa de urinar, às vezes sem conseguir chegar ao "
            "banheiro a tempo. Causa: bexiga hiperativa.</li>"
            "</ul>"
            "<p><strong>Fisioterapia pélvica:</strong> é o tratamento de primeira escolha para incontinência de "
            "esforço. Exercícios específicos (Kegel) fortalecem o assoalho pélvico e resolvem ou melhoram "
            "significativamente os sintomas em 60\u201370% dos casos. Resultados aparecem em 6\u201312 semanas de "
            "prática regular.</p>"
            "<p><strong>Como fazer o exercício de Kegel:</strong> contraia os músculos que você usaria para interromper "
            "o xixi no meio. Segure por 5 segundos, relaxe por 5. Repita 10\u201315 vezes, 3 vezes ao dia. Não retenha "
            "a respiração.</p>"
            "<p>Para incontinência de urgência, existem medicamentos e técnicas de reeducação vesical. Converse com "
            "seu médico sobre a melhor opção para o seu caso.</p>"
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
            "<p>A <strong>insuficiência ovariana prematura (POI)</strong> \u2014 também chamada de menopausa precoce "
            "\u2014 é quando os ovários param de funcionar normalmente antes dos 40 anos. Pode causar menstruação "
            "irregular ou ausente, fogachos e dificuldade para engravidar.</p>"
            "<p><strong>Por que investigar com urgência?</strong><br>Sem estrogênio, os ossos perdem densidade "
            "rapidamente e o risco cardiovascular aumenta. O diagnóstico e o tratamento precoces protegem a saúde "
            "óssea, cardíaca e a qualidade de vida.</p>"
            "<p><strong>Fertilidade:</strong> o diagnóstico de POI não significa infertilidade absoluta. Em algumas "
            "mulheres, os ovários voltam a funcionar esporadicamente. Se há desejo de gestação, o encaminhamento para "
            "reprodução assistida deve ser feito rapidamente.</p>"
            "<p><strong>Terapia hormonal:</strong> diferente da menopausa natural, na POI a reposição hormonal é "
            "fortemente recomendada até pelo menos os 50 anos \u2014 não apenas para sintomas, mas para proteção de "
            "ossos e coração. Os riscos da TH nesse contexto são muito menores do que os riscos de não tratar.</p>"
            "<p>O acompanhamento com endocrinologista vai confirmar o diagnóstico, descartar outras causas e definir "
            "o tratamento ideal para você.</p>"
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
            "<p>Um resultado <strong>reagente ou positivo</strong> nas sorologias para hepatite B, hepatite C ou HIV "
            "não é um diagnóstico definitivo \u2014 é um sinal que precisa de investigação complementar. Na maioria "
            "dos casos, o resultado é confirmado por exames adicionais antes de qualquer conduta.</p>"
            "<p><strong>Hepatite B (HBsAg reagente):</strong> a hepatite B tem vacina e tratamento eficaz. Muitas "
            "pessoas convivem com o vírus por anos sem sintomas. O acompanhamento com especialista define se o vírus "
            "está ativo e se o tratamento é necessário. Familiares próximos devem ser vacinados.</p>"
            "<p><strong>Hepatite C (HCV reagente):</strong> hoje existe cura para a hepatite C \u2014 em mais de 95% "
            "dos casos, com medicamentos orais de curta duração (8\u201312 semanas). O tratamento impede a progressão "
            "para cirrose e câncer de fígado.</p>"
            "<p><strong>HIV reagente:</strong> o HIV é uma infecção crônica controlável. Com tratamento (TARV), as "
            "pessoas vivem décadas com qualidade de vida normal e não transmitem o vírus. O tratamento é gratuito pelo "
            "SUS. Quanto antes iniciado, melhor o prognóstico.</p>"
            "<p>O encaminhamento ao especialista será feito ainda nessa consulta. Não adie \u2014 o diagnóstico "
            "precoce muda completamente o curso dessas doenças.</p>"
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
            "<p>O <strong>hiperandrogenismo</strong> é o excesso de hormônios masculinos (androgênios) na mulher. "
            "Pode se manifestar como acne persistente, pelos em excesso (hirsutismo), queda de cabelo com padrão "
            "masculino ou, em casos mais intensos, engrossamento da voz e aumento do clitóris.</p>"
            "<p><strong>Causas mais comuns:</strong> Síndrome dos Ovários Policísticos (SOP) \u2014 a mais frequente. "
            "Hiperplasia adrenal congênita de início tardio. Em casos raros, tumor produtor de androgênios (suspeitar "
            "quando os sintomas surgem de forma rápida e intensa).</p>"
            "<p><strong>Quando é urgente:</strong> Virilização de início rápido (semanas a poucos meses) é um sinal "
            "de alerta que requer investigação imediata. Nesse caso, o encaminhamento ao especialista deve ser "
            "prioritário.</p>"
            "<p><strong>Tratamento:</strong> depende da causa. SOP responde bem a anticoncepcionais hormonais, "
            "metformina e mudanças no estilo de vida. Para hirsutismo, antiandrógenos (como espironolactona) reduzem "
            "os pelos ao longo de meses. Métodos cosméticos (laser, cera) podem ser usados em conjunto com o "
            "tratamento médico.</p>"
            "<p>Os exames solicitados nessa consulta (testosterona, DHEA-S, 17-OHP) ajudarão o especialista a "
            "identificar a origem do problema.</p>"
        ),
        "conteudo": ""
    }
]

# Insert the 5 new orientacoes before the last item (Orientacao geral de saude)
for ori in reversed(new_orientacoes):
    oris.insert(-1, ori)

# Save
with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\nSalvo. Verificando...')

# Verify
with open(path, encoding='utf-8') as f:
    data2 = json.load(f)

for node in data2.get('nodes', []):
    if node.get('type') == 'conduct' and 'dico' in node.get('data', {}).get('label', ''):
        oris2 = node['data']['condutaDataNode']['orientacao']
        print(f'Novo total de orientacoes: {len(oris2)}')
        print('Lista:')
        for i, o in enumerate(oris2, 1):
            nome = o.get('nome', '?')
            cond = o.get('condicao', '(empty)')[:80]
            print(f'  {i:2}. {nome}')
            print(f'      cond: {cond}')

print('\nJSON valido e salvo com sucesso.')
