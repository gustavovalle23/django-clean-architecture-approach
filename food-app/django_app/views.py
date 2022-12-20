import json
from django.http import JsonResponse

from django_app.repositories import DjangoProductRepository
from application.use_cases import SaveProductUseCase


storage = DjangoProductRepository()
use_case = SaveProductUseCase(storage)


def create_product(request):
    req_data = json.loads(request.body)
    product = use_case.execute(
        name=req_data.get("name"), quantity=req_data.get("quantity")
    )

    return JsonResponse({"product": product.to_dict()}, status=200)
