#!/usr/bin/env python3
"""Basic API authentication.
"""
import os
import uuid
from typing import Tuple, TypeVar
from .auth import Auth


class SessionAuth(Auth):
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.__class__.user_id_by_session_id[session_id] = user_id
        return session_id
