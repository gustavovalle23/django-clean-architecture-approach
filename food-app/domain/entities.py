from typing import Optional


class Product:
    def __init__(self, name: str, quantity: int, id: Optional[int] = None) -> None:
        self._id = id
        self._name = name
        self._quantity = quantity

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def to_dict(self):
        return {"name": self.name, "quantity": self.quantity}
