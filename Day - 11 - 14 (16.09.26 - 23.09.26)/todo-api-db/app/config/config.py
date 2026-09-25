import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL env is not set !")

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET env is not set !")