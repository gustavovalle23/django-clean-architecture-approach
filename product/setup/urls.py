from django.urls import path, include
from django.contrib import admin

from django_app.views import ViewWrapper
from django_app.factories import ProductViewFactory

urlpatterns = [
    path('', include('django_prometheus.urls')),
    path("admin/", admin.site.urls),
    path("product/", ViewWrapper.as_view(view_factory=ProductViewFactory)),
]
