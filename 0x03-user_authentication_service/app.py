#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """POST /user
    Return: register user email
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
