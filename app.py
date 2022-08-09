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
        if form.chinese.data:
            search("chinese restaurants")
        elif form.french.data:
            search("french restaurants")
        elif form.hamburger.data:
            search("hamburger restaurants")
        elif form.indian.data:
            search("indian restaurants")
        elif form.italian.data:
            search("italian restaurants")
        elif form.japanese.data:
            search("japanese restaurants")
        elif form.mexican.data:
            search("mexican restaurants")
        elif form.middle_eastern.data:
            search("middle eastern restaurants")
        elif form.pizza.data:
            search("pizza restaurants")
        elif form.seafood.data:
            search("seafood restaurants")
        elif form.sushi.data:
            search("sushi restaurants")
        elif form.thai.data:
            search("thair restaurants")
        elif form.vietnamese.data:
            search("vietnamese restaurants")

        return redirect(url_for("result"))

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


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
