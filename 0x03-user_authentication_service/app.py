#!/usr/bin/env python3
"""Flask APP"""

from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth
from user import User, Base

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=['GET'])
def welcome() -> str:
    """GET /
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
