"""Domain entity tests. Pure unit tests, no Django."""

import unittest
from datetime import datetime
from unittest.mock import patch

from product.domain.entities import Product
from product.domain.errors import EntityValidationError


class TestProductEntity(unittest.TestCase):
    def test_constructor_sets_defaults(self):
        with patch.object(Product, "_validate"):
            product = Product("Product1")
            self.assertEqual(product.name, "Product1")
            self.assertEqual(product.quantity, 1)
            self.assertIsNone(product.id)
            self.assertTrue(product.is_active)
            self.assertIsInstance(product.created_at, datetime)

    def test_constructor_validates(self):
        with patch.object(Product, "_validate") as mock_validate:
            Product("Product1", 2)
            mock_validate.assert_called_once()

    def test_validation_raises_on_empty_name(self):
        self.assertRaises(EntityValidationError, lambda: Product("", 1))
        self.assertRaises(EntityValidationError, lambda: Product("  ", 1))

    def test_validation_raises_on_invalid_quantity(self):
        self.assertRaises(EntityValidationError, lambda: Product("Ok", -1))

    def test_to_dict(self):
        with patch.object(Product, "_validate"):
            product = Product("A", 2, id=10)
            d = product.to_dict()
            self.assertEqual(d["id"], 10)
            self.assertEqual(d["name"], "A")
            self.assertEqual(d["quantity"], 2)
            self.assertTrue(d["is_active"])
