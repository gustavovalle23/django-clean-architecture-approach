from django.urls import path
from django.contrib import admin

from django_app.views import ViewWrapper
from django_app.factories import ProductViewFactory

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", ViewWrapper.as_view(view_factory=ProductViewFactory)),
]
