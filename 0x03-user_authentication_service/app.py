#!/usr/bin/env python3
""" Basic Flask app
"""
from auth import Auth
from flask import Flask, jsonify, request


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
        user = AUTH.register_user(email=email, password=password)
        return jsonify(email=user.email, message='user created')
    except ValueError:
        return jsonify(message='email already registered'), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
