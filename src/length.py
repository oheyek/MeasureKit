"""
@brief Module for length unit conversions.
"""

from src.base import Unit


class Length(Unit):
    """
    @brief Base class for length units.
    """

    pass


class Millimeter(Length):
    """
    @brief Represents millimeter unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert millimeters to meters (base unit).

        @param value Value in millimeters.
        @return Value in meters.
        """
        return value * 0.001

    def from_base(self, value: float) -> float:
        """
        @brief Convert meters (base unit) to millimeters.

        @param value Value in meters.
        @return Value in millimeters.
        """
        return value / 0.001


class Centimeter(Length):
    """
    @brief Represents centimeter unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert centimeters to meters (base unit).

        @param value Value in centimeters.
        @return Value in meters.
        """
        return value * 0.01

    def from_base(self, value: float) -> float:
        """
        @brief Convert meters (base unit) to centimeters.

        @param value Value in meters.
        @return Value in centimeters.
        """
        return value / 0.01


class Meter(Length):
    """
    @brief Represents meter unit (base unit).
    """

    def to_base(self, value: float) -> float:
        """
        @brief Return value as is since meter is the base unit.

        @param value Value in meters.
        @return Value in meters.
        """
        return value

    def from_base(self, value: float) -> float:
        """
        @brief Return value as is since meter is the base unit.

        @param value Value in meters.
        @return Value in meters.
        """
        return value


class Kilometer(Length):
    """
    @brief Represents kilometer unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert kilometers to meters (base unit).

        @param value Value in kilometers.
        @return Value in meters.
        """
        return value * 1000

    def from_base(self, value: float) -> float:
        """
        @brief Convert meters (base unit) to kilometers.

        @param value Value in meters.
        @return Value in kilometers.
        """
        return value / 1000


class Inch(Length):
    """
    @brief Represents inch unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert inches to meters (base unit).

        @param value Value in inches.
        @return Value in meters.
        """
        return value * 0.0254

    def from_base(self, value: float) -> float:
        """
        @brief Convert meters (base unit) to inches.

        @param value Value in inches.
        @return Value in inches.
        """
        return value / 0.0254


class Foot(Length):
    """
    @brief Represents foot unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert feet to meters (base unit).

        @param value Value in feet.
        @return Value in meters.
        """
        return value * 0.3048

    def from_base(self, value: float) -> float:
        """
        @brief Convert meters (base unit) to feet.

        @param value Value in feet.
        @return Value in feet.
        """
        return value / 0.3048


class Yard(Length):
    """
    @brief Represents yard unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert yards to meters (base unit).

        @param value Value in yards.
        @return Value in meters.
        """
        return value * 0.9144

    def from_base(self, value: float) -> float:
        """
        @brief Convert meters (base unit) to yards.

        @param value Value in yards.
        @return Value in yards.
        """
        return value / 0.9144


class Mile(Length):
    """
    @brief Represents mile unit.
    """

    def to_base(self, value: float) -> float:
        """
        @brief Convert miles to meters (base unit).

        @param value Value in miles.
        @return Value in meters.
        """
        return value * 1609.344

    def from_base(self, value: float) -> float:
        """
        @brief Convert meters (base unit) to miles.

        @param value Value in miles.
        @return Value in miles.
        """
        return value / 1609.344
