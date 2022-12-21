import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django_app.repositories import DjangoProductRepository
from application.use_cases import SaveProductUseCase
from api.serializers import ProductSerializer


repository = DjangoProductRepository()
save_product_use_case = SaveProductUseCase(repository)


@api_view(["POST"])
def create_product(request):
    req_data = json.loads(request.body)
    product = save_product_use_case.execute(
        name=req_data.get("name"), quantity=req_data.get("quantity")
    )

    response = ProductSerializer.serialize(product)

    return Response(response, status=status.HTTP_201_CREATED)
