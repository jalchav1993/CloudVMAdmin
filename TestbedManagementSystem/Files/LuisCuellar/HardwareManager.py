<<<<<<< HEAD
from Clone import Clone
from Server import Server
from VirtualMachine import VirtualMachine

class HardwareManager:
    def __init__(self):
        print("Hardware Manager Created")
        self.__vmSet = set()
        self.__serverSet = set()
        
    def __getVM(self, vmname):
        for vm in self.__vmSet: 
            if vmname == vm.getName(): 
                return vm
            return None 
        
    def __getServer(self, serverIP):
        for server in self.__serverSet:
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
        if(newVM in self.__vmSet):
            return False
        else:
            self.__vmList.add(newVM)
            return True
        
    # Configurations is a dictionary with keys: ipAddress, username, password
    def addServer(self, configurations):
        newServer = Server(configurations)
        if(newServer in self.__serverSet):
            return False
        else:
            self.__serverSet.add(newServer)
=======
from Clone import Clone
from Server import Server
from VirtualMachine import VirtualMachine

class HardwareManager:
    def __init__(self):
        print("Hardware Manager Created")
        self.__vmSet = set()
        self.__serverSet = set()
        
    def __getVM(self, vmname):
        for vm in self.__vmSet: 
            if vmname == vm.getName(): 
                return vm
            return None 
        
    def __getServer(self, serverIP):
        for server in self.__serverSet:
            if serverIP == server.getIP():
                return server
            return None
        
    def startVM(self, vmname):
        vm = self.__getVM(vmname)
        vm.startVM()
    
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
        if(newVM in self.__vmSet):
            return False
        else:
            self.__vmList.add(newVM)
            return True
        
    # Configurations is a dictionary with keys: ipAddress, username, password
    def addServer(self, configurations):
        newServer = Server(configurations)
        if(newServer in self.__serverSet):
            return False
        else:
            self.__serverSet.add(newServer)
>>>>>>> 60c5cc35dc452055da630d513ef02cf6a512d26d
            return True