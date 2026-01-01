from abc import ABC, abstractmethod


class Unit(ABC):
    @abstractmethod
    def to_base(self, value: float) -> float:
        pass

    @abstractmethod
    def from_base(self, value: float) -> float:
        pass

    def convert_to(self, value: float, target_unit: "Unit") -> float:
        base_value = self.to_base(value)
        return target_unit.from_base(base_value)
