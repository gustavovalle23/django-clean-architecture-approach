"""Application view (create_product) tests. No Django; mock use case."""

import unittest
from unittest.mock import Mock

from product.application.views import create_product
from product.application.use_cases import CreateProductUseCase
from product.application.dtos import ProductResponse
from product.domain.errors import EntityValidationError, EntityAlreadyExists


class TestCreateProductView(unittest.TestCase):
    def test_returns_201_and_body_on_success(self):
        use_case = Mock(spec=CreateProductUseCase)
        use_case.execute.return_value = ProductResponse(
            id=1, name="P", quantity=2, is_active=True
        )
        body, status = create_product(use_case, {"name": "P", "quantity": 2})
        self.assertEqual(status, 201)
        self.assertEqual(body["id"], 1)
        self.assertEqual(body["name"], "P")
        self.assertEqual(body["quantity"], 2)
        use_case.execute.assert_called_once()

    def test_returns_422_on_validation_error(self):
        use_case = Mock(spec=CreateProductUseCase)
        use_case.execute.side_effect = EntityValidationError({"name": ["Required"]})
        body, status = create_product(use_case, {"name": "", "quantity": 1})
        self.assertEqual(status, 422)
        self.assertIn("error", body)
        self.assertIn("details", body)

    def test_returns_409_on_already_exists(self):
        use_case = Mock(spec=CreateProductUseCase)
        use_case.execute.side_effect = EntityAlreadyExists()
        body, status = create_product(use_case, {"name": "P", "quantity": 1})
        self.assertEqual(status, 409)
        self.assertIn("error", body)
