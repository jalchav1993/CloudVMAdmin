class VirtualMachine:
    def __init__(self, name, vrdp, host):
        print("Virtual Machine created")
        self.__name = name
        self.__vrdp = vrdp
        self.__host = host
        
    def __eq__(self, other):
        return self.__name == other.getName()
    
    def __hash__(self):
        return hash(self.__name)
    
    def getName(self):
        return self.__name
    
    def getVRDP(self):
        return self.__vrdp
    
    def getHost(self):
        return self.__host
        