import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from fuctions import *
import validators

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_url = request.form.get("url")
        key = generate_random_string(9)
        user_url = check_url(user_url)
        both = str(user_url) + key
        if validators.url(user_url):
            if not check_if_id_exists(user_url):
                yy = check_if_id_exists(user_url)
                print(f"this is result from check funtion {yy}")
                with sqlite3.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO links (link, id) VALUES (?, ?)",(user_url, key))
                    con.commit()
                cur.execute("SELECT * FROM links")
                print(cur.fetchall())
                con.close()
            # return a dictionary and parse through it in order to generate a hyper reference in html

                return render_template("index.html", new_link = user_url, short_link = key)
            else:
                previous_id = ''.join(return_id(user_url))
                msg = ''.join(return_link(previous_id))
                return render_template("index.html", exist = msg, key = previous_id)
        if not validators.url(user_url):
            both = "That is not a valid link!"
            return render_template("index.html", result = both)
    return render_template("index.html")
