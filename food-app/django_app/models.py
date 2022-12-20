from django.db import models

from domain.entities import Product


class ProductModel(models.Model):
    name: str = models.CharField(max_length=100)
    quantity: int = models.IntegerField()

    def to_entity(self) -> Product:
        return Product(self.name, self.quantity)

    @staticmethod
    def from_entity(product: Product) -> "ProductModel":
        return Product(name=product.name, quantity=product.quantity)

    class Meta:
        db_table = "products"
