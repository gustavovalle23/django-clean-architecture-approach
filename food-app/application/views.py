from typing import Dict, Any

from django_app.serializers import ProductSerializer
from application.use_cases import SaveProductUseCase
from domain.errors import EntityAlreadyExist


class ProductView:
    def __init__(self, save_product_use_case: SaveProductUseCase):
        self.save_product_use_case = save_product_use_case

    def post(self, request: Dict[str, Any]):
        name = request.get("name")
        quantity = request.get("quantity")

        try:
            product = self.save_product_use_case.execute(name, quantity)
        except EntityAlreadyExist:
            body = {"error": "Product already exists!"}
            status = 412
        else:
            body = ProductSerializer.serialize(product)
            status = 201
        return body, status
