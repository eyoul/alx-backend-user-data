import base64
from typing import List, TypeVar

from api.v1.auth.auth import Auth

T = TypeVar('T')


class BasicAuth(Auth):
    """Basic authentication class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header for Basic Authentication"""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for the given path"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False
        return True

    def authorization_header(self, request) -> str:
        """Extracts the authorization header from the request"""
        return request.headers.get('Authorization', None)

    def current_user(self, request) -> TypeVar('T'):
        """Returns the current user"""
        return None

    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticates the user"""
        return False

    def authenticate_token(self, token: str) -> bool:
        """Authenticates the token"""
        return False