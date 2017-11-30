from . import hardware
#import manager
@hardware.route("/hardware/get")
def get():
    return HardwareManager.getVM();

@hardware.route("/hardware/get/VRDP/<name>")
def get(name):
    return HardwareManager.getVRDP(name);
    
@hardware.route("/hardware/get/networ_adapter/<name>")
def get (name):
    return HardwareManager.getNetworkAdapter(name) 
    
@hardware.route("/hardware/get/host_server/<name>") 
def get(name):
    return HardwareManager.getHostServer(name)
    
@hardware.route("/hardware/get/cpu_use/<name>") 
def get(name):
    return HardwareManager.getCPUusage(name)
    
@hardware.route("/hardware/get/get_memory_use/<name>") 
def get(name):
    return HardwareManager.getMemoryusage(name)

@hardware.route("/hardware/get/create_clone/<vmName, numOfClones>") 
def get(ip):
    return HardwareManager.createClone(vmName, numOfClones)(name)
