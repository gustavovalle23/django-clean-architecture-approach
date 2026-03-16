"""Domain events. Immutable, framework-free."""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


@dataclass(frozen=True)
class DomainEvent:
    """Base for all domain events."""

    event_id: str
    occurred_at: datetime

    def to_dict(self) -> Dict[str, Any]:
        """For serialization (e.g. to Kafka)."""
        return {
            "event_id": self.event_id,
            "occurred_at": self.occurred_at.isoformat(),
            "event_type": self.__class__.__name__,
        }


@dataclass(frozen=True)
class ProductCreated(DomainEvent):
    """Raised when a product is created."""

    product_id: int
    name: str
    quantity: int
    is_active: bool

    def to_dict(self) -> Dict[str, Any]:
        base = super().to_dict()
        base.update(
            product_id=self.product_id,
            name=self.name,
            quantity=self.quantity,
            is_active=self.is_active,
        )
        return base


@dataclass(frozen=True)
class ProductDeactivated(DomainEvent):
    """Raised when a product is deactivated (e.g. by business rule)."""

    product_id: int
    reason: str

    def to_dict(self) -> Dict[str, Any]:
        base = super().to_dict()
        base.update(product_id=self.product_id, reason=self.reason)
        return base
