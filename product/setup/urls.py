from django.urls import path, include
from django.contrib import admin

from django_app.views import CreateProductView
from proto.product_pb2_grpc import add_ProductModelControllerServicer_to_server
from proto.services import ProductGrpcService


def grpc_handlers(server):
    add_ProductModelControllerServicer_to_server(
        ProductGrpcService.as_servicer(), server
    )


urlpatterns = [
    path("", include("django_prometheus.urls")),
    path("admin/", admin.site.urls),
    path("product/", CreateProductView.as_view()),
]
