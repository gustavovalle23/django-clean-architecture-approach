"""Infrastructure: repository implementations."""

from product.domain.entities import Product
from product.domain.repositories import ProductRepository
from django_app.models import ProductModel


class DjangoProductRepository(ProductRepository):
    """Persist Product via Django ORM. Adapter: domain entity <-> model."""

    def save(self, product: Product) -> Product:
        if product.id is not None:
            model = ProductModel.objects.get(pk=product.id)
            model.name = product.name
            model.quantity = product.quantity
            model.is_active = product.is_active
            model.save()
            return model.to_entity()
        model = ProductModel.from_entity(product)
        model.save()
        return model.to_entity()

    def get_by_id(self, product_id: int) -> Product | None:
        try:
            model = ProductModel.objects.get(pk=product_id)
            return model.to_entity()
        except ProductModel.DoesNotExist:
            return None
