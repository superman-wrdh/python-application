# -*- encoding: utf-8 -*-
from flask import Flask, request, Response
from flask import render_template, redirect, url_for, jsonify
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/search", methods=["POST", "GET"])
def search():
    keyword = request.form.get("keyword", type=str, default=None)
    print("词汇", keyword)
    item = request.form.get("item", type=str, default=None)
    if keyword is not None:
        d = query(keyword, item)
        count = len(d)
        return render_template("result.html", data=d, keyword=keyword,count=count)
    else:
        return render_template('index.html')


@app.route("/detail/<uid>", methods=["POST", "GET"])
def detail(uid):
    if uid is not None:
        from query import get_by_id
        r = get_by_id(id=uid)
        return render_template("detail.html", data=r)
    else:
        return render_template('index.html')


def query(keyword, item=None):
    from query import query_by_name
    df = query_by_name(keyword)
    # if len(df) > 100:
    #     df = df.loc[0:100]
    df = df.fillna('-')
    return df.to_dict(orient='records')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True)
