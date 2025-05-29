from flask import Flask, render_template, request
from recipes.scraper import scrape_recipe

app = Flask(__name__)  # <- this must exist

@app.route("/", methods=["GET", "POST"])
def index():
    recipe = None
    if request.method == "POST":
        url = request.form["url"]
        recipe = scrape_recipe(url)
    return render_template("index.html", recipe=recipe)


