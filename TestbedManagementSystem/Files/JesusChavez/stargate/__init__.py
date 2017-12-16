from flask import Flask, request, send_from_directory, send_file, request
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
@stargate.route('/api/session/login/', methods=['POST'])
def login():
  if request.json.get('id') == "alex" and request.json.get('pwd') == "123":
    return "login-success"
  return "login-denied"
@stargate.route('/api/init')
def get_init_req():
  return send_from_directory('static', "init.json")
@stargate.route('/templates/servers/')
def get_template_servers():
  return send_from_directory('./static/templates/servers/', 'servers.html')
@stargate.route('/templates/vm/')
def get_template_vm():
  return send_from_directory('./static/templates/vm/', 'vm.html')
@stargate.route('/templates/workshop_groups/')
def get_template_wg():
  return send_from_directory('./static/templates/workshop_groups/', 'workshop_groups.html')
@stargate.route('/templates/workshop_units/')
def get_template_wu():
  return send_from_directory('./static/templates/workshop_units/', 'workshop_units.html')