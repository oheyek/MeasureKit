"""
@brief Module for weight unit conversions.
"""

from src.base import Unit


class Weight(Unit):
    """
    @brief Base class for weight units.
    """

    pass


class Milligram(Weight):
    """
    @brief Represents milligram unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert milligrams to grams (base unit).

        @param value Value in milligrams.
        @return Value in grams.
        """
        return value * 0.001

    def from_base(self, value: float) -> float:
        """
        @brief Convert grams (base unit) to milligrams.

        @param value Value in grams.
        @return Value in milligrams.
        """
        return value / 0.001


class Gram(Weight):
    """
    @brief Represents gram unit (base unit).
    """

    def to_base(self, value: float) -> float:
        """
        @brief Return value as is since gram is the base unit.

        @param value Value in grams.
        @return Value in grams.
        """
        return value

    def from_base(self, value: float) -> float:
        """
        @brief Return value as is since gram is the base unit.

        @param value Value in grams.
        @return Value in grams.
        """
        return value


class Kilogram(Weight):
    """
    @brief Represents kilogram unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert kilograms to grams (base unit).

        @param value Value in kilograms.
        @return Value in grams.
        """
        return value * 1000

    def from_base(self, value: float) -> float:
        """
        @brief Convert grams (base unit) to kilograms.

        @param value Value in grams.
        @return Value in kilograms.
        """
        return value / 1000


class Ounce(Weight):
    """
    @brief Represents ounce unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert ounces to grams (base unit).

        @param value Value in ounces.
        @return Value in grams.
        """
        return value * 28.349523125

    def from_base(self, value: float) -> float:
        """
        @brief Convert grams (base unit) to ounces.

        @param value Value in grams.
        @return Value in ounces.
        """
        return value / 28.349523125


class Pound(Weight):
    """
    @brief Represents pound unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert pounds to grams (base unit).

        @param value Value in pounds.
        @return Value in grams.
        """
        return value * 453.59237

    def from_base(self, value: float) -> float:
        """
        @brief Convert grams (base unit) to pounds.

        @param value Value in grams.
        @return Value in pounds.
        """
        return value / 453.59237
