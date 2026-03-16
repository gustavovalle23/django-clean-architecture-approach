"""Repository ports (interfaces). Defined by domain/application, implemented in infra."""

from abc import ABC, abstractmethod

from product.domain.entities import Product


class ProductRepository(ABC):
    """Port: persist and retrieve Product aggregate."""

    @abstractmethod
    def save(self, product: Product) -> Product:
        """Persist product. Returns saved entity with id set."""
        ...

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product | None:
        """Return product by id or None."""
        ...
