from base import Unit


class Weight(Unit):
    pass


class Miligram(Weight):
    def to_base(self, value: float) -> float:
        return value / 0.001

    def from_base(self, value: float) -> float:
        return value * 0.001


class Gram(Weight):
    def to_base(self, value: float) -> float:
        return value

    def from_base(self, value: float) -> float:
        return value


class Kilogram(Weight):
    def to_base(self, value: float) -> float:
        return value / 1000

    def from_base(self, value: float) -> float:
        return value * 1000


class Ounce(Weight):
    def to_base(self, value: float) -> float:
        return value / 28.3495

    def from_base(self, value: float) -> float:
        return value * 28.3495


class Pound(Weight):
    def to_base(self, value: float) -> float:
        return value / 453.592

    def from_base(self, value: float) -> float:
        return value * 453.592
