"""
@brief Flask application for unit conversions.
"""

from flask import Flask, redirect, render_template, request, url_for
import src.convertion_handler

app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    """
    @brief Main route handler for the application.

    @return Rendered template or redirect.
    """
    if request.method == "POST":
        action: str = request.form["action"]
        if action == "temperature":
            return redirect(url_for("temperature"))
        elif action == "length":
            return redirect(url_for("length"))
        elif action == "weight":
            return redirect(url_for("weight"))
    return render_template("index.html")


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    """
    @brief Handle temperature conversion page.

    @return Rendered temperature template with result.
    """
    if request.method == "POST":
        value_str: str = request.form.get("value-to-convert") or ""
        unit_from: str = request.form.get("unit-select-1") or ""
        unit_to: str = request.form.get("unit-select-2") or ""
        result: str = src.convertion_handler.handle_convertion(
            value_str, unit_from, unit_to, "temperature"
        )
        return render_template("temperature.html", result=result)

    return render_template("temperature.html", result=None)


@app.route("/length", methods=["GET", "POST"])
def length():
    """
    @brief Handle length conversion page.

    @return Rendered length template with result.
    """
    if request.method == "POST":
        value_str: str = request.form.get("value-to-convert") or ""
        unit_from: str = request.form.get("unit-select-1") or ""
        unit_to: str = request.form.get("unit-select-2") or ""
        result: str = src.convertion_handler.handle_convertion(
            value_str, unit_from, unit_to, "length"
        )
        return render_template("length.html", result=result)

    return render_template("length.html", result=None)


@app.route("/weight", methods=["GET", "POST"])
def weight():
    """
    @brief Handle weight conversion page.

    @return Rendered weight template with result.
    """
    if request.method == "POST":
        value_str: str = request.form.get("value-to-convert") or ""
        unit_from: str = request.form.get("unit-select-1") or ""
        unit_to: str = request.form.get("unit-select-2") or ""
        result: str = src.convertion_handler.handle_convertion(
            value_str, unit_from, unit_to, "weight"
        )
        return render_template("weight.html", result=result)

    return render_template("weight.html", result=None)


if __name__ == "__main__":
    app.run(debug=True)
