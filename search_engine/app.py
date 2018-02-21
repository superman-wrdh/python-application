# -*- encoding: utf-8 -*-
from flask import Flask, request, Response
from flask import render_template, redirect, url_for,jsonify
from flask_cors import *
from baidu import search as ts
from qihu import search as tq
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def search():
    w = request.form.get("w", type=str, default=None)
    if w or len(w) == 0:
        d_baidu = ts(w)
        d_360 = tq(w)
        d_baidu.extend(d_360)
        return render_template("result.html", data=d_baidu, word=w)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3010)



