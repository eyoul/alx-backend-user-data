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
        """Register a new user.

        Args:
            email (str): The user's email
            password (str): The user's password

        Returns:
            User: The newly registered user object

        Raises:
            ValueError: If a user with the given email already exists
        """
        if self._db.get_user_by_email(email):
            raise ValueError(f'User {email} already exists')

        hashed_password = self._hash_password(password)
        user = User(email, hashed_password)
        self._db.add_user(user)
        return user