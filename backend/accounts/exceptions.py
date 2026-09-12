class UserAlreadyExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class InvalidPasswordError(Exception):
    def __init__(self, messages=None):
        self.messages = messages or ["Invalid password"]
        super().__init__(self.messages)


class ValidationError(Exception):
    def __init__(self, messages=None):
        self.messages = messages or ["Validation error"]
        super().__init__(self.messages)