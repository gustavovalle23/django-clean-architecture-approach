from typing import Dict, List


class EntityDoesNotExist(Exception):
    pass


class EntityAlreadyExist(Exception):
    pass


ErrorFields = Dict[str, List[str]]


class EntityValidationException(Exception):
    def __init__(self, error: ErrorFields) -> None:
        super().__init__("Entity Validation Error " + str(error))
