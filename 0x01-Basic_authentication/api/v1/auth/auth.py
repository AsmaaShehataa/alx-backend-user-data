#!/usr/bin/env python3
""" Authentication module """
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """ class auth for authenticating users"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth function that returns false"""
        if excluded_paths and path:
            if path[-1] == '/':
                new_path = path[:-1]
            else:
                new_path = path
            new_excluded_path = []
            for element in excluded_paths:
                if element[-1] == '/':
                    new_excluded_path.append(element[:-1])
                if element[-1] == '*':
                    if new_path.startswith(element[:-1]):
                        return False

            if new_path not in new_excluded_path:
                return True
            else:
                return False
        if path is None:
            return True
        if not excluded_paths:
            return True

    def current_user(self, request=None) -> User:
        """ return current user else None"""
        return None
