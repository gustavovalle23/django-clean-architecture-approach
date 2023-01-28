from dataclasses import dataclass

from app.__seedwork.application.use_cases import UseCase
from app.domain.repositories import SupplierRepository


@dataclass(frozen=True)
class Input:
    name: str


@dataclass(frozen=True)
class Output:
    id: str
    name: str


class CreateSupplierUseCase(UseCase[Input, Output]):
    def __init__(self, supplier_repository: SupplierRepository) -> None:
        self.supplier_repository = supplier_repository

    def execute(self, input_use_case: Input) -> Output:
        supplier = self.supplier_repository.save()
        return supplier
