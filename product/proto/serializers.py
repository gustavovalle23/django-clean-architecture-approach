from django_grpc_framework.proto_serializers import ModelSerializer

from django_app.models import ProductModel
from proto.product_pb2 import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        proto_class = Product
        fields = ['id', 'name', 'quantity']
