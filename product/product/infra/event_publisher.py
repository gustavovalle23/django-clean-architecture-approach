"""Infrastructure: event publisher implementations."""

import logging
from typing import List

from product.domain.events import DomainEvent
from product.application.ports import EventPublisher

logger = logging.getLogger(__name__)


class LoggingEventPublisher(EventPublisher):
    """Publish events to logs. Use in dev or when no broker is configured."""

    def publish(self, events: List[DomainEvent]) -> None:
        for event in events:
            logger.info("Domain event: %s", event.to_dict())
