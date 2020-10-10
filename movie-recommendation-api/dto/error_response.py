class ErrorResponse:
    def __init__(self, message, status_code=500):
        self.error_message = message
        self.status_code = status_code

    def as_json(self):
        return self.__dict__ if self else {}
