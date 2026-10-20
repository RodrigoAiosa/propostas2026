"""Conteúdo das ferramentas de leitura fácil: lacunas, simulador, quiz e glossário.

Regra de ouro: só entra aqui o que está no plano de governo ou foi reportado pela
imprensa consultada. Quando o plano não diz algo, o site diz "não informado".
Não calculamos valores em reais: os planos não trazem números por pessoa.
"""

# ---------------------------------------------------------------------------
# 4) O que falta saber, por setor e candidato (alimenta o selo de detalhamento)
# ---------------------------------------------------------------------------
FALTAM = {
    ("fiscal", "lula"): [
        "Não indica quais despesas seriam contidas para chegar à meta fiscal.",
        "Controle das despesas obrigatórias e financiamento dos compromissos de renda não são explicados.",
    ],
    ("fiscal", "flavio"): [
        "Não lista quais despesas seriam cortadas nem apresenta cronograma.",
        "O corte de cerca de 1,5% do PIB (R$ 190 bi) foi dito pela equipe, mas não consta como meta no plano protocolado no TSE.",
    ],
    ("tributos", "lula"): [
        "A alíquota final do IVA depende de regulamentação (a estimativa de julho do Comitê Gestor do IBS, de 27,91%, não é definitiva).",
    ],
    ("tributos", "flavio"): [
        "Não diz quais tributos seriam reduzidos.",
        "A alíquota de IVA de 20%, citada em evento, não aparece como compromisso no plano.",
        "Não explica como compensaria a queda de arrecadação.",
    ],
    ("estatais", "lula"): [],
    ("estatais", "flavio"): [
        "Não lista quais estatais seriam privatizadas.",
        "Prevê mudanças de gestão antes de decidir vendas, sem critérios definidos.",
    ],
    ("trabalho", "lula"): [
        "O fim da escala 6x1 depende de aprovação legislativa e de regras de transição.",
    ],
    ("trabalho", "flavio"): [
        "Não traz regra de reajuste real do salário mínimo.",
        "Posições sobre reajuste de salários e aposentadorias seguem sem detalhamento (Folha, 14/10).",
        "Regras dos novos modelos de contrato não são detalhadas.",
    ],
    ("infra", "lula"): [
        "Os valores do Novo PAC são investimentos previstos, não necessariamente já executados.",
    ],
    ("infra", "flavio"): [
        "Não diz quais imóveis e ativos da União entrariam no fundo.",
        "Não define como o fundo seria administrado nem as condições financeiras das operações.",
        "As fontes dos R$ 900 bi não são detalhadas.",
    ],
    ("energia", "lula"): [],
    ("energia", "flavio"): [
        "A redução de impostos sobre energia e combustíveis não diz quais tributos nem como seria compensada.",
    ],
    ("credito", "lula"): [],
    ("credito", "flavio"): [
        "A proposta de refinanciamento de dívidas pela Caixa surgiu no 2º turno, fora do plano original.",
    ],
    ("agro", "lula"): [],
    ("agro", "flavio"): [],
    ("social", "lula"): [],
    ("social", "flavio"): [],
}

SELO = {"alta": "Detalhada", "media": "Parcial", "baixa": "Vaga"}

# ---------------------------------------------------------------------------
# 1) Simulador: "Quanto isso afeta o meu bolso?"
# ---------------------------------------------------------------------------
CERTEZA = {
    "no_plano": "Está no plano",
    "congresso": "Depende do Congresso",
    "sem_detalhe": "Sem detalhe ou fonte",
    "campanha": "Declaração de campanha",
}

CAMPOS = [
    {
        "id": "renda", "rotulo": "Sua renda mensal",
        "opcoes": [
            {"v": "ate_3k", "t": "Até R$ 3 mil"},
            {"v": "3k_5k", "t": "De R$ 3 mil a R$ 5 mil"},
            {"v": "5k_10k", "t": "De R$ 5 mil a R$ 10 mil"},
            {"v": "acima_10k", "t": "Acima de R$ 10 mil"},
        ],
    },
    {
        "id": "vinculo", "rotulo": "Sua situação",
        "opcoes": [
            {"v": "clt", "t": "Empregado com carteira assinada (CLT)"},
            {"v": "autonomo", "t": "Autônomo, MEI ou trabalhador de aplicativo"},
            {"v": "empresario", "t": "Dono de empresa ou empregador"},
            {"v": "servidor", "t": "Servidor público"},
            {"v": "aposentado", "t": "Aposentado ou pensionista"},
            {"v": "desempregado", "t": "Desempregado"},
            {"v": "produtor", "t": "Produtor rural"},
        ],
    },
    {
        "id": "bolsa", "rotulo": "Recebe Bolsa Família?", "padrao": "nao",
        "opcoes": [{"v": "nao", "t": "Não"}, {"v": "sim", "t": "Sim"}],
    },
    {
        "id": "divida", "rotulo": "Está endividado?", "padrao": "nao",
        "opcoes": [{"v": "nao", "t": "Não"}, {"v": "sim", "t": "Sim"}],
    },
]

# quando: lista de alternativas (OU); dentro de cada uma, todos os campos precisam bater (E).
# quando=None => vale para todos os perfis.
IMPACTOS = [
    # ---- Lula ----
    {"cand": "lula", "titulo": "Imposto de Renda", "certeza": "no_plano",
     "texto": "Mantém a isenção do Imposto de Renda para quem ganha até R$ 5 mil por mês.",
     "quando": [{"renda": ["ate_3k", "3k_5k"]}]},
    {"cand": "lula", "titulo": "Salário mínimo", "certeza": "no_plano",
     "texto": "Mantém a política de reajuste do salário mínimo acima da inflação (ganho real limitado a 2,5% ao ano). Benefícios ligados ao piso acompanham.",
     "quando": [{"renda": ["ate_3k"]}, {"vinculo": ["aposentado"]}]},
    {"cand": "lula", "titulo": "Jornada de trabalho", "certeza": "congresso",
     "texto": "Defende o fim da escala 6x1, com jornada de 40 horas semanais sem redução de salário.",
     "quando": [{"vinculo": ["clt"]}]},
    {"cand": "lula", "titulo": "Aplicativos e contratação por PJ", "certeza": "no_plano",
     "texto": "Prevê proteção a trabalhadores de plataformas digitais e fiscalização contra contratações fraudulentas como pessoa jurídica.",
     "quando": [{"vinculo": ["autonomo"]}]},
    {"cand": "lula", "titulo": "Bolsa Família", "certeza": "no_plano",
     "texto": "Promete manter, aperfeiçoar e ampliar o Bolsa Família e a proteção social.",
     "quando": [{"bolsa": ["sim"]}]},
    {"cand": "lula", "titulo": "Micro e pequenas empresas", "certeza": "no_plano",
     "texto": "Amplia fundos garantidores e programas de crédito como Pronampe e Acredita, e promete atenção ao tratamento tributário das micro e pequenas empresas.",
     "quando": [{"vinculo": ["empresario", "autonomo"]}]},
    {"cand": "lula", "titulo": "Dívidas", "certeza": "no_plano",
     "texto": "Cita alívio do comprometimento da renda com dívidas de famílias e empresas e renegociação de dívidas. Confira as condições no plano oficial.",
     "quando": [{"divida": ["sim"]}]},
    {"cand": "lula", "titulo": "Fundos no exterior", "certeza": "no_plano",
     "texto": "Mantém a tributação de fundos exclusivos e de investimentos no exterior (offshores) criada neste governo.",
     "quando": [{"renda": ["acima_10k"]}]},
    {"cand": "lula", "titulo": "Servidores públicos", "certeza": "no_plano",
     "texto": "Prevê aprofundar a valorização dos servidores federais e manter a Mesa Nacional de Negociação Permanente.",
     "quando": [{"vinculo": ["servidor"]}]},
    {"cand": "lula", "titulo": "Crédito rural", "certeza": "no_plano",
     "texto": "Amplia os recursos do Plano Safra, diversifica fontes de financiamento e simplifica o acesso ao crédito.",
     "quando": [{"vinculo": ["produtor"]}]},
    {"cand": "lula", "titulo": "Moradia e obras", "certeza": "no_plano",
     "texto": "Mantém o Novo PAC, que inclui obras de habitação e urbanização.",
     "quando": [{"renda": ["ate_3k", "3k_5k"]}]},
    {"cand": "lula", "titulo": "Reforma tributária", "certeza": "no_plano",
     "texto": "Implementa a reforma do consumo já aprovada (IVA). A alíquota final ainda não está definida. Cria também o Imposto Seletivo sobre produtos prejudiciais à saúde, que pode encarecê-los.",
     "quando": None},
    {"cand": "lula", "titulo": "Combustíveis", "certeza": "no_plano",
     "texto": "Quer a Petrobras de volta à distribuição de combustíveis e ampliando o refino.",
     "quando": None},
    # ---- Flávio Bolsonaro ----
    {"cand": "flavio", "titulo": "Reforma tributária e IVA", "certeza": "sem_detalhe",
     "texto": "Quer revisar a reforma para reduzir a alíquota do IVA e a carga sobre o consumo. Citou 20% em evento, mas o número não está no plano.",
     "quando": None},
    {"cand": "flavio", "titulo": "Energia e combustíveis", "certeza": "sem_detalhe",
     "texto": "Propõe reduzir impostos sobre energia elétrica e combustíveis, sem dizer quais tributos nem como compensar.",
     "quando": None},
    {"cand": "flavio", "titulo": "Estatais", "certeza": "sem_detalhe",
     "texto": "Retoma o programa de desestatização, avaliando caso a caso. Não lista quais empresas seriam privatizadas.",
     "quando": None},
    {"cand": "flavio", "titulo": "Custo de contratar", "certeza": "congresso",
     "texto": "Reduz gradualmente os encargos sobre a folha de pagamento, o que baixaria o custo de contratar.",
     "quando": [{"vinculo": ["empresario"]}]},
    {"cand": "flavio", "titulo": "Primeiro emprego e 50+", "certeza": "congresso",
     "texto": "Cria modalidades de contrato para jovens de 18 a 24 anos em busca do primeiro emprego e para maiores de 50 anos desempregados há 12 meses ou mais.",
     "quando": [{"vinculo": ["desempregado"]}]},
    {"cand": "flavio", "titulo": "CLT ou pagamento por hora", "certeza": "congresso",
     "texto": "Assinou proposta legislativa que permitiria escolher entre a CLT e um regime de remuneração por horas trabalhadas, com benefícios proporcionais. Também defende jornadas flexíveis.",
     "quando": [{"vinculo": ["clt", "autonomo"]}]},
    {"cand": "flavio", "titulo": "Escala 6x1", "certeza": "campanha",
     "texto": "Passou a apoiar o fim da escala 6x1 no Senado. A posição é recente e não está no plano original.",
     "quando": [{"vinculo": ["clt"]}]},
    {"cand": "flavio", "titulo": "Salário mínimo", "certeza": "sem_detalhe",
     "texto": "O plano não traz regra de reajuste real do salário mínimo. Declarações recentes indicam apoio à continuidade de direitos e programas sociais.",
     "quando": [{"renda": ["ate_3k"]}, {"vinculo": ["aposentado"]}]},
    {"cand": "flavio", "titulo": "Aposentadorias", "certeza": "sem_detalhe",
     "texto": "Segundo a imprensa, as posições sobre reajuste de aposentadorias seguem sem detalhamento.",
     "quando": [{"vinculo": ["aposentado"]}]},
    {"cand": "flavio", "titulo": "Programas sociais", "certeza": "campanha",
     "texto": "Declarações recentes do candidato indicam apoio à continuidade de programas sociais. Nas fontes consultadas não há detalhes sobre cada programa.",
     "quando": [{"bolsa": ["sim"]}]},
    {"cand": "flavio", "titulo": "Moradia", "certeza": "no_plano",
     "texto": "Retoma o Casa Verde e Amarela, com meta de 2,5 milhões de moradias.",
     "quando": [{"renda": ["ate_3k", "3k_5k"]}]},
    {"cand": "flavio", "titulo": "Seguro e armazenagem rural", "certeza": "no_plano",
     "texto": "Amplia o seguro rural, reorganiza dívidas do setor e aumenta a capacidade de armazenagem das safras.",
     "quando": [{"vinculo": ["produtor"]}]},
    {"cand": "flavio", "titulo": "Serviço público", "certeza": "sem_detalhe",
     "texto": "Propõe reforma administrativa, corte de ao menos 10 ministérios e de cargos comissionados e combate a privilégios e penduricalhos. Não detalha quais despesas seriam cortadas.",
     "quando": [{"vinculo": ["servidor"]}]},
    {"cand": "flavio", "titulo": "Crédito para empreendedores", "certeza": "no_plano",
     "texto": "Quer transformar a Caixa no \"Banco da Prosperidade\", com crédito para empreendedores e financiamento habitacional.",
     "quando": [{"vinculo": ["empresario", "autonomo"]}]},
    {"cand": "flavio", "titulo": "Refinanciamento de dívidas", "certeza": "campanha",
     "texto": "Apresentou, no 2º turno, uma proposta de refinanciamento de dívidas pela Caixa.",
     "quando": [{"divida": ["sim"]}]},
]

SIMULADOR = {"campos": CAMPOS, "impactos": IMPACTOS, "certeza": CERTEZA}

# ---------------------------------------------------------------------------
# 2) Quiz: opções embaralhadas e sem nome de candidato até o resultado
# ---------------------------------------------------------------------------
QUIZ = [
    {"tema": "Estatais", "pergunta": "Qual deve ser o papel das empresas estatais?",
     "opcoes": [
         {"cand": "lula", "texto": "Usá-las como instrumento de política industrial e energética, como a Petrobras ampliando refino e distribuição de combustíveis."},
         {"cand": "flavio", "texto": "Reduzir a presença do Estado nas empresas, avaliando caso a caso quais podem ser privatizadas."},
     ]},
    {"tema": "Contas públicas", "pergunta": "Como equilibrar as contas do governo?",
     "opcoes": [
         {"cand": "lula", "texto": "Manter as regras do arcabouço fiscal e apostar no crescimento e na eficiência do gasto."},
         {"cand": "flavio", "texto": "Cortar despesas: menos ministérios, menos cargos comissionados e um teto para a dívida."},
     ]},
    {"tema": "Impostos", "pergunta": "O que fazer com a reforma tributária?",
     "opcoes": [
         {"cand": "lula", "texto": "Implementar a reforma já aprovada e manter a isenção de Imposto de Renda até R$ 5 mil e a tributação de offshores."},
         {"cand": "flavio", "texto": "Revisar a reforma para reduzir a carga sobre o consumo, a energia e os combustíveis."},
     ]},
    {"tema": "Emprego", "pergunta": "Como estimular o emprego e proteger quem trabalha?",
     "opcoes": [
         {"cand": "lula", "texto": "Regras de proteção e jornada: fim da escala 6x1 e amparo a trabalhadores de aplicativos."},
         {"cand": "flavio", "texto": "Menos custo de contratação: reduzir encargos sobre a folha e ampliar contratos flexíveis."},
     ]},
    {"tema": "Infraestrutura", "pergunta": "Quem deve liderar os investimentos em obras?",
     "opcoes": [
         {"cand": "lula", "texto": "O governo, com o Novo PAC, somado a concessões de ferrovias, portos e aeroportos."},
         {"cand": "flavio", "texto": "Parcerias com o setor privado (PPPs e concessões) e um fundo com ativos da União."},
     ]},
    {"tema": "Energia", "pergunta": "Qual o caminho para a energia e os combustíveis?",
     "opcoes": [
         {"cand": "lula", "texto": "Fortalecer a Petrobras: mais exploração e refino e volta à distribuição de combustíveis."},
         {"cand": "flavio", "texto": "Ampliar petróleo e gás, incluindo liberar o fracking, e reduzir impostos sobre energia e combustíveis."},
     ]},
    {"tema": "Crédito e indústria", "pergunta": "Como apoiar empresas e indústria?",
     "opcoes": [
         {"cand": "lula", "texto": "Política industrial com bancos públicos (BNDES), fundos garantidores e programas como o Pronampe."},
         {"cand": "flavio", "texto": "Desregulamentar, baixar o custo de produzir e ampliar o crédito para empreendedores via Caixa."},
     ]},
    {"tema": "Área social", "pergunta": "Qual a prioridade na área social?",
     "opcoes": [
         {"cand": "lula", "texto": "Manter e ampliar o Bolsa Família e a proteção social."},
         {"cand": "flavio", "texto": "Retomar o programa habitacional Casa Verde e Amarela, com meta de 2,5 milhões de moradias."},
     ]},
    {"tema": "Serviço público", "pergunta": "O que fazer com o serviço público?",
     "opcoes": [
         {"cand": "lula", "texto": "Valorizar os servidores e manter a negociação permanente."},
         {"cand": "flavio", "texto": "Fazer reforma administrativa e combater privilégios e penduricalhos."},
     ]},
    {"tema": "Crescimento", "pergunta": "Qual a estratégia para o país crescer?",
     "opcoes": [
         {"cand": "lula", "texto": "Investimento público, indústria e renda, sem meta numérica de PIB."},
         {"cand": "flavio", "texto": "Meta de crescer 4% ao ano por uma década, com corte de gastos e de impostos."},
     ]},
]

# ---------------------------------------------------------------------------
# 3) Glossário em português claro (aparece como dica nos textos do site)
# ---------------------------------------------------------------------------
GLOSSARIO = [
    {"termo": "arcabouço fiscal", "alias": [],
     "def": "Conjunto de regras que limita o crescimento dos gastos do governo federal em relação à arrecadação e define metas para as contas públicas."},
    {"termo": "resultado primário", "alias": ["superávit", "déficit", "déficit primário", "superávit primário"],
     "def": "Diferença entre o que o governo arrecada e o que gasta, sem contar os juros da dívida. Se sobra dinheiro, é superávit; se falta, é déficit."},
    {"termo": "dívida bruta", "alias": [],
     "def": "Total que o governo deve, medido em proporção do PIB. Em agosto de 2026 estava em 82,9% do PIB, segundo dados do Banco Central reunidos pelo InvestNews."},
    {"termo": "teto da dívida", "alias": [],
     "def": "Limite para o tamanho da dívida pública. No plano de Flávio Bolsonaro o valor do limite não é detalhado."},
    {"termo": "PIB", "alias": [],
     "def": "Soma de tudo o que o país produz em um ano. É a medida mais usada do tamanho da economia."},
    {"termo": "IVA", "alias": ["imposto sobre valor agregado"],
     "def": "Imposto cobrado sobre o consumo de bens e serviços. A reforma tributária cria um IVA que substitui vários tributos atuais. A alíquota final ainda não está definida."},
    {"termo": "reforma tributária", "alias": [],
     "def": "Mudança aprovada pelo Congresso na forma de cobrar os impostos sobre o consumo. Ainda depende de regulamentação para valer por completo."},
    {"termo": "Imposto Seletivo", "alias": [],
     "def": "Imposto extra sobre produtos considerados prejudiciais à saúde, o que pode torná-los mais caros."},
    {"termo": "offshore", "alias": ["offshores"],
     "def": "Investimento ou empresa mantidos no exterior, muitas vezes por pessoas de renda alta."},
    {"termo": "fundos exclusivos", "alias": [],
     "def": "Fundos de investimento criados para um único cotista ou poucos, geralmente pessoas de alta renda."},
    {"termo": "encargos sobre a folha", "alias": ["encargos", "folha de pagamento", "desoneração da folha"],
     "def": "Tributos e contribuições que a empresa paga além do salário ao contratar. Reduzi-los baixa o custo de contratar, mas também reduz a arrecadação."},
    {"termo": "escala 6x1", "alias": ["6x1"],
     "def": "Jornada em que a pessoa trabalha seis dias e folga um."},
    {"termo": "PPP", "alias": ["PPPs", "parceria público-privada", "parcerias público-privadas"],
     "def": "Parceria público-privada: contrato de longo prazo em que uma empresa privada constrói ou opera um serviço público e é paga pelo governo, por tarifas ou pelos dois."},
    {"termo": "concessão", "alias": ["concessões"],
     "def": "O governo repassa a uma empresa, por um período, a exploração de uma rodovia, ferrovia, porto ou aeroporto, e a empresa investe e cobra pelo uso."},
    {"termo": "securitização", "alias": [],
     "def": "Transformar valores que o governo tem a receber no futuro em títulos vendidos hoje, para antecipar dinheiro."},
    {"termo": "privatização", "alias": ["privatizações", "privatizadas", "privatizar", "desestatização"],
     "def": "Venda ou redução da participação do governo em uma empresa estatal. No plano de Flávio, o programa se chama Programa Nacional de Desestatização (PND)."},
    {"termo": "estatais", "alias": ["estatal"],
     "def": "Empresas controladas pelo governo, como Petrobras, Caixa e Correios."},
    {"termo": "reforma administrativa", "alias": [],
     "def": "Mudanças nas regras e na estrutura do serviço público: cargos, carreiras, remuneração e número de ministérios."},
    {"termo": "cargos comissionados", "alias": [],
     "def": "Cargos de confiança preenchidos por indicação, sem concurso público."},
    {"termo": "penduricalhos", "alias": [],
     "def": "Pagamentos extras que elevam a remuneração de servidores acima do salário-base."},
    {"termo": "BNDES", "alias": [],
     "def": "Banco público de fomento que financia investimentos de longo prazo de empresas e governos."},
    {"termo": "Pronampe", "alias": [],
     "def": "Programa de crédito para micro e pequenas empresas, com garantia do governo."},
    {"termo": "Novo PAC", "alias": [],
     "def": "Programa do governo federal de investimentos em obras de infraestrutura, habitação, energia e outras áreas."},
    {"termo": "Nova Indústria Brasil", "alias": [],
     "def": "Política industrial do governo Lula, com financiamento e incentivos a setores considerados estratégicos."},
    {"termo": "Plano Safra", "alias": [],
     "def": "Conjunto de linhas de crédito rural anunciado pelo governo a cada safra, com juros e condições definidos para o produtor."},
    {"termo": "fracking", "alias": [],
     "def": "Técnica de extração de petróleo e gás por fratura hidráulica de rochas. É debatida por seus impactos ambientais."},
    {"termo": "Casa Verde e Amarela", "alias": [],
     "def": "Programa de habitação popular do governo Bolsonaro, substituído em 2023 pelo Minha Casa, Minha Vida."},
    {"termo": "ganho real", "alias": ["acima da inflação"],
     "def": "Aumento acima da inflação. Quando o salário mínimo tem ganho real, o poder de compra cresce, não só o valor nominal."},
    {"termo": "MEI", "alias": [],
     "def": "Microempreendedor individual: trabalhador por conta própria com CNPJ e regras simplificadas."},
]
