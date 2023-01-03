import unittest
from freezegun import freeze_time

from application.use_cases import CreateProductUseCase
from domain.entities import Product


class MockRepository:
    called_times = 0

    def save(self, product: Product):
        self.called_times += 1
        return Product(
            product.name, product.quantity, 123, product.is_active, product.created_at
        )


class TestCreateProductUseCase(unittest.TestCase):
    @freeze_time("2023-01-01")
    def test_should_execute_create_product_use_case_with_inactived_product(self):
        mock_repository = MockRepository()
        product = {"name": "Product Test", "quantity": 5}

        use_case = CreateProductUseCase(mock_repository)
        result = use_case.execute(product["name"], product["quantity"])

        assert result.id is not None
        assert result.name == product["name"]
        assert result.quantity == product["quantity"]
        assert result.is_active == False
        assert mock_repository.called_times == 1

    @freeze_time("2023-01-02")
    def test_should_execute_create_product_use_case_with_actived_product(self):
        mock_repository = MockRepository()
        product = {"name": "Product Test", "quantity": 5}

        use_case = CreateProductUseCase(mock_repository)
        result = use_case.execute(product["name"], product["quantity"])

        assert result.id is not None
        assert result.name == product["name"]
        assert result.quantity == product["quantity"]
        assert result.is_active == True
        assert mock_repository.called_times == 1
