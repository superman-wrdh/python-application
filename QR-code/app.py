# -*- encoding: utf-8 -*-
from flask import Flask, request, Response,send_file
from flask import render_template, redirect, url_for,jsonify
from flask_cors import *
from io import BytesIO
import base64
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
    # if w or len(w) == 0:
    #     d = ts(w, 10, 0)
    #     return render_template("result.html", data=d, word=w)
    # else:
    #     return render_template('index.html')


@app.route("/qrcode/<code>")
def qrcode(code):
    byte_io = BytesIO()
    import qr_util
    img = qr_util.make_qr(code)
    img.save(byte_io, "PNG")
    byte_io.seek(0)
    resp = Response(byte_io, mimetype="image/png")
    return resp


@app.route("/qrcode/base64/<code>")
def qrcode_base64(code):
    byte_io = BytesIO()
    import qr_util
    img = qr_util.make_qr(code)
    img.save(byte_io, "PNG")
    byte_io.seek(0)
    resp = Response(byte_io, mimetype="image/png")
    v = ""
    output = BytesIO()
    b = base64.encode(byte_io, output)
    return jsonify({
        "base64": str(b)
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3012, threaded=True)



