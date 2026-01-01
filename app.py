from flask import Flask, redirect, render_template, request, url_for
import src.temperatures
import src.weight
import src.length

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        action = request.form["action"]
        if action == "temperature":
            return redirect(url_for("temperature"))
        elif action == "length":
            return redirect(url_for("length"))
        elif action == "weight":
            return redirect(url_for("weight"))
    return render_template("index.html")


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    if request.method == "POST":
        value_str = request.form.get("value-to-convert")
        unit_from = request.form.get("unit-select-1")
        unit_to = request.form.get("unit-select-2")
        if not value_str or not unit_from or not unit_to:
            return "All fields are required."
        try:
            value_to_convert = float(value_str)
        except ValueError:
            return "Value must be a number."
        try:
            convert_from_unit = getattr(src.temperatures, unit_from.capitalize())
            convert_to_unit = getattr(src.temperatures, unit_to.capitalize())
        except AttributeError:
            return "Invalid unit selection."
        if unit_from.lower() == unit_to.lower():
            result = "You cannot convert the same units."
        else:
            result_value = convert_from_unit().convert_to(
                value_to_convert, convert_to_unit()
            )
            unit_symbols = {"celsius": "°C", "fahrenheit": "°F", "kelvin": "K"}
            unit_symbol = unit_symbols.get(unit_to.lower(), unit_to)
            result = f"{result_value:.2f} {unit_symbol}"
        return render_template("temperature.html", result=result)

    return render_template("temperature.html", result=None)


@app.route("/length", methods=["GET", "POST"])
def length():
    if request.method == "POST":
        value_str = request.form.get("value-to-convert")
        unit_from = request.form.get("unit-select-1")
        unit_to = request.form.get("unit-select-2")
        if not value_str or not unit_from or not unit_to:
            return "All fields are required."
        try:
            value_to_convert = float(value_str)
        except ValueError:
            return "Value must be a number."
        try:
            convert_from_unit = getattr(src.length, unit_from.capitalize())
            convert_to_unit = getattr(src.length, unit_to.capitalize())
        except AttributeError:
            return "Invalid unit selection."
        if unit_from.lower() == unit_to.lower():
            result = "You cannot convert the same units."
        else:
            result_value = convert_from_unit().convert_to(
                value_to_convert, convert_to_unit()
            )
            unit_symbols = {
                "milimeter": "mm",
                "centimeter": "cm",
                "meter": "m",
                "kilometer": "km",
                "inch": "in",
                "foot": "ft",
                "yard": "yd",
                "mile": "mi",
            }
            unit_symbol = unit_symbols.get(unit_to.lower(), unit_to)
            result = f"{result_value:.2f} {unit_symbol}"
        return render_template("length.html", result=result)

    return render_template("length.html", result=None)


@app.route("/weight", methods=["GET", "POST"])
def weight():
    if request.method == "POST":
        value_str = request.form.get("value-to-convert")
        unit_from = request.form.get("unit-select-1")
        unit_to = request.form.get("unit-select-2")
        if not value_str or not unit_from or not unit_to:
            return "All fields are required."
        try:
            value_to_convert = float(value_str)
        except ValueError:
            return "Value must be a number."
        try:
            convert_from_unit = getattr(src.weight, unit_from.capitalize())
            convert_to_unit = getattr(src.weight, unit_to.capitalize())
        except AttributeError:
            return "Invalid unit selection."
        if unit_from.lower() == unit_to.lower():
            result = "You cannot convert the same units."
        else:
            result_value = convert_from_unit().convert_to(
                value_to_convert, convert_to_unit()
            )

            unit_symbols = {
                "miligram": "mg",
                "gram": "g",
                "kilogram": "kg",
                "ounce": "oz",
                "pound": "lb",
            }
            unit_symbol = unit_symbols.get(unit_to.lower(), unit_to)
            result = f"{result_value:.2f} {unit_symbol}"
        return render_template("weight.html", result=result)

    return render_template("weight.html", result=None)


if __name__ == "__main__":
    app.run(debug=True)
