#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

from api.v1.views.index import *
from api.v1.views.session_auth import *
from api.v1.views.users import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

User.load_from_file()
"""Import the views here
"""
from api.v1.views.session_db_auth import *
from api.v1.views.session_exp_auth import *
from api.v1.views.session_flask_auth import *
from api.v1.views.session_redis_auth import *

""" Add the views here
"""
app_views.add_url_rule('/', view_func=index)
app_views.add_url_rule('/status', view_func=status)
app_views.add_url_rule('/stats', view_func=stats)
app_views.add_url_rule('/users', view_func=users, methods=['GET', 'POST'])
app_views.add_url_rule('/users/<user_id>', view_func=user_id, methods=['GET', 'DELETE', 'PUT'])
app_views.add_url_rule('/auth_session/login', view_func=login, methods=['POST'], strict_slashes=False)
app_views.add_url_rule('/auth_session/logout', view_func=session_logout, methods=['DELETE'], strict_slashes=False)