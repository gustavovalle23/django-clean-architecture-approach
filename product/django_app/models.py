"""Django ORM models. Persistence only; no business logic."""

from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from product.domain.entities import Product


class ProductModel(ExportModelOperationsMixin('product'), models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def to_entity(self) -> Product:
        return Product(
            name=self.name,
            quantity=int(self.quantity),
            id=self.pk,
            is_active=self.is_active,
        )

    @staticmethod
    def from_entity(product: Product) -> "ProductModel":
        return ProductModel(
            name=product.name,
            quantity=product.quantity,
            is_active=product.is_active,
        )

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
