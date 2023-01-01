from typing import Dict, Any

from application.serializers import ProductSerializer
from application.use_cases import CreateProductUseCase
from domain.errors import EntityAlreadyExist


class ProductView:
    def __init__(self, create_product_use_case: CreateProductUseCase):
        self.create_product_use_case = create_product_use_case

    def post(self, request: Dict[str, Any]):
        name = request.get("name")
        quantity = request.get("quantity")

        try:
            product = self.create_product_use_case.execute(name, quantity)
        except EntityAlreadyExist:
            body = {"error": "Product already exists!"}
            status = 412
        else:
            body = ProductSerializer.serialize(product)
            status = 201
        return body, status
