import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from gen import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        key = generate_random_string(9)
        both = str(url) + key
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO links (link, id) VALUES (?, ?)",(url, key))
            con.commit()
        con.close()
        return render_template("index.html", result = both)
    return render_template("index.html")
