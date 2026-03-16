"""Application command DTOs. Inputs to use cases."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CreateProductCommand:
    """Input for CreateProductUseCase."""

    name: str
    quantity: int = 1
