"""Dependency composition. Build use cases with concrete adapters."""

from product.application.use_cases import CreateProductUseCase
from product.application.ports import EventPublisher
from product.infra.repositories import DjangoProductRepository
from product.infra.event_publisher import LoggingEventPublisher


def get_product_repository() -> DjangoProductRepository:
    return DjangoProductRepository()


def get_event_publisher() -> EventPublisher:
    return LoggingEventPublisher()


def get_create_product_use_case() -> CreateProductUseCase:
    return CreateProductUseCase(
        product_repository=get_product_repository(),
        event_publisher=get_event_publisher(),
    )
