"""
Application use cases. Orchestrate domain and ports only.
No Django or framework imports. Highly testable.
"""

from datetime import datetime
from uuid import uuid4

from product.domain.entities import Product
from product.domain.events import ProductCreated, ProductDeactivated
from product.domain.repositories import ProductRepository
from product.application.ports import EventPublisher
from product.application.commands import CreateProductCommand
from product.application.dtos import ProductResponse


def _is_weekend(dt: datetime) -> bool:
    """Business rule: weekend = Fri(4), Sat(5), Sun(6)."""
    return dt.weekday() in (4, 5, 6)


class CreateProductUseCase:
    """Create a product and publish domain events."""

    def __init__(
        self,
        product_repository: ProductRepository,
        event_publisher: EventPublisher,
    ) -> None:
        self._repository = product_repository
        self._event_publisher = event_publisher

    def execute(self, command: CreateProductCommand) -> ProductResponse:
        product = Product(name=command.name, quantity=command.quantity)
        was_deactivated_by_rule = False
        if _is_weekend(datetime.now()):
            product.deactivate()
            was_deactivated_by_rule = True

        saved = self._repository.save(product)
        events = [
            ProductCreated(
                event_id=str(uuid4()),
                occurred_at=datetime.now(),
                product_id=saved.id,
                name=saved.name,
                quantity=saved.quantity,
                is_active=saved.is_active,
            )
        ]
        if was_deactivated_by_rule and saved.id:
            events.append(
                ProductDeactivated(
                    event_id=str(uuid4()),
                    occurred_at=datetime.now(),
                    product_id=saved.id,
                    reason="weekend_rule",
                )
            )
        self._event_publisher.publish(events)

        return ProductResponse(
            id=saved.id,
            name=saved.name,
            quantity=saved.quantity,
            is_active=saved.is_active,
        )
