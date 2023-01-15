from app.__seedwork.domain.validators import ErrorFields


class ValidationException(Exception):
    pass


class EntityValidationException(Exception):
    error: ErrorFields

    def __init__(self, error: ErrorFields) -> None:
        self.error = error
        super().__init__("Entity Validation Error")


class NotFoundException(Exception):
    pass
