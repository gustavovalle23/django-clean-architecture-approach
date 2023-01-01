from application.use_cases import CreateProductUseCase
from django_app.repositories import DjangoProductRepository
from application.views import ProductView


class ProductRepoFactory:
    @staticmethod
    def get():
        return DjangoProductRepository()


class CreateProductUseCaseFactory:
    @staticmethod
    def get():
        product_repo = ProductRepoFactory.get()
        return CreateProductUseCase(product_repo)


class ProductViewFactory:
    @staticmethod
    def create():
        create_product_use_case = CreateProductUseCaseFactory.get()
        return ProductView(create_product_use_case)
