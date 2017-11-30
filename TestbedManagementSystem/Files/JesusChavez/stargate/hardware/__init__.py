from flask import Blueprint, url_for

hardware = Blueprint('hardware', __name__)

from . import routes