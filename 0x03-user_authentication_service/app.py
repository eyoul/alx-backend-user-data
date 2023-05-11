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


@app.route('/', methods=['GET'])
def index() -> str:
    """
    Return json response
    {"message": "Bienvenue"}
    """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'])
def users() -> str:
    """
    Args:
        email (str): new user's email address
        password (str): new user's password
    Return:
        Register new users
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """
    Args:
        email (str): new user's email address
        password (str): new user's password
    Return:
        LogIn users
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({'email': f'{email}', 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
