from flask import Flask, request
app = Flask(__name__)

step = 0

# The Fibonacci function
def fibo(index: int):
    """
    Calculating the fibonacci numbers
    """
    if index < 1:
        return 0
    elif index == 1:
        return 1
    else:
        return fibo(index-1) + fibo(index-2)

# The actual route
@app.route("/next")
def next_fibo():
    """
    Sending the fibonacci number to the user, telling him if
    he uses improper input
    """
    try:
        global step
        step = step + 1
        return str(fibo(step))
    except ValueError:
        return "Please use a number as the 'n' argument"

@app.route("/prev")
def prev_fibo():
    """
    Sending the fibonacci number to the user, telling him if
    he uses improper input
    """
    try:
        global step
        step = step - 1
        return str(fibo(step))
    except ValueError:
        return "Please use a number as the 'n' argument"

@app.route("/current")
def current_fibo():
    """
    Sending the fibonacci number to the user, telling him if
    he uses improper input
    """
    try:
        return str(fibo(step))
    except ValueError:
        return "Please use a number as the 'n' argument"
