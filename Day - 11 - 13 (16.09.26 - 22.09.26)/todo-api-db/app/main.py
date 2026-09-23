from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import category, todo, user

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
    return {"message": "Todo API Working!"}

app.include_router(todo.router)
app.include_router(category.router)
app.include_router(user.router)
