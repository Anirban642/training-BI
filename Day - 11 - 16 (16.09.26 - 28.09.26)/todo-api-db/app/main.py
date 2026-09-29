from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.errors import register_exception_handlers
from app.middleware.request_time import RequestTimeMiddleware
from app.routers import category, todo, user


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Alembic manages schema — no create_all here
    yield


app = FastAPI(lifespan=lifespan)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.add_middleware(RequestTimeMiddleware)
register_exception_handlers(app)


@app.get("/")
async def home():
    return {"message": "Todo API Working!"}


app.include_router(todo.router)
app.include_router(category.router)
app.include_router(user.router)