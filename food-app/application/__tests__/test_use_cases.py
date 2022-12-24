from application.use_cases import SaveProductUseCase
from domain.entities import Product


class MockRepository:
    called_times = 0

    def save(self, product: Product):
        self.called_times += 1
        return Product(product.name, 123, product.quantity)


def test_should_execute_save_product_use_case():
    mock_repository = MockRepository()
    product = Product("Product Test", 5)

    use_case = SaveProductUseCase(mock_repository)
    result = use_case.execute(product.name, product.quantity)

    assert result.id is not None
    assert result.name == product.name
    assert result.quantity == product.quantity
    assert mock_repository.called_times == 1
