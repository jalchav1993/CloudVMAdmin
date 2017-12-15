class WorkshopGroup:
    def __init__(self, configurations):
        
        # configurations is a dictionary holding the following information
        # groupname, a SET of associated units, a description, reference material, session type, workshop end date
        print("Workshop Group created")
        self.__groupName = configurations['groupName']
        self.__associatedUnits = configurations['associatedUnits']
        self.__description = configurations['description']
        self.__referenceMaterial = configurations['referenceMaterial']
        self.__sessionType = configurations['sessionType']
        self.__endDate = configurations['endDate']
        
        self.__status = configurations['status']
        
        # used to create database record
        self.__createGroupRecord()
        
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
    
    def cloneGroup(self, numGroups):
        newGroups = set()
        newUnits = set()
        for i in range(0, numGroups):
            #need to finish
            
            
        
    def workshopGroupDetailView(self):
        return configurations
    
        
    