import unittest

from application.use_cases import CreateProductUseCase
from domain.entities import Product


class MockRepository:
    called_times = 0

    def save(self, product: Product):
        self.called_times += 1
        return Product(product.name, product.quantity, 123)


class TestCreateProductUseCase(unittest.TestCase):
    def test_should_execute_create_product_use_case(self):
        mock_repository = MockRepository()
        product = Product("Product Test", 5)

        use_case = CreateProductUseCase(mock_repository)
        result = use_case.execute(product.name, product.quantity)

        assert result.id is not None
        assert result.name == product.name
        assert result.quantity == product.quantity
        assert mock_repository.called_times == 1
