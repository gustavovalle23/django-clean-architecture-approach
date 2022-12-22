from abc import ABC, abstractmethod

from domain.entities import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        """responsable for save product model"""
        pass
