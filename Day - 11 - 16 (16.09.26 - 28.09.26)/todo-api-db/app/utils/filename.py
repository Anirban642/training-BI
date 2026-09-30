import re
from datetime import datetime, timezone


def safe_filename_part(value: str, max_len: int = 50) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    cleaned = cleaned.strip("._")[:max_len]
    return cleaned or "user"


def export_filename(username: str, suffix: str = "todos_export", ext: str = "json") -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    return f"{safe_filename_part(username)}_{suffix}_{stamp}.{ext}"