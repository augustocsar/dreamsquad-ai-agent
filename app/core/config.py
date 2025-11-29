import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para a memória
load_dotenv()

class Settings:
    PROJECT_NAME = "DreamSquad AI Chat"
    # Busca do .env, se não achar, usa o valor padrão (segundo argumento)
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    MODEL_ID = os.getenv("MODEL_ID", "llama3.2")

settings = Settings()