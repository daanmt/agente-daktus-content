#!/usr/bin/env python3
"""
audit_logic.py — Auditoria lógica profunda de protocolo Daktus JSON.
Verifica:
  1. UIDs referenciados em expressoes/condições existem no protocolo
  2. IDs de opções referenciados existem nas questões correspondentes
  3. Questões condicionais cujos campos-pai têm escopo restrito (risco de null)
  4. Loops (resultado de exame → solicitar mesmo exame)
  5. Artefatos de conduta com condições inválidas ou variáveis inexistentes
  6. Comparações numéricas sem guard de coleta
  7. Duplicatas de artefatos com condições idênticas
"""
import json, re, sys
from collections import defaultdict

SEV = {"CRITICO": "[CRITICO]", "ALTO": "[ALTO]", "MEDIO": "[MEDIO]", "INFO": "[INFO]"}

class ProtocolAuditor:
    def __init__(self, filepath):
        self.data = json.load(open(filepath, encoding="utf-8"))
        self.issues = []

        # Mapas globais
        self.all_questions = {}   # uid -> {question, node_id, expressao}
        self.all_options = {}     # uid -> set(option_ids)
        self.node_map = {}        # node_id -> node
        self.conduct_nodes = []
        self.summary_nodes = []

        self._build_maps()

    def _build_maps(self):
        for node in self.data["nodes"]:
            self.node_map[node["id"]] = node
            ntype = node.get("type", "")

            if ntype == "conduct":
                self.conduct_nodes.append(node)
            elif ntype == "summary":
                self.summary_nodes.append(node)

            if "questions" in node.get("data", {}):
                for q in node["data"]["questions"]:
                    uid = q.get("uid", "")
                    if uid:
                        self.all_questions[uid] = {
                            "q": q,
                            "node_id": node["id"],
                            "node_label": node["data"].get("label",""),
                            "expressao": q.get("expressao",""),
                            "select": q.get("select",""),
                        }
                        opts = {o["id"] for o in q.get("options", []) if o.get("id")}
                        self.all_options[uid] = opts

        # Registrar clinicalExpressions do summary como UIDs validos (tipo boolean)
        for snode in self.summary_nodes:
            exprs = snode.get("data", {}).get("clinicalExpressions", [])
            for expr in exprs:
                if not isinstance(expr, dict):
                    continue
                name = expr.get("name", "") or expr.get("uid", "")
                if name and name not in self.all_questions:
                    self.all_questions[name] = {
                        "q": expr,
                        "node_id": snode["id"],
                        "node_label": snode["data"].get("label", "Summary"),
                        "expressao": expr.get("formula", ""),
                        "select": "clinicalExpression",
                    }

    def _add(self, sev, loc, problem, impact, fix):
        self.issues.append((sev, loc, problem, impact, fix))

    # -------------------------------------------------------
    # 1. Extrair UIDs e opções citados em uma expressão
    # -------------------------------------------------------
    def _parse_uid_refs(self, expr):
        """Retorna lista de (uid, option_id_or_None) mencionados na expressão."""
        refs = []
        # padrão: 'opt' in uid  ou  not 'opt' in uid
        for opt, uid in re.findall(r"'([^']+)'\s+in\s+(\w+)", expr):
            refs.append((uid, opt))
        # padrão: uid == 'opt'
        for uid, opt in re.findall(r"(\w+)\s*==\s*'([^']+)'", expr):
            refs.append((uid, opt))
        # padrão: uid is True/False
        for uid in re.findall(r"(\w+)\s+is\s+(?:True|False)", expr):
            refs.append((uid, None))
        # padrão: uid > / < / >= / <= valor
        for uid in re.findall(r"(\w+)\s*[><=!]+\s*[\d.]+", expr):
            refs.append((uid, None))
        # selected_any(uid, ...)
        for m in re.finditer(r"selected_any\s*\(\s*(\w+)\s*,([^)]+)\)", expr):
            uid = m.group(1)
            opts = re.findall(r"'([^']+)'", m.group(2))
            for opt in opts:
                refs.append((uid, opt))
            if not opts:
                refs.append((uid, None))
        return refs

    # -------------------------------------------------------
    # 2. Verificar que UIDs e opções existem
    # -------------------------------------------------------
    def check_uid_existence(self):
        # Questões
        for uid, info in self.all_questions.items():
            expr = info["expressao"]
            if not expr:
                continue
            for ref_uid, ref_opt in self._parse_uid_refs(expr):
                if ref_uid not in self.all_questions:
                    # Pode ser clinicalExpression do summary — skip se começar com minúscula típica de variável calculada
                    if ref_uid not in {"age", "sex"}:
                        self._add("ALTO", f"N/{uid}.expressao",
                            f"UID '{ref_uid}' referenciado em expressao não existe como questão",
                            "Pergunta nunca aparecerá (condição inválida)",
                            f"Verificar se '{ref_uid}' é variável do summary ou corrigir UID")
                elif ref_opt and ref_opt not in self.all_options.get(ref_uid, set()):
                    self._add("ALTO", f"N/{uid}.expressao",
                        f"Opção '{ref_opt}' de '{ref_uid}' não existe nas options",
                        "Condição nunca satisfeita — pergunta nunca aparece",
                        f"Verificar se id='{ref_opt}' existe em {ref_uid}.options")

        # Artefatos de conduta
        for node in self.conduct_nodes:
            cnd = node["data"].get("condutaDataNode") or {}
            node_label = node["data"].get("label","")
            for section in ["exame", "medicamento", "encaminhamento", "mensagem", "orientacao"]:
                for item in cnd.get(section, []):
                    cond = item.get("condicao", "") or ""
                    if not cond:
                        continue
                    nome = item.get("nome","?")[:50]
                    for ref_uid, ref_opt in self._parse_uid_refs(cond):
                        if ref_uid not in self.all_questions and ref_uid not in {"age", "sex"}:
                            self._add("CRITICO", f"Conduta/{section}/{nome}",
                                f"UID '{ref_uid}' na condicao não existe",
                                f"Artefato nunca dispara (referência fantasma)",
                                f"Corrigir para UID existente ou criar variável no summary")
                        elif ref_opt and ref_opt not in self.all_options.get(ref_uid, set()):
                            self._add("CRITICO", f"Conduta/{section}/{nome}",
                                f"Opção '{ref_opt}' de '{ref_uid}' não existe nas options",
                                "Condição nunca satisfeita — artefato nunca dispara",
                                f"Verificar id='{ref_opt}' em {ref_uid}.options")

    # -------------------------------------------------------
    # 3. Questões numéricas sem guard de coleta
    # -------------------------------------------------------
    def check_numeric_null_safety(self):
        # Coleta UIDs numéricos por exames_recentes
        numeric_guarded = set()

        # Mapear quais multiChoice de exames_recentes existem
        exames_rec_opts = self.all_options.get("exames_recentes", set())

        for uid, info in self.all_questions.items():
            if info["select"] != "number":
                continue
            expr = info["expressao"]
            # Guard esperado: 'trouxe_X' in exames_recentes
            has_guard = bool(re.search(r"'trouxe_\w+'\s+in\s+exames_recentes", expr))
            if has_guard:
                numeric_guarded.add(uid)

        # Agora verificar artefatos de conduta que comparam numéricos sem guard
        for node in self.conduct_nodes:
            cnd = node["data"].get("condutaDataNode") or {}
            for section in ["exame", "medicamento", "encaminhamento", "mensagem", "orientacao"]:
                for item in cnd.get(section, []):
                    cond = item.get("condicao","") or ""
                    nome = item.get("nome","?")[:50]
                    # Encontrar comparações numéricas
                    num_uids = re.findall(r"(\w+)\s*[><=!]+\s*[\d.]+", cond)
                    for nuid in num_uids:
                        if nuid in {"age", "sex"}:
                            continue  # Campos sistema — sempre disponiveis
                        if nuid not in self.all_questions:
                            continue
                        if self.all_questions[nuid]["select"] != "number":
                            continue
                        # Verificar se há guard na condição
                        has_guard_in_cond = bool(re.search(
                            r"'trouxe_\w+'\s+in\s+exames_recentes", cond))
                        if not has_guard_in_cond:
                            self._add("MEDIO", f"Conduta/{section}/{nome}",
                                f"Comparação com '{nuid}' (number) sem guard de coleta",
                                "Se campo não preenchido, comparação com null pode dar resultado inesperado",
                                f"Adicionar ('trouxe_lab' in exames_recentes) or similar antes da comparação")

    # -------------------------------------------------------
    # 4. Loops: resultado de exame → solicitar mesmo exame
    # -------------------------------------------------------
    def check_loops(self):
        # Mapa: resultado_uid -> exame_solicitado (por código TUSS ou nome similar)
        resultado_map = {
            "hpv_resultado": ["HPV", "DNA-HPV"],
            "mamo_resultado": ["Mamografia", "mamografia"],
            "t_score": ["Densitometria", "DXA", "densitometria"],
            "colposcopia_resultado": ["Colposcopia", "colposcopia"],
            "usgtv_achados": ["Ultrassonografia transvaginal", "USGTV"],
            "rm_pelve_resultado": ["RM", "pelve", "Ressonância"],
        }

        for node in self.conduct_nodes:
            cnd = node["data"].get("condutaDataNode") or {}
            exames = cnd.get("exames", [])
            for exame in exames:
                nome = exame.get("nome","")
                cond = exame.get("condicao","") or ""
                for res_uid, keywords in resultado_map.items():
                    if res_uid not in cond:
                        continue
                    # Verificar se o exame solicitado é do mesmo tipo
                    for kw in keywords:
                        if kw.lower() in nome.lower():
                            self._add("ALTO", f"Conduta/exames/{nome[:50]}",
                                f"Loop: resultado '{res_uid}' aciona pedido do próprio exame ({kw})",
                                "Paciente que traz resultado recebe novo pedido do mesmo exame",
                                f"Remover '{res_uid}' da condição ou separar resultado de 'não realizado'")
                            break

    # -------------------------------------------------------
    # 5. Artefatos duplicados com condições idênticas
    # -------------------------------------------------------
    def check_duplicates(self):
        for node in self.conduct_nodes:
            cnd = node["data"].get("condutaDataNode") or {}
            for section in ["exames", "medicamentos", "encaminhamentos"]:
                seen = defaultdict(list)
                for item in cnd.get(section, []):
                    cond = item.get("condicao","") or ""
                    nome = item.get("nome","?")
                    seen[(cond.strip(), section)].append(nome)
                for (cond, sec), names in seen.items():
                    if len(names) > 1 and cond:
                        self._add("MEDIO", f"Conduta/{sec}",
                            f"Condição idêntica em {len(names)} itens: {names[:3]}",
                            "Possível duplicata — dois artefatos sempre disparam juntos",
                            "Verificar se é intencional; se não, consolidar ou diferenciar condições")

    # -------------------------------------------------------
    # 6. Prescrições sem gate de contraindicação
    # -------------------------------------------------------
    def check_missing_ci_gates(self):
        trh_items_sem_gate = []
        for node in self.conduct_nodes:
            cnd = node["data"].get("condutaDataNode") or {}
            for item in cnd.get("medicamentos", []):
                nome = item.get("nome","")
                cond = item.get("condicao","") or ""
                # TRH sistêmica deve ter gate de contraindicação
                if any(k in nome.lower() for k in ["estradiol", "progesterona", "estrogênio"]):
                    if "estradiol vaginal" in nome.lower():
                        # Estradiol vaginal tem CI específica (ca_mama)
                        if "ca_mama_pessoal" not in cond and "contraindicacao_trh" not in cond:
                            self._add("CRITICO", f"Conduta/medicamentos/{nome[:60]}",
                                "Estradiol vaginal sem gate de contraindicação (ca_mama)",
                                "SOBRAC: contraindicado em ca_mama pessoal",
                                "Adicionar and not 'ca_mama_pessoal' in contraindicacao_trh")
                    elif "trh_indicada" not in cond and "contraindicacao_trh" not in cond and "sem_ci_trh" not in cond:
                        trh_items_sem_gate.append(nome[:50])
        if trh_items_sem_gate:
            self._add("ALTO", "Conduta/medicamentos/TRH",
                f"{len(trh_items_sem_gate)} medicamentos TRH sem verificação de CI: {trh_items_sem_gate[:3]}",
                "TRH prescrita para pacientes com contraindicação formal",
                "Usar variável trh_indicada do summary ou verificar 'sem_ci_trh' in contraindicacao_trh")

    # -------------------------------------------------------
    # 7. Verificar existência do nó summary e clinicalExpressions
    # -------------------------------------------------------
    def check_summary_node(self):
        if not self.summary_nodes:
            self._add("ALTO", "Arquitetura/nós",
                "Nó summary (Processamento Clínico) não encontrado no JSON",
                "Variáveis calculadas (alto_risco_mama, trh_indicada, etc.) não existem — condições na conduta falharão",
                "Adicionar nó type=summary entre Fluxo de Seguimento e Conduta Médica")
            return

        expected_vars = [
            "alto_risco_mama", "rastreio_cervical_habitual", "rastreio_cervical_intensificado",
            "co_teste_papanicolau", "trh_indicada", "espessamento_endometrial_significativo",
            "poi_suspeita", "anemia_laboratorial", "alt_tsh"
        ]
        for snode in self.summary_nodes:
            exprs = snode.get("data", {}).get("clinicalExpressions", [])
            defined = {e.get("name","") or e.get("uid","") for e in exprs if isinstance(e, dict)}
            for v in expected_vars:
                if v not in defined:
                    self._add("MEDIO", f"Summary/{snode['id'][:20]}",
                        f"Variável calculada '{v}' não definida no summary",
                        "Condições na conduta que referenciam esta variável falharão",
                        f"Adicionar clinicalExpression com uid='{v}'")

    # -------------------------------------------------------
    # 8. Questões com scope restrito consumidas globalmente
    # -------------------------------------------------------
    def check_restricted_scope_global_use(self):
        """Identifica questões que só aparecem sob certas queixas
        mas são usadas em condições gerais da conduta."""
        # Mapeamento de UIDs críticos e seus escopos esperados
        scope_restricted = {}
        for uid, info in self.all_questions.items():
            expr = info["expressao"]
            if not expr:
                continue
            # Detectar questões que dependem de uma queixa específica
            queixa_deps = re.findall(r"'(\w+)'\s+in\s+queixa_principal", expr)
            if queixa_deps:
                scope_restricted[uid] = queixa_deps

        # Verificar se alguma conduta usa esses UIDs sem o escopo correspondente
        for node in self.conduct_nodes:
            cnd = node["data"].get("condutaDataNode") or {}
            for section in ["exames", "medicamentos", "encaminhamentos"]:
                for item in cnd.get(section, []):
                    cond = item.get("condicao","") or ""
                    nome = item.get("nome","?")[:50]
                    for ref_uid, _ in self._parse_uid_refs(cond):
                        if ref_uid not in scope_restricted:
                            continue
                        queixas_req = scope_restricted[ref_uid]
                        # Verificar se a conduta inclui pelo menos uma das queixas-pai
                        has_queixa_guard = any(
                            qr in cond for qr in queixas_req
                        ) or "queixa_principal" in cond
                        if not has_queixa_guard:
                            self._add("MEDIO", f"Conduta/{section}/{nome}",
                                f"UID '{ref_uid}' só coletado se {queixas_req} — conduta sem esse guard",
                                f"'{ref_uid}' pode ser null para pacientes sem essa queixa",
                                f"Adicionar guard de queixa ou mover para artefato condicional")

    # -------------------------------------------------------
    # 9. Verificar condicionais de roteamento de nós
    # -------------------------------------------------------
    def check_routing(self):
        for node in self.data["nodes"]:
            if node.get("type") in ("conduct",):
                continue
            condicionais = node["data"].get("condicionais", [])
            for cond_entry in condicionais:
                link_id = cond_entry.get("linkId","")
                cond_expr = cond_entry.get("condicao","")
                if link_id and link_id not in self.node_map:
                    self._add("CRITICO", f"Routing/{node['id'][:20]}",
                        f"linkId '{link_id}' não existe no grafo",
                        "Roteamento quebrado — fluxo pode travar",
                        "Corrigir linkId para ID de nó válido")
                if cond_expr:
                    for ref_uid, ref_opt in self._parse_uid_refs(cond_expr):
                        if ref_uid not in self.all_questions and ref_uid not in {"age","sex"}:
                            self._add("CRITICO", f"Routing/{node['id'][:20]}/condicao",
                                f"UID '{ref_uid}' na condicao de roteamento não existe",
                                "Roteamento nunca ativado ou sempre ativo (undefined)",
                                f"Corrigir para UID existente")

    # -------------------------------------------------------
    # MAIN
    # -------------------------------------------------------
    def run(self):
        self.check_summary_node()
        self.check_uid_existence()
        self.check_numeric_null_safety()
        self.check_loops()
        self.check_duplicates()
        self.check_missing_ci_gates()
        self.check_restricted_scope_global_use()
        self.check_routing()
        return self.issues

    def report(self):
        issues = self.run()

        by_sev = {"CRITICO": [], "ALTO": [], "MEDIO": [], "INFO": []}
        for sev, loc, prob, imp, fix in issues:
            by_sev.get(sev, by_sev["INFO"]).append((loc, prob, imp, fix))

        total = sum(len(v) for v in by_sev.values())
        print(f"\n{'='*70}")
        print(f"AUDITORIA LÓGICA — {self.data['metadata'].get('id','?')} v{self.data['metadata'].get('version','?')}")
        print(f"Nós: {len(self.data['nodes'])} | Edges: {len(self.data['edges'])}")
        print(f"Questões mapeadas: {len(self.all_questions)}")
        print(f"Issues encontrados: {total}")
        print(f"{'='*70}")

        order = ["CRITICO", "ALTO", "MEDIO", "INFO"]
        for sev in order:
            items = by_sev[sev]
            if not items:
                continue
            print(f"\n{SEV[sev]} {sev} ({len(items)})")
            print("-"*60)
            for i, (loc, prob, imp, fix) in enumerate(items, 1):
                print(f"#{i} [{loc}]")
                print(f"   Problema: {prob}")
                print(f"   Impacto:  {imp}")
                print(f"   Correção: {fix}")

        print(f"\n{'='*70}")
        print(f"Resumo: {len(by_sev['CRITICO'])} críticos | {len(by_sev['ALTO'])} altos | {len(by_sev['MEDIO'])} médios")
        print(f"{'='*70}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audit_logic.py <ficha.json>")
        sys.exit(1)
    auditor = ProtocolAuditor(sys.argv[1])
    auditor.report()
