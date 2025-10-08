# 🧠 Material Didático de Processamento de Linguagem Natural (NLP)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow.svg)](https://huggingface.co/transformers)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)

> **Autor:** [Sérgio Mendes dos Santos Filho](https://github.com/Sergiosmf)  
> **Professor:** [Dimmy Magalhães](https://github.com/dimmykarson)  
> **Instituição:** ICEV - Instituto de Ensino Superior - Pós-Graduação em Inteligência Artificial - MODULO 06 - Processamento de Lingaugem Natural  
> **Propósito:** Material educativo completo para aprendizado de NLP e Transformers

## 📚 Sobre este Repositório

Este repositório contém material didático abrangente sobre **Processamento de Linguagem Natural (NLP)**, baseado no curso ministrado pelo professor Dimmy Magalhães na pós-graduação do iCEV. O conteúdo aborda desde conceitos fundamentais até técnicas avançadas com modelos Transformer, proporcionando uma jornada completa de aprendizado com implementações práticas.

## 🗂️ Estrutura do Projeto

```
NLP/
├── MATERIAL_DIDATICO/          # 📖 Notebooks educacionais principais
│   ├── Aula_1,_2,_3.ipynb    # Fundamentos ao Transformers
│   ├── Aula_4.ipynb          # Transformers em Produção
│   └── Aula_5.ipynb          # RAG (Retrieval-Augmented Generation)
├── LEGAL_CHAT_BOT/            # 🤖 Projeto prático - Chatbot Jurídico
│   ├── Chatbot_Juridico_RAG_Lite.ipynb
│   ├── docs/                 # Documentos legais para análise
│   └── data_raw_demo/         # Dados de demonstração
├── ATIVIDADE_SALA/            # 📝 Exercícios e atividades práticas
└── README.md                  # 📋 Este arquivo
```

## 📖 Conteúdo Programático

### 🚀 **Aula 1, 2 e 3: Jornada NLP - Dos Fundamentos aos Transformers**
- **Preparação do Ambiente:** Configuração completa do ecossistema Hugging Face
- **Introdução ao NLP:** Conceitos fundamentais e aplicações
- **Hugging Face e Ollama:** Plataformas e ferramentas essenciais
- **Modelos Transformer:** Arquitetura, funcionamento e implementação
- **Projetos Práticos:** 
  - Classificação de sentimentos
  - Sumarização de texto
  - Geração de texto em português

### ⚡ **Aula 4: Transformers Eficientes em Produção**
- **Otimização de Modelos:** Técnicas para reduzir tamanho e latência
- **Knowledge Distillation:** Destilação de conhecimento para modelos menores
- **Quantização:** Redução de precisão numérica para eficiência
- **Pruning:** Remoção de parâmetros desnecessários
- **Deployment:** Estratégias para colocar modelos em produção

### 🔍 **Aula 5: RAG - Retrieval-Augmented Generation**
- **Conceitos Fundamentais:** O que é RAG e como funciona
- **Arquitetura RAG:** Componentes e fluxo de funcionamento
- **Implementação Prática:** 
  - Vector Stores e embeddings
  - Sistemas de recuperação
  - Integração com LLMs
- **Vantagens e Limitações:** Quando usar RAG
- **Casos de Uso:** Aplicações práticas em diferentes domínios

## 🤖 Projeto Destacado: Chatbot Jurídico RAG

O repositório inclui uma implementação completa de um **chatbot jurídico** utilizando técnicas de RAG:

### 🛠️ Tecnologias Utilizadas
- **BERT Português:** `neuralmind/bert-base-portuguese-cased`
- **FAISS:** Vector search com IndexFlatIP
- **PDF Processing:** Extração de texto com pdfplumber
- **Hugging Face Hub:** Integração com modelos e APIs
- **Sistema Offline:** Fallback para operação sem conectividade

### 📚 Base de Conhecimento
- **Código de Defesa do Consumidor (CDC)**
- **Consolidação das Leis do Trabalho (CLT)**
- **Constituição Federal**
- **Código Civil**
- **Total:** 13 PDFs processados em 5.874 chunks

### 🎯 Funcionalidades
- **Busca Semântica:** Encontra informações relevantes automaticamente
- **Classificação de Intenções:** Identifica o tipo de consulta jurídica
- **Modo Dual:** Online (com HF API) e Offline (template-based)
- **Interface Interativa:** Chat amigável para consultas

## 🚀 Como Começar

### 1. **Pré-requisitos**
```bash
Python 3.11+
Jupyter Lab/Notebook
Git
```

### 2. **Instalação das Dependências**
```bash
# Ecossistema Hugging Face
pip install transformers datasets evaluate accelerate torch

# Processamento de texto
pip install spacy nltk scikit-learn pandas numpy

# Manipulação de PDFs e texto
pip install beautifulsoup4 regex unidecode sentencepiece protobuf

# Visualização
pip install matplotlib seaborn wordcloud plotly

# Jupyter
pip install jupyterlab
```

### 3. **Configuração Adicional**
```bash
# Modelo spaCy para português
python -m spacy download pt_core_news_sm

# FAISS para busca vetorial (para RAG)
pip install faiss-cpu

# pdfplumber para processamento de PDFs
pip install pdfplumber
```

### 4. **Executar os Notebooks**
```bash
jupyter lab
```

## 🎓 Metodologia de Ensino

### 📊 **Abordagem Pedagógica**
- **Aprendizado Incremental:** Do básico ao avançado
- **Teoria + Prática:** Conceitos explicados com implementações
- **Projetos Reais:** Aplicações práticas com dados reais
- **Hands-on Experience:** Código executável e experimentos

### 🛠️ **Recursos Didáticos**
- **Notebooks Interativos:** Explicações detalhadas com código
- **Visualizações:** Gráficos e diagramas explicativos
- **Exemplos Práticos:** Casos de uso do mundo real
- **Exercícios Guiados:** Atividades para fixação

## 🔧 Tecnologias e Ferramentas

| Categoria | Tecnologias |
|-----------|-------------|
| **Linguagem** | Python 3.11+ |
| **ML/DL** | PyTorch, Transformers, scikit-learn |
| **NLP** | spaCy, NLTK, Hugging Face |
| **Dados** | Pandas, NumPy |
| **Visualização** | Matplotlib, Seaborn, Plotly |
| **RAG** | FAISS, Sentence Transformers |
| **Desenvolvimento** | Jupyter, Git |

## 🎯 Objetivos de Aprendizado

Ao concluir este material, o estudante será capaz de:

### 🧠 **Conhecimentos Fundamentais**
- ✅ Compreender os conceitos básicos de NLP
- ✅ Entender a arquitetura dos modelos Transformer
- ✅ Trabalhar com o ecossistema Hugging Face
- ✅ Implementar pipelines de processamento de texto

### 🚀 **Habilidades Práticas**
- ✅ Desenvolver sistemas de classificação de texto
- ✅ Criar modelos de sumarização e geração
- ✅ Implementar sistemas RAG completos
- ✅ Otimizar modelos para produção
- ✅ Construir aplicações práticas de NLP

### 🔬 **Competências Avançadas**
- ✅ Avaliar e comparar diferentes arquiteturas
- ✅ Resolver problemas reais com NLP
- ✅ Aplicar técnicas de otimização
- ✅ Desenvolver soluções end-to-end

## 👥 Contribuições

Este repositório documenta o aprendizado obtido no curso de NLP ministrado pelo professor Dimmy Magalhães. Sugestões, melhorias e correções são bem-vindas:

1. **Issues:** Reporte problemas ou sugira melhorias
2. **Pull Requests:** Contribua com correções ou novo conteúdo
3. **Discussões:** Participe de discussões sobre NLP e implementações

## 📧 Contato

**Sérgio Mendes dos Santos Filho** (Autor do Repositório)
- 🌐 GitHub: [@Sergiosmf](https://github.com/Sergiosmf)
- 📧 Email: [contato]
- 🎓 Estudante: iCEV Pós-Graduação

**Dimmy Magalhães** (Professor do Módulo)
- 🌐 GitHub: [@dimmykarson](https://github.com/dimmykarson)
- 🎓 Instrutor: iCEV Pós-Graduação

## 📜 Licença

Este material é disponibilizado para fins **educacionais**. Os notebooks originais foram desenvolvidos com base no conteúdo do curso do professor Dimmy Magalhães. O uso comercial deve ser discutido com os autores.

## 🙏 Agradecimentos

- **Professor Dimmy Magalhães:** Pelos excelentes ensinamentos e metodologia do curso
- **Comunidade Hugging Face:** Pela plataforma e modelos
- **Instituição iCEV:** Pelo suporte educacional e estrutura do curso
- **Colegas de Turma:** Pelo aprendizado colaborativo
- **Comunidade Open Source:** Pelas ferramentas utilizadas

---

> 💡 **Dica:** Para uma experiência completa, recomenda-se seguir a ordem dos notebooks e experimentar modificações no código para consolidar o aprendizado.

**🌟 Bons estudos e que a jornada pelo mundo do NLP seja transformadora!**
