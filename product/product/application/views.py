"""
Application-level view logic. Maps HTTP input to commands and use case results to HTTP output.
No Django request/response objects; pure dict in, (dict, int) out. Testable without Django.
"""

from typing import Any, Dict, Tuple

from product.application.use_cases import CreateProductUseCase
from product.application.commands import CreateProductCommand
from product.domain.errors import EntityValidationError, EntityAlreadyExists


def create_product(
    use_case: CreateProductUseCase,
    payload: Dict[str, Any],
) -> Tuple[Dict[str, Any], int]:
    """
    Handle create-product request. Returns (response_body, status_code).
    """
    name = payload.get("name") or ""
    quantity = payload.get("quantity", 1)
    try:
        if isinstance(quantity, str) and quantity.isdigit():
            quantity = int(quantity)
    except (TypeError, ValueError):
        quantity = 1

    try:
        command = CreateProductCommand(name=name.strip(), quantity=quantity)
    except Exception:
        return {"error": "Invalid input."}, 400

    try:
        result = use_case.execute(command)
        return result.to_dict(), 201
    except EntityValidationError as e:
        return {"error": "Validation failed.", "details": e.errors}, 422
    except EntityAlreadyExists:
        return {"error": "Product already exists."}, 409
