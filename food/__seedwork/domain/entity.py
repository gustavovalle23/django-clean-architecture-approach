from typing import Any


class Entity:
    def _set(self, field: str, value: Any):
        object.__setattr__(self, field, value)
