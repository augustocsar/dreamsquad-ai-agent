from functools import lru_cache
from strands import Agent
from strands.models.ollama import OllamaModel
from app.core.config import settings
from app.core.tools import calculator_tool

class AgentService:
    def __init__(self):
        print(f"🤖 Inicializando Agente com modelo: {settings.MODEL_ID}")
        
        self.model = OllamaModel(
            host=settings.OLLAMA_HOST,
            model_id=settings.MODEL_ID,
        )
        
        self.agent = Agent(
            model=self.model,
            tools=[calculator_tool],
            system_prompt="""Você é um assistente útil.
            Se o usuário pedir cálculo, USE a ferramenta 'calculator_tool'.
            Para o resto, responda normalmente."""
        )

    def process_message(self, message: str) -> str:
        try:
            result = self.agent(message)
            return result.text if hasattr(result, "text") else str(result)
        except Exception as e:
            print(f"Erro no agente: {e}")
            raise e

@lru_cache()
def get_agent_service() -> AgentService:
    return AgentService()