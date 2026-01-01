from typing import Any

import src.temperatures
import src.length
import src.weight


def handle_convertion(value: str, unit_from: str, unit_to: str, category: str) -> str:
    if not value or not unit_from or not unit_to:
        return "All fields are required."
    try:
        value_to_convert: float = float(value)
    except ValueError:
        return "Value must be a number."

    if unit_from.lower() == unit_to.lower():
        return "You cannot convert the same units."

    if category == "temperature":
        unit_symbols: dict[str, str] = {
            "celsius": "°C",
            "fahrenheit": "°F",
            "kelvin": "K",
        }
        if (
            unit_from.lower() not in unit_symbols.keys()
            or unit_to.lower() not in unit_symbols.keys()
        ):
            return "Invalid unit selection."
        convert_from_unit: Any = getattr(src.temperatures, unit_from.capitalize())
        convert_to_unit: Any = getattr(src.temperatures, unit_to.capitalize())

    elif category == "length":
        unit_symbols: dict[str, str] = {
            "milimeter": "mm",
            "centimeter": "cm",
            "meter": "m",
            "kilometer": "km",
            "inch": "in",
            "foot": "ft",
            "yard": "yd",
            "mile": "mi",
        }
        if (
            unit_from.lower() not in unit_symbols.keys()
            or unit_to.lower() not in unit_symbols.keys()
        ):
            return "Invalid unit selection."
        convert_from_unit: Any = getattr(src.length, unit_from.capitalize())
        convert_to_unit: Any = getattr(src.length, unit_to.capitalize())

    else:
        unit_symbols: dict[str, str] = {
            "miligram": "mg",
            "gram": "g",
            "kilogram": "kg",
            "ounce": "oz",
            "pound": "lb",
        }
        if (
            unit_from.lower() not in unit_symbols.keys()
            or unit_to.lower() not in unit_symbols.keys()
        ):
            return "Invalid unit selection."

        convert_from_unit: Any = getattr(src.weight, unit_from.capitalize())
        convert_to_unit: Any = getattr(src.weight, unit_to.capitalize())

    result_value: float = convert_from_unit().convert_to(
        value_to_convert, convert_to_unit()
    )
    unit_symbol: str = unit_symbols.get(unit_to.lower(), unit_to)
    return f"{result_value:.4f} {unit_symbol}"
