from flask import Blueprint, url_for

workshop = Blueprint('workshop', __name__)

from . import routes