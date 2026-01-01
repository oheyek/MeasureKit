import pytest
import src.convertion_handler


def test_millimeter() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "1000", "millimeter", "centimeter", "length"
        )
        == "100.0000 cm"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "1000", "millimeter", "meter", "length"
        )
        == "1.0000 m"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "1000", "millimeter", "kilometer", "length"
        )
        == "0.0010 km"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "millimeter", "inch", "length")
        == "39.3701 in"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "millimeter", "foot", "length")
        == "3.2808 ft"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "millimeter", "yard", "length")
        == "1.0936 yd"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "millimeter", "mile", "length")
        == "0.0006 mi"
    )


def test_centimeter() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "100", "centimeter", "millimeter", "length"
        )
        == "1000.0000 mm"
    )
    assert (
        src.convertion_handler.handle_convertion("100", "centimeter", "meter", "length")
        == "1.0000 m"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "100", "centimeter", "kilometer", "length"
        )
        == "0.0010 km"
    )
    assert (
        src.convertion_handler.handle_convertion("100", "centimeter", "inch", "length")
        == "39.3701 in"
    )
    assert (
        src.convertion_handler.handle_convertion("100", "centimeter", "foot", "length")
        == "3.2808 ft"
    )
    assert (
        src.convertion_handler.handle_convertion("100", "centimeter", "yard", "length")
        == "1.0936 yd"
    )
    assert (
        src.convertion_handler.handle_convertion("100", "centimeter", "mile", "length")
        == "0.0006 mi"
    )


def test_meter() -> None:
    assert (
        src.convertion_handler.handle_convertion("1", "meter", "millimeter", "length")
        == "1000.0000 mm"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "meter", "centimeter", "length")
        == "100.0000 cm"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "meter", "kilometer", "length")
        == "0.0010 km"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "meter", "inch", "length")
        == "39.3701 in"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "meter", "foot", "length")
        == "3.2808 ft"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "meter", "yard", "length")
        == "1.0936 yd"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "meter", "mile", "length")
        == "0.0006 mi"
    )


def test_kilometer() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "1", "kilometer", "millimeter", "length"
        )
        == "1000000.0000 mm"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "1", "kilometer", "centimeter", "length"
        )
        == "100000.0000 cm"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilometer", "meter", "length")
        == "1000.0000 m"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilometer", "inch", "length")
        == "39370.0787 in"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilometer", "foot", "length")
        == "3280.8399 ft"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilometer", "yard", "length")
        == "1093.6133 yd"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilometer", "mile", "length")
        == "0.6214 mi"
    )


def test_inch() -> None:
    assert (
        src.convertion_handler.handle_convertion("12", "inch", "millimeter", "length")
        == "304.8000 mm"
    )
    assert (
        src.convertion_handler.handle_convertion("12", "inch", "centimeter", "length")
        == "30.4800 cm"
    )
    assert (
        src.convertion_handler.handle_convertion("12", "inch", "meter", "length")
        == "0.3048 m"
    )
    assert (
        src.convertion_handler.handle_convertion("12", "inch", "kilometer", "length")
        == "0.0003 km"
    )
    assert (
        src.convertion_handler.handle_convertion("12", "inch", "foot", "length")
        == "1.0000 ft"
    )
    assert (
        src.convertion_handler.handle_convertion("12", "inch", "yard", "length")
        == "0.3333 yd"
    )
    assert (
        src.convertion_handler.handle_convertion("12", "inch", "mile", "length")
        == "0.0002 mi"
    )


def test_foot() -> None:
    assert (
        src.convertion_handler.handle_convertion("3", "foot", "millimeter", "length")
        == "914.4000 mm"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "foot", "centimeter", "length")
        == "91.4400 cm"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "foot", "meter", "length")
        == "0.9144 m"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "foot", "kilometer", "length")
        == "0.0009 km"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "foot", "inch", "length")
        == "36.0000 in"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "foot", "yard", "length")
        == "1.0000 yd"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "foot", "mile", "length")
        == "0.0006 mi"
    )


def test_yard() -> None:
    assert (
        src.convertion_handler.handle_convertion("3", "yard", "millimeter", "length")
        == "2743.2000 mm"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "yard", "centimeter", "length")
        == "274.3200 cm"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "yard", "meter", "length")
        == "2.7432 m"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "yard", "kilometer", "length")
        == "0.0027 km"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "yard", "inch", "length")
        == "108.0000 in"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "yard", "foot", "length")
        == "9.0000 ft"
    )
    assert (
        src.convertion_handler.handle_convertion("3", "yard", "mile", "length")
        == "0.0017 mi"
    )


def test_mile() -> None:
    assert (
        src.convertion_handler.handle_convertion("1", "mile", "millimeter", "length")
        == "1609344.0000 mm"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "mile", "centimeter", "length")
        == "160934.4000 cm"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "mile", "meter", "length")
        == "1609.3440 m"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "mile", "kilometer", "length")
        == "1.6093 km"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "mile", "inch", "length")
        == "63360.0000 in"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "mile", "foot", "length")
        == "5280.0000 ft"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "mile", "yard", "length")
        == "1760.0000 yd"
    )


def test_empty_fields() -> None:
    assert (
        src.convertion_handler.handle_convertion("", "meter", "kilometer", "length")
        == "All fields are required."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "", "kilometer", "length")
        == "All fields are required."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "meter", "", "length")
        == "All fields are required."
    )


def test_invalid_number() -> None:
    assert (
        src.convertion_handler.handle_convertion("abc", "meter", "kilometer", "length")
        == "Value must be a number."
    )


def test_same_units() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "meter", "meter", "length")
        == "You cannot convert the same units."
    )


def test_unsupported_units() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "smoot", "kilometer", "length")
        == "Unsupported unit."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "meter", "furlong", "length")
        == "Unsupported unit."
    )


def test_invalid_category() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "meter", "kilometer", "speed")
        == "Invalid category."
    )


def test_units_not_matching_category() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "meter", "celsius", "length")
        == "Invalid unit selection."
    )
    assert (
        src.convertion_handler.handle_convertion("100", "foot", "kelvin", "length")
        == "Invalid unit selection."
    )
