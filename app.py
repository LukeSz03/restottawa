from flask import Flask, render_template, redirect, url_for
from forms import TypeForm, FastFoodForm, RestaurantForm
from search_api import search

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
        if form.chinese.data:
            search("chineserestaurants")
        elif form.french.data:
            search("frenchrestaurants")
        elif form.hamburger.data:
            search("hamburgerrestaurants")
        elif form.indian.data:
            search("indianrestaurants")
        elif form.italian.data:
            search("italianrestaurants")
        elif form.japanese.data:
            search("japaneserestaurants")
        elif form.mexican.data:
            search("mexicanrestaurants")
        elif form.middle_eastern.data:
            search("middleeasternrestaurants")
        elif form.pizza.data:
            search("pizzarestaurants")
        elif form.seafood.data:
            search("seafoodrestaurants")
        elif form.sushi.data:
            search("sushirestaurants")
        elif form.thai.data:
            search("thairestaurants")
        elif form.vietnamese.data:
            search("vietnameserestaurants")

        return redirect(url_for("results"))

    return render_template("restaurant.html", form=form)


@app.route("/fast_food", methods=["GET", "POST"])
def fast_food():

    form = FastFoodForm()

    if form.validate_on_submit():
        if form.mcdonalds.data:
            restaurants = search("McDonald's")
            return render_template("results.html", restaurants=restaurants)
        elif form.wendys.data:
            search("Wendy's")
        elif form.harveys.data:
            search("Harvey's")
        elif form.burger_king.data:
            search("Burger King")
        elif form.aw.data:
            search("A&W")

    return render_template("fast_food.html", form=form)


@app.route("/results", methods=["GET", "POST"])
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
