from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.ai_service import analyze_ticket, TicketAnalysis


app = FastAPI(
    title="AI Customer Support Ticket Analyzer",
    version="1.0.0"
)


class AnalyseRequest(BaseModel):
    message: str = Field(
        min_length=3,
        max_length=1000,
        description="Customer support ticket message"
    )


@app.get("/")
def root():
    return {
        "message": "I am your AI ticket analyser."
    }


@app.post(
    "/analyse",
    response_model=TicketAnalysis
)
def analyse(request: AnalyseRequest):

    response = analyze_ticket(request.message)

    return response