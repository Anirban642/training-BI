from datetime import datetime, timedelta, timezone
import jwt
from app.config.config import JWT_ALGORITHM, JWT_SECRET

def create_access_token(user_id: int):
    exp = datetime.now(timezone.utc) + timedelta(minutes=30)
    data = {
        "sub": str(user_id),
        "exp": exp
    }
    return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM) 