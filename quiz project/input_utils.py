class InvalidAnswerError(Exception):
    """Custom exception raised when the input is not a valid integer."""
    def __init__(self, message="Answer must be a valid integer."):
        super().__init__(message)

def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError as ve:
        raise InvalidAnswerError("Custom Exception: Please enter a valid integer.") from ve
