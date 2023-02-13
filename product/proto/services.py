from django_grpc_framework import generics

from django_app.models import ProductModel
from proto.serializers import ProductSerializer


class UserService(generics.ModelService):
    """
    gRPC service that allows products to be retrieved or updated.
    """
    queryset = ProductModel.objects.all().order_by('-id')
    serializer_class = ProductSerializer
