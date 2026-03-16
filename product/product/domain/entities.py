"""Domain entities. Business logic only, no framework dependencies."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from product.domain.errors import EntityValidationError
from product.domain.validators import validate_product_data


@dataclass
class Product:
    """
    Product aggregate root. All product business rules live here.
    Immutable-friendly: mutating methods return new state (we use in-place for simplicity).
    """

    name: str
    quantity: int = 1
    id: Optional[int] = None
    is_active: bool = True
    created_at: Optional[datetime] = None

    def __post_init__(self) -> None:
        if self.created_at is None:
            object.__setattr__(self, "created_at", datetime.now())
        self._validate()

    def _validate(self) -> None:
        is_valid, errors = validate_product_data(
            {"name": self.name, "quantity": self.quantity}
        )
        if not is_valid:
            raise EntityValidationError(errors)

    def increment_quantity(self, delta: int) -> None:
        """Business rule: only positive increments."""
        if delta <= 0:
            return
        object.__setattr__(self, "quantity", self.quantity + delta)

    def activate(self) -> None:
        object.__setattr__(self, "is_active", True)

    def deactivate(self) -> None:
        object.__setattr__(self, "is_active", False)

    def to_dict(self) -> dict:
        """Minimal DTO for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
