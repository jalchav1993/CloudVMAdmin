import virtualbox
from virtualbox.library import NetworkAttachmentType

class VirtualMachine:
    def __init__(self, configurations):
        print("Virtual Machine created")
        self.__vmname = configurations['vmname']
        self.__vrdp = configurations['vrdp']
        self.__networkAdapter = configurations['networkAdapter']
        
        self.__host = configurations['host']
        self.__vb = virtualbox.VirtualBox()
        self.__session = None
        self.__iVM = None
        
        
        #self.__createVMRecord()
        
    def __setNetworkAdapter(self):
        self.__iVM = self.__vb.find_machine(self.__vmname)
        self.__session = self.__iVM.create_session()
        adapter = self.__session.machine.get_network_adapter(0)
        adapter.attachment_type = NetworkAttachmentType.internal
        adapter.internal_network = self.__networkAdapter
        self.__session.machine.save_settings()
        self.__session.unlock_machine()
        
    def startVM(self):
        self.__setNetworkAdapter()     
        self.__progress = self.__iVM.launch_vm_process(None, 'headless', '')
        
    def pauseVM(self):
        session.console.pause()
        
    def resumeVM(self):
        session.console.resume()
        
    def powerOff(self):
        session.console.powerDown()
        
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
        
    