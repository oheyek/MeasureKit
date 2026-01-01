import pytest
import src.convertion_handler


def test_celsius() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "10", "celsius", "fahrenheit", "temperature"
        )
        == "50.0000 °F"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "10", "celsius", "kelvin", "temperature"
        )
        == "283.1500 K"
    )


def test_fahrenheit() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "50", "fahrenheit", "celsius", "temperature"
        )
        == "10.0000 °C"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "50", "fahrenheit", "kelvin", "temperature"
        )
        == "283.1500 K"
    )


def test_kelvin() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "283.15", "kelvin", "celsius", "temperature"
        )
        == "10.0000 °C"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "283.15", "kelvin", "fahrenheit", "temperature"
        )
        == "50.0000 °F"
    )


def test_empty_fields() -> None:
    assert (
        src.convertion_handler.handle_convertion("", "celsius", "kelvin", "temperature")
        == "All fields are required."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "", "kelvin", "temperature")
        == "All fields are required."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "celsius", "", "temperature")
        == "All fields are required."
    )


def test_invalid_number() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "abc", "celsius", "kelvin", "temperature"
        )
        == "Value must be a number."
    )


def test_same_units() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "10", "celsius", "celsius", "temperature"
        )
        == "You cannot convert the same units."
    )


def test_unsupported_units() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "10", "celsius", "lightyear", "temperature"
        )
        == "Unsupported unit."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "smoot", "kelvin", "temperature")
        == "Unsupported unit."
    )


def test_invalid_category() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "celsius", "kelvin", "speed")
        == "Invalid category."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "meter", "kilometer", "volume")
        == "Invalid category."
    )


def test_units_not_matching_category() -> None:
    assert (
        src.convertion_handler.handle_convertion(
            "10", "celsius", "meter", "temperature"
        )
        == "Invalid unit selection."
    )
    assert (
        src.convertion_handler.handle_convertion(
            "5", "fahrenheit", "yard", "temperature"
        )
        == "Invalid unit selection."
    )
