from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.ai_service import analyze_ticket, TicketRequest, TicketResponse
from app.chat_service import chat_with_customer, ChatRequest, ChatResponse


app = FastAPI(
    title="AI Customer Support Ticket Analyzer",
    version="1.0.0"
)
    


@app.get("/")
def root():
    return {
        "message": "I am your AI ticket analyser."
    }


@app.post(
    "/analyse",
    response_model=TicketResponse
)
def analyse(request: TicketRequest):

    response = analyze_ticket(request.message)

    return response



@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = chat_with_customer(request.message)

    return ChatResponse(response=response)