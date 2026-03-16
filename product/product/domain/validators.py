"""Domain validators. Pure functions / stateless. No framework dependencies."""

from typing import Dict, List, Tuple

from product.domain.errors import ErrorFields


def validate_product_name(name: str) -> List[str]:
    """Validate product name. Returns list of error messages for this field."""
    errors: List[str] = []
    if not name or not str(name).strip():
        errors.append("Name is required.")
    return errors


def validate_product_quantity(quantity: int) -> List[str]:
    """Validate quantity. Returns list of error messages for this field."""
    errors: List[str] = []
    if quantity is None:
        errors.append("Quantity is required.")
    elif not isinstance(quantity, int) or quantity < 0:
        errors.append("Quantity must be a non-negative integer.")
    return errors


def validate_product_data(data: Dict) -> Tuple[bool, ErrorFields]:
    """
    Validate product input. Returns (is_valid, errors_dict).
    errors_dict maps field name to list of error messages.
    """
    errors: ErrorFields = {}
    name_errors = validate_product_name(data.get("name", ""))
    if name_errors:
        errors["name"] = name_errors
    quantity = data.get("quantity", 0)
    quantity_errors = validate_product_quantity(quantity)
    if quantity_errors:
        errors["quantity"] = quantity_errors
    return len(errors) == 0, errors
