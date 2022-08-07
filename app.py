from ast import Sub
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField
import scraper

app = Flask(__name__)
app.secret_key = "asdasd"

# Forms
class TypeForm(FlaskForm):
    restaurant = SubmitField()
    fast_food = SubmitField()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/type", methods=["GET", "POST"])
def type():
    form = TypeForm()

    if form.validate_on_submit():
        if form.restaurant.data:
            return redirect(url_for("rest"))
        elif form.fast_food.data:
            return redirect(url_for("fast_food"))

    return render_template("type.html", form=form)


@app.route("/restaurant")
def rest():
    return render_template("restaurant.html")


@app.route("/fast_food")
def fast_food():
    return render_template("fast_food.html")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html")


@app.route("/cost")
def cost():
    return render_template("cost.html")


if __name__ == "__main__":
    app.run(debug=True)
