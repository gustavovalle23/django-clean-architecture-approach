from abc import ABC
from typing import Any
from dataclasses import Field, dataclass, asdict


@dataclass(frozen=True)
class Entity(ABC):

    id: int

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self):
        entity_dict = asdict(self)
        return entity_dict

    @classmethod
    def get_field(cls, entity_field: str) -> Field:
        return cls.__dataclass_fields__[entity_field]
