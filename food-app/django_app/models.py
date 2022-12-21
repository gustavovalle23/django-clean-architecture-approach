from django.db import models

from domain.entities import Product


class ProductModel(models.Model):
    name: str = models.CharField(max_length=100)
    quantity: int = models.IntegerField()

    def to_entity(self) -> Product:
        return Product(self.name, self.quantity, self.pk)

    @staticmethod
    def from_entity(product: Product) -> "ProductModel":
        return ProductModel(name=product.name, quantity=product.quantity)

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
