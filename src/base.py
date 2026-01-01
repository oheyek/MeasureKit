"""
@brief Base module for unit conversion classes.
"""

from abc import ABC, abstractmethod


class Unit(ABC):
    """
    @brief Abstract base class for unit conversion.
    """

    @abstractmethod
    def to_base(self, value: float) -> float:
        """
        @brief Convert the given value to the base unit.

        @param value The value in the current unit.
        @return The equivalent value in the base unit.
        """
        pass

    @abstractmethod
    def from_base(self, value: float) -> float:
        """
        @brief Convert the given value from the base unit to this unit.

        @param value The value in the base unit.
        @return The equivalent value in this unit.
        """
        pass

    def convert_to(self, value: float, target_unit: "Unit") -> float:
        """
        @brief Convert a value from this unit to another unit.

        @param value The value in this unit.
        @param target_unit The target unit to convert to.
        @return The converted value in the target unit.
        """
        base_value = self.to_base(value)
        return target_unit.from_base(base_value)
