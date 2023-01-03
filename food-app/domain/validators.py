from typing import Dict, List

from domain.errors import ErrorFields


class ProductValidator:
    errors: List[ErrorFields] = []

    def validate(self, data: Dict) -> bool:
        if not data.get("name"):
            self.errors.append({"name": ["Name is required"]})

        return len(self.errors) == 0


class ProductValidatorFactory:
    @staticmethod
    def create():
        return ProductValidator()
