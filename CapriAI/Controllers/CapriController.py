from uuid import uuid4

from fastapi import APIRouter

from DTOs.CapriSettings import CapriSettings
import CapriAI

from DTOs.Request import Request

router = APIRouter(
    prefix="/api/capri",
    tags=["Capri"])

conversations = {}
capri_settings = CapriSettings

@router.get("/health")
async def health():
    return {
        "status": "healthy"
    }

@router.post("/chat/message")
async def ask_capri(request: Request):
    conversation_id = request.conversationId

    if not conversation_id:
        conversation_id = str(uuid4())
        conversations[conversation_id] = []

    history = conversations[conversation_id]

    history.append({
        "role": "user",
        "content": request.question
    })
    
    history = history[-20:]

    answer = CapriAI.ask_ai(history)

    history.append({
        "role": "assistant",
        "content": answer
    })

    conversations[conversation_id] = history[-20:]

    return {
        "conversation_id": conversation_id,
        "answer": answer,
        "events":[
            {
                "type": "MESSAGE_RECEIVED",
                "data": {}
            }
        ]
    }

@router.get("/state")
async def get_capri_state():
    return {
        "is_visible": capri_settings.is_visible,
        "animations_enabled": capri_settings.animations_enabled,
        "status": "online"
        }

@router.patch("/settings")
async def update_capri_settings(settings: CapriSettings):
    global capri_settings

    capri_settings = settings

    return {
        "message": "Settings updated",
        "settings": capri_settings
        }