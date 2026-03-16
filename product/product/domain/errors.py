"""Domain exceptions. No framework dependencies."""

from typing import Dict, List

ErrorFields = Dict[str, List[str]]


class DomainException(Exception):
    """Base for all domain errors."""

    pass


class EntityDoesNotExist(DomainException):
    """Raised when an entity is not found."""

    pass


class EntityAlreadyExists(DomainException):
    """Raised when an entity duplicate would be created."""

    pass


class EntityValidationError(DomainException):
    """Raised when entity validation fails."""

    def __init__(self, errors: ErrorFields) -> None:
        self.errors = errors
        super().__init__(f"Validation failed: {errors}")
