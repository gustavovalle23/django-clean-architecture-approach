from typing import Optional
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django_app.factories import ProductViewFactory


class ViewWrapper(APIView):
    view_factory: Optional[ProductViewFactory] = None

    def post(self, request: Request, *args, **kwargs):
        body, status = self.view_factory.create().post(request.POST)

        return Response(body, status=status)
