#!/usr/bin/env python3
"""Module of session authenticating views.
"""
from os import getenv

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Authenticates a user using session authentication"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({'error': 'email missing'}), 400
    if password is None or password == '':
        return jsonify({'error': 'password missing'}), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({'error': 'no user found for this email'}), 404
    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    cookie_name = getenv('SESSION_NAME')
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)
    return response
