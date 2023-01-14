from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field

from __seedwork.domain.entity import Entity
from product.domain.errors import EntityValidationException
from product.domain.validators import ProductValidatorFactory


@dataclass(frozen=True)
class Product(Entity):
    name: str
    quantity: Optional[int] = 1
    id: Optional[int] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.created_at:
            self._set("created_at", datetime.now())
        self.validate()

    def increment_quantity(self, quantity: int) -> int:
        if quantity > 0:
            self._set("quantity", self.quantity + quantity)
        return self.quantity

    def activate(self):
        self._set("is_active", True)

    def deactivate(self):
        self._set("is_active", False)

    def validate(self):
        validator = ProductValidatorFactory.create()
        is_valid = validator.validate(self.to_dict())

        if not is_valid:
            raise EntityValidationException(validator.errors)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "quantity": self.quantity}
