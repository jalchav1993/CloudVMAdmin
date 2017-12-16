class WorkshopUnit:
    def __init__(self, configurations):
        print("Workshop Unit created")
        self.__unitName = configurations['unitName']
        self.__vms = configurations['vms']
        self.__description = configurations['description']
        self.__referenceMaterial = configurations['referenceMaterial']
        self.__connectionString = configuration['connectionString']
        self.__sessionType = configurations['sessionType']
        self.__status = configurations['status']
        self.__hwmgr = HardwareManager()
        #self.__createUnitRecord()
        
    def __eq__(self, other):
        return self.__unitName == other.getUnitName()
    
    def __hash__(self):
        return hash(self.__unitName)    
        
    def getVmList(self):
        return self.__vms
    
    def getUnitName(self):
        return self.__unitName
    
    def getConnectionString(self):
        return self.__connectionString
    
    def getStatus(self):
        return self.__status
    
    def isAvailable(self):
        return self.__status == 0 #Available
    
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
        if vmname in vms:
            self.__hwMgr.startVM(vmname)
            
    # the followig methods exist but still need to be implemented
    
    def pauseVM(self, vmname):
        if vmname in self.__vms:
            self.__hwmgr.pauseVM(vmname)
    
    def pauseAllVMs(self):
        for vmname in self.__vms:
            self.pauseVM(vmname)
            
    def resumeVM(self, vmname):
        if vmname in self.__vms:
            self.__hwmgr.resumeVM(vmname)
    
    def resumeAllVMs(self):
        for vmname in self.__vms:
            self.resumeVM(vmname)            
    
    def power_downVM(self, vmname):
        if vmname in self.__vms:
            self.__hwmgr.power_downVM(vmname)
    def power_downAllVMs(self):
        for vmname in self.__vms:
            self.power_downVM(vmname)
    
    def removeVM(self, vmname):
        if vmname in vms:
            vms.remove(vmname)
        
    def removeAllVMs(self):
        vms.clear()
        
    #def createUnit(self, configurations):
        #newUnit = WorkshopUnit(configurations)
        #new = set()
        #for vm in vms:
            #set.add(HardwareManager.clone(vm))
            
    def cloneUnits(self, numUnits):
        newUnits = set()
        
        for i in range(0, numUnits):
            uName = self.__unitName + i
            uPort = self.__connectionString
            newVms = set()
            
            for vm in self.__vms:
                newVm = HardwareManager.clone(vm)
                newVms.add(newVm)
            
            unitConfig = {"unitName" : uName, "vms" : newVms, "description" : self.__description, "referenceMaterial" : self.__referenceMaterial, "connectionString" : uPort, "sessionType" : self.__sessionType, "status" : self.__status} 
            newUnit = WorkshopUnit(unitConfig)
            newUnits.add(unitConfig)
            
        return newUnits
     
    def unitDetailView(self):
        return configurations
                
            
    
     
    