#!/usr/bin/env python3
""" Basic Flask app
"""
from auth import Auth
from flask import (
    Flask,
    request,
    abort,
    jsonify
)


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Return json response
    {"message": "Bienvenue"}
    """
    return jsonify(message='Bienvenue')


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """
    Args:
        email (str): new user's email address
        password (str): new user's password
    Return:
        Register new users
    """
    try:
        email = request.form['email']
        password = request.form['password']
        user = AUTH.register_user(email=email, password=password)
        return jsonify(email=user.email, message='user created')
    except ValueError:
        return jsonify(message='email already registered'), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Args:
        email (str): new user's email address
        password (str): new user's password
    Return:
        LogIn users
    """
    try:
        email = request.form['email']
        password = request.form['password']
        if not AUTH.valid_login(email=email, password=password):
            session_id = AUTH.create_session(email=email)
            response = jsonify(email=email, message='logged in')
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(401)
    except Exception:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
