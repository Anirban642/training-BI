import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
MAILTRAP_TOKEN = os.getenv("MAILTRAP_TOKEN")
MAILTRAP_INBOX_ID = os.getenv("MAILTRAP_INBOX_ID")
MAIL_SENDER_EMAIL = os.getenv("MAIL_SENDER_EMAIL", "hello@demomailtrap.co")
MAIL_SENDER_NAME = os.getenv("MAIL_SENDER_NAME", "Todo App")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL env is not set !")

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET env is not set !")