from datetime import datetime

from product.domain.repositories import ProductRepository
from product.domain.entities import Product


class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self, name: str, quantity: int) -> Product:
        product = Product(name, quantity)

        if datetime.today().weekday() in (4, 5, 6):
            product.deactivate()

        return self.product_repository.save(product)
