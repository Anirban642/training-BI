from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.errors import register_exception_handlers
from app.middleware.request_time import RequestTimeMiddleware
from app.models.models import Category, Todo
from app.models.user import User
from app.routers import category, todo, user


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

# Custom Process-Time Middleware
app.add_middleware(RequestTimeMiddleware)

# Register central error handlers
register_exception_handlers(app)


@app.get("/")
async def home():
    return {"message": "Todo API Working!"}


app.include_router(todo.router)
app.include_router(category.router)
app.include_router(user.router)