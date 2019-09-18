from functools import wraps
from flask import Flask, request, Response
from flask import render_template, redirect, url_for, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

allow_user = {
    "123456": {"user_name": "superman", "role": "admin"},
    "111111": {"user_name": "superman", "role": "user"}
}


def auth(role=None):
    def _auth(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            user_obj = allow_user.get(token)
            if user_obj is None:
                d = {"message": "forbid"}
                return Response(json.dumps(d), status=403, mimetype="application/json")
            user_role = user_obj.get("role")
            allow = False
            if isinstance(role, str):
                if role == user_role:
                    allow = True
            if isinstance(role, list):
                if user_role in role:
                    allow = True
            if not allow:
                d = {"message": "auth failed"}
                return Response(json.dumps(d), status=401, mimetype="application/json")
            request.current_user = user_obj
            return func(*args, **kwargs)

        return wrapper

    return _auth


@app.route("/", methods=["GET", "POST"])
def temp():
    return "index"


@app.route("/upload", methods=["POST"])
@auth(role="admin")
def upload():
    f = request.files['file']
    basepath = os.path.dirname(__file__)
    upload_path = os.path.join(basepath, "static", "uploads", f.filename)
    f.save(upload_path)
    return jsonify({"file": f.filename})


@app.route("/img/<imgid>")
@auth(role=["user", "admin"])
def get_img(imgid):
    basepath = os.path.dirname(__file__)
    image = open(os.path.join(basepath, "static", "uploads", str(imgid)), "rb")
    resp = Response(image, mimetype="image/jpeg")
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, threaded=True)
