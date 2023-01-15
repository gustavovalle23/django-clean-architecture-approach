from django_grpc_framework.proto_serializers import ModelSerializer

from django_app.models import ProductModel
from proto import product_pb2


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        proto_class = product_pb2.Product
