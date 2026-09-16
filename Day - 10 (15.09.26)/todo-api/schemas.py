from pydantic import BaseModel

class CategoryIn(BaseModel):
    name: str
    
class CategoryOut(BaseModel):
    id: int
    name: str
    
class TodoIn(BaseModel):
    title: str
    description: str  
    category_id: int
    
class TodoUpdate(BaseModel):
    title: str
    description: str
    isDone: bool
    category_id: int
    
class TodoOut(BaseModel):
    id: int
    title: str
    description: str
    isDone: bool  
    category_id: int      