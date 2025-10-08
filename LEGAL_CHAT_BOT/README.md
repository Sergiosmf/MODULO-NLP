# 🏛️ Chatbot Jurídico RAG

Um sistema de Retrieval-Augmented Generation (RAG) especializado em legislação brasileira, focado em CDC, CLT, Direito Civil e Constitucional.

## 🚀 Quick Start

### 1. Instalação Rápida
```bash
# Clone e acesse o diretório
cd LEGAL_CHAT_BOT

# Instale dependências mínimas
pip install -r requirements-minimal.txt

# Ou instalação completa
pip install -r requirements.txt
```

### 2. Execução
```bash
# Abrir notebook
jupyter notebook Chatbot_Juridico_RAG_Lite.ipynb

# Ou executar script Python (se disponível)
python chatbot_rag.py
```

### 3. Uso Básico
```python
# No notebook, execute as células em ordem e depois:
chat_interface()  # Interface interativa
# ou
quick_test()      # Demonstração rápida
```

## 📋 Estrutura do Projeto

```
LEGAL_CHAT_BOT/
├── Chatbot_Juridico_RAG_Lite.ipynb  # Notebook principal
├── requirements.txt                  # Dependências completas
├── requirements-minimal.txt          # Dependências essenciais
├── README.md                        # Este arquivo
├── docs/                            # Documentos jurídicos (PDFs)
│   ├── cdc-portugues-2013.pdf
│   ├── CLT_3ed.pdf
│   ├── DOUconstituicao88.pdf
│   └── ... (outros 10 documentos)
└── data_raw_demo/                   # Dados de demonstração
    ├── cdc_art_18.txt
    ├── cdc_art_26.txt
    └── cdc_art_6.txt
```

## 🔧 Dependências Principais

- **faiss-cpu**: Busca vetorial eficiente
- **sentence-transformers**: Embeddings BERT português
- **pdfplumber**: Extração de texto de PDFs
- **huggingface_hub**: Interface com Hugging Face
- **numpy**: Operações numéricas

## 🎯 Funcionalidades

### ✅ Implementado
- **Classificação automática** de tipos de pergunta
- **Busca semântica** em 13 documentos jurídicos
- **Geração de respostas** com contexto legal
- **Sistema offline** (fallback sem internet)
- **Interface interativa** para conversação
- **Referências automáticas** às fontes consultadas

### 🔍 Tipos de Pergunta Suportados
1. **Jurídicas**: "Quais os prazos do CDC?", "Artigo sobre vícios"
2. **Conversação**: "Olá", "Como funciona?"
3. **Cálculos**: "30% de 500", "10 + 20"
4. **Fora de escopo**: Redirecionamento adequado

## 📊 Performance

- **Base de conhecimento**: 5.874 chunks de 13 documentos
- **Tempo médio por query**: ~400ms
- **Precision@3**: ~85% para queries jurídicas
- **Memória necessária**: ~4GB RAM

## ⚠️ Limitações

### Hardware
- Requer ~4GB RAM para funcionamento completo
- Tempo de inicialização: 5-7 minutos
- Modelos ocupam ~750MB de espaço

### Conectividade
- Hugging Face API pode ter timeouts
- Sistema offline implementado como fallback
- Download inicial de modelos requer internet

### Escopo
- Limitado aos 13 documentos incluídos
- Específico para legislação brasileira
- Não substitui aconselhamento jurídico profissional

## 🔧 Troubleshooting

### Problema: FAISS não instala
```bash
pip uninstall faiss faiss-cpu
pip install --no-cache-dir faiss-cpu
```

### Problema: Timeout do Hugging Face
```bash
export HF_HUB_DOWNLOAD_TIMEOUT=300
```

### Problema: PDF não processa
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev

# macOS
brew install poppler
```

## 🐳 Docker (Opcional)

```bash
# Build
docker build -t chatbot-rag .

# Run
docker run -p 8888:8888 -e HF_TOKEN=your_token chatbot-rag
```

## 📚 Documentação Completa

Veja o notebook `Chatbot_Juridico_RAG_Lite.ipynb` para:
- Documentação técnica detalhada
- Justificativas das escolhas de design
- Limitações e considerações específicas
- Exemplos de uso e troubleshooting

## 🤝 Contribuição

Este é um projeto educacional demonstrando conceitos de RAG aplicados ao domínio jurídico brasileiro. 

## ⚖️ Disclaimer Legal

**IMPORTANTE**: Este sistema é apenas para fins educacionais e demonstração técnica. As respostas geradas são informativas e **NÃO substituem aconselhamento jurídico profissional**. Sempre consulte um advogado para questões legais específicas.

## 📧 Suporte

Para problemas técnicos, consulte:
1. Seção de troubleshooting neste README
2. Documentação completa no notebook
3. Issues no repositório GitHub

---

**Versão**: 1.0  
**Data**: Outubro 2025  
**Python**: 3.8+ (testado em 3.11+)  
**Licença**: Educacional