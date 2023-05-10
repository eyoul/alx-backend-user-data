#!/usr/bin/env python3
"""return Hash password
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

import bcrypt


def _hash_password(password: str) -> bcrypt:
    """Hashes the given password using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with the given email and password
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = self._hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user
