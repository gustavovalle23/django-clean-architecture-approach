from typing import Dict, List


class EntityDoesNotExist(Exception):
    pass


class EntityAlreadyExist(Exception):
    pass


ErrorFields = Dict[str, List[str]]


class EntityValidationException(Exception):
    error: ErrorFields

    def __init__(self, error: ErrorFields) -> None:
        self.error = error
        super().__init__("Entity Validation Error")
