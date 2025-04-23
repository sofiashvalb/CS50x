import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        user_id = session["user_id"]
        transactions_db = db.execute(
            "SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id = ? GROUP BY symbol",
            user_id,
        )
        cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = cash_db[0]["cash"]

        total_value = cash

        for stock in transactions_db:
            quote = lookup(stock["symbol"])
            stock["price"] = quote["price"]
            stock["value"] = stock["price"] * stock["shares"]
            total_value += stock["value"]

        return render_template(
            "index.html", transactions=transactions_db, cash=cash, sum=total_value
        )

    else:
        user_id = session["user_id"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash_int = user_cash[0]["cash"]

        if not request.form.get("cash").isdigit():
            return apology("Must enter a number")

        if request.form.get("cash"):
            new_cash = user_cash_int + int(request.form.get("cash"))
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)

        return redirect("/")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("You need to enter a symbol", 400)

        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        if stock == None:
            return apology("Invalid symbol", 400)

        if not request.form.get("shares").isdigit():
            return apology("Must enter an integer")

        shares = int(request.form.get("shares"))
        if shares == None or shares <= 0 or not shares.is_integer():
            return apology(
                "Please make sure that the shares you are buying are more than 0"
            )

        transaction = shares * (stock["price"])
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = user_cash_db[0]["cash"]

        if transaction > user_cash:
            return apology(
                "Sorry, you cannot afford the number of shares at the current price"
            )

        update_cash = user_cash - transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id)

        #'user_id' INTEGER, 'symbol' TEXT, 'shares' INTEGER, 'price' REAL, 'date' DATETIME);
        date = datetime.datetime.now()
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
            user_id,
            stock["symbol"],
            shares,
            stock["price"],
            date,
        )

        flash("Bought!")

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute(
        "SELECT * FROM transactions WHERE user_id = ?", user_id
    )

    return render_template("history.html", transactions=transactions_db)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

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
        if not request.form.get("symbol"):
            return apology("You need to enter a symbol", 400)

        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if quote == None:
            return apology("Invalid symbol", 400)

        else:
            name = quote["symbol"]
            price = usd(quote["price"])
            symbol = quote["symbol"]
            return render_template("quoted.html", name=name, price=price, symbol=symbol)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("The password does not matche the confirmation", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Check if username exists and password is correct
        if len(rows) != 0:
            return apology("This username already exsits", 400)

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password")),
        )

        # generate a new on after insertion
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        symbols_db = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            user_id,
        )

        return render_template(
            "sell.html", symbols=[row["symbol"] for row in symbols_db]
        )

    else:
        user_id = session["user_id"]
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("You need to enter a symbol", 400)

        stock = lookup(symbol)

        if stock == None:
            return apology("Invalid symbol", 400)

        shares = request.form.get("shares")

        if not shares.isnumeric():
            return apology("Shares must be a number")

        shares = int(shares)

        if not shares:
            return apology("You need to enter a number")

        if shares <= 0:
            return apology("Share not allowed")

        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = user_cash_db[0]["cash"]

        user_shares_db = db.execute(
            "SELECT SUM(shares) AS shares FROM transactions WHERE user_id = ? and symbol = ? GROUP BY symbol",
            user_id,
            symbol,
        )
        user_shares = user_shares_db[0]["shares"]

        if int(user_shares) <= 0 or int(user_shares) < shares:
            return apology("You don't have enough shares")

        elif 0 < shares <= int(user_shares):
            transaction_value = shares * stock["price"]
            update_cash = user_cash + transaction_value
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?", float(update_cash), user_id
            )

            #'user_id' INTEGER, 'symbol' TEXT, 'shares' INTEGER, 'price' REAL, 'date' DATETIME);
            date = datetime.datetime.now()
            db.execute(
                "INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
                user_id,
                stock["symbol"],
                shares * (-1),
                float(stock["price"]),
                date,
            )

            flash("Sold!")
            return redirect("/")


@app.route("/change", methods=["GET", "POST"])
@login_required
def change():
    """Change user's password"""
    user_id = session["user_id"]

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide old password", 400)

        elif not request.form.get("npassword"):
            return apology("must provide new password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        elif request.form.get("npassword") != request.form.get("confirmation"):
            return apology("The new password does not match the confirmation", 400)

        new_pass = generate_password_hash(request.form.get("npassword"))
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        # Check if username exists and password is correct
        if len(rows) != 1 and not (
            check_password_hash(rows[0]["hash"]),
            request.form.get("password"),
        ):
            return apology("This username doesn't exsits/ password doesn't match", 400)

        db.execute(
            "UPDATE users SET hash = ? WHERE id = ?",
            generate_password_hash(request.form.get("npassword")),
            user_id,
        )

        # generate a new on after insertion
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("change.html")
