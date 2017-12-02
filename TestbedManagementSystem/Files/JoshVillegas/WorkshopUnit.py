class WorkshopUnit:
    def __init__(self, configurations):
        print("Workshop Unit created")
        self.__unitName = configurations['unitName']
        self.__vms = configurations['vms']
        self.__connectionString = configuration['connectionString']
        self.__createUnitRecord()
        
    def getVmList(self):
        return self.__vms
    
    def getUnitName(self):
        return self.__unitName
    
    def getConnectionString(self):
        return self.__connectionString
    
    def __createUnitRecord(self):
        dbMgr = DatabaseManager.Instance()
        dbMgr.addRecord(dbMgr.getUnitID(), self.__toDict())
    
    def __toDict(self):
        dict = {'unitName' : self.__unitName, 'vms' : self.__vms, 'connectionString' : self.__connectionString}
        return dict
    
    #question to ak for the follow action methods:
    #should they be called in the manager in order to allow all communication to happen through the managers?
    #example for how it would look in the manager class:
    # def startVm(workshopName, unitName, vmName):
    #maybe only for the start all, pause all, etc... methods??
    
    def startAllVms(self):
        for vmname in vms:
            self.startVM(vmname)
            
    def startVM(self, vmname):
        hwMgr = HardwareManager.instance()
        if vmname in vms:
            hwMgr.startVM(vmname)
            
    # the followig methods exist but still need to be implemented
    
    def pauseVm(self, vmname):
    
    def pauseAllVms(self):
        
    def suspendVm(self, vmname):
    
    def suspendAllVms(self):
    
    def removeVm(self, vmname):
        
    def removeAllVms(self):
    
     
    