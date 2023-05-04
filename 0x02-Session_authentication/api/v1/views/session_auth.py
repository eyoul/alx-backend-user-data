#!/usr/bin/env python3
"""Module of session authenticating views.
"""
import os
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Create a new session for a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({'error': 'email missing'}), 400
    if password is None or password == '':
        return jsonify({'error': 'password missing'}), 400

    user = User.search({'email': email})
    if len(user) == 0:
        return jsonify({'error': 'no user found for this email'}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    user_dict = user.to_json()
    response = jsonify(user_dict)
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response
