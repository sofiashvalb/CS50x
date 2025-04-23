from cs50 import SQL
from flask import Flask, render_template, request
from helpers import random_string
import random

app = Flask(__name__)

db = SQL("sqlite:///history.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
       page = request.form.get("page")

       try:
            page = int(page)
       except ValueError:
            return render_template("index.html", random_string="Try inserting an integer")

       if page < 0:
          return render_template("index.html", random_string="Try inserting positive integer!")

       db.execute("INSERT INTO history (page) VALUES (?);", page)
       print(search)

       #lets me set the random page number to the random string to always access it there again and again
       random.seed(page)

    string = random_string(1000)
    #returns a list of all the rows as dictionaries
    rows = db.execute("SELECT * FROM history;")
    return render_template("index.html", random_string=string, history=rows)
