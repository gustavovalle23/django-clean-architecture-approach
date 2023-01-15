from abc import ABC
import orjson as json
from dataclasses import dataclass, fields


@dataclass(frozen=True)
class ValueObject(ABC):
    def __str__(self) -> str:
        fields_name = [field.name for field in fields(self)]

        if len(fields_name) == 1:
            return str(getattr(self, fields_name[0]))

        response = {field: getattr(self, field) for field in fields_name}
        return json.dumps(response)
