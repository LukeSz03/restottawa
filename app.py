from flask import Flask, render_template
import scraper

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/type")
def type():
    return render_template("type.html")


@app.route("/restaurant")
def rest():
    return render_template("restaurant.html")


@app.route("/fast_food")
def fast_food():
    return render_template("fast_food.html")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html")


if __name__ == "__main__":
    app.run(debug=True)
