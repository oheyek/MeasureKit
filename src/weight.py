from src.base import Unit


class Weight(Unit):
    pass


class Milligram(Weight):
    def to_base(self, value: float) -> float:
        return value * 0.001

    def from_base(self, value: float) -> float:
        return value / 0.001


class Gram(Weight):
    def to_base(self, value: float) -> float:
        return value

    def from_base(self, value: float) -> float:
        return value


class Kilogram(Weight):
    def to_base(self, value: float) -> float:
        return value * 1000

    def from_base(self, value: float) -> float:
        return value / 1000


class Ounce(Weight):
    def to_base(self, value: float) -> float:
        return value * 28.349523125

    def from_base(self, value: float) -> float:
        return value / 28.349523125


class Pound(Weight):
    def to_base(self, value: float) -> float:
        return value * 453.59237

    def from_base(self, value: float) -> float:
        return value / 453.59237
