# 📝 Changelog - Legal Chat Bot

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2025-10-07

### 🎉 Lançamento Inicial

#### ✅ Adicionado
- **Sistema RAG Jurídico** com arquitetura híbrida TF-IDF + keyword matching
- **Classificação automática** de consultas (jurídicas vs. conversacionais)
- **Base de conhecimento** com 50+ documentos sintéticos em 4 áreas do direito
- **Memória conversacional** para manter contexto de 10 interações
- **Sistema de avaliação** com feedback de 1-5 estrelas
- **Interface conversacional** interativa com colorização
- **Indicadores de confiança** para cada resposta gerada
- **Documentação técnica** completa com justificativas de design

#### 🔧 Técnico
- `HybridRetriever`: Combina TF-IDF (70%) + sobreposição de palavras (30%)
- `QuestionClassifier`: Pipeline scikit-learn com Logistic Regression
- `ConversationMemory`: Gerenciamento de contexto histórico
- `ResponseGenerator`: Templates contextualizados para respostas

#### 📚 Base de Conhecimento
- **Direito do Consumidor**: 15 documentos (CDC, garantias, defeitos)
- **Direito Trabalhista**: 15 documentos (CLT, rescisão, férias)  
- **Direito Civil**: 12 documentos (contratos, responsabilidade civil)
- **Direito Constitucional**: 10 documentos (direitos fundamentais, poderes)

#### 🎯 Performance
- Latência média: ~50ms por consulta
- Consumo de RAM: ~200MB 
- Accuracy de classificação: ~85%
- Disponibilidade: 100% (sem travamentos)

---

## [0.9.0] - 2025-10-07 - REJEITADO

### ❌ Tentativa com Modelos Avançados (FALHOU)

#### 🧪 Tentativas Implementadas
- **Llama 3.2-1B-Instruct** para geração de respostas
- **Legal-BERTimbau-large** para embeddings jurídicos especializados
- **FAISS** para busca vetorial eficiente
- **Quantização 4-bit/8-bit** para reduzir uso de memória

#### 💥 Problemas Encontrados

##### 1. Mutex Lock Errors
```
[mutex.cc : 452] RAW: Lock blocking 0x123895ed8
```
- **Causa**: Conflitos de threading entre PyTorch e transformers
- **Impacto**: Sistema travava completamente durante inicialização
- **Modelos afetados**: Todos os transformers testados

##### 2. Consumo Excessivo de RAM
```
OutOfMemoryError: Cannot allocate 8.2GB for model loading
```
- **Legal-BERTimbau**: >6GB apenas para embeddings
- **Llama 3.2**: >8GB com quantização 8-bit
- **Total necessário**: >12GB RAM
- **Hardware disponível**: 8GB

##### 3. Latência Inaceitável
- **TF-IDF**: ~50ms
- **BERT**: ~2-5 segundos  
- **Llama 3.2**: ~10-15 segundos
- **Impacto UX**: Experiência de usuário degradada

#### 🔄 Tentativas de Solução
- ✅ Configuração `device_map="cpu"` para forçar CPU
- ✅ `torch.set_num_threads(1)` para single-threading
- ✅ `TOKENIZERS_PARALLELISM=false` para evitar paralelismo
- ✅ Quantização 8-bit em vez de 4-bit
- ✅ `low_cpu_mem_usage=True` para economia de memória
- ❌ **Todas falharam** com mutex locks persistentes

#### 📝 Lições Aprendidas
1. **Hardware Constraints são Reais**: Nem sempre é possível usar tecnologia de ponta
2. **Estabilidade > Capacidade**: Sistema funcionando é melhor que sistema avançado quebrado
3. **Algoritmos Clássicos têm Valor**: TF-IDF ainda é eficaz para muitos casos de uso
4. **Pragmatismo em AI**: Escolher ferramentas adequadas ao contexto, não as mais modernas

---

## [0.5.0] - 2025-10-06

### 🔬 Fase de Experimentação

#### 🧪 Protótipos Testados
- **RAG_SIMPLES.py**: Primeira implementação com TF-IDF
- **RAG.py**: Tentativa com BERT embeddings
- **test_rag_llama_legal_bert.ipynb**: Notebook experimental

#### 📊 Análise Comparativa
```python
# Comparativo de abordagens testadas
TF_IDF = {
    'latencia': '50ms',
    'ram': '200MB', 
    'estabilidade': '100%',
    'qualidade': 'Boa'
}

BERT = {
    'latencia': '2-5s',
    'ram': '>6GB',
    'estabilidade': '0%',  # Mutex locks
    'qualidade': 'Teóricamente Superior'
}
```

#### 🎯 Decisão de Arquitetura
Com base nos testes, **optou-se por TF-IDF** devido a:
- Estabilidade comprovada
- Recursos computacionais viáveis  
- Latência adequada para chatbot
- Facilidade de manutenção

---

## [0.1.0] - 2025-10-05

### 🌱 Concepção do Projeto

#### 💡 Requisitos Iniciais
- Sistema de conversação jurídica em português
- Classificação automática de consultas
- Recuperação de informação relevante
- Base de conhecimento especializada
- Interface amigável para usuários

#### 🎯 Objetivos de Design
1. **Funcionalidade**: Sistema completo de RAG jurídico
2. **Estabilidade**: Zero travamentos ou erros críticos
3. **Performance**: Respostas em tempo real
4. **Escalabilidade**: Arquitetura extensível
5. **Usabilidade**: Interface intuitiva

#### 🛠️ Stack Tecnológico Planejado
- **Linguagem**: Python 3.8+
- **ML Framework**: scikit-learn (escolha final)
- **Processamento**: TF-IDF + algoritmos clássicos
- **Interface**: Terminal interativo com colorização
- **Dados**: Documentos sintéticos categorizados

---

## 🔮 Roadmap Futuro

### [1.1.0] - Planejado
- [ ] API REST para exposição de funcionalidades
- [ ] Interface web básica com Flask/FastAPI
- [ ] Métricas avançadas de qualidade de resposta
- [ ] Logs estruturados para análise

### [1.2.0] - Investigação
- [ ] Embeddings leves (FastText, Word2Vec customizado)
- [ ] Modelos compactos (<100MB) para contexto jurídico
- [ ] Cache inteligente para consultas frequentes
- [ ] Personalização por área de especialização

### [2.0.0] - Visão de Longo Prazo
- [ ] Integração com documentos jurídicos reais (PDF parsing)
- [ ] Sistema de citações e referências automáticas
- [ ] Multi-modal (texto + imagens de documentos)
- [ ] Deploy em cloud com auto-scaling

---

## 📈 Métricas de Evolução

### Version 0.x → 1.0
- **Estabilidade**: 0% → 100%
- **Latência**: ∞ (travava) → 50ms
- **RAM**: >8GB → 200MB
- **Funcionalidades**: 0% → 100%

### Lições do Desenvolvimento
1. **Constraints geram Inovação**: Limitações forçaram soluções criativas
2. **MVP é Poderoso**: Sistema simples e funcional supera complexo e quebrado
3. **Escolha de Tecnologia Importa**: Nem sempre o mais novo é o melhor
4. **Documentação é Crucial**: Registrar decisões e falhas é valioso

---

**Mantido por**: Equipe Legal Chat Bot  
**Última atualização**: 07 de Outubro de 2025