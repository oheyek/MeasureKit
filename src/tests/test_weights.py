import pytest
import src.convertion_handler


def test_milligram() -> None:
    assert (
        src.convertion_handler.handle_convertion("1000", "milligram", "gram", "weight")
        == "1.0000 g"
    )
    assert (
        src.convertion_handler.handle_convertion(
            "1000", "milligram", "kilogram", "weight"
        )
        == "0.0010 kg"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "milligram", "ounce", "weight")
        == "0.0353 oz"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "milligram", "pound", "weight")
        == "0.0022 lb"
    )


def test_gram() -> None:
    assert (
        src.convertion_handler.handle_convertion("1000", "gram", "milligram", "weight")
        == "1000000.0000 mg"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "gram", "kilogram", "weight")
        == "1.0000 kg"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "gram", "ounce", "weight")
        == "35.2740 oz"
    )
    assert (
        src.convertion_handler.handle_convertion("1000", "gram", "pound", "weight")
        == "2.2046 lb"
    )


def test_kilogram() -> None:
    assert (
        src.convertion_handler.handle_convertion("1", "kilogram", "milligram", "weight")
        == "1000000.0000 mg"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilogram", "gram", "weight")
        == "1000.0000 g"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilogram", "ounce", "weight")
        == "35.2740 oz"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "kilogram", "pound", "weight")
        == "2.2046 lb"
    )


def test_ounce() -> None:
    assert (
        src.convertion_handler.handle_convertion("16", "ounce", "milligram", "weight")
        == "453592.3700 mg"
    )
    assert (
        src.convertion_handler.handle_convertion("16", "ounce", "gram", "weight")
        == "453.5924 g"
    )
    assert (
        src.convertion_handler.handle_convertion("16", "ounce", "kilogram", "weight")
        == "0.4536 kg"
    )
    assert (
        src.convertion_handler.handle_convertion("16", "ounce", "pound", "weight")
        == "1.0000 lb"
    )


def test_pound() -> None:
    assert (
        src.convertion_handler.handle_convertion("1", "pound", "milligram", "weight")
        == "453592.3700 mg"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "pound", "gram", "weight")
        == "453.5924 g"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "pound", "kilogram", "weight")
        == "0.4536 kg"
    )
    assert (
        src.convertion_handler.handle_convertion("1", "pound", "ounce", "weight")
        == "16.0000 oz"
    )


def test_empty_fields() -> None:
    assert (
        src.convertion_handler.handle_convertion("", "gram", "kilogram", "weight")
        == "All fields are required."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "", "kilogram", "weight")
        == "All fields are required."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "gram", "", "weight")
        == "All fields are required."
    )


def test_invalid_number() -> None:
    assert (
        src.convertion_handler.handle_convertion("abc", "gram", "kilogram", "weight")
        == "Value must be a number."
    )


def test_same_units() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "gram", "gram", "weight")
        == "You cannot convert the same units."
    )


def test_unsupported_units() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "stone", "kilogram", "weight")
        == "Unsupported unit."
    )
    assert (
        src.convertion_handler.handle_convertion("10", "gram", "carat", "weight")
        == "Unsupported unit."
    )


def test_invalid_category() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "gram", "kilogram", "speed")
        == "Invalid category."
    )


def test_units_not_matching_category() -> None:
    assert (
        src.convertion_handler.handle_convertion("10", "gram", "celsius", "weight")
        == "Invalid unit selection."
    )
    assert (
        src.convertion_handler.handle_convertion("100", "pound", "kelvin", "weight")
        == "Invalid unit selection."
    )
