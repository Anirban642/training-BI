from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
class Credentials(BaseModel):
    email: str
    password: str
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: str   
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str         