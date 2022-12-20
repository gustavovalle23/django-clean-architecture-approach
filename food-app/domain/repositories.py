from abc import ABC, abstractmethod

from domain.entities import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, name: str, quantity: int) -> Product:
        """responsable for save product model"""
        pass
