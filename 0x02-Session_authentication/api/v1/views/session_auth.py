#!/usr/bin/env python3
"""Module of session authenticating views.
"""
import os
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=False)
def create_session() -> str:
    """Create a new session for a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({'error': 'email missing'}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({'error': 'no user found for this email'}), 404

    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401

    session_id = auth.create_session(user.id)
    user_dict = user.to_json()
    response = jsonify(user_dict)
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response
