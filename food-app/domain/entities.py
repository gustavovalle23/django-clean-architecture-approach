class Product:
    def __init__(self, id: int, name: str, quantity: int) -> None:
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
