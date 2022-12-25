from application.use_cases import SaveProductUseCase
from django_app.repositories import DjangoProductRepository
from application.views import ProductView


class ProductRepoFactory:
    @staticmethod
    def get():
        return DjangoProductRepository()


class SaveProductUseCaseFactory:
    @staticmethod
    def get():
        product_repo = ProductRepoFactory.get()
        return SaveProductUseCase(product_repo)


class ProductViewFactory:
    @staticmethod
    def create():
        save_product_use_case = SaveProductUseCaseFactory.get()
        return ProductView(save_product_use_case)
