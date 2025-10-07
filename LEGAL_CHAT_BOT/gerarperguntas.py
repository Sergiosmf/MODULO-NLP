from legal_chat_bot import AdvancedLegalChatbot

# instanciar o bot
bot = AdvancedLegalChatbot()

# exemplo de perguntas por categoria (adicione as suas 25/15/10 conforme necessário)
perguntas_rag = [
    # Direito do Consumidor (exemplos)
    "Quais são os direitos do consumidor ao comprar um produto com defeito?",
    "O que diz o Código de Defesa do Consumidor sobre propaganda enganosa?",
    "Existe prazo de garantia legal para produtos usados?",
    "Em compras online, o consumidor pode devolver o produto sem justificar?",
    "Quem é responsável por danos causados por um produto defeituoso?",
    "O que caracteriza venda casada segundo o CDC?",
    "Qual é o prazo para reclamar de vício oculto em um bem durável?",
    # Direito Trabalhista (exemplos)
    "Quais são os direitos do empregado em caso de demissão sem justa causa?",
    "Como funciona o cálculo de horas extras na CLT?",
    "Qual o tempo de licença maternidade previsto em lei?",
    "O que é aviso prévio proporcional ao tempo de serviço?",
    "Quais são as obrigações do empregador em relação ao FGTS?",
    "Como se calcula o 13º salário?",
    "Quais são os direitos do trabalhador doméstico?",
    # Direito Civil (exemplos)
    "Como funciona a usucapião ordinária?",
    "O que é contrato de comodato?",
    "Quais são os requisitos para a doação ser válida?",
    "Qual a diferença entre posse e propriedade?",
    "Como é feita a partilha de bens no divórcio?",
    "Quais são os herdeiros necessários segundo o Código Civil?",
    # Direito Constitucional (exemplos)
    "O que diz a Constituição sobre liberdade de expressão?",
    "Quais são os direitos sociais previstos na Constituição de 1988?",
    "Como se caracteriza o habeas corpus?",
    "O que é controle de constitucionalidade difuso?",
    "Quais são os poderes da União segundo a Constituição?",
]
perguntas_conversa = [
    "Oi, tudo bem?",
    "Qual é o seu nome?",
    "Como você está hoje?",
    "Pode me contar uma piada?",
    "Você gosta de música?",
    "Qual é a capital do Brasil?",
    "Que dia é hoje?",
    "Qual é a sua cor favorita?",
    "Você gosta de futebol?",
    "Quem foi o primeiro homem na Lua?",
    "Qual é a sua comida preferida?",
    "Você pode sugerir um filme bom?",
    "Quais são seus hobbies?",
    "Você gosta de viajar?",
    "Quem é o seu escritor favorito?",
    "Qual é o seu animal preferido?",
    "Você sabe cantar?",
    "Pode conversar comigo sobre o tempo?",
    "Qual é o seu livro favorito?",
    "Você gosta de café ou de chá?",
    "Quem descobriu o Brasil?",
    "Pode me dar um conselho de vida?",
    "Qual é a sua estação do ano favorita?",
    "Você prefere praia ou montanha?",
    "Você gosta de videogames?",
]
perguntas_calculo = [
    "Quanto é 2 + 2?",
    "Calcule 10 dividido por 2.",
    "Qual é a raiz quadrada de 16?",
    "Multiplique 6 por 7.",
    "Somar 15 e 30.",
    "Subtraia 20 de 50.",
    "Quanto é 3 elevado à 4?",
    "Calcule 100 menos 25.",
    "Divida 81 por 9.",
    "Qual é o resto de 10 dividido por 3?",
    "Qual é a área de um quadrado de lado 5?",
    "Quanto dá 8 vezes 9?",
    "Some 11 e 22.",
    "Quanto é 7 ao quadrado?",
    "Calcule 144 dividido por 12.",
    "Subtraia 75 de 200.",
    "Quanto é 2 elevado à 10?",
    "Calcule 99 menos 33.",
    "Quanto dá 4 vezes 25?",
    "Divida 121 por 11.",
    "Some 18 e 27.",
    "Qual é a raiz cúbica de 27?",
    "Multiplique 12 por 12.",
    "Qual é o valor de 64 dividido por 8?",
    "Subtraia 9 de 90.",
]
perguntas_fora = [
    "Quem ganhou a Copa do Mundo de 2018?",
    "Como fazer um bolo de chocolate simples?",
    "Qual é a distância da Terra à Lua?",
    "Explique a teoria da relatividade.",
    "Quem é o presidente dos Estados Unidos?",
    "Como programar em Python?",
    "Qual é a capital da Austrália?",
    "Quem pintou a Mona Lisa?",
    "O que é algoritmo de Dijkstra?",
    "Como cuidar de plantas suculentas?",
    "Qual a altura do Monte Everest?",
    "Quem escreveu Dom Casmurro?",
    "Como tocar violão?",
    "O que é a Via Láctea?",
    "Qual é a fórmula da água?",
    "Quem ganhou o Oscar de melhor filme em 2020?",
    "Como fazer arroz soltinho?",
    "Qual é a velocidade da luz?",
    "Quem foi Albert Einstein?",
    "Como aprender espanhol rapidamente?",
    "O que é JavaScript?",
    "Quem inventou o telefone?",
    "Como funciona a blockchain?",
    "Qual é a maior cachoeira do mundo?",
    "Como plantar tomates em vaso?",
]

# 1) Avaliação do classificador
eval_fns = bot.evaluation_functions()
test_queries = perguntas_rag + perguntas_conversa + perguntas_calculo + perguntas_fora
test_labels  = (
    ["rag_required"] * len(perguntas_rag) +
    ["general_conversation"] * len(perguntas_conversa) +
    ["calculation"] * len(perguntas_calculo) +
    ["out_of_scope"] * len(perguntas_fora)
)
metrics = eval_fns["eval_classifier"](test_queries, test_labels)
print("Métricas do classificador:", metrics)

# 2) Avaliação do retriever (exemplo simples)
# Estrutura: [(pergunta, [titulos_de_fontes_esperados]), …]
exemplos_retriever = [
    ("Quais são os direitos do consumidor em compras online?", ["Direito de Arrependimento"]),
    ("Explique o conceito de usucapião no Código Civil.", ["Usucapião"]),
    # … outras (pergunta, lista de fontes corretas) …
]
precision_at3 = eval_fns["eval_retriever"](exemplos_retriever)
print("Precisão@3 do retriever:", precision_at3)

# 3) Processar as perguntas e salvar respostas em CSV
import csv

with open("resultados_chatbot.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Pergunta", "Categoria prevista", "Resposta"])
    for pergunta, etiqueta in zip(test_queries, test_labels):
        resposta = bot.ask(pergunta)
        writer.writerow([pergunta, etiqueta, resposta])

print("Respostas salvas em resultados_chatbot.csv")