"""Domain validator tests. Pure unit tests."""

import unittest
from product.domain.validators import (
    validate_product_name,
    validate_product_quantity,
    validate_product_data,
)


class TestValidateProductName(unittest.TestCase):
    def test_empty_name_returns_errors(self):
        self.assertEqual(validate_product_name(""), ["Name is required."])
        self.assertEqual(validate_product_name("   "), ["Name is required."])

    def test_valid_name_returns_empty(self):
        self.assertEqual(validate_product_name("Ok"), [])
        self.assertEqual(validate_product_name("A"), [])


class TestValidateProductQuantity(unittest.TestCase):
    def test_negative_quantity_returns_errors(self):
        self.assertIn("Quantity must be a non-negative integer.", validate_product_quantity(-1))

    def test_valid_quantity_returns_empty(self):
        self.assertEqual(validate_product_quantity(0), [])
        self.assertEqual(validate_product_quantity(1), [])


class TestValidateProductData(unittest.TestCase):
    def test_valid_data(self):
        ok, errors = validate_product_data({"name": "X", "quantity": 2})
        self.assertTrue(ok)
        self.assertEqual(errors, {})

    def test_missing_name(self):
        ok, errors = validate_product_data({"quantity": 1})
        self.assertFalse(ok)
        self.assertIn("name", errors)
