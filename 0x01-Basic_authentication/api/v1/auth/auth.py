#!/usr/bin/env python3
"""API authentication.
"""
import re
from typing import List, TypeVar
from flask import request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False for now.
        """
        if path is not None and excluded_paths is not None:
            for excluded_paths in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if excluded_paths[-1] == '*':
                    pattern = '{}.*'.format(excluded_paths[0:-1])
                elif excluded_paths[-1] == '/':
                    pattern = '{}/*'.format(excluded_paths[0:-1])
                else:
                    pattern = '{}/*'.format(excluded_paths)
                if re.match(pattern, path):
                    return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None for now.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None for now.
        """
        return None
