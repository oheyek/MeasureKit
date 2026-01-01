from src.base import Unit


class Length(Unit):
    pass


class Milimeter(Length):
    def to_base(self, value: float) -> float:
        return value * 0.001

    def from_base(self, value: float) -> float:
        return value / 0.001


class Centimeter(Length):
    def to_base(self, value: float) -> float:
        return value * 0.01

    def from_base(self, value: float) -> float:
        return value / 0.01


class Meter(Length):
    def to_base(self, value: float) -> float:
        return value

    def from_base(self, value: float) -> float:
        return value


class Kilometer(Length):
    def to_base(self, value: float) -> float:
        return value * 1000

    def from_base(self, value: float) -> float:
        return value / 1000


class Inch(Length):
    def to_base(self, value: float) -> float:
        return value * 0.0254

    def from_base(self, value: float) -> float:
        return value / 0.0254


class Foot(Length):
    def to_base(self, value: float) -> float:
        return value * 0.3048

    def from_base(self, value: float) -> float:
        return value / 0.3048


class Yard(Length):
    def to_base(self, value: float) -> float:
        return value * 0.9144

    def from_base(self, value: float) -> float:
        return value / 0.9144


class Mile(Length):
    def to_base(self, value: float) -> float:
        return value * 1609.34

    def from_base(self, value: float) -> float:
        return value / 1609.34
