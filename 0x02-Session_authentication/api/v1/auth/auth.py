#!/usr/bin/env python3
"""API authentication.
"""
import os
import re
from flask import request
from typing import List, TypeVar
from .auth import SessionAuth


class Auth:
    """Returns Autentication for now.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header
        from the Flask request object.
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None for now.
        """
        return None


    def __init__(self):

        self.session_auth = SessionAuth()
        self.session_name = os.environ.get("SESSION_NAME", "_my_session_id")
  
    def session_cookie(self, request=None):
        if request is None:
            return None
        return request.cookies.get(self.session_name, None)