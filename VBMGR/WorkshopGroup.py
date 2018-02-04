class WorkshopGroup:
    def __init__(self, configurations):
        
        # configurations is a dictionary holding the following information
        # groupname, a SET of associated units, a description, reference material, session type, workshop end date
        print("Workshop Group created")
        self.__groupName = configurations['groupName']
        self.__units = configurations['associatedUnits']
        self.__description = configurations['description']
        self.__referenceMaterial = configurations['referenceMaterial']
        self.__sessionType = configurations['sessionType']
        self.__endDate = configurations['endDate']
        
        self.__status = configurations['status']
        
        # used to create database record
        #self.__createGroupRecord()
        
    def __eq__(self, other):
        return self.__groupName == other.getGroupName()
    
    def __hash__(self):
        return hash(self.__groupName)     
        
    def getGroupName(self):
        return self.__groupName
    
    def getAssociatedUnits(self):
        return self.__associatedUnits
    
    def __createGroupRecord(self):
        dbMgr = DatabaseManager.Instance()
        dbMgr.addRecord(dbMgr.getUnitID(), self.__toDict())
        
    def __toDict(self):
        dict = {'groupName' : self.__groupName, 'associatedUnits' : self.__associatedUnits}
        return dict
    
    def pauseUnit(self, unit):
        if unit in self.__units:
            unit.pauseAllVMs()    
    
    def pauseAllUnits(self):
        for unit in self.__units:
            self.pauseUnit(unit)
            
    def resumeUnit(self, unit):
        if unit in self.__units:
            unit.resumeAllVMs()       
    
    def resumeAllUnits(self):
        for unit in self.__units:
            self.resumeUnit(unit)   
            
    def power_downUnit(self, unit):
        if unit in self.__units:
            unit.power_downAllVMs()             
    
    def power_downAllUnits(self):
        for unit in self.__units:
            self.power_downUnit(unit)     
            
    def startUnit(self, unit):
        if unit in self.__units:
            unit.startAllVMs()
            
    def startAllUnits(self):
        for unit in self.__units:
            print("Test")
            self.startUnit(unit)     