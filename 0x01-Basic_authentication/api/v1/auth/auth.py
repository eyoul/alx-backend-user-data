#!/usr/bin/env python3
"""API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Returns Autentication for now.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if the path is not in the list of excluded_paths.
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
            if excluded_path.endswith('/') and path.startswith(excluded_path
                                                               [:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header
        from the Flask request object.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None for now.
        """
        return None
