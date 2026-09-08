from exceptions import DuplicateUserError, UserNotFoundError

def register_user(users, id, name):
    for user in users:
        if user["id"] == id:
            raise DuplicateUserError("User ID already exists")
    user = {
        "id": id,
        "name": name
    }
    users.append(user)

def get_user(users, id):
    for user in users:
        if user["id"] == id:
            return user
    raise UserNotFoundError("User not found")