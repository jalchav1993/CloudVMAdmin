from flask import Flask, render_template, request, send_from_directory
from .users import users as user_blueprint
from .hardware import hardware as hardware_blueprint
from .workshop import workshop as workshop_blueprint
stargate = Flask(__name__)
stargate.register_blueprint(user_blueprint)
stargate.register_blueprint(hardware_blueprint)
stargate.register_blueprint(workshop_blueprint)

@stargate.route('/')
def get_index():
    return send_from_directory('static', "index.html")
@stargate.route('/<path:path>')
def get_static(path):
    return send_from_directory('static', path)
@stargate.route('/api/menu/')
def get_menu():
    return send_from_directory('static', "admin.json")