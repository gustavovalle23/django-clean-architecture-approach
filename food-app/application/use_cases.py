from domain.repositories import ProductRepository


class SaveProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self, name: str, quantity: int):
        return self.product_repository.save(name=name, quantity=quantity)
