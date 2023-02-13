from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from product.domain.entities import Product


class ProductModel(ExportModelOperationsMixin('product'), models.Model):
    name: str = models.CharField(max_length=100)
    quantity: int = models.IntegerField()

    def to_entity(self) -> Product:
        return Product(self.name, int(self.quantity), self.pk)

    @staticmethod
    def from_entity(product: Product) -> "ProductModel":
        return ProductModel(name=product.name, quantity=product.quantity)

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
