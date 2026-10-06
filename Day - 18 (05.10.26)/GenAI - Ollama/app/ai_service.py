from typing import Literal
from ollama import chat
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class TicketAnalysis(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"]
    category: Literal["payment", "refund", "auth", "other"]
    priority: Literal["high", "medium", "low"]
    summary: str


model_name = os.getenv("OLLAMA_MODEL", "llama3:latest")


SYS_INSTRUCTION = """
You are an AI customer support ticket analysis assistant.

Your task is to carefully analyze the customer's support ticket and return
a structured analysis.

Follow these rules strictly:

1. SENTIMENT
   - positive: The customer is satisfied, happy, or appreciative.
   - negative: The customer is frustrated, angry, dissatisfied, or reporting a problem.
   - neutral: The customer is asking for information without showing a clear emotion.

2. CATEGORY
   - payment: Problems involving charges, duplicate charges, payments, invoices,
     or payment methods.
   - refund: Requests for refunds, returned money, cancelled purchases, or
     money that should be returned.
   - auth: Login, logout, password, account access, authentication, or verification issues.
   - other: Anything that does not clearly belong to the above categories.

3. PRIORITY
   - high: The issue has an urgent or serious impact, such as duplicate charges,
     inability to access an important account, major payment problems, or service outages.
   - medium: The issue is important but does not require immediate attention.
   - low: General questions, minor issues, or requests that can wait.

4. SUMMARY
   - Provide one concise sentence describing the customer's main issue.
   - Do not add information that was not provided by the customer.

Analyze the ticket based only on the information provided.
Return only the requested structured data.
"""


def analyze_ticket(message: str) -> TicketAnalysis:

    response = chat(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": SYS_INSTRUCTION
            },
            {
                "role": "user",
                "content": f"Analyze this customer support ticket:\n\n{message}"
            }
        ],
        format=TicketAnalysis.model_json_schema()
    )

    return TicketAnalysis.model_validate_json(
        response["message"]["content"]
    )