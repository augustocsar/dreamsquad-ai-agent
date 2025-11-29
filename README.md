# API de Chat com Agente de IA (FastAPI + Strands + Ollama)

Este projeto implementa uma API de Chat utilizando **FastAPI** integrada a um Agente de IA orquestrado pelo **Strands Agents SDK**. O agente possui capacidade de raciocínio matemático através de uma Tool customizada e executa localmente utilizando **Ollama**.

## 🚀 Pré-requisitos

1.  Python 3.10+
2.  [Ollama](https://ollama.com/) instalado e rodando.
3.  Modelo Llama 3 baixado: `ollama pull llama3`

## 🛠️ Instalação

1.  Clone o repositório.
2.  Crie um ambiente virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    # ou .venv\Scripts\activate  # Windows
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4.  Configure o arquivo `.env` baseando-se no exemplo.

## ▶️ Execução

Inicie o servidor API:
```bash
uvicorn app.main:app --reload