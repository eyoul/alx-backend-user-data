#!/usr/bin/env python3
"""return Hash password
"""
from db import DB
from user import User
import hashlib


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password):
        """Hashes a password using SHA-256 algorithm"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, email, password):
        """Registers a new user with the given email and password"""

        user = self._db.get_user_by_email(email)
        if user is not None:
            raise ValueError("User {} already exists".format(email))

        hashed_password = self._hash_password(password)
        user = User(email, hashed_password)
        self._db.save_user(user)

        return user
