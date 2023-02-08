from dataclasses import dataclass

from app.__seedwork.domain.entities import Entity


@dataclass(frozen=True)
class Supplier(Entity[int]):
    name: str
