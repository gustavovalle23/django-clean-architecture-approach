"""Integration tests: HTTP endpoint -> use case -> DB."""

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


pytestmark = pytest.mark.django_db


class TestProductEndpoints:
    endpoint = "/product/"

    def test_create_returns_201_and_product(self, api_client: APIClient):
        response = api_client.post(
            self.endpoint,
            {"name": "Product1", "quantity": 2},
            format="json",
        )
        assert response.status_code == 201
        data = response.json()
        assert data.get("id") is not None
        assert data.get("name") == "Product1"
        assert data.get("quantity") == 2
        assert "is_active" in data
