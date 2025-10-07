# 🔧 Guia de Configuração e Setup - Sistema RAG Jurídico

## 📋 Lista de Verificação de Setup

### ✅ Pré-requisitos
- [ ] Python 3.8+ instalado
- [ ] 8GB+ RAM disponível
- [ ] 5GB+ espaço em disco
- [ ] Conexão com internet estável

### ✅ Instalação das Dependências
```bash
# Método 1: Pip install direto
pip install torch transformers sentence-transformers faiss-cpu beautifulsoup4 lxml requests pandas jupyter

# Método 2: Usando requirements.txt
pip install -r requirements.txt

# Método 3: Conda (alternativo)
conda install pytorch transformers pandas jupyter
pip install sentence-transformers faiss-cpu beautifulsoup4
```

### ✅ Verificação da Instalação
```python
# Execute este código para verificar se tudo está funcionando:
import torch
import transformers
import sentence_transformers
import faiss
import bs4
import pandas as pd
print("✅ Todas as dependências instaladas com sucesso!")
```

## 🤖 Configuração de Modelos

### 🔑 Token HuggingFace (Opcional - apenas para LLaMA 3.2)
```python
# Se quiser usar LLaMA 3.2, configure seu token:
HF_TOKEN = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Para obter seu token:
# 1. Vá para https://huggingface.co/
# 2. Crie uma conta
# 3. Vá em Settings > Access Tokens
# 4. Crie um novo token
```

### 📦 Download Automático de Modelos
Os modelos são baixados automaticamente na primeira execução:

- **BERT Português:** ~400MB (`neuralmind/bert-base-portuguese-cased`)
- **LLaMA 3.2:** ~2.5GB (`meta-llama/Llama-3.2-1B-Instruct`)

## 📁 Estrutura de Arquivos

```
NLP/
├── 📄 README.md                              # Guia do usuário
├── 📄 DOCUMENTACAO_TECNICA.md                # Documentação completa
├── 📄 SETUP_GUIDE.md                         # Este arquivo
├── 📄 requirements.txt                       # Dependências Python
├── 
├── 📓 sistema_rag_juridico_desafio.ipynb     # 🌟 ARQUIVO PRINCIPAL
├── 📓 consumer_rag_full_cdc_chat.ipynb       # Chat interativo
├── 📓 consumer_rag_pipeline.ipynb            # Pipeline isolado
├── 📓 cdc_rag_sistema_limpo.ipynb           # Versão simplificada
├── 
├── 🐍 consumer_rights_tool.py                # Ferramenta standalone
├── 
├── 📁 data/
│   ├── 📁 raw/
│   │   ├── 📄 cdc.txt                       # CDC em texto
│   │   └── 📄 planalto_html.html            # CDC em HTML
│   └── ...
├── 
├── 📄 cdc-portugues-2013.pdf                # CDC em PDF
├── 📄 l8078compilado.htm                     # Lei compilada
└── 📁 __pycache__/                          # Cache Python
```

## 🚀 Passos de Execução

### 1️⃣ **Primeira Execução (Setup Completo)**
```bash
# 1. Abrir Jupyter
jupyter notebook

# 2. Abrir arquivo principal
# sistema_rag_juridico_desafio.ipynb

# 3. Executar células na ordem (1-34)
# Primeira execução: ~5-10 minutos (download de modelos)
```

### 2️⃣ **Execuções Seguintes (Rápidas)**
```python
# Modelos já baixados, execução rápida
# Tempo: ~30 segundos para carregar tudo
```

### 3️⃣ **Consultas Imediatas**
```python
# Depois do setup, consultas são instantâneas:
resposta = rag_system.query("Como devolver produto com defeito?")
```

## ⚙️ Configurações Avançadas

### 🔧 **Ajuste de Performance**

#### Para Computadores com Pouca Memória (<8GB):
```python
# Use apenas sistema template (mais leve)
rag_system.generator = legal_generator  # Ao invés de LLaMA

# Reduza batch size
rag_system.retriever.batch_size = 16  # Padrão: 32
```

#### Para Computadores Potentes (16GB+):
```python
# Use sistema completo com LLaMA 3.2
rag_system.generator = llama_legal_generator

# Aumente cache
rag_system.cache_size = 1000  # Padrão: 100
```

### 🎯 **Configurações de Qualidade**

#### Máxima Precisão:
```python
# Use enhanced_query para melhores resultados
resposta = rag_system.enhanced_query("sua pergunta")
```

#### Máxima Velocidade:
```python
# Use query básica com cache
resposta = rag_system.query("sua pergunta")
```

## 🔍 Diagnóstico e Troubleshooting

### 🩺 **Verificação Automática**
```python
# Execute no notebook para verificar sistema:
diagnose_system()

# Resultados esperados:
# ✅ rag_system: Existe, ready = True
# ✅ legal_generator: Existe, status = template_mode
# ✅ llama_generator: Existe (se configurado)
```

### 🛠️ **Problemas Comuns e Soluções**

#### ❌ `ModuleNotFoundError: No module named 'torch'`
```bash
# Solução:
pip install torch transformers
```

#### ❌ `CUDA out of memory`
```python
# Solução: Force CPU
import torch
torch.cuda.empty_cache()
device = "cpu"  # Em vez de "cuda"
```

#### ❌ `Connection timeout` para modelos
```python
# Solução: Download manual
from transformers import AutoModel
model = AutoModel.from_pretrained("neuralmind/bert-base-portuguese-cased")
```

#### ❌ Respostas irrelevantes
```python
# Solução: Reconfigure sistema
rag_system.retriever.rebuild_index()
```

### 🔄 **Reset Completo**
```python
# Se algo der errado, reset completo:
# 1. Restart kernel (Kernel > Restart)
# 2. Execute todas as células novamente
# 3. Ou execute:
del rag_system
# Depois execute células de inicialização novamente
```

## 📊 Monitoramento

### 📈 **Verificar Performance**
```python
# Tempo de resposta
import time
start = time.time()
resposta = rag_system.query("test")
print(f"Tempo: {time.time() - start:.2f}s")

# Uso de memória
import psutil
print(f"RAM: {psutil.virtual_memory().percent}%")
```

### 🎯 **Verificar Qualidade**
```python
# Execute avaliação automática
evaluation_results = rag_system.evaluate()
print(f"Score: {evaluation_results['overall_score']}/5")
```

## 🔐 Segurança e Privacidade

### 🛡️ **Dados Locais**
- ✅ Todos os dados ficam em seu computador
- ✅ Nenhuma informação é enviada para servidores externos
- ✅ Consultas são processadas localmente

### 🔑 **Tokens e Credenciais**
- Token HuggingFace é opcional (só para LLaMA 3.2)
- Mantido localmente no seu ambiente
- Nunca compartilhado ou enviado

## 🎉 Verificação Final

### ✅ **Lista de Verificação Final**
Após o setup, você deve conseguir:

- [ ] Abrir o notebook principal sem erros
- [ ] Executar todas as células sem falhas
- [ ] Ver mensagem "Sistema pronto para uso!"
- [ ] Fazer uma consulta de teste: `rag_system.query("Como devolver produto?")`
- [ ] Receber uma resposta sobre direitos do consumidor

### 🎯 **Teste de Funcionamento**
```python
# Teste final - cole no notebook:
print("🧪 TESTE FINAL DO SISTEMA")
print("="*40)

teste = rag_system.query("Posso devolver compra online?")
if 'answer' in teste:
    print("✅ Sistema funcionando perfeitamente!")
    print(f"📝 Resposta: {teste['answer'][:100]}...")
else:
    print("❌ Sistema precisa de ajustes")
    print("💡 Execute: diagnose_system()")
```

---

## 📞 Suporte Adicional

### 🆘 **Se nada funcionar:**
1. Verifique versão do Python: `python --version` (deve ser 3.8+)
2. Atualize pip: `pip install --upgrade pip`
3. Instale em ambiente virtual limpo
4. Consulte a documentação técnica completa

### 💡 **Dicas de Sucesso:**
- Execute células na ordem (não pule nenhuma)
- Aguarde downloads na primeira execução
- Use `enhanced_query()` para melhores resultados
- Mantenha internet ligada na primeira vez

**🎉 Pronto! Seu sistema RAG jurídico está configurado e funcionando!**