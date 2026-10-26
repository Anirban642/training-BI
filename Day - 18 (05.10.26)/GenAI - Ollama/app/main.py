from fastapi import FastAPI
import time

from app.ai_service import analyze_ticket, TicketRequest, TicketResponse
from app.chat_service import chat_with_customer, ChatRequest, ChatResponse


app = FastAPI(
    title="AI Customer Support API",
    description="AI-powered customer support system using FastAPI and Ollama.",
    version="1.0.0"
)
    


@app.get("/")
def root():
    return {
        "message": "I am your AI ticket analyser."
    }
    
 
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "llama3:latest",
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
    start_time = time.time()
    
    response = chat_with_customer(request.message)
    
    processing_time = round(time.time() - start_time, 2)

    return ChatResponse(response=response, processing_time=processing_time)