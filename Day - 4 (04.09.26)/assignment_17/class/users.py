from exceptions import DuplicateUserError, UserNotFoundError

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class UserManager:
    def __init__(self):
        self.users = [
            User(2, "Anirban"),
            User(1, "Pritam"),
            User(4, "Tarun"),
            User(5, "Alinda")
        ]

    def register_user(self, id, name):
        for user in self.users:
            if user.id == id:
                raise DuplicateUserError("User ID already exists")
        user = User(id, name)
        self.users.append(user)

    def get_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        raise UserNotFoundError("User not found")