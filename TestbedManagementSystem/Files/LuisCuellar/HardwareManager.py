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
        
    def getVM(self, vmname):
        for vm in self.__vmList: 
            if vmname == vm.getName(): 
                return vm
            return None 
    