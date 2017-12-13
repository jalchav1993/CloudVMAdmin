from flask import Flask, request, send_from_directory, send_file
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
@stargate.route('/api/menu/sidenav')
def get_menu_sidenav():
  return send_from_directory('static', "admin.json")
@stargate.route('/api/menu/header')
def get_menu_header():
  return send_from_directory('static', "header.json")
@stargate.route('/api/init')
def get_init_req():
  return send_from_directory('static', "init.json")
@stargate.route('/templates/servers/')
def get_template():
  return send_from_directory('./static/templates/servers/', 'servers.html')