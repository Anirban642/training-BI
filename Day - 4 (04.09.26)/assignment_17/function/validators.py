def validate_id(id):
    if id <= 0:
        raise ValueError("ID must be positive")

def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")

def validate_text(text):
    if not text.strip():
        raise ValueError("Input cannot be empty")