from base import Unit


class Temperature(Unit):
    pass


class Celsius(Temperature):
    def to_base(self, value: float) -> float:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        return value

    def from_base(self, value: float) -> float:
        return value


class Fahrenheit(Temperature):
    def to_base(self, value: float) -> float:
        return (value - 32) * 5 / 9

    def from_base(self, value: float) -> float:
        return (value * 9 / 5) + 32


class Kelvin(Temperature):
    def to_base(self, value: float) -> float:
        return value - 273.15

    def from_base(self, value: float) -> float:
        return value + 273.15
