class GetProductInteractor:
    def __init__(self, product_repository) -> None:
        self.product_repository = product_repository

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.product_repository.get_product(id=self.id)
