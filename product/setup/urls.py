from django.urls import path, include
from django.contrib import admin

from django_app.views import ViewWrapper
from django_app.factories import ProductViewFactory
from proto.product_pb2_grpc import add_ProductModelControllerServicer_to_server
from proto.services import ProductSerializer


def grpc_handlers(server):
    add_ProductModelControllerServicer_to_server(
        ProductSerializer.as_servicer(), server
    )


urlpatterns = [
    path('', include('django_prometheus.urls')),
    path("admin/", admin.site.urls),
    path("product/", ViewWrapper.as_view(view_factory=ProductViewFactory)),
]
