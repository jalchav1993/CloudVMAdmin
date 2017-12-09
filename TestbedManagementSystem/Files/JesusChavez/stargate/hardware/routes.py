from . import hardware
#import manager
#check session in control

@hardware.route("/hardware/get")
def get():
    return HardwareManager.getVM();


@hardware.route("/hardware/get/VRDP/<ws_name>", methods=['GET'])
def getVRDP(ws_name):
    return HardwareManager.getVRDP(name);
    
@hardware.route("/hardware/get/networ_adapter/<name>")
def get_networ_adapter(name):
    return HardwareManager.getNetworkAdapter(name) 
    
@hardware.route("/hardware/get/host_server/<name>") 
def get_host_server(name):
    return HardwareManager.getHostServer(name)
    
@hardware.route("/hardware/get/cpu_use/<name>") 
def get_cpu_use(name):
    return HardwareManager.getCPUusage(name)
    
@hardware.route("/hardware/get/get_memory_use/<name>") 
def get_get_memory_use(name):
    return HardwareManager.getMemoryusage(name)

@hardware.route("/hardware/get/create_clone/<ip>") 
def get_create_clone(ip):
    return HardwareManager.createClone(vmName, numOfClones)(name)
#add server
#add virtual machine
