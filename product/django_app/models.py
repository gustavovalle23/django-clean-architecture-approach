from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from product.domain.entities import Product


class ProductModel(models.Model):
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


@receiver(post_save, sender=ProductModel)
def change_product_handler(sender: ProductModel, **kwargs):
    from proto.serializers import ProductSerializer

    serializer = ProductSerializer(sender)
    # sending serializer to kafka topic...
