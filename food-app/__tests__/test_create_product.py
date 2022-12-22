import pytest
from rest_framework.test import APIClient

from domain.entities import Product


@pytest.fixture
def api_client():
    return APIClient


pytestmark = pytest.mark.django_db


class TestProductEndpoints:
    endpoint = "/product/"

    def test_create(self, api_client: APIClient):
        product = Product("Product1", 2)
        response = api_client().post(
            self.endpoint, {"name": product.name, "quantity": product.quantity}
        )

        assert response.status_code == 201

        product_response = response.json()

        assert product_response.get("id") is not None
        assert product_response.get("name") == product.name
        assert int(product_response.get("quantity")) == product.quantity
