import os
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth

if os.environ.get('AUTH_TYPE') == 'session_auth':
    auth = SessionAuth()
else:
    auth = Auth()