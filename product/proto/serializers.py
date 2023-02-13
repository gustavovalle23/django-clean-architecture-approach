from django_grpc_framework import proto_serializers
from rest_framework.serializers import SerializerMethodField

from django_app.models import ProductModel
from proto.product_pb2 import Product


class ProductSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = ProductModel
        proto_class = Product
        fields = ['id', 'name', 'quantity']
