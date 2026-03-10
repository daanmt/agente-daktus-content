"""patch_vdraft2_to_v022.py
=========================
Produz amil-ficha_psiquiatria-v0.2.2.json a partir de vdraft (2).json.

INPUT:  C:\\Users\\daanm\\Downloads\\amil-ficha_psiquiatria-vdraft (2).json
OUTPUT: especialidades/psiquiatria/jsons/amil-ficha_psiquiatria-v0.2.2.json

OPERACOES:
  BUG FIX 1  — Schema normalization: 7 medicamentos com `conteudo`/`observacao`
               -> converter para `posologia`/`mensagemMedico`/`via`
  BUG FIX 2  — Aripiprazol: 1 item com 2 MEVOs -> dividir em Aripiprazol 10mg + 15mg
  BUG FIX 3  — `nomeMed` ausente em Quetiapina 50mg e Quetiapina 100mg -> preencher
  BUG FIX 4  — IDs nao-canonicos (cf9ooj5a, 5p6fdllf, 0k5sfwqn) -> substituir por UUID v4
  ADICAO     — 11 farmacos essenciais do playbook ausentes em vdraft
  METADATA   — version -> "0.2.2"

Sessao: session_022 -- 2026-03-10
"""

import json
import os
import sys
import io
import uuid

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

VDRAFT_PATH = r"C:\Users\daanm\Downloads\amil-ficha_psiquiatria-vdraft (2).json"
BASE = os.path.join(os.path.dirname(__file__), "..", "especialidades", "psiquiatria", "jsons")
OUTPUT_PATH = os.path.join(BASE, "amil-ficha_psiquiatria-v0.2.2.json")

NON_CANONICAL_IDS = {"cf9ooj5a", "5p6fdllf", "0k5sfwqn"}


def new_uuid():
    return str(uuid.uuid4())


# ---------------------------------------------------------------------------
# BUG FIX 1 — Schema normalization map
# Chave = nome exato do medicamento
# Valor = campos a adicionar/substituir
# ---------------------------------------------------------------------------
SCHEMA_FIX = {
    "Quetiapina 50 mg": {
        "nomeMed": "Quetiapina 50 mg",
        "posologia": "<p>50 mg/noite (dose de in\u00edcio).</p>",
        "mensagemMedico": (
            "<p>Estabilizador/antipsic\u00f3tico at\u00edpico. Titular para 100\u2013300 mg/dia (humor) "
            "ou 300\u2013800 mg/dia (psicose). Monitorar glicemia, lip\u00eddios e peso. "
            "Titula\u00e7\u00e3o lenta reduz seda\u00e7\u00e3o diurna.</p>"
        ),
        "via": "oral",
    },
    "Quetiapina 100 mg": {
        "nomeMed": "Quetiapina 100 mg",
        "posologia": "<p>100 mg/noite (dose intermedi\u00e1ria).</p>",
        "mensagemMedico": (
            "<p>Estabilizador/antipsic\u00f3tico at\u00edpico. Dose-alvo 100\u2013300 mg/dia (humor) "
            "ou 300\u2013800 mg/dia (psicose). Monitorar glicemia, lip\u00eddios e peso.</p>"
        ),
        "via": "oral",
    },
    "Olanzapina 5 mg": {
        "posologia": "<p>5 mg/noite (dose de in\u00edcio).</p>",
        "mensagemMedico": (
            "<p>Antipsic\u00f3tico at\u00edpico. Titular para 10\u201320 mg/dia. Alto risco metab\u00f3lico "
            "\u2014 monitorar glicemia, peso e lip\u00eddios a cada 3 meses. "
            "Evitar em diabetes ou s\u00edndrome metab\u00f3lica estabelecida.</p>"
        ),
        "via": "oral",
    },
    "Olanzapina 10 mg": {
        "posologia": "<p>10 mg/noite.</p>",
        "mensagemMedico": (
            "<p>Antipsic\u00f3tico at\u00edpico. Dose-alvo 10\u201320 mg/dia. Alto risco metab\u00f3lico "
            "\u2014 monitorar glicemia, peso e lip\u00eddios a cada 3 meses. "
            "Evitar em diabetes ou s\u00edndrome metab\u00f3lica estabelecida.</p>"
        ),
        "via": "oral",
    },
    "Risperidona 1 mg": {
        "posologia": "<p>1 mg/dia (dose de in\u00edcio).</p>",
        "mensagemMedico": (
            "<p>Antipsic\u00f3tico at\u00edpico. Titular para 2\u20136 mg/dia (psicose) "
            "ou 0,5\u20132 mg/dia (TEA). Monitorar EPS e hiperprolactinemia. "
            "Indica\u00e7\u00e3o ANVISA para irritabilidade grave no TEA.</p>"
        ),
        "via": "oral",
    },
    "Risperidona 2 mg": {
        "posologia": "<p>2 mg/dia.</p>",
        "mensagemMedico": (
            "<p>Antipsic\u00f3tico at\u00edpico. Dose-alvo 2\u20136 mg/dia (psicose) "
            "ou 0,5\u20132 mg/dia (TEA). Monitorar EPS e hiperprolactinemia.</p>"
        ),
        "via": "oral",
    },
}


def _make_codigo(mevo_code):
    """Retorna array de codigo para um MEVO code (str) ou [] se None."""
    if mevo_code:
        return [{"iid": new_uuid(), "sistema": "MEVO", "codigo": mevo_code, "nome": ""}]
    return []


def _make_med(
    nome, condicao, posologia, mensagemMedico, categoria,
    mevo_code=None, quantidade=1,
):
    """Cria um medicamento com schema canonico completo."""
    return {
        "id": new_uuid(),
        "nome": nome,
        "descricao": "",
        "condicional": "visivel",
        "condicao": condicao,
        "condicionalMedicamento": "domiciliar",
        "quantidade": quantidade,
        "codigo": _make_codigo(mevo_code),
        "nomeMed": nome,
        "posologia": posologia,
        "mensagemMedico": mensagemMedico,
        "via": "oral",
        "narrativa": "",
        "categorias": [
            {"iid": new_uuid(), "sistema": "", "codigo": "", "nome": categoria, "texto": ""}
        ],
    }


# ---------------------------------------------------------------------------
# BUG FIX 2 — Aripiprazol: substitui item duplo por 2 itens canonicos
# ---------------------------------------------------------------------------
ARIP_CONDICAO = "(esquizofrenia_refrataria is True) or selected_any(diagnostico_ativo, 'tab', 'tdm')"

ARIP_10 = _make_med(
    nome="Aripiprazol 10 mg",
    condicao=ARIP_CONDICAO,
    posologia="<p>10 mg/dia pela manh\u00e3 (dose de in\u00edcio).</p>",
    mensagemMedico=(
        "<p>Agonista parcial D2 \u2014 baixo risco metab\u00f3lico e de EPS. "
        "Titular para 15\u201330 mg/dia (psicose) ou 5\u201315 mg/dia (potencializa\u00e7\u00e3o). "
        "Prefer\u00eancia quando h\u00e1 risco de s\u00edndrome metab\u00f3lica ou ganho de peso.</p>"
    ),
    categoria="Antipsic\u00f3tico at\u00edpico",
    mevo_code="35461",
)

ARIP_15 = _make_med(
    nome="Aripiprazol 15 mg",
    condicao=ARIP_CONDICAO,
    posologia="<p>15 mg/dia pela manh\u00e3.</p>",
    mensagemMedico=(
        "<p>Agonista parcial D2. Dose-alvo 15\u201330 mg/dia (psicose) "
        "ou 5\u201315 mg/dia (potencializa\u00e7\u00e3o). Baixo risco metab\u00f3lico e de EPS.</p>"
    ),
    categoria="Antipsic\u00f3tico at\u00edpico",
    mevo_code="32613",
)


# ---------------------------------------------------------------------------
# ADICAO — 11 farmacos essenciais do playbook
# ---------------------------------------------------------------------------
NEW_MEDS = [
    # --- IRSN ---
    _make_med(
        nome="Venlafaxina XR 75mg",
        condicao=(
            "selected_any(diagnostico_ativo, 'tdm', 'tag', 'tept') "
            "and selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada', 'depressao_grave')"
        ),
        posologia="<p>75 mg/dia pela manh\u00e3 (2 c\u00e1psulas de 37,5 mg).</p>",
        mensagemMedico=(
            "<p>IRSN. Iniciar 37,5 mg/dia na 1\u00aa semana; aumentar para 75 mg/dia. "
            "Titular at\u00e9 150\u2013225 mg/dia se resposta parcial. "
            "N\u00e3o interromper abruptamente \u2014 reduzir gradualmente. "
            "MEVO de refer\u00eancia: 42348 (37,5 mg LP).</p>"
        ),
        categoria="IRSN",
        mevo_code="42348",
    ),
    _make_med(
        nome="Duloxetina 60mg",
        condicao=(
            "selected_any(diagnostico_ativo, 'tdm', 'tag') "
            "and selected_any(episodio_atual_humor, 'depressao_moderada', 'depressao_grave')"
        ),
        posologia="<p>60 mg/dia pela manh\u00e3.</p>",
        mensagemMedico=(
            "<p>IRSN. Iniciar 30 mg/dia na 1\u00aa semana. Titular at\u00e9 120 mg/dia se resposta parcial. "
            "\u00datil em dor neuropati\u00e7a comm\u00f3rbida. N\u00e3o interromper abruptamente.</p>"
        ),
        categoria="IRSN",
        mevo_code="35537",
    ),
    # --- IRND ---
    _make_med(
        nome="Bupropiona 150mg",
        condicao=(
            "selected_any(diagnostico_ativo, 'tdm', 'tdah') "
            "and selected_any(episodio_atual_humor, 'depressao_leve', 'depressao_moderada', 'depressao_grave')"
        ),
        posologia="<p>150 mg/dia pela manh\u00e3.</p>",
        mensagemMedico=(
            "<p>IRND. Titular para 300 mg/dia ap\u00f3s 1 semana. "
            "Contraindicado em epilepsia, bulimia ou anorexia. "
            "Pode ser usada como 2\u00aa linha no TDAH sem comorbidade an\u00edmica. "
            "C\u00f3digo MEVO n\u00e3o encontrado no cat\u00e1logo Amil (Mevo..xlsx).</p>"
        ),
        categoria="IRND",
        mevo_code=None,
    ),
    # --- NaSSA ---
    _make_med(
        nome="Mirtazapina 15mg",
        condicao=(
            "'tdm' in diagnostico_ativo "
            "and selected_any(episodio_atual_humor, 'depressao_moderada', 'depressao_grave')"
        ),
        posologia="<p>15 mg/noite (dose de in\u00edcio).</p>",
        mensagemMedico=(
            "<p>NaSSA. Efeito sedativo e orex\u00edgeno \u00fatil em depress\u00e3o com ins\u00f4nia e baixo peso. "
            "Titular para 30\u201345 mg/noite se resposta parcial. Cautela em obesidade. "
            "C\u00f3digo MEVO n\u00e3o encontrado no cat\u00e1logo Amil (Mevo..xlsx).</p>"
        ),
        categoria="NaSSA",
        mevo_code=None,
    ),
    # --- ISRS 2a linha ---
    _make_med(
        nome="Paroxetina 20mg",
        condicao="selected_any(diagnostico_ativo, 'tept', 'panico', 'fobia_social')",
        posologia="<p>20 mg/dia pela manh\u00e3.</p>",
        mensagemMedico=(
            "<p>ISRS. Titular at\u00e9 40\u201360 mg/dia se resposta parcial. "
            "Potente inibidor CYP2D6 \u2014 verificar intera\u00e7\u00f5es. "
            "N\u00e3o interromper abruptamente (s\u00edndrome de descontinua\u00e7\u00e3o).</p>"
        ),
        categoria="ISRS",
        mevo_code="8751",
    ),
    # --- Estabilizadores de humor ---
    _make_med(
        nome="Valproato de s\u00f3dio 500mg",
        condicao=(
            "'tab' in diagnostico_ativo "
            "and selected_any(episodio_atual_humor, 'mania', 'hipomania', 'eutimia')"
        ),
        posologia=(
            "<p>500 mg/dia em 2 tomadas. "
            "N\u00edvel-alvo: 50\u2013100 mcg/mL (mania aguda), 50\u201380 mcg/mL (manuten\u00e7\u00e3o).</p>"
        ),
        mensagemMedico=(
            "<p>Estabilizador de humor. Titular conforme valproatemia. "
            "CONTRAINDICADO na gesta\u00e7\u00e3o (risco fetal alto \u2014 alerta GESTANTE+VPA obrigat\u00f3rio). "
            "Monitorar hepatotoxicidade e trombocitopenia.</p>"
        ),
        categoria="Estabilizador de humor",
        mevo_code="42471",
    ),
    _make_med(
        nome="Carbamazepina 200mg",
        condicao=(
            "'tab' in diagnostico_ativo "
            "and selected_any(episodio_atual_humor, 'mania', 'hipomania')"
        ),
        posologia=(
            "<p>200 mg 2\u00d7/dia (in\u00edcio). "
            "Titular conforme carbamazepinemia (4\u201312 mcg/mL).</p>"
        ),
        mensagemMedico=(
            "<p>Estabilizador de humor. Indutor enzim\u00e1tico potente \u2014 verificar intera\u00e7\u00f5es. "
            "Coletar HLA-B*1502 antes do in\u00edcio em pacientes de origem asi\u00e1tica. "
            "Monitorar hiponatremia e leucopenia. "
            "C\u00f3digo MEVO n\u00e3o encontrado no cat\u00e1logo Amil (Mevo..xlsx).</p>"
        ),
        categoria="Estabilizador de humor",
        mevo_code=None,
    ),
    # --- Antipsicótico típico ---
    _make_med(
        nome="Haloperidol 5mg",
        condicao=(
            "selected_any(episodio_atual_humor, 'mania') "
            "or 'esquizofrenia' in diagnostico_ativo"
        ),
        posologia="<p>5 mg/dia (dose de in\u00edcio). Ajustar conforme resposta cl\u00ednica.</p>",
        mensagemMedico=(
            "<p>Antipsic\u00f3tico t\u00edpico. Prefer\u00eancia em mania aguda grave ou quando custo \u00e9 limitante. "
            "Alto risco de EPS e discin\u00e9sia tardia \u2014 monitorar. "
            "Evitar em longo prazo se alternativa at\u00edpica dispon\u00edvel.</p>"
        ),
        categoria="Antipsic\u00f3tico t\u00edpico",
        mevo_code="14996",
    ),
    # --- Antipsicótico refratário ---
    _make_med(
        nome="Clozapina 25mg",
        condicao="esquizofrenia_refrataria is True",
        posologia=(
            "<p>25 mg/noite (dose de in\u00edcio). "
            "Titular lentamente (semanas) at\u00e9 dose eficaz (300\u2013450 mg/dia).</p>"
        ),
        mensagemMedico=(
            "<p>Antipsic\u00f3tico de \u00faltima linha. Reservado para esquizofrenia refrat\u00e1ria. "
            "Exige monitoramento semanal de hemograma (risco de agranulocitose). "
            "Protocolo espec\u00edfico de dispensa\u00e7\u00e3o. N\u00e3o interromper abruptamente. "
            "C\u00f3digo MEVO n\u00e3o encontrado no cat\u00e1logo Amil (Mevo..xlsx).</p>"
        ),
        categoria="Antipsic\u00f3tico at\u00edpico (refrat\u00e1rio)",
        mevo_code=None,
    ),
    # --- TDAH 2a linha ---
    _make_med(
        nome="Atomoxetina 40mg",
        condicao="'tdah' in diagnostico_ativo",
        posologia="<p>40 mg/dia pela manh\u00e3. Titular para 80\u2013100 mg/dia ap\u00f3s 4 semanas.</p>",
        mensagemMedico=(
            "<p>Inibidor seletivo da recapta\u00e7\u00e3o de noradrenalina. "
            "2\u00aa linha no TDAH ou 1\u00aa linha quando estimulantes s\u00e3o contraindicados "
            "(abuso de subst\u00e2ncias ativo). Efeito m\u00e1ximo em 6\u20138 semanas. "
            "C\u00f3digo MEVO n\u00e3o encontrado no cat\u00e1logo Amil (Mevo..xlsx).</p>"
        ),
        categoria="N\u00e3o estimulante (TDAH)",
        mevo_code=None,
    ),
    # --- Ansiolitico BZD ---
    _make_med(
        nome="Clonazepam 0,5mg",
        condicao="selected_any(diagnostico_ativo, 'tag', 'panico', 'fobia_social')",
        posologia="<p>0,5 mg/noite (in\u00edcio). Ajustar conforme resposta, m\u00e1x 2 mg/dia.</p>",
        mensagemMedico=(
            "<p>BZD. Uso adjuvante a curto prazo (m\u00e1x 4\u20138 semanas) durante in\u00edcio do antidepressivo. "
            "Alto risco de depend\u00eancia \u2014 n\u00e3o prescrever isoladamente nem em longo prazo. "
            "C\u00f3digo MEVO 40857 = 2 mg comprimido (cat\u00e1logo Amil); confirmar 0,5 mg com equipe Amil.</p>"
        ),
        categoria="Ansiol\u00edtico BZD",
        mevo_code="40857",
    ),
]


# ---------------------------------------------------------------------------
# PROCESSAMENTO PRINCIPAL
# ---------------------------------------------------------------------------

def process_medications(meds):
    """
    Recebe lista de medicamentos e retorna lista corrigida.
    Aplica: BUG FIX 1, 2, 3, 4 + ADICAO.
    """
    result = []
    stats = {
        "schema_fixed": 0,
        "uuid_fixed": 0,
        "nomeMed_added": 0,
        "arip_split": 0,
    }

    for m in meds:
        nome = m.get("nome", "")
        mid = m.get("id", "")

        # BUG FIX 2 — Aripiprazol com 2 MEVOs: substituir por 2 itens
        if "Aripiprazol" in nome and len(m.get("codigo", [])) == 2:
            print(f"  [BUG2] Aripiprazol duplo removido -> inserindo Aripiprazol 10mg + 15mg")
            result.append(ARIP_10)
            result.append(ARIP_15)
            stats["arip_split"] += 1
            continue

        # BUG FIX 4 — UUID nao-canonico
        if mid in NON_CANONICAL_IDS:
            novo_id = new_uuid()
            print(f"  [BUG4] UUID '{mid}' -> '{novo_id}' ({nome})")
            m = dict(m)
            m["id"] = novo_id
            stats["uuid_fixed"] += 1

        # BUG FIX 1 — Schema normalization (conteudo -> posologia/mensagemMedico/via)
        if "conteudo" in m:
            fix = SCHEMA_FIX.get(nome)
            if fix is None:
                print(f"  [WARN] Sem fix definido para '{nome}' — mantendo conteudo")
                result.append(m)
                continue
            m = dict(m)
            # Remover campos nao-canonicos
            m.pop("conteudo", None)
            m.pop("observacao", None)
            # Adicionar campos canonicos
            m.setdefault("quantidade", 1)
            m["posologia"] = fix["posologia"]
            m["mensagemMedico"] = fix["mensagemMedico"]
            m["via"] = fix.get("via", "oral")
            if "nomeMed" in fix:
                m["nomeMed"] = fix["nomeMed"]
                if "nomeMed" not in m or not m.get("nomeMed"):
                    stats["nomeMed_added"] += 1
            # Garantir narrativa
            m.setdefault("narrativa", "")
            print(f"  [BUG1] Schema normalizado: '{nome}'")
            stats["schema_fixed"] += 1

        # BUG FIX 3 — nomeMed ausente (para itens nao cobertos pelo BUG1)
        if not m.get("nomeMed"):
            m = dict(m)
            m["nomeMed"] = nome
            print(f"  [BUG3] nomeMed preenchido: '{nome}'")
            stats["nomeMed_added"] += 1

        # Garantir quantidade
        if "quantidade" not in m:
            m = dict(m)
            m["quantidade"] = 1

        result.append(m)

    return result, stats


def main():
    print(f"Input:  {VDRAFT_PATH}")
    print(f"Output: {os.path.abspath(OUTPUT_PATH)}")
    print()

    with open(VDRAFT_PATH, encoding="utf-8") as f:
        data = json.load(f)

    target_node = None
    for node in data["nodes"]:
        if node.get("id") == "node-psiq-06-conduta":
            target_node = node
            break

    if target_node is None:
        print("ERRO: node-psiq-06-conduta nao encontrado!")
        sys.exit(1)

    cdn = target_node["data"].get("condutaDataNode", {})
    meds_before = cdn.get("medicamento", [])
    print(f"Medicamentos no vdraft: {len(meds_before)}")
    print()

    # Processar medicamentos existentes
    print("--- Aplicando bug fixes ---")
    meds_fixed, stats = process_medications(meds_before)

    # Adicionar 11 novos medicamentos
    print()
    print("--- Adicionando farmacos faltantes ---")
    for m in NEW_MEDS:
        print(f"  [ADD] {m['nome']} (MEVO: {m['codigo'][0]['codigo'] if m['codigo'] else '[]'})")
    meds_fixed.extend(NEW_MEDS)

    cdn["medicamento"] = meds_fixed

    # Atualizar metadata.version
    if "metadata" in data:
        old_ver = data["metadata"].get("version", "?")
        data["metadata"]["version"] = "0.2.2"
        print(f"\n[METADATA] version: '{old_ver}' -> '0.2.2'")

    # Salvar output
    os.makedirs(os.path.dirname(os.path.abspath(OUTPUT_PATH)), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Resumo
    meds_after = len(meds_fixed)
    mevo_filled = sum(1 for m in meds_fixed if m.get("codigo"))
    mevo_empty = sum(1 for m in meds_fixed if not m.get("codigo"))
    nomemed_ok = sum(1 for m in meds_fixed if m.get("nomeMed"))
    condmed_ok = sum(1 for m in meds_fixed if m.get("condicionalMedicamento"))
    posologia_ok = sum(1 for m in meds_fixed if m.get("posologia"))

    print(f"\n{'='*60}")
    print(f"Medicamentos antes  : {len(meds_before)}  (vdraft)")
    print(f"Medicamentos depois : {meds_after}  (v0.2.2)")
    print(f"Schema normalizado  : {stats['schema_fixed']}  (conteudo -> posologia/mensagemMedico)")
    print(f"UUID corrigidos     : {stats['uuid_fixed']}")
    print(f"nomeMed preenchidos : {stats['nomeMed_added']}")
    print(f"Aripiprazol split   : {stats['arip_split']}  (duplo -> 10mg + 15mg)")
    print(f"Farmacos adicionados: {len(NEW_MEDS)}")
    print()
    print(f"nomeMed preenchido  : {nomemed_ok}/{meds_after}")
    print(f"condicionalMed ok   : {condmed_ok}/{meds_after}")
    print(f"posologia ok        : {posologia_ok}/{meds_after}")
    print(f"MEVO preenchido     : {mevo_filled}/{meds_after}")
    print(f"MEVO vazio (sem cod) : {mevo_empty}/{meds_after}")
    print()
    print(f"Output: {os.path.abspath(OUTPUT_PATH)}")

    # Listar medicamentos sem MEVO
    if mevo_empty:
        print("\nMedicamentos sem MEVO (nao no catalogo Amil):")
        for m in meds_fixed:
            if not m.get("codigo"):
                print(f"  - {m['nome']}")


if __name__ == "__main__":
    main()
