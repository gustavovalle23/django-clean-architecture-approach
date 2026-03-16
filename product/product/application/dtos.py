"""Application data transfer objects. Outputs from use cases."""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class ProductResponse:
    """Output DTO for product (REST/API)."""

    id: int | None
    name: str
    quantity: int
    is_active: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "is_active": self.is_active,
        }
