from domain.entities import Product
from django_app.models import ProductModel


class DjangoProductRepository:
    def save(self, product) -> Product:
        django_product = ProductModel.from_entity(product)
        django_product.save()
        return django_product.to_entity()
