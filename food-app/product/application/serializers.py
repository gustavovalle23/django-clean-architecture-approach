from product.domain.entities import Product


class ProductSerializer:
    @staticmethod
    def serialize(product: Product):
        return {"id": product.id, "name": product.name, "quantity": product.quantity}
