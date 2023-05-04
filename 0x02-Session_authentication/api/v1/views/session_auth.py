#!/usr/bin/env python3
""" Module of Session auth views
"""
import os
from api.v1.views import app_views
from api.v1.app import auth
from typing import Tuple
from flask import abort, jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """Handle session-based authentication login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        abort(400, {'error': 'email missing'})
    if not password:
        abort(400, {'error': 'password missing'})

    user = User.search({'email': email})
    if not user:
        abort(404, {'error': 'no user found for this email'})

    if not user.is_valid_password(password):
        abort(401, {'error': 'wrong password'})

    session_id = auth.create_session(user.id)
    user_dict = user.to_json()
    response = jsonify(user_dict)
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response
