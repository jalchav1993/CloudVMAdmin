from flask import Blueprint, url_for

users = Blueprint('users', __name__)

from . import routes