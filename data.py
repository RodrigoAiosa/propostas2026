"""Dados e metodologia do comparador de propostas econômicas (Lula x Flávio Bolsonaro).

ESCALA "liberal" (0-10):
    0  = máxima presença do Estado (controle, empresas estatais, subsídios diretos)
    10 = mínima presença do Estado (corte de gasto, privatização, desregulação, menos imposto)

DETALHAMENTO: "alta" | "media" | "baixa"  -> quão concreta/verificável é a proposta no plano.
O índice AJUSTADO encolhe a nota em direção ao neutro (5) quando a proposta é vaga,
para responder: "quem REALMENTE entrega menos Estado?" e não só "quem promete".

Todas as notas são um julgamento editorial transparente: edite aqui e o site recalcula.
"""

ATUALIZADO_EM = "20/10/2026"

FATOR_DETALHAMENTO = {"alta": 1.0, "media": 0.8, "baixa": 0.6}

CANDIDATOS = {
    "lula": {"nome": "Lula", "partido": "PT", "cor": "#c0392b"},
    "flavio": {"nome": "Flávio Bolsonaro", "partido": "PL", "cor": "#1f5fbf"},
}

# top5=True => aparece na tabela "Top 5"
SETORES = [
    {
        "id": "fiscal", "nome": "Gastos públicos e fiscal", "top5": True,
        "lula": {
            "resumo": "Mantém o arcabouço fiscal; meta de ir de déficit de 0,5% do PIB (2026) a superávit de 1,5% em 2030. Não prevê cortes de despesa.",
            "nota": 3, "detalhamento": "media",
        },
        "flavio": {
            "resumo": "'Tesouraço': reforma administrativa, corte de ao menos 10 ministérios e de cargos comissionados, teto da dívida. Equipe cita ~1,5% do PIB (R$ 190 bi), fora do plano oficial.",
            "nota": 7, "detalhamento": "baixa",
        },
    },
    {
        "id": "tributos", "nome": "Impostos", "top5": True,
        "lula": {
            "resumo": "Implementar a reforma do consumo aprovada; manter isenção de IR até R$ 5 mil, tributação de offshores/fundos exclusivos e Imposto Seletivo.",
            "nota": 3, "detalhamento": "alta",
        },
        "flavio": {
            "resumo": "Revisar a reforma para reduzir a carga (IVA menor; citou 20%), cortar tributos sobre energia e combustíveis e desonerar exportações. Não diz quais tributos nem a compensação.",
            "nota": 7, "detalhamento": "baixa",
        },
    },
    {
        "id": "estatais", "nome": "Estatais e privatizações", "top5": True,
        "lula": {
            "resumo": "Estatais como instrumento de política industrial e energética; Petrobras na distribuição de combustíveis; descarta privatizar os Correios.",
            "nota": 1, "detalhamento": "alta",
        },
        "flavio": {
            "resumo": "Retomar o Programa Nacional de Desestatização, caso a caso. Não lista empresas; analistas não esperam privatização de Petrobras ou Banco do Brasil. Caixa vira 'Banco da Prosperidade'.",
            "nota": 6, "detalhamento": "baixa",
        },
    },
    {
        "id": "trabalho", "nome": "Trabalho e renda", "top5": True,
        "lula": {
            "resumo": "Fim da escala 6x1 (40h semanais sem redução salarial); ganho real do salário mínimo (teto de 2,5%/ano); proteção a trabalhadores de plataformas.",
            "nota": 3, "detalhamento": "alta",
        },
        "flavio": {
            "resumo": "Reduzir gradualmente encargos sobre a folha; contratos para jovens de 18-24 e maiores de 50 desempregados; jornadas flexíveis. Também passou a apoiar o fim da 6x1.",
            "nota": 7, "detalhamento": "media",
        },
    },
    {
        "id": "infra", "nome": "Infraestrutura e investimento", "top5": True,
        "lula": {
            "resumo": "Novo PAC (~R$ 1,9 tri previstos), mais concessões ferroviárias, portos e aeroportos regionais. Sem meta numérica de PIB.",
            "nota": 3, "detalhamento": "alta",
        },
        "flavio": {
            "resumo": "R$ 900 bi em 4 anos via PPPs, concessões e fundo de ativos da União; meta de PIB de 4% ao ano por uma década. Fontes de recurso não especificadas.",
            "nota": 6, "detalhamento": "baixa",
        },
    },
    {
        "id": "energia", "nome": "Energia e petróleo", "top5": False,
        "lula": {
            "resumo": "Petrobras central: mais exploração, refino e volta à distribuição de combustíveis.",
            "nota": 2, "detalhamento": "alta",
        },
        "flavio": {
            "resumo": "Expandir petróleo e gás, liberar fracking e reduzir impostos sobre energia e combustíveis.",
            "nota": 6, "detalhamento": "media",
        },
    },
    {
        "id": "credito", "nome": "Crédito e indústria", "top5": False,
        "lula": {
            "resumo": "Nova Indústria Brasil, BNDES, fundos garantidores e programas como Pronampe e Acredita (> R$ 130 bi).",
            "nota": 2, "detalhamento": "alta",
        },
        "flavio": {
            "resumo": "Refinanciamento de dívidas e crédito via Caixa; foco em desregulamentação e menor custo de produção.",
            "nota": 5, "detalhamento": "baixa",
        },
    },
    {
        "id": "agro", "nome": "Agronegócio", "top5": False,
        "lula": {
            "resumo": "Ampliar o Plano Safra, diversificar fontes de financiamento e simplificar o crédito.",
            "nota": 4, "detalhamento": "media",
        },
        "flavio": {
            "resumo": "Ampliar o seguro rural, reorganizar dívidas e aumentar a capacidade de armazenagem.",
            "nota": 5, "detalhamento": "media",
        },
    },
    {
        "id": "social", "nome": "Habitação e proteção social", "top5": False,
        "lula": {
            "resumo": "Manter e ampliar Bolsa Família e programas de proteção social; Novo PAC habitação.",
            "nota": 2, "detalhamento": "alta",
        },
        "flavio": {
            "resumo": "Retomar o Casa Verde e Amarela (meta de 2,5 milhões de moradias).",
            "nota": 4, "detalhamento": "media",
        },
    },
]

# Planos oficiais. Não hospedamos os PDFs: apontamos para a fonte original.
DOCUMENTOS = [
    {
        "candidato": "lula",
        "titulo": "Programa de Governo Lula 2026 (PDF)",
        "url": "https://static.poder360.com.br/uploads/2026/08/Programa-Governo-LULA-2026.pdf",
        "tipo": "PDF",
    },
    {
        "candidato": "flavio",
        "titulo": "'Para o Brasil Vencer o Atraso' (76 págs.) - buscar no TSE",
        "url": "https://divulgacandcontas.tse.jus.br/",
        "tipo": "Portal TSE",
    },
    {
        "candidato": "flavio",
        "titulo": "Resumo do plano - Agência Brasil",
        "url": "https://agenciabrasil.ebc.com.br/politica/noticia/2026-09/flavio-bolsonaro-propoe-enxugar-estado-e-endurecer-acoes-de-seguranca",
        "tipo": "Reportagem",
    },
]

FONTES = [
    ("BPMoney - Compare as propostas econômicas", "https://bpmoney.com.br/economia/lula-x-flavio-propostas-economicas-2026/"),
    ("Forbes Brasil - 'Tesouraço'", "https://forbes.com.br/forbes-money/2026/10/tesouraco-flavio-bolsonaro-plano-economico/"),
    ("Nexo - O plano de Flávio é um cheque em branco?", "https://www.nexojornal.com.br/expresso/2026/09/24/flavio-bolsonaro-proposta-economica-ministra-economia-flavio"),
    ("InfoMoney - O que Lula prometeu para a economia", "https://www.infomoney.com.br/politica/o-que-lula-ja-prometeu-para-a-economia-se-conquistar-a-reeleicao/"),
    ("Exame - Planos de Lula e Flávio", "https://exame.com/brasil/eleicoes-2026-veja-os-planos-de-economia-de-lula-e-flavio-bolsonaro/"),
    ("Gazeta do Povo - Plano de Lula", "https://www.gazetadopovo.com.br/eleicoes/2026/plano-de-governo-lula-economia/"),
]


def _ajustada(nota: float, detalhamento: str) -> float:
    """Encolhe a nota em direção ao neutro (5) conforme a vagueza da proposta."""
    return round(5 + (nota - 5) * FATOR_DETALHAMENTO[detalhamento], 1)


def _media(valores):
    return round(sum(valores) / len(valores), 1)


def calcular():
    """Devolve setores enriquecidos + placar geral + veredito."""
    setores = []
    for s in SETORES:
        item = {"id": s["id"], "nome": s["nome"], "top5": s["top5"]}
        for c in CANDIDATOS:
            d = s[c]
            item[c] = {**d, "ajustada": _ajustada(d["nota"], d["detalhamento"])}
        mais_liberal = max(CANDIDATOS, key=lambda c: item[c]["nota"])
        empate = item["lula"]["nota"] == item["flavio"]["nota"]
        item["mais_liberal"] = None if empate else mais_liberal
        setores.append(item)

    def placar(subconjunto):
        out = {}
        for c in CANDIDATOS:
            out[c] = {
                "intencao": _media([s[c]["nota"] for s in subconjunto]),
                "ajustada": _media([s[c]["ajustada"] for s in subconjunto]),
            }
        return out

    geral = placar(setores)
    top5 = placar([s for s in setores if s["top5"]])

    def lider(p, chave):
        a, b = p["lula"][chave], p["flavio"][chave]
        if a == b:
            return None
        return "lula" if a > b else "flavio"

    veredito = {
        "mais_liberal_intencao": lider(geral, "intencao"),
        "mais_liberal_ajustada": lider(geral, "ajustada"),
        "mais_estatal": None,
    }
    menos = lider(geral, "intencao")
    if menos:
        veredito["mais_estatal"] = "lula" if menos == "flavio" else "flavio"

    return {
        "setores": setores,
        "top5": [s for s in setores if s["top5"]],
        "placar_geral": geral,
        "placar_top5": top5,
        "veredito": veredito,
        "atualizado_em": ATUALIZADO_EM,
    }
