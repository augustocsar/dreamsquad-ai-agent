import os
from dotenv import load_dotenv
from strands import Agent
# IMPORTANTE: Importamos o conector específico do Ollama
from strands.models.ollama import OllamaModel 
from app.tools import calculator_tool

load_dotenv()

def get_agent():
    """
    Fabrica e retorna uma instância do Agente configurado EXPLICITAMENTE para o Ollama.
    """
    # 1. Configura o modelo para apontar para seu Ollama local
    # Isso evita que ele tente conectar na AWS (o que causava o erro de credenciais)
    model = OllamaModel(
        host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
        model_id="llama3.2",  # Modelo mais novo do Ollama
    )
    
    # 2. Inicializa o Agente passando o objeto 'model' configurado
    agent = Agent(
        model=model,
        tools=[calculator_tool],
        system_prompt="""Você é um assistente útil e inteligente.
        Sempre que o usuário pedir um cálculo matemático, USE a ferramenta 'calculator_tool'.
        Para perguntas gerais, responda diretamente."""
    )
    
    return agent

# Instância global
agent_instance = get_agent()