from product.application.use_cases import CreateProductUseCase
from product.infra.repositories import DjangoProductRepository
from product.application.views import ProductView


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
