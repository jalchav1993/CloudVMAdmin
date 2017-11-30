from flask import Flask
from .users import users as user_blueprint
from .hardware import hardware as hardware_blueprint
from .workshop import workshop as workshop_blueprint

stargate = Flask(__name__)
stargate.register_blueprint(user_blueprint)
stargate.register_blueprint(hardware_blueprint)
stargate.register_blueprint(workshop_blueprint)
