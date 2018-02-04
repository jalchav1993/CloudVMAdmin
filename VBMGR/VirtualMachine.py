import virtualbox
from virtualbox.library import NetworkAttachmentType
from time import gmtime, strftime, sleep

class VirtualMachine:
    def __init__(self, configurations):
        
        self.__vmname = configurations['vmname']
        self.__vrdp = configurations['vrdp']
        self.__networkAdapter = configurations['networkAdapter']
        
        self.__host = configurations['host']
        self.__vb = virtualbox.VirtualBox()
        self.__session = None
        self.__iVM = None
        self.__snapshot = {"Snapshot": None, "name": ""}
        
        self.__setNetworkAdapter()
        self.takeSnapshot()
        
        print("Virtual Machine: "+self.__vmname+" created")        
        #self.__createVMRecord()
        
    def __setNetworkAdapter(self):
        self.__iVM = self.__vb.find_machine(self.__vmname)
        self.__session = self.__iVM.create_session()
        
        adapter = self.__session.machine.get_network_adapter(0)
        adapter.attachment_type = NetworkAttachmentType.internal
        adapter.internal_network = self.__networkAdapter
        
        server = self.__session.machine.vrde_server
        server.enabled = True
        server.set_vrde_property("TCP/Ports", str(self.__vrdp['port']))
        
        self.__session.machine.save_settings()
        self.__session.unlock_machine()
        
    def takeSnapshot(self):
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        name = self.__vmname + "_snapshot_" + time
        if(self.__iVM.session_state != 2):
            self.__iVM.lock_machine(self.__session, virtualbox.library.LockType.write)
        progress = self.__session.machine.take_snapshot(name, "desc", False)
        self.__snapshot['Snapshot'] = self.__iVM.current_snapshot
        self.__snapshot['name'] = name
        
    def clone(self,numOfClones):
        
        wasRunning = self.__iVM.state == 5
        
        if(wasRunning): #is running
            self.pauseVM()
            sleep(5)
            
        
        if(self.__snapshot['Snapshot'] is None):
            print("Taking Snapshot")
            self.takeSnapshot()
        
        self.__snapshot['Snapshot'] = self.__iVM.current_snapshot
        
        newVMs = set()
        
        for i in range(1,numOfClones+1):

            
            newName = self.__vmname + str(i)
            newPort = self.__vrdp['port'] + i
            newVRDP = {'ip': self.__vrdp['ip'], 'port': newPort}
            newConfig = {'vmname': newName, 'vrdp': newVRDP, 'networkAdapter': self.__networkAdapter, 'host': self.__host}
            newiVM = self.__iVM.clone(snapshot_name_or_id = self.__snapshot['Snapshot'], name = newName)
            
            newVM = VirtualMachine(newConfig)
            newVMs.add(newVM)
        
        self.__session.unlock_machine()
        
        if(wasRunning and self.__iVM.state == 6):
            self.resumeVM()
        
        return newVMs
        
        
    def startVM(self):    
        if(self.__iVM.session_state == 2):
            #self.__session = self.__iVM.create_session()
            self.__session.unlock_machine()
        progress = self.__iVM.launch_vm_process(None, 'headless', '')
        
    def pauseVM(self):
        self.__session = self.__iVM.create_session()
        self.__session.console.pause()
        
    def resumeVM(self):
        self.__session = self.__iVM.create_session()
        self.__session.console.resume()
        
    def power_down(self):
        self.__session = self.__iVM.create_session()
        self.__session.console.power_down()
        
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
        
    