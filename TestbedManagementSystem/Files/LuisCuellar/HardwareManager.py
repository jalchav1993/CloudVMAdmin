from Clone import Clone
from Server import Server
from VirtualMachine import VirtualMachine

class HardwareManager:
    vmSet = set()
    serverSet = set()
    
    def __init__(self):
        print("HardwareManager Created")
        
    def __getVM(self, vmname):
        for vm in HardwareManager.vmSet: 
            if vmname == vm.getVMName(): 
                return vm
            print(vmname + ", ", vm.getVMName())
        return None 
        
    def __getServer(self, serverIP):
        for server in HardwareManager.serverSet:
            if serverIP == server.getIP():
                return server
        return None
        
    def startVM(self, vmname):
        vm = self.__getVM(vmname)
        vm.startVM()
        
    def pauseVM(self, vmname):
        vm = self.__getVM(vmname)
        vm.pauseVM()
        
    def resumeVM(self, vmname):
        vm = self.__getVM(vmname)
        vm.resumeVM()
        
    def power_downVM(self, vmname):
        vm = self.__getVM(vmname)
        vm.power_down()
    
    def getVRDP(self, vmname):
        vm = self.__getVM(vmname)
        return (vm.getVRDP())
    
    def getNetworkAdapter(self, vmname):
        vm = self.__getVM(vmname)
        return (vm.getNetworkAdapter())
    
    def getHostServer(self, vmname):
        vm = self.__getVM(vmname)
        return (vm.getHost())
    
    def getCPUUsage(self, vmname):
        vm = self.__getVM(vmname)
        return (vm.getCPUUsage())
    
    def getMemoryUsage(self, vmname):
        vm = self.__getVM(vmname)
        return (vm.getMemoryUsage())
    
    def getServerStatus(self, serverIP):
        server = self.__getServer(serverIP)
        return server.getIP()
    
    # Not in SDD
    
    # Configurations is a dictionary with keys: vmname, vrdp, networkAdapter, host
    def addVirtualMachine(self, configurations):
        newVM = VirtualMachine(configurations)
        if(newVM in HardwareManager.vmSet):
            return False
        else:
            HardwareManager.vmSet.add(newVM)
            return True
        
    # Configurations is a dictionary with keys: ipAddress, username, password
    def addServer(self, configurations):
        newServer = Server(configurations)
        if(newServer in HardwareManager.serverSet):
            return False
        else:
            HardwareManager.serverSet.add(newServer)
            
    def cloneVM(self, vmname, numOfClones):
        vm = self.__getVM(vmname)
        return vm.clone(numOfClones)