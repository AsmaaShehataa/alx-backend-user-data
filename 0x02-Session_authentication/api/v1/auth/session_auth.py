#!/usr/bin/env python3
""" Session Authentication module """
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ Session Auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a user session id.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a user ID based on session_id
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Retrieves the user associated with the request.
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Destroy session current session
        """
        sessn_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sessn_cookie)
        if (request is None or sessn_cookie is None) or user_id is None:
            return False
        if sessn_cookie in self.user_id_by_session_id:
            del self.user_id_by_session_id[sessn_cookie]
        return True
