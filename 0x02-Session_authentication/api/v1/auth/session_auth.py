#!/usr/bin/env python3
"""Basic API authentication.
"""
import os
import uuid
from models.user import User
from typing import Tuple, TypeVar
from .auth import Auth


class SessionAuth(Auth):
    """Creating a class Session authentication
    """
    def __init__(self):
        self.user_id_by_session_id = {}

    def create_session(self, user_id: str) -> str:
        """Creating an session instance method
        """
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Creating an user_id_for_session_id method
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
    def current_user(self, request=None) -> str:
        """Return a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_for_session_id(session_id)
            if user_id:
                return User.get(user_id)
        return None
