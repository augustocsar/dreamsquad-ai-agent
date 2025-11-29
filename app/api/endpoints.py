from fastapi import APIRouter, HTTPException, Depends
from app.schemas.base import HealthCheckResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import AgentService, get_agent_service

router = APIRouter()

@router.get("/", tags=["Status"], response_model=HealthCheckResponse)
async def root():
    return {
        "message": "Bem-vindo à API DreamSquad AI Chat! 🤖",
        "docs": "Acesse /docs para testar o chat",
        "status": "online"
    }

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    service: AgentService = Depends(get_agent_service)
):
    try:
        response_text = service.process_message(request.message)
        return ChatResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))