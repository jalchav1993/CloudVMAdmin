class VirtualMachine:
    def __init__(self, configurations):
        print("Virtual Machine created")
        self.__vmname = configurations['vmname']
        self.__vrdp = configurations['vrdp']
        self.__networkAdapter = configurations['networkAdapter']
        self.__host = configurations['host']
        
        self.__createVMRecord()
        
    def __eq__(self, other):
        return self.__vmname == other.getVMName()
    
    def __hash__(self):
        return hash(self.__vmname)
    
    def getVMName(self):
        return self.__vmname
    
    def getVRDP(self):
        return self.__vrdp
    
    def getNetworkAdapter(self):
        return self.__networkAdapter
    
    def getHost(self):
        return self.__host
    
    def getSnapshot(self):
        return "something"
    
    def __createVMRecord(self):
        dbMgr = DatabaseManager.Instance()
        dbMgr.addRecord( dbMgr.getVMID(), self.__toDict() )
        
    def __toDict(self):
        dict = {'vmname': self.__vmname, 'vrdp': self.__vrdp, 'networkAdapter': self.__networkAdapter, 'snapshot': self.__getSnapshot(), 'host': self.__host}
        return dict
        