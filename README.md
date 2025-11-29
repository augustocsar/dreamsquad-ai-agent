# 🧠 DreamSquad AI Chat API

> Solução técnica desenvolvida para o desafio de Agente de IA da DreamSquad.

Este projeto consiste em uma **API RESTful** robusta construída com **FastAPI**, seguindo os princípios de **Clean Architecture** (Arquitetura em Camadas).

O núcleo da aplicação é um **Agente de IA** orquestrado pelo **Strands Agents SDK**, capaz de raciocínio lógico e execução de ferramentas (*Function Calling*) utilizando o modelo **Llama 3.2** rodando localmente via **Ollama**.

---

## 🏗️ Arquitetura do Projeto

O projeto foi refatorado para garantir escalabilidade, testabilidade e separação de responsabilidades:

```text
chat-api/
├── app/
│   ├── api/          # 🌐 Camada de Interface (Endpoints e Rotas)
│   ├── core/         # ⚙️ Configurações e Ferramentas (Tools) do Sistema
│   ├── services/     # 🧠 Lógica de Negócio (Orquestração do Agente - Singleton)
│   ├── schemas/      # 📦 Modelos de Dados e Contratos (Pydantic)
│   └── main.py       # 🚀 Ponto de entrada da aplicação
├── .env              # Variáveis de ambiente
└── requirements.txt  # Dependências do projeto
```
## 🚀 Tecnologias

* **Python 3.10+**
* **FastAPI:** Framework web de alta performance.
* **Strands Agents:** SDK para criação de agentes inteligentes.
* **Ollama:** Execução local de LLMs.
* **Llama 3.2:** Modelo leve otimizado para *Tool Use*.
* **Pydantic Settings:** Gerenciamento robusto de configurações.

---

## ⚙️ Pré-requisitos

1. Python 3.10 ou superior instalado.
2. Ollama instalado e em execução.
3. Modelo **Llama 3.2** baixado (necessário para suporte a tools):

```bash
ollama pull llama3.2
```
## 🛠️ Instalação e Configuração

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/augustocsar/dreamsquad-ai-agent.git  
cd dreamsquad-ai-agent
```

### 2️⃣ Crie e ative o ambiente virtual
```bash
python -m venv .venv

**Windows:**  
.venv\Scripts\activate

**Linux/Mac:**  
source .venv/bin/activate
```
### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Configure as variáveis de ambiente

Crie um arquivo **.env** na raiz do projeto com o conteúdo:
```bash
PROJECT_NAME="DreamSquad AI Chat"  
OLLAMA_HOST="http://localhost:11434"  
MODEL_ID="llama3.2"
```
---

## ▶️ Como Executar

Inicie o servidor:
```bash
uvicorn app.main:app --reload
```

A API estará disponível em:
```bash  
http://127.0.0.1:8000
```
---

## 🧪 Testando a API

Swagger UI:
```bash  
http://127.0.0.1:8000/docs
```
Ou Postman / Insomnia.

---

## 🔍 Endpoints

### 1️⃣ Health Check

GET /  
Retorno esperado:
```bash  
{
  "message": "Bem-vindo à API DreamSquad AI Chat! 🤖",
  "docs": "Acesse /docs para testar o chat",
  "status": "online"
}
```
---

### 2️⃣ Chat – Agente Inteligente

POST /chat

#### 🧮 Cenário Hipotético A: Uso de Ferramenta (Cálculo)

Request:
```bash  
{  
  "message": "Quanto é 25 vezes 48 dividido por 12?"  
}
```
Response esperada:
```bash  
{  
  "response": "O resultado é 100.0"  
}
```
---

#### 💬 Cenário Hipotético B: Conversação Geral

Request:
```bash  
{  
  "message": "Qual a capital do Japão?"  
}
```
Response esperada:
```bash  
{  
  "response": "A capital do Japão é Tóquio."  
}
```
---

## ✍️ Autor

Desenvolvido por **Augusto César Farias Carvalho**.
