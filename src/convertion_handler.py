"""
@brief Module for handling unit conversions.
"""

from typing import Any

import src.temperatures
import src.length
import src.weight


UNITS = (
    "millimeter",
    "centimeter",
    "meter",
    "kilometer",
    "inch",
    "foot",
    "yard",
    "mile",
    "milligram",
    "gram",
    "kilogram",
    "ounce",
    "pound",
    "celsius",
    "fahrenheit",
    "kelvin",
)

CATEGORIES = ("temperature", "length", "weight")


def handle_convertion(value: str, unit_from: str, unit_to: str, category: str) -> str:
    """
    @brief Handle unit conversion based on input parameters.

    @param value The value to convert as a string.
    @param unit_from The source unit.
    @param unit_to The target unit.
    @param category The category of units (temperature, length, weight).
    @return The converted value with unit symbol as a string, or an error message.
    """
    if not value or not unit_from or not unit_to:
        return "All fields are required."
    try:
        value_to_convert: float = float(value)
    except ValueError:
        return "Value must be a number."

    if unit_from.lower() == unit_to.lower():
        return "You cannot convert the same units."

    if unit_from.lower() not in UNITS or unit_to.lower() not in UNITS:
        return "Unsupported unit."

    if category not in CATEGORIES:
        return "Invalid category."

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
            "millimeter": "mm",
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
            "milligram": "mg",
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
