import unittest
from unittest.mock import patch
from datetime import datetime

from domain.entities import Product


class TestProductUnit(unittest.TestCase):
    def test_constructor(self):
        with patch.object(Product, "validate") as mock_validate_method:
            product = Product("Product1")
            mock_validate_method.assert_called_once()
            self.assertEqual(product.name, "Product1")
            self.assertIsNone(product.id)
            self.assertEqual(product.quantity, 1)
            self.assertTrue(product.is_active)
            self.assertIsInstance(product.created_at, datetime)
