from core import app
from flask import render_template

@app.route('/')
def index():
    greeting="Hello there, Ace"
    return render_template("base.html", greet=greeting)
