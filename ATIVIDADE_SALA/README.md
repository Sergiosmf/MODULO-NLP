# 🎓 Sistema RAG Jurídico - Consulta de Direitos do Consumidor

> **Sistema inteligente de consulta ao Código de Defesa do Consumidor (CDC) usando tecnologia RAG (Retrieval-Augmented Generation)**

![Status](https://img.shields.io/badge/Status-Funcional-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Score](https://img.shields.io/badge/Score-3.8%2F5-success)

## 🎯 O que é este projeto?

Este é um **assistente jurídico inteligente** que responde perguntas sobre direitos do consumidor brasileiro. Ele usa inteligência artificial para:

- 📚 **Consultar automaticamente** o Código de Defesa do Consumidor
- 🤖 **Gerar respostas precisas** sobre seus direitos
- ⚡ **Responder rapidamente** dúvidas jurídicas comuns
- 🎯 **Contextualizar** informações legais de forma clara

## 🚀 Como funciona?

```mermaid
graph LR
    A[Sua Pergunta] --> B[Busca no CDC]
    B --> C[Encontra Artigos Relevantes]
    C --> D[Gera Resposta Inteligente]
    D --> E[Resposta Clara e Fundamentada]
```

**Exemplo prático:**
- **Você pergunta:** "Como devolver um produto com defeito?"
- **Sistema responde:** "Segundo o CDC, você tem direito a: 1) Substituição do produto, 2) Restituição do valor pago, ou 3) Abatimento do preço. O prazo é de 30 dias para produtos não duráveis e 90 dias para duráveis..."

## 📋 O que você pode perguntar?

### ✅ Perguntas Suportadas

#### 🛒 **Compras e Defeitos**
- "Como devolver produto com defeito?"
- "O que fazer se o produto chegou quebrado?"
- "Tenho direito a troca se não gostei?"

#### ⏰ **Prazos e Garantias**
- "Qual o prazo para reclamar de vício?"
- "Como funciona a garantia legal?"
- "Posso devolver depois do prazo?"

#### 💻 **Compras Online**
- "Posso cancelar compra pela internet?"
- "Direito de arrependimento funciona como?"
- "Prazo para devolução de compra online?"

#### 🏢 **PROCON e Órgãos**
- "Como fazer reclamação no PROCON?"
- "Onde reclamar meus direitos?"
- "PROCON pode me ajudar?"

## 🛠️ Como usar?

### 📖 **Opção 1: Usar o Notebook (Recomendado)**

1. **Abra o arquivo principal:**
   ```
   sistema_rag_juridico_desafio.ipynb
   ```

2. **Execute todas as células em ordem** (Shift + Enter em cada uma)

3. **Faça suas perguntas:**
   ```python
   # Consulta básica
   resposta = rag_system.query("Como devolver produto com defeito?")
   
   # Consulta avançada (recomendado)
   resposta = rag_system.enhanced_query("Como devolver produto com defeito?")
   
   print(resposta['answer'])
   ```

### 💬 **Opção 2: Chat Interativo**

1. **Abra o chat:**
   ```
   consumer_rag_full_cdc_chat.ipynb
   ```

2. **Digite suas perguntas diretamente** e receba respostas instantâneas

### 🔧 **Opção 3: Script Python**

```python
# Importar e usar direto
from consumer_rights_tool import ConsumerRightsRAG

rag = ConsumerRightsRAG()
resposta = rag.query("Sua pergunta aqui")
print(resposta)
```

## ⚙️ Instalação

### 📋 **Pré-requisitos**
- Python 3.8 ou superior
- 8GB RAM (recomendado 16GB)
- Conexão com internet (para baixar modelos)

### 🔧 **Passo a passo**

1. **Clone ou baixe o projeto**
   ```bash
   git clone [url-do-projeto]
   cd NLP
   ```

2. **Instale as dependências**
   ```bash
   pip install torch transformers sentence-transformers faiss-cpu
   pip install beautifulsoup4 lxml requests pandas jupyter
   ```

3. **Execute o notebook**
   ```bash
   jupyter notebook sistema_rag_juridico_desafio.ipynb
   ```

4. **Pronto! Execute todas as células e comece a usar**

## 🎯 Exemplos de Uso

### 🔍 **Consultas Básicas**

```python
# Exemplo 1: Produto defeituoso
pergunta = "Comprei um celular com defeito, o que posso fazer?"
resposta = rag_system.query(pergunta)

# Exemplo 2: Compra online
pergunta = "Posso cancelar uma compra feita na internet?"
resposta = rag_system.query(pergunta)

# Exemplo 3: Garantia
pergunta = "Quanto tempo tenho para reclamar de garantia?"
resposta = rag_system.query(pergunta)
```

### 🚀 **Consultas Avançadas (Melhores Resultados)**

```python
# Sistema aprimorado com cache e otimizações
resposta_melhorada = rag_system.enhanced_query(
    "Como funciona o direito de arrependimento em compras online?"
)
```

## 📊 Qualidade das Respostas

### 🎯 **Métricas de Performance**
- **Precisão:** 4.0/5 ⭐⭐⭐⭐⭐
- **Relevância:** 3.5/5 ⭐⭐⭐⭐
- **Clareza:** 4.0/5 ⭐⭐⭐⭐⭐
- **Score Geral:** 3.8/5 ⭐⭐⭐⭐

### ⚡ **Velocidade**
- Resposta típica: 2-5 segundos
- Com cache: < 1 segundo
- Primeira execução: ~30 segundos (carregamento dos modelos)

## 🔧 Tecnologia Utilizada

### 🤖 **Inteligência Artificial**
- **BERT Português:** Para entender suas perguntas
- **LLaMA 3.2:** Para gerar respostas naturais (opcional)
- **Templates Jurídicos:** Para garantir precisão legal

### 📚 **Base de Conhecimento**
- Código de Defesa do Consumidor completo
- Lei 8.078/1990 atualizada
- Artigos e parágrafos indexados

### ⚙️ **Tecnologias**
- Python + Jupyter Notebook
- HuggingFace Transformers
- FAISS (busca vetorial)
- BeautifulSoup (processamento de documentos)

## ⚠️ Limitações e Avisos

### 🚨 **Importante - Leia antes de usar**

- ✅ **Para orientação geral:** Excelente para entender seus direitos
- ⚠️ **Não substitui advogado:** Para casos complexos, consulte um profissional
- 📚 **Baseado no CDC:** Focado especificamente em direitos do consumidor
- 🔄 **Sempre verifique:** Confirme informações em fontes oficiais

### 📋 **O que NÃO faz**
- Não dá conselhos jurídicos específicos para seu caso
- Não substitui consultoria jurídica profissional
- Não cobre outras áreas do direito (só consumidor)
- Não garante resultados em processos judiciais

## 🆘 Problemas Comuns

### 🔧 **Soluções Rápidas**

#### ❌ "Erro de memória"
```python
# Solução: Use apenas o sistema template
rag_system.generator = legal_generator  # Menos memória
```

#### ❌ "LLaMA não carrega"
```python
# Solução: Sistema funciona sem LLaMA
# Use apenas: rag_system.query() com templates
```

#### ❌ "Respostas irrelevantes"
```python
# Solução: Use o sistema aprimorado
resposta = rag_system.enhanced_query("sua pergunta")
```

#### ❌ "Muito lento"
```python
# Solução: Use queries similares (ativa cache)
# Primeira vez é mais lenta, depois acelera
```

## 📞 Suporte

### 🤔 **Precisa de Ajuda?**

1. **Verifique a documentação técnica:** `DOCUMENTACAO_TECNICA.md`
2. **Execute o diagnóstico:** `diagnose_system()` no notebook
3. **Consulte os exemplos** nos notebooks de demonstração

### 🔍 **Para Desenvolvedores**
- Veja `DOCUMENTACAO_TECNICA.md` para detalhes técnicos completos
- Explore os notebooks de exemplo
- Teste as funções de diagnóstico incluídas

## 📈 Melhorias Futuras

### 🚀 **Roadmap**
- [ ] Interface web amigável
- [ ] Mais áreas do direito (trabalhista, civil)
- [ ] Base de jurisprudência integrada
- [ ] App móvel
- [ ] Sistema de feedback dos usuários

### 💡 **Quer contribuir?**
- Reporte bugs ou suggira melhorias
- Teste com diferentes tipos de perguntas
- Compartilhe casos de uso interessantes

---

## 🎉 Conclusão

Este sistema representa uma **ferramenta poderosa e acessível** para consultar direitos do consumidor brasileiro. Com tecnologia de ponta em inteligência artificial, oferece:

- ✅ **Respostas rápidas e precisas**
- ✅ **Base sólida no CDC**
- ✅ **Fácil de usar**
- ✅ **Totalmente funcional**

**🚀 Comece agora:** Abra o notebook e faça sua primeira pergunta!

---

### 📄 **Licença**
Este projeto é open source e pode ser usado livremente para fins educacionais e pessoais.

### ⚖️ **Disclaimer Legal**
Este sistema é uma ferramenta educacional e informativa. Não constitui aconselhamento jurídico profissional. Para questões legais específicas, consulte sempre um advogado qualificado.