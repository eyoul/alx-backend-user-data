#!/usr/bin/env python3
"""return Hash password
"""
import bcrypt

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes the given password using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with the given email and password
        """
        if self._db.get_user_by_email(email):
            raise ValueError(f"User {email} already exists")

        hashed_password = self._hash_password(password)
        user = self._db.create_user(email, hashed_password) 
        return user
