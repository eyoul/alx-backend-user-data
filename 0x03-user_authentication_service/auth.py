#!/usr/bin/env python3
"""return Hash password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes the given password using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
