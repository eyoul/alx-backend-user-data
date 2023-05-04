#!/usr/bin/env python3
""" Module of Users views
"""
import os
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth

@app_views.route('/auth_session/login', methods=['POST', 'OPTIONS'], strict_slashes=False)
@app_views.route('/auth_session/login/', methods=['POST', 'OPTIONS'], strict_slashes=False)
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
    if not user_list:
        return jsonify({ "error": "no user found for this email" }), 404

    user = user_list[0]
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(auth.session_cookie_name, session_id)
    return response, 200
