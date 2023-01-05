import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        if not name:
            message = "Name Required"

        elif not month:
            message = "Month Required"

        elif not day:
            message = "Date Required"

        elif int(month) < 1 or int(month) > 12:
            message = "Enter a month between 1 to 12"

        elif (int(month) in [1,3,5,7,8,10,12] and (int(day) > 31 or int(day) < 1)) or (int(month) in [4,6,9,11] and (int(day) >30 or int(day) < 1)) or (int(month) == 2 and (int(day) > 29 or int(day) < 1)):
            message = "Enter a valid date"

        else:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        birthday_list = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", message = message, birthday_list = birthday_list)

    else:

        birthday_list = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthday_list = birthday_list)


