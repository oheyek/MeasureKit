from flask import Flask, redirect, render_template, request, url_for

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


@app.route("/temperature")
def temperature():
    return "<p>temperature endpoint</p>"


@app.route("/length")
def length():
    return "<p>length endpoint</p>"


@app.route("/weight")
def weight():
    return "<p>weight endpoint</p>"


if __name__ == "__main__":
    app.run(debug=True)
