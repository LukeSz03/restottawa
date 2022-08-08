from flask import Flask, render_template, redirect, url_for
from forms import TypeForm, FastFoodForm, RestaurantForm
from scraper import search

app = Flask(__name__)
app.secret_key = "secret_key"


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


@app.route("/restaurant", methods=["GET", "POST"])
def rest():
    form = RestaurantForm()

    if form.validate_on_submit():
        print("ye")

    return render_template("restaurant.html", form=form)


@app.route("/fast_food", methods=["GET", "POST"])
def fast_food():

    form = FastFoodForm()

    if form.validate_on_submit():
        if form.mcdonalds.data:
            search("McDonald's")
        elif form.wendys.data:
            search("Wendy's")
        elif form.harveys.data:
            search("Harvey's")
        elif form.burger_king.data:
            search("Burger King")
        elif form.aw.data:
            search("A&W")

    return render_template("fast_food.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
