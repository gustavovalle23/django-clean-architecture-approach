"""Application ports (interfaces). Implemented in infrastructure."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from product.domain.events import DomainEvent


class EventPublisher(ABC):
    """Port: publish domain events (e.g. to Kafka)."""

    @abstractmethod
    def publish(self, events: List[DomainEvent]) -> None:
        """Publish one or more domain events."""
        ...


class EventPublisherFake:
    """In-memory implementation for tests. Collects events."""

    def __init__(self) -> None:
        self.published: List[DomainEvent] = []

    def publish(self, events: List[DomainEvent]) -> None:
        self.published.extend(events)

    def clear(self) -> None:
        self.published.clear()
