from dataclasses import dataclass

from supplier.app.__seedwork.domain.entities import Entity


@dataclass
class Suplier(Entity):
    name: str
