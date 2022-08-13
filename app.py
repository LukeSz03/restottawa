from flask import Flask, render_template, redirect, url_for
from forms import TypeForm, FastFoodForm, RestaurantForm
from search_api import search
import os

from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/type", methods=["GET", "POST"])
def type():
    form = TypeForm()

    if form.validate_on_submit():
        if form.restaurant.data:
            return redirect(url_for("restaurants"))
        elif form.fast_food.data:
            return redirect(url_for("fast_foods"))

    return render_template("type.html", form=form)


@app.route("/restaurants", methods=["GET", "POST"])
def restaurants():
    form = RestaurantForm()

    if form.validate_on_submit():
        if form.chinese.data:
            restaurants = search("chineserestaurants")
        elif form.french.data:
            restaurants = search("frenchrestaurants")
        elif form.hamburger.data:
            restaurants = search("hamburgerrestaurants")
        elif form.indian.data:
            restaurants = search("indianrestaurants")
        elif form.italian.data:
            restaurants = search("italianrestaurants")
        elif form.japanese.data:
            restaurants = search("japaneserestaurants")
        elif form.mexican.data:
            restaurants = search("mexicanrestaurants")
        elif form.middle_eastern.data:
            restaurants = search("middleeasternrestaurants")
        elif form.pizza.data:
            restaurants = search("pizzarestaurants")
        elif form.seafood.data:
            restaurants = search("seafoodrestaurants")
        elif form.sushi.data:
            restaurants = search("sushirestaurants")
        elif form.thai.data:
            restaurants = search("thairestaurants")
        elif form.vietnamese.data:
            restaurants = search("vietnameserestaurants")
        return render_template("results.html", restaurants=restaurants)

    return render_template("restaurants.html", form=form)


@app.route("/fast_foods", methods=["GET", "POST"])
def fast_foods():
    form = FastFoodForm()

    if form.validate_on_submit():
        if form.mcdonalds.data:
            restaurants = search("McDonald's")
        elif form.wendys.data:
            restaurants = search("Wendy's")
        elif form.harveys.data:
            restaurants = search("Harvey's")
        elif form.burger_king.data:
            restaurants = search("Burger King")
        elif form.aw.data:
            restaurants = search("AWCanada")
        return render_template("results.html", restaurants=restaurants)

    return render_template("fast_foods.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
