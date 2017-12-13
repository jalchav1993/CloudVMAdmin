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
        if vmname in vms:
            vms.remove(vmname)
        
    def removeAllVms(self):
        vms.clear()
        
    def createUnit(self, configurations):
        newUnit = WorkshopUnit(configurations)
        new = set()
        for vm in vms:
            set.add(HardwareManager.clone(vm))
            
            
    def cloneUnit(self, unitName):
        numUnits = GetFromGui
        for x in range(numUnits):
            hardwareManager.clone(unitName)
            x.vrdp = getFromGui
            x.nAdapterName = GetFromGui
            x.nAdampterSeed = GetFromGui
            
    def cloneUnits(self, numUnits):
        a = 0
        
            for each numUnits:
                newName = unitName + a
                newUnit = WorkshopUnit(configurations)
                unitSet.add(newUnit)
                a+=1
            return unitSet
        
    def unitDetailView(self):
        return configurations
                
            
    
     
    