#!/usr/bin/env python3
""" Module of Users views
"""
from os import getenv

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """POST /api/v1/auth_session/login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({ "error": "email missing" }), 400
    if password is None or password == '':
        return jsonify({ "error": "password missing" }), 400

    user_list = User.search({'email': email})
    if len(user_list):
        return jsonify({ "error": "no user found for this email" }), 404

    user = user_list[0]
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    cookie_name = getenv('SESSION_NAME')
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)
    return response
