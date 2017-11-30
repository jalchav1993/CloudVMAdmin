from . import hardware
#import manager
@hardware.route("/hardware/get")
def get():
    return HardwareManager.getVM();
