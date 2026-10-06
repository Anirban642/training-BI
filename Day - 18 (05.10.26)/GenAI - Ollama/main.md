from ollama import chat
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="AI Support Ticket Analysis API")


class AnalyseRequest(BaseModel):
    message: str = Field(min_length=3, max_length=100)
    

class AnalyseResponse(BaseModel):
    analysis: str  
    

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Support Ticket Analysis API!"}



@app.post("/analyse", response_model=AnalyseResponse)
def analyse(request: AnalyseRequest):
    try:
        response = chat(
                model="llama3:latest",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that analyzes customer support tickets."},
                ]
            )
        return AnalyseResponse(analysis=response["message"]["content"])
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=502, detail="The API provider went wrong. Please try again later.")
        

query = "What is RAG based on AI context?"

    
    
# if __name__ == "__main__":
#     output = analyse("I am having trouble logging into my account.")
#     json_output = json.loads(output)
#     print(json_output['Sentiment'])
    
