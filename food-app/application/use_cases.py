from domain.repositories import ProductRepository
from domain.entities import Product


class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self, name: str, quantity: int) -> Product:
        product = Product(name, quantity)
        return self.product_repository.save(product)
