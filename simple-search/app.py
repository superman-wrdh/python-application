# -*- encoding: utf-8 -*-
from flask import Flask, request, Response
from flask import render_template, redirect, url_for,jsonify
from flask_cors import *
import os
from torrent import search as ts
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def search():
    w = request.form.get("w", type=str, default=None)
    if w:
        d = ts(w, 10, 0)
        print("-------")
        print(d)
        print("-------")
        return render_template("result.html", data=d, word=w)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)



