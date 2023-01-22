from dataclasses import is_dataclass

from app.domain.entities import Supplier


def test_if_is_a_dataclass():
    assert is_dataclass(Supplier)
