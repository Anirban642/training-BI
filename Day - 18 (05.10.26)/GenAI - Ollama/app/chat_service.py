from ollama import chat
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

model_name = os.getenv("OLLAMA_MODEL", "llama3:latest")


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=2,
        max_length=1000,
        description="Message from the customer to the AI assistant"
    )
    
    
class ChatResponse(BaseModel):
    response: str


SYS_INSTRUCTION = """ 

You are a helpful and friendly AI customer support assistant.

Your job is to have a natural conversation with customers and answer
their questions clearly and accurately.

Rules:
- Be polite, professional, and helpful.
- You can answer general questions and explain concepts.
- You can help customers troubleshoot common problems.
- Understand the context of the customer's message before answering.
- If you don't know the answer, clearly say that you don't know.
- Never make up information.
- Keep answers concise and easy to understand unless the customer
  asks for a detailed explanation.


"""


def chat_with_customer(message: str) -> str:
    response = chat(
        model=model_name,
        messages=[
            {"role": "system", "content": SYS_INSTRUCTION},
            {"role": "user", "content": message},
        ],
    )
    return response["message"]["content"]