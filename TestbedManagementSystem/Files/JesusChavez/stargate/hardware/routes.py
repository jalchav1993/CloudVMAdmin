from . import hardware
import json
#import manager
@hardware.route("/hardware/getVms/")
def getVms():
    c = [
      {
        "vmname":"some name", 
        "vrdp": "jndndn", 
        "networkAdapter": "some adapter",
        "host":"187.234.132.1"
      }
    ];
    return json.dumps(c);

@hardware.route("/hardware/get/VRDP/<name>")
def getVRDP(name):
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
def get_memory_use(name):
    return HardwareManager.getMemoryusage(name)

@hardware.route("/hardware/get/create_clone/<ip>") 
def get_create_clone(ip):
    return HardwareManager.createClone(vmName, numOfClones)
