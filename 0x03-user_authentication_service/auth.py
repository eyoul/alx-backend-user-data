#!/usr/bin/env python3
"""return Hash password
"""
from db import DB
from user import User
from hashlib import sha256


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        # Check if user already exists
        if self._db.get_user_by_email(email):
            raise ValueError(f"User {email} already exists")

        # Hash password
        hashed_password = self._hash_password(password)

        # Create user object
        user = User(email, hashed_password)

        # Save user to database
        self._db.save_user(user)

        return user

    def _hash_password(self, password: str) -> str:
        """Hashes password using sha256."""
        return sha256(password.encode()).hexdigest()
