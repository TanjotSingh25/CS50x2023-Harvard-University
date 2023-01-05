import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    user = user[0]
    purchases = db.execute("SELECT * FROM user_share_data WHERE id = ?", session["user_id"])
    user_shares = {}
    for share in purchases:
        if share["symbol"] not in user_shares:
            user_shares[share["symbol"]] = share["number"]
        else:
            user_shares[share["symbol"]] += share["number"]
    shares = []
    sumtotal = 0
    for share in user_shares:
        if user_shares[share] <= 0:
            continue
        share_info = lookup(share)
        dict = {}
        dict["name"] = share_info["name"]
        dict["symbol"] = share
        dict["number"] = user_shares[share]
        dict["price"] = share_info["price"]
        dict["total"] = round(dict["number"] * dict["price"], 3)
        sumtotal += dict["total"]
        shares.append(dict)
    sumtotal += user["cash"]
    return render_template("index.html", shares=shares, total=int(user["cash"]), sumtotal=int(sumtotal))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        number = request.form.get("shares")

        if not symbol:
            return apology("Symbol required")
        elif not number:
            return apology("Number of Shares required")

        if not number.isdigit():
            return apology("must provide valid number of shares (integer)")
        if float(number) <= 0:
            return apology("must provide valid number of shares (integer)")

        stock = lookup(symbol)
        number = int(number)

        if not stock:
            return apology("Enter valid Symbol")

        now = datetime.now()
        time = now.strftime("%B %d, %Y %H:%M")

        users = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        if users[0]["cash"] < stock["price"]*number:
            return apology("Not enough Cash to buy")
        else:
            users[0]["cash"] = users[0]["cash"] - stock["price"]*number
            db.execute("INSERT INTO user_share_data (id, name, symbol, number, price, time) VALUES (?, ?, ?, ?, ?, ?)",
                       session["user_id"], stock["name"], stock["symbol"], number, stock["price"], time)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", users[0]["cash"], session["user_id"])

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    purchases = db.execute("SELECT * FROM user_share_data WHERE id = ?", session["user_id"])
    for item in purchases:
        if item["number"] < 0:
            item["buy_or_sell"] = "Sell"
            item["number"] = -1 * item["number"]
        else:
            item["buy_or_sell"] = "Buy"
    money_history = db.execute("SELECT * FROM money_transactions WHERE id = ?", session["user_id"])
    return render_template("history.html", purchases=purchases, money_history=money_history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Symbol required")
        stock = lookup(symbol)
        if not stock:
            return apology("Enter valid Symbol")
        stock["price"] = usd(stock["price"])
        return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        elif not confirm_password:
            return apology("must fill confirm password", 400)

        elif password != confirm_password:
            return apology("password doesnot match confirm password", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 0:
            return apology("username already exists", 400)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    purchases = db.execute("SELECT * FROM user_share_data WHERE id = ?", session["user_id"])
    shares = {}
    for share in purchases:
        if share["symbol"] not in shares:
            shares[share["symbol"]] = share["number"]
        else:
            shares[share["symbol"]] += share["number"]
    temp = {}
    for share in shares:
        if shares[share] > 0:
            temp[share] = shares[share]
    shares = temp
    if request.method == "POST":
        symbol = request.form.get("symbol")
        number = request.form.get("shares")
        if not symbol:
            return apology("Symbol required")
        elif not number:
            return apology("Number of shares required")

        number = int(number)
        if number > shares[symbol]:
            return apology("Not enough shares")

        money = number * lookup(symbol)["price"]
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        user = user[0]
        now = datetime.now()
        time = now.strftime("%B %d, %Y %H:%M")
        stock = lookup(symbol)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", money+user["cash"], session["user_id"])
        db.execute("INSERT INTO user_share_data (id, name, symbol, number, price, time) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], stock["name"], stock["symbol"], -1*number, stock["price"], time)
        return redirect("/")
    else:
        return render_template("sell.html", shares=shares)


@app.route("/addMoney", methods=["GET", "POST"])
@login_required
def addMoney():
    if request.method == "POST":
        amount = request.form.get("amount")
        if not amount:
            return apology("Amount required")
        amount = float(amount)
        if amount <= 0.0:
            return apology("Enter a valid amount")
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        user = user[0]
        now = datetime.now()
        time = now.strftime("%B %d, %Y %H:%M")
        db.execute("UPDATE users SET cash = ? WHERE id = ?", amount+user["cash"], session["user_id"])
        db.execute("INSERT INTO money_transactions (id, amount, time) VALUES (?, ?, ?)", session["user_id"], amount, time)
        return redirect("/")
    else:
        return render_template("addMoney.html")
