class WorkshopGroup:
    def __init__(self, configurations):
        print("Workshop Group created")
        self.__groupName = configurations['groupName']
        self.__associatedUnits = configurations['associatedUnits']
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
    