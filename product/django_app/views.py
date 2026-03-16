"""Django REST adapter. Thin layer: request -> application -> response."""

from typing import Any, Optional

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from product.application.views import create_product
from product.application.use_cases import CreateProductUseCase
from django_app.factories import get_create_product_use_case


class CreateProductView(APIView):
    """POST /product/ -> create product. Delegates to application layer."""

    def __init__(self, use_case: Optional[CreateProductUseCase] = None, **kwargs: Any):
        super().__init__(**kwargs)
        self._use_case = use_case

    def get_use_case(self) -> CreateProductUseCase:
        return self._use_case or get_create_product_use_case()

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        payload = request.data if hasattr(request, "data") else (request.POST or {})
        body, status = create_product(self.get_use_case(), dict(payload))
        return Response(body, status=status)
