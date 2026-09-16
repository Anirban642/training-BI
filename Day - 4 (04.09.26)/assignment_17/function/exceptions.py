class DuplicateBookError(Exception):
    pass

class DuplicateUserError(Exception):
    pass

class BookNotFoundError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class BookUnavailableError(Exception):
    pass

class BookNotIssuedError(Exception):
    pass

class IssuedBookError(Exception):
    pass