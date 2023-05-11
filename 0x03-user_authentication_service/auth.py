#!/usr/bin/env python3
"""return Hash password
"""
from uuid import uuid4
import uuid
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


def _hash_password(password: str) -> bytes:
    """Hashes the given password using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """
    Generates a new UUID and returns it as a string.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user and return a user object
        Args:
            email (str): new user's email address
            password (str): new user's password
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a user's login credentials and return True if they are correct
        or False if they are not
        Return:
            True if credentials are correct,
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_password = user.hashed_password
        passwd = password.encode("utf-8")
        return bcrypt.checkpw(passwd, user_password)

    def create_session(self, email: str) -> Union[None, str]:
        """
        Return: the session ID.
        Corresponding to the email, generate a
        new UUID and store it in the database
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id):
        """
        Return: the corresponding User or None
        If the session ID is None or no user is found,
        return None. Otherwise return the corresponding user.
        """
        if session_id is None:
            return None
        user = self._db.query(User).filter_by(session_id=session_id).first()
        return user
