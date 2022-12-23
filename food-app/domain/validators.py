from typing import Dict

from domain.errors import ErrorFields


class FoodValidator:
    errors: ErrorFields = []

    def validate(self, data: Dict) -> bool:
        """pendent implementation"""
        pass


class FoodValidatorFactory:
    @staticmethod
    def create():
        return FoodValidator()
