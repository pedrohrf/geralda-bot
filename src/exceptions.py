from src.enums import messages


class BaseDiscordResponseException(Exception):
    def __init__(self, message):
        super(BaseDiscordResponseException, self).__init__()
        self.message = message


class DBConnectException(BaseDiscordResponseException):
    def __init__(self):
        super(DBConnectException, self).__init__(messages.DB_CONNECTION_ERROR)


class InvalidCommand(BaseDiscordResponseException):
    def __init__(self):
        super(InvalidCommand, self).__init__(messages.INVALID_COMMAND)
