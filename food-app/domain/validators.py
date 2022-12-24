from typing import Dict, List

from domain.errors import ErrorFields


class FoodValidator:
    errors: List[ErrorFields] = []

    def validate(self, data: Dict) -> bool:
        if data.get("name") is None:
            self.errors.append({"name": ["Name can not be null"]})
        if data.get("nae") == "":
            self.errors.append({"name": ["Name can not be empty"]})

        return len(self.errors) == 0


class FoodValidatorFactory:
    @staticmethod
    def create():
        return FoodValidator()
