"""
Versão avançada do Chatbot Jurídico com RAG.

Este módulo implementa um chatbot em português que cumpre os requisitos
descritos no projeto final: classificação automática de perguntas,
sistema RAG aprimorado com busca híbrida, interface conversacional com
memória e feedback, indicadores de confiança, referências às fontes e
funções de avaliação. A base de conhecimento usa mais de 50
documentos sintéticos de diversas áreas do direito brasileiro.

Autor: OpenAI Assistant
"""

from __future__ import annotations

import re
import random
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support


def _normalize(text: str) -> str:
    """Normaliza texto para comparação."""
    return re.sub(r"\s+", " ", text.strip().lower())


@dataclass
class HybridRetriever:
    """Combina TF‑IDF e sobreposição de palavras-chave para busca.

    Além das listas de documentos e títulos, armazena uma categoria para cada
    documento. Isso permite filtrar a busca por especialidade jurídica,
    retornando apenas documentos que correspondam a um domínio específico
    quando um filtro é fornecido. A pesquisa híbrida combina 70% da
    similaridade TF‑IDF com 30% da sobreposição de palavras-chave. Se o
    usuário fornecer um filtro de categoria, documentos de outras áreas
    recebem pontuação zero e são descartados na ordenação.
    """

    documents: List[str]
    titles: List[str]
    categories: List[str]
    vectorizer: TfidfVectorizer = field(default_factory=lambda: TfidfVectorizer())
    tfidf_matrix: Optional[np.ndarray] = None

    def __post_init__(self) -> None:
        # Pré-processa todos os documentos para a matriz TF‑IDF.
        normalized = [_normalize(doc) for doc in self.documents]
        self.tfidf_matrix = self.vectorizer.fit_transform(normalized)

    def search(self, query: str, top_k: int = 3, category_filter: Optional[str] = None) -> List[Tuple[str, str, float, float]]:
        """Realiza busca híbrida. Retorna lista de (title, doc, score_híbrido, score_tfidf).

        Se category_filter for fornecida, somente documentos cuja
        categoria corresponda ao filtro serão considerados no ranking. Caso
        contrário, todos os documentos participam da busca. A ordenação é
        feita pelo score híbrido (70% TF‑IDF + 30% palavra-chave).
        """
        if not query:
            return []
        q_norm = _normalize(query)
        q_vec = self.vectorizer.transform([q_norm])
        # similaridade TF‑IDF
        tfidf_scores = (self.tfidf_matrix @ q_vec.T).toarray().ravel()
        # sobreposição de palavras-chave
        query_tokens = set(q_norm.split())
        keyword_scores = []
        for doc in self.documents:
            doc_tokens = set(_normalize(doc).split())
            overlap = len(query_tokens & doc_tokens)
            keyword_scores.append(overlap)
        keyword_scores = np.array(keyword_scores, dtype=float)
        # normaliza pontuações
        if keyword_scores.max() > 0:
            keyword_scores /= keyword_scores.max()
        if tfidf_scores.max() > 0:
            tfidf_scores /= tfidf_scores.max()
        hybrid_scores = 0.7 * tfidf_scores + 0.3 * keyword_scores
        # aplica filtro de categoria: se definido, zera pontuações de docs de outras categorias
        if category_filter:
            for idx, cat in enumerate(self.categories):
                if cat.lower() != category_filter.lower():
                    hybrid_scores[idx] = -np.inf  # descarte
        # seleciona os top_k índices com scores mais altos
        ranked_indices = np.argsort(-hybrid_scores)[:top_k]
        results: List[Tuple[str, str, float, float]] = []
        for idx in ranked_indices:
            # ignora itens com pontuação negativa infinita
            if hybrid_scores[idx] == -np.inf:
                continue
            results.append((self.titles[idx], self.documents[idx], float(hybrid_scores[idx]), float(tfidf_scores[idx])))
        return results


class AdvancedQueryClassifier:
    """Classificador de queries em três categorias: rag_required, general, out_of_scope."""

    def __init__(self) -> None:
        self.pipeline: Pipeline[str] = Pipeline([
            ("tfidf", TfidfVectorizer()),
            ("clf", LogisticRegression(max_iter=200))
        ])
        self.is_trained = False
        self._metrics: Tuple[float, float, float] = (0.0, 0.0, 0.0)
        self._train()

    def _train(self) -> None:
        queries: List[str] = []
        targets: List[str] = []
        # Perguntas jurídicas (RAG)
        rag_q = [
            "O que diz o Código de Defesa do Consumidor sobre garantia de produtos?",
            "Quais são os deveres do empregador segundo a CLT?",
            "Explique o conceito de usucapião no Código Civil.",
            "Quais são os direitos fundamentais na Constituição?",
            "O que é crime de furto simples?",
            "Como funciona a sucessão legítima?",
            "Quais são os direitos do réu em processo penal?",
            "Direitos trabalhistas de gestantes segundo a CLT.",
            "Responsabilidade civil em caso de dano moral.",
            "Quais são os direitos do consumidor em compras online?"
        ]
        queries += rag_q
        targets += ["rag_required"] * len(rag_q)
        # Perguntas gerais (conversa)
        general_q = [
            "Oi, como você está?",
            "Qual é o seu nome?",
            "Pode me contar uma piada?",
            "Qual é a capital do Brasil?",
            "Vamos conversar?",
            "Olá!",
            "Você gosta de música?",
            "Quem foi o primeiro homem na lua?",
            "Quais são seus hobbies?",
            "Como você se sente hoje?"
        ]
        queries += general_q
        targets += ["general_conversation"] * len(general_q)
        # Perguntas fora do escopo
        out_q = [
            "Como fazer um bolo de chocolate?",
            "Qual é a distância da Terra à Lua?",
            "Quem ganhou o último mundial de futebol?",
            "Explique a teoria da relatividade.",
            "Como programar em Python?",
            "Qual é a capital da Austrália?",
            "Quem pintou a Mona Lisa?",
            "O que é algoritmo de Dijkstra?",
            "Como cuidar de plantas suculentas?",
            "Qual a altura do Monte Everest?"
        ]
        queries += out_q
        targets += ["out_of_scope"] * len(out_q)

        # Perguntas de cálculo simples (nova categoria para maior cobertura)
        calc_q = [
            "Quanto é 2 + 2?",
            "Calcule 10 dividido por 2.",
            "Qual é a raiz quadrada de 16?",
            "Multiplique 6 por 7.",
            "Somar 15 e 30.",
            "Subtraia 20 de 50.",
            "Quanto é 3 elevado à 4?",
            "Calcule 100 menos 25.",
            "Divida 81 por 9.",
            "Qual é o resto de 10 dividido por 3?"
        ]
        queries += calc_q
        targets += ["calculation"] * len(calc_q)
        X_train, X_test, y_train, y_test = train_test_split(queries, targets, test_size=0.2, random_state=42)
        self.pipeline.fit(X_train, y_train)
        self.is_trained = True
        prec, rec, f1, _ = precision_recall_fscore_support(y_test, self.pipeline.predict(X_test), average='weighted', zero_division=0)
        self._metrics = (prec, rec, f1)

    def predict(self, query: str) -> str:
        return self.pipeline.predict([query])[0]

    def metrics(self) -> Tuple[float, float, float]:
        return self._metrics


@dataclass
class AdvancedLegalChatbot:
    """Combina classificação, busca híbrida, interface de conversa, confiança e referências."""

    retriever: HybridRetriever = field(init=False)
    classifier: AdvancedQueryClassifier = field(init=False)
    history: List[Tuple[str, str]] = field(default_factory=list)
    feedback_log: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        docs, titles, categories = self._generate_documents()
        # instancia o retriever com categorias
        self.retriever = HybridRetriever(documents=docs, titles=titles, categories=categories)
        self.classifier = AdvancedQueryClassifier()

    def _generate_documents(self) -> Tuple[List[str], List[str], List[str]]:
        """Gera uma base sintética de 70+ snippets de várias disciplinas jurídicas.

        Retorna três listas paralelas: documentos, títulos e categorias. Cada
        categoria corresponde ao ramo do direito de onde o snippet foi extraído.
        """
        docs: List[str] = []
        titles: List[str] = []
        categories: List[str] = []
        # Cada sublista representa uma especialidade; cada item (titulo, texto)
        data = {
            "Consumidor": [
                ("Direito de Arrependimento", "O consumidor pode desistir de compras online em até 7 dias, com reembolso integral."),
                ("Garantia Legal", "Produtos duráveis possuem garantia legal mínima de 90 dias conforme o CDC."),
                ("Propaganda Enganosa", "É proibido veicular publicidade enganosa ou abusiva; o fornecedor deve corrigir e indenizar."),
                ("Troca de Produtos", "Lojas não são obrigadas a trocar produtos sem defeito, exceto se oferecerem essa política."),
                ("Responsabilidade Solidária", "Fabricante, distribuidor e vendedor respondem solidariamente por vícios do produto."),
                ("Dano Moral ao Consumidor", "Cobrança indevida gera direito à repetição do indébito e indenização por dano moral."),
                ("Entrega em Atraso", "O atraso na entrega permite ao consumidor rescindir o contrato ou exigir cumprimento forçado."),
                ("Cadastro Positivo", "Consumidores têm direito de acessar e corrigir seus dados em cadastros de crédito."),
                ("Compras Internacionais", "Importações pela internet seguem as regras do CDC quanto a garantia e arrependimento."),
                ("Venda Casada", "É vedada a prática de condicionar a venda de um produto à compra de outro."),
                # Mais direitos do consumidor (ampliação da base)
                ("Direito à Informação", "O consumidor tem direito de ser informado de forma clara e adequada sobre produtos e serviços."),
                ("Preços Claros", "O fornecedor deve informar preços de forma clara e sem ambiguidades."),
                ("Indenização por Danos", "Consumidores lesados por produtos ou serviços têm direito a indenização por perdas e danos."),
                ("Direito à Segurança", "Produtos e serviços não devem apresentar riscos à saúde ou segurança do consumidor."),
                ("Proteção contra Cláusulas Abusivas", "Contratos de consumo não podem conter cláusulas que coloquem o consumidor em desvantagem excessiva."),
                ("Direito de Reclamar", "O consumidor pode reclamar de falhas na prestação do serviço ou qualidade do produto a qualquer momento."),
            ],
            "Trabalho": [
                ("Férias Anuais", "Após 12 meses de trabalho, o empregado tem direito a 30 dias de férias remuneradas."),
                ("Décimo Terceiro", "O 13º salário corresponde à remuneração devida em dezembro, pago em duas parcelas."),
                ("FGTS", "O Fundo de Garantia do Tempo de Serviço é depositado mensalmente pelo empregador."),
                ("Aviso Prévio", "O aviso prévio proporcional ao tempo de serviço deve ser concedido na rescisão sem justa causa."),
                ("Horas Extras", "Trabalho além da jornada normal deve ser remunerado com adicional mínimo de 50%."),
                ("Licença Maternidade", "A gestante tem direito a 120 dias de licença remunerada, prorrogáveis em alguns casos."),
                ("Licença Paternidade", "O pai tem direito a 5 dias de licença remunerada após o nascimento do filho."),
                ("Seguro-Desemprego", "Trabalhadores dispensados sem justa causa podem receber parcelas de seguro-desemprego."),
                ("Trabalho Noturno", "Trabalho noturno urbano entre 22h e 5h deve ter remuneração superior."),
                ("Intervalo Intrajornada", "Empregados que trabalham mais de 6 horas têm direito a intervalo mínimo de 1 hora."),
            ],
            "Civil": [
                ("Contratos", "Contratos são acordos entre partes com obrigações recíprocas; exigem boa-fé."),
                ("Posse", "Posse é o exercício de fato de poderes inerentes à propriedade."),
                ("Usucapião", "A aquisição de propriedade por usucapião exige posse contínua e incontestada por certo prazo."),
                ("Responsabilidade Civil", "Quem causa dano a outrem é obrigado a repará-lo."),
                ("Doação", "Doação é o contrato em que uma pessoa transfere bens ou vantagens a outra gratuitamente."),
                ("Herança", "Na sucessão legítima, os herdeiros recebem o patrimônio conforme a ordem de vocação hereditária."),
                ("Casamento", "É união entre duas pessoas, instituída perante a lei, com regime de bens escolhido pelos cônjuges."),
                ("Locação", "Contrato de locação de imóvel é oneroso e requer prazo e valor estabelecidos."),
                ("Alienação Fiduciária", "Bem é transferido em garantia até o cumprimento da obrigação pelo devedor."),
                ("Penhor", "Bem móvel dado em garantia, podendo a posse ficar com o devedor ou credor."),
            ],
            "Constitucional": [
                ("Liberdade de Expressão", "A Constituição assegura a livre manifestação do pensamento, vedado o anonimato."),
                ("Igualdade", "Todos são iguais perante a lei, sem distinção de qualquer natureza."),
                ("Direito à Vida", "O direito à vida é inviolável, abrangendo proteção contra ameaças."),
                ("Direito de Propriedade", "A propriedade deve atender à sua função social."),
                ("Separação de Poderes", "Executivo, Legislativo e Judiciário são independentes e harmônicos."),
                ("Saúde e Educação", "São direitos de todos e dever do Estado, garantidos mediante políticas sociais."),
                ("Direitos Sociais", "Trabalho, moradia, lazer e segurança são direitos fundamentais."),
                ("Mandado de Segurança", "Garantia constitucional para proteger direito líquido e certo."),
                ("Habeas Corpus", "Remédio constitucional contra ilegalidade ou abuso de poder na liberdade de ir e vir."),
                ("Nacionalidade", "Regula quem é brasileiro nato ou naturalizado."),
            ],
            "Penal": [
                ("Furto Simples", "Subtrair para si ou para outrem coisa alheia móvel sem violência ou grave ameaça."),
                ("Roubo", "Subtrair coisa móvel com emprego de grave ameaça ou violência à pessoa."),
                ("Homicídio", "Tirar a vida de alguém; pena varia conforme qualificadoras."),
                ("Lesão Corporal", "Ofender a integridade corporal ou a saúde de outrem."),
                ("Estelionato", "Obter vantagem ilícita induzindo alguém a erro mediante fraude."),
                ("Receptação", "Adquirir, receber ou transportar coisa proveniente de crime."),
                ("Tráfico de Drogas", "Importar, exportar ou comercializar drogas sem autorização."),
                ("Lavagem de Dinheiro", "Ocultar a origem ilícita de bens ou valores."),
                ("Crimes Cibernéticos", "Praticar delitos por meio de dispositivos digitais ou rede."),
                ("Pena de Multa", "Pena pecuniária aplicada isoladamente ou cumulada com outra pena."),
            ],
            "Família": [
                ("Guarda Compartilhada", "Responsabilidade conjunta dos pais nas decisões sobre os filhos."),
                ("Adoção", "Processo judicial que estabelece vínculo parental entre adotante e adotado."),
                ("Pensão Alimentícia", "Prestação financeira devida para subsistência de filhos ou cônjuges."),
                ("Divórcio", "Extinção do vínculo matrimonial com partilha de bens e definição de guarda."),
                ("União Estável", "Convivência pública e duradoura configurada como entidade familiar."),
                ("Tutela", "Proteção de menores quando os pais não podem exercer o poder familiar."),
                ("Curatela", "Administração dos bens de pessoas incapazes maiores de idade."),
                ("Regime de Bens", "Define como se dará a administração e partilha do patrimônio do casal."),
                ("Alimentos Gravídicos", "Prestação devida para cobrir despesas da gestante."),
                ("Paternidade Socioafetiva", "Reconhecimento jurídico do vínculo afetivo como parentalidade."),
            ],
            "Administrativo": [
                ("Atos Administrativos", "Manifestação unilateral da Administração que produz efeitos jurídicos."),
                ("Poder de Polícia", "Competência da Administração de restringir direitos individuais em benefício coletivo."),
                ("Licitações", "Procedimentos para contratação de serviços ou compras pela Administração."),
                ("Improbidade Administrativa", "Condutas ilícitas de agentes que atentem contra a administração pública."),
                ("Serviços Públicos", "Atividades de interesse coletivo prestadas ou reguladas pelo Estado."),
                ("Bens Públicos", "Bens pertencentes às pessoas jurídicas de direito público, inalienáveis enquanto conservarem a sua afetação."),
                ("Agentes Públicos", "Indivíduos que exercem função pública seja efetiva ou temporariamente."),
                ("Concurso Público", "Processo seletivo para ingresso em cargos efetivos na Administração."),
                ("Responsabilidade do Estado", "O Estado responde pelos danos que seus agentes causarem a terceiros."),
                ("Convênios Administrativos", "Instrumentos de cooperação entre entes para execução de objetivos comuns."),
            ],
        }
        # Agrega todos em listas planas
        for category, snippets in data.items():
            for title, content in snippets:
                titles.append(title)
                docs.append(content)
                categories.append(category)
        return docs, titles, categories

    def _format_response(self, answer: str, used_rag: bool, confidence: float, sources: List[str]) -> str:
        explanation = "(Resposta direta)" if not used_rag else "(Resposta via RAG)"
        conf_pct = int(confidence * 100)
        sources_str = "; ".join(sources) if sources else "Nenhuma fonte relevante"
        disclaimer = "⚠️ Esta resposta é informativa e não substitui consulta profissional."
        limitacoes = "Limitações: base de conhecimento sintética; respostas podem ser incompletas."
        return f"{explanation} Confiança: {conf_pct}%\n{answer}\n\nFontes: {sources_str}\n{disclaimer}\n{limitacoes}"

    def _handle_general(self, query: str) -> str:
        greetings = [
            "Olá! Como posso ajudar?",
            "Oi! Estou aqui para conversar ou esclarecer dúvidas jurídicas.",
            "Olá! Pergunte-me algo sobre leis ou apenas cumprimente."
        ]
        if any(w in query.lower() for w in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]):
            return random.choice(greetings)
        return "Estou disponível para falar sobre direitos, leis e também bater um papo."

    def _handle_out_of_scope(self, query: str) -> str:
        return "Desculpe, essa pergunta está fora do escopo do meu conhecimento jurídico."

    def _handle_calculation(self, query: str) -> str:
        """Avalia expressões aritméticas simples presentes na pergunta."""
        expr_norm = query.lower()
        # Mapas de palavras para operadores
        replacements = {
            "mais": "+", "somar": "+", "adição": "+", "soma": "+", "e": "+", "add": "+",
            "menos": "-", "subtrair": "-", "subtraia": "-",
            "vezes": "*", "multiplicar": "*", "multiplique": "*",
            "dividido por": "/", "dividir": "/",
            "elevado à": "**", "elevado a": "**"
        }
        for k, v in replacements.items():
            expr_norm = expr_norm.replace(k, v)
        expr_norm = re.sub(r"[^0-9+\-*/().]", " ", expr_norm)
        expr_norm = re.sub(r"\s+", "", expr_norm)
        try:
            result = eval(expr_norm)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return f"O resultado é {result}."
        except Exception:
            return "Desculpe, não consegui calcular essa expressão."

    def _handle_rag(self, query: str) -> Tuple[str, float, List[str]]:
        # detecta a especialidade provável para filtrar resultados
        category = self._detect_specialty(query)
        results = self.retriever.search(query, top_k=3, category_filter=category)
        if not results:
            return "Não encontrei informações relevantes.", 0.0, []
        answer_lines: List[str] = []
        sources: List[str] = []
        top_score = results[0][2]
        for title, doc, hybrid_score, _ in results:
            answer_lines.append(doc)
            sources.append(title)
        answer_text = " ".join(answer_lines)
        return answer_text, top_score, sources

    def ask(self, query: str) -> str:
        self.history.append(("user", query))
        category = self.classifier.predict(query)
        used_rag = False
        confidence = 0.0
        sources: List[str] = []
        if category == "general_conversation":
            answer = self._handle_general(query)
        elif category == "out_of_scope":
            answer = self._handle_out_of_scope(query)
        elif category == "calculation":
            answer = self._handle_calculation(query)
        else:
            used_rag = True
            # coleta resposta usando RAG com filtro por especialidade
            answer, confidence, sources = self._handle_rag(query)
        formatted = self._format_response(answer, used_rag, confidence, sources)
        self.history.append(("assistant", formatted))
        return formatted

    def _detect_specialty(self, query: str) -> Optional[str]:
        """Tenta identificar a área do direito a partir de palavras‑chave presentes na pergunta.

        O objetivo é restringir a busca a documentos da especialidade correta quando
        possível. A detecção é feita usando listas simples de palavras para cada
        categoria. Se nenhuma categoria for identificada, retorna None.
        """
        q = query.lower()
        # mapeamento de especialidade para palavras‑chave
        keywords: Dict[str, List[str]] = {
            "Consumidor": ["consumidor", "consumidores", "produto", "compra", "cdc", "defesa do consumidor", "venda", "garantia", "Produto com Defeito", "Em caso de vício do produto, o consumidor pode exigir a substituição do item por outro da mesma espécie, a restituição imediata da quantia paga ou o abatimento proporcional do preço, conforme o CDC."],
            "Trabalho": ["trabalh", "clt", "empregad", "empregador", "licença", "salário", "ferias", "fgts"],
            "Civil": ["civil", "usucapi", "posse", "propriedade", "contrato", "herança", "família", "casamento"],
            "Constitucional": ["constitui", "direitos fundamentais", "liberdade", "igualdade", "habeas", "mandado de segurança"],
            "Penal": ["penal", "crime", "homicídio", "furto", "estelionato", "pena", "roubo"],
            "Família": ["guarda", "adoção", "pensão", "divórcio", "união estável", "tutela", "curatela"],
            "Administrativo": ["licita", "servidor", "agente público", "improbidade", "bens públicos", "concurso público"]
        }
        for category, words in keywords.items():
            for w in words:
                if w in q:
                    return category
        return None

    def chat(self) -> None:
        print("Chatbot Jurídico (avançado) iniciado. Digite 'sair' para encerrar.")
        while True:
            try:
                user_input = input("Você: ")
            except EOFError:
                break
            if user_input.strip().lower() in {"sair", "exit", "quit"}:
                print("Até logo!")
                break
            response = self.ask(user_input)
            print(f"Chatbot: {response}\n")
            fb = input("Essa resposta foi útil? (sim/não) ")
            self.feedback_log.append(fb.strip().lower())
            print()

    def evaluation_functions(self) -> Dict[str, callable]:
        """Retorna utilitários para avaliar classificador e retriever."""
        def eval_classifier(test_queries: List[str], test_labels: List[str]) -> Dict[str, float]:
            preds = self.classifier.pipeline.predict(test_queries)
            precision, recall, f1, _ = precision_recall_fscore_support(test_labels, preds, average='weighted', zero_division=0)
            return {"precision": precision, "recall": recall, "f1": f1}
        def eval_retriever(example_queries: List[Tuple[str, List[str]]]) -> float:
            hits = 0
            for query, expected_sources in example_queries:
                results = self.retriever.search(query, top_k=3)
                retrieved = [title for title, _, _, _ in results]
                if any(src in retrieved for src in expected_sources):
                    hits += 1
            return hits / len(example_queries) if example_queries else 0.0
        return {"eval_classifier": eval_classifier, "eval_retriever": eval_retriever}
    