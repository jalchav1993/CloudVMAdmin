from Clone import Clone
from Server import Server
from VirtualMachine import VirtualMachine

class HardwareManager:
    def __init__(self):
        print("Hardware Manager Created")
        self.__vmList = set()
        self.__serverList = set()
        
    def addVM(self, vmname, vrdp, host):
        newVM = VirtualMachine(vmname, vrdp, host)
        self.__vmList.add(newVM)
        
    def __getVM(self, vmname):
        for vm in self.__vmList: 
            if vmname == vm.getName(): 
                return vm
            return None 
    
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
    
    # Not in SDD
    
    # Configurations is a dictionary with keys: vmname, vrdp, networkAdapter, host
    def createVirtualMachine(self, configurations):
        newVM = VirtualMachine(configurations['vmname'], configurations['vrdp'], configurations['networkAdapter'], configurations['host'])
        if(newVM in self.__vmList):
            return False
        else:
            self.__vmList.add(newVM)
            return True
        
    