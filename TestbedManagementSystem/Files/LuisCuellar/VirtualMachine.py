class VirtualMachine:
    def __init__(self, name, vrdp, networkAdapter, host):
        print("Virtual Machine created")
        self.__name = name
        self.__vrdp = vrdp
        self.__networkAdapter = networkAdapter
        self.__host = host
        
    def __eq__(self, other):
        return self.__name == other.getName()
    
    def __hash__(self):
        return hash(self.__name)
    
    def getName(self):
        return self.__name
    
    def getVRDP(self):
        return self.__vrdp
    
    def getNetworkAdapter(self):
        return self.__networkAdapter
    
    def getHost(self):
        return self.__host
    
    def storeVM(self):
        DBM mgr = DBM()
        mgr.addRecord( mgr.getVMID(), self.__toDict() )
        
    def __toDict(self):
        dict = {'vmname': self__name, 'vrdp': self__vrdp, 'host': self__host}
        return dict
        