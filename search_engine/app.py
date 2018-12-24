# -*- encoding: utf-8 -*-
from flask import Flask, request, Response
from flask import render_template, redirect, url_for, jsonify
from flask_cors import CORS
from baidu import search as ts
from qihu import search as tq
from es import search_by_name,get_by_id

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def search():
    w = request.form.get("w", type=str, default=None)
    content = []
    if w or len(w) == 0:
        try:
            d_baidu = ts(w)
            content.extend(d_baidu)
        except Exception as e:
            pass
        try:
            d_360 = tq(w)
            content.extend(d_360)
        except Exception as e:
            pass
        person = search_by_name(w)
        return render_template("result.html", data=content, word=w, person=person)
    else:
        return render_template('index.html')


@app.route("/detail/<uid>", methods=["POST", "GET"])
def detail(uid):
    if uid is not None:
        r = get_by_id(id=uid)
        return render_template("detail.html", data=r)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3010, threaded=True)
