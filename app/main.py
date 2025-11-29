from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import agent_instance

app = FastAPI(
    title="Chat API com Agente IA",
    description="API que integra FastAPI com Strands Agents e Ollama.",
    version="1.0.0"
)

# Modelos Pydantic para validação
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Recebe uma mensagem, processa com o Agente de IA e retorna a resposta.
    """
    try:
        user_message = request.message
        
        # Chama o agente. O SDK do Strands torna o objeto 'agent' chamável (callable)
        # O retorno geralmente possui um campo .text ou similar com a resposta final
        result = agent_instance(user_message)
        
        # Nota: Verifique na documentação exata do Strands se o retorno é objeto ou string.
        # Geralmente é um objeto com metadados. Assumindo .text ou conversão para str.
        response_text = result.text if hasattr(result, "text") else str(result)

        return ChatResponse(response=response_text)

    except Exception as e:
        # Log do erro real no console para debug
        print(f"Erro no processamento do agente: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao processar a solicitação.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)