# 🤖 Legal Chat Bot

> Sistema de Conversação Jurídica com RAG Otimizado para Recursos Limitados

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Visão Geral

O **Legal Chat Bot** é um sistema conversacional especializado em direito brasileiro que implementa técnicas de Retrieval-Augmented Generation (RAG) usando algoritmos clássicos de Machine Learning. O projeto foi desenvolvido com foco em **estabilidade**, **baixo consumo de recursos** e **respostas instantâneas**.

### 🎯 Características Principais

- ⚡ **Respostas instantâneas** (~50ms por consulta)
- 🧠 **Classificação automática** de consultas jurídicas vs. conversacionais  
- 🔍 **Busca híbrida** (TF-IDF + keyword matching)
- 📚 **Base de conhecimento** com 50+ documentos jurídicos sintéticos
- 💭 **Memória conversacional** para contexto contínuo
- 🎯 **Especialização** em 4 áreas: Consumidor, Civil, Trabalhista, Constitucional

## 🚫 Por que NÃO usamos LLMs modernos?

Este projeto **deliberadamente evita** modelos complexos como BERT, Llama ou GPT devido a limitações técnicas reais:

### Problemas Identificados:
```
❌ Mutex Locks: [mutex.cc : 452] RAW: Lock blocking 0x123895ed8
❌ RAM Overflow: >8GB necessários apenas para carregamento
❌ Threading Conflicts: Incompatibilidade com ambiente de desenvolvimento
❌ Latência Alta: 2-15s por resposta vs. 50ms com TF-IDF
```

### Modelos Testados e Rejeitados:
- `rufimelo/Legal-BERTimbau-large` → Mutex locks
- `meta-llama/Llama-3.2-1B-Instruct` → RAM overflow  
- `neuralmind/bert-base-portuguese-cased` → Threading issues

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────┐
│           Legal Chat Bot                │
├─────────────────────────────────────────┤
│  QuestionClassifier                     │
│  ├── TF-IDF Vectorizer                 │
│  └── Logistic Regression               │
├─────────────────────────────────────────┤
│  HybridRetriever                        │
│  ├── 70% TF-IDF Similarity             │
│  ├── 30% Keyword Overlap               │
│  └── Category Filtering                │
├─────────────────────────────────────────┤
│  ResponseGenerator                      │
│  ├── Template-based Responses          │
│  ├── Context Integration               │
│  └── Confidence Scoring                │
├─────────────────────────────────────────┤
│  ConversationMemory                     │
│  └── 10 Interaction History            │
└─────────────────────────────────────────┘
```

## 🚀 Quick Start

### 1. Instalação

```bash
# Clone o repositório
git clone <repo-url>
cd legal-chat-bot

# Instale dependências (apenas 2 pacotes principais!)
pip install scikit-learn numpy

# Ou use o requirements completo
pip install -r requirements.txt
```

### 2. Execução

```python
from legal_chat_bot import AdvancedLegalChatbot

# Inicializar o chatbot
bot = AdvancedLegalChatbot()

# Começar conversação
bot.conversar()
```

### 3. Exemplo de Uso

```
👋 Olá! Eu sou seu assistente jurídico virtual.

🤔 Sua pergunta: Quais são os direitos do consumidor em compras online?

🔍 Classificação: rag (confiança: 95%)
📚 Categoria: consumidor  
🎯 Documentos encontrados: 3
⭐ Confiança: 87%

📖 O Código de Defesa do Consumidor garante ao consumidor...
[resposta detalhada]

💬 Esta resposta foi útil? (1-5): 
```

## 📁 Estrutura do Projeto

```
legal-chat-bot/
├── legal_chat_bot.py          # Código principal do chatbot
├── gerarperguntas.py          # Script para gerar perguntas de teste
├── requirements.txt           # Dependências mínimas
├── DOCUMENTACAO_TECNICA.md    # Documentação técnica completa
├── README.md                  # Este arquivo
└── resultados_chatbot.csv     # Resultados de avaliações
```

## 🔧 Componentes Técnicos

### QuestionClassifier
```python
Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('classifier', LogisticRegression())
])
```
- **Função:** Classifica consultas como jurídicas (`rag`) ou conversacionais (`conversa`)
- **Performance:** ~85% accuracy

### HybridRetriever  
```python
score = (tfidf_similarity * 0.7) + (keyword_overlap * 0.3)
```
- **Função:** Busca híbrida combinando TF-IDF e sobreposição de palavras
- **Filtros:** Por categoria jurídica (consumidor, civil, trabalhista, constitucional)

### ResponseGenerator
- **Templates contextualizados** para respostas jurídicas
- **Integração de contexto** dos documentos recuperados  
- **Fallbacks** para consultas sem contexto relevante

## 📊 Performance

| Métrica | Valor |
|---------|-------|
| Latência média | ~50ms |
| Uso de RAM | ~200MB |
| Accuracy classificação | 85% |
| Confiança média respostas | 82% |

## 🧪 Testes e Avaliação

### Executar Testes
```python
from gerarperguntas import *

# Gerar perguntas de teste
perguntas = perguntas_rag + perguntas_conversa

# Avaliar sistema
for pergunta in perguntas:
    resposta = bot.perguntar(pergunta)
    # Avaliação manual ou automática
```

### Sistema de Feedback
```python
bot.avaliar_resposta(pergunta, resposta, nota_1_a_5)
```

## 📚 Base de Conhecimento

- **50+ documentos sintéticos** organizados por área jurídica
- **Categorias:** Consumidor (15), Trabalhista (15), Civil (12), Constitucional (10)
- **Indexação:** TF-IDF com 5000 features máximas
- **Busca:** Híbrida com filtros por especialidade

## 🔮 Limitações e Futuro

### Limitações Atuais
- ❌ Sem compreensão semântica profunda
- ❌ Base de conhecimento sintética limitada  
- ❌ Respostas baseadas em templates
- ❌ Impossibilidade de usar LLMs por restrições técnicas

### Roadmap Futuro
- 🔄 Investigar embeddings leves (<100MB)
- 🌐 API REST para separar interface/lógica
- 📄 Integração com documentos jurídicos reais
- 🎯 Modelo de ranking aprendido para relevância

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)  
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🆘 Suporte

Para dúvidas, problemas ou sugestões:

- 📧 Abra uma [issue](../../issues)
- 📖 Consulte a [documentação técnica](DOCUMENTACAO_TECNICA.md)
- 💬 Entre em contato com a equipe

---

**Desenvolvido com foco em estabilidade e eficiência** 🎯

> "Às vezes, soluções simples são mais eficazes que as complexas" - Princípio de engenharia aplicado ao NLP jurídico