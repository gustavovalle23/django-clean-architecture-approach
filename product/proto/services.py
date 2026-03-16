from django_grpc_framework import generics

from django_app.models import ProductModel
from proto.serializers import ProductProtoSerializer


class ProductGrpcService(generics.ModelService):
    """gRPC service: products CRUD. Uses Django model for persistence only."""
    queryset = ProductModel.objects.all().order_by("-id")
    serializer_class = ProductProtoSerializer
