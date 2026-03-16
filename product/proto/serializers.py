from django_grpc_framework import proto_serializers

from django_app.models import ProductModel
from proto.product_pb2 import Product


class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    """gRPC serializer: ProductModel <-> proto Product."""
    class Meta:
        model = ProductModel
        proto_class = Product
        fields = ["id", "name", "quantity"]
