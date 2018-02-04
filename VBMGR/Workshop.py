class Workshop:
    def __init__(self, configurations):
        print("Workshop created")
        self.__workshopName = configurations['workshopName']
        self.__referenceMaterial = configurations['referenceMaterial']
        self.__status = "magic"
        
        #self.__createWorkshopRecord()
        
    def getName():
        return self.__workshopName
    
    def getWorkshopName(self):
        return self.__workshopName
    
    def getReferenceMaterial(self):
        return self.__referenceMaterial
    
    def getWorkshopStatus(self):
        return self.__status
    
    def getVmStatus(self):
        print("status")
        #status of all associated vms?
        
    def getServerStatus(self):
        print("status")
        #status of host server??
        
    def __createWorkshopRecord(self):
        dbMgr = DatabaseManager.Instance()
        dbMgr.addRecord(dbMgr.getUnitID(), self.__toDict())
        
    def __toDict(self):
        dict = {'workshopName' : self.__workshopName, 'referenceMaterial' : self.__referenceMaterial, 'status' : self.__status}
        return dict
    
    