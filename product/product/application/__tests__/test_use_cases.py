"""Use case tests. Mock repository and event publisher; no Django."""

import unittest
from freezegun import freeze_time

from product.application.use_cases import CreateProductUseCase
from product.application.commands import CreateProductCommand
from product.application.ports import EventPublisherFake
from product.domain.entities import Product
from product.domain.events import ProductCreated, ProductDeactivated


class InMemoryProductRepository:
    """Fake repository for tests."""

    def __init__(self):
        self._next_id = 1
        self.saved: list[Product] = []

    def save(self, product: Product) -> Product:
        object.__setattr__(product, "id", self._next_id)
        self._next_id += 1
        self.saved.append(product)
        return product

    def get_by_id(self, product_id: int) -> Product | None:
        for p in self.saved:
            if p.id == product_id:
                return p
        return None


class TestCreateProductUseCase(unittest.TestCase):
    @freeze_time("2023-01-01")  # Sunday
    def test_creates_product_deactivated_on_weekend(self):
        repo = InMemoryProductRepository()
        events = EventPublisherFake()
        use_case = CreateProductUseCase(repo, events)
        command = CreateProductCommand(name="Product Test", quantity=5)

        result = use_case.execute(command)

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, "Product Test")
        self.assertEqual(result.quantity, 5)
        self.assertFalse(result.is_active)
        self.assertEqual(len(repo.saved), 1)
        self.assertFalse(repo.saved[0].is_active)
        self.assertEqual(len(events.published), 2)  # ProductCreated + ProductDeactivated
        self.assertTrue(any(isinstance(e, ProductCreated) for e in events.published))
        self.assertTrue(any(isinstance(e, ProductDeactivated) for e in events.published))

    @freeze_time("2023-01-02")  # Monday
    def test_creates_product_active_on_weekday(self):
        repo = InMemoryProductRepository()
        events = EventPublisherFake()
        use_case = CreateProductUseCase(repo, events)
        command = CreateProductCommand(name="Product Test", quantity=5)

        result = use_case.execute(command)

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, "Product Test")
        self.assertEqual(result.quantity, 5)
        self.assertTrue(result.is_active)
        self.assertEqual(len(events.published), 1)
        self.assertIsInstance(events.published[0], ProductCreated)
