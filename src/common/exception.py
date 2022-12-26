class InputParamError(Exception):
    def __init__(self, message: str):
        self.message = message


class CustomError(Exception):
    def __init__(self, message: str):
        self.message = message


class Unauthorized(Exception):
    def __init__(self, message: str):
        self.message = message if message else "Unauthorized"


class ConflictMessage(Exception):
    def __init__(self, message: str):
        self.message = message
