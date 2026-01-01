"""
@brief Module for temperature unit conversions.
"""

from src.base import Unit


class Temperature(Unit):
    """
    @brief Base class for temperature units.
    """

    pass


class Celsius(Temperature):
    """
    @brief Represents Celsius unit (base unit).
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert Celsius to Celsius (base unit), with validation.

        @param value Value in Celsius.
        @return Value in Celsius.
        @throws ValueError if temperature is below absolute zero.
        """
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        return value

    def from_base(self, value: float) -> float:
        """
        @brief Convert Celsius (base unit) to Celsius.

        @param value Value in Celsius.
        @return Value in Celsius.
        """
        return value


class Fahrenheit(Temperature):
    """
    @brief Represents Fahrenheit unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert Fahrenheit to Celsius (base unit).

        @param value Value in Fahrenheit.
        @return Value in Celsius.
        """
        return (value - 32) * 5 / 9

    def from_base(self, value: float) -> float:
        """
        @brief Convert Celsius (base unit) to Fahrenheit.

        @param value Value in Celsius.
        @return Value in Fahrenheit.
        """
        return (value * 9 / 5) + 32


class Kelvin(Temperature):
    """
    @brief Represents Kelvin unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert Kelvin to Celsius (base unit).

        @param value Value in Kelvin.
        @return Value in Celsius.
        """
        return value - 273.15

    def from_base(self, value: float) -> float:
        """
        @brief Convert Celsius (base unit) to Kelvin.

        @param value Value in Celsius.
        @return Value in Kelvin.
        """
        return value + 273.15
