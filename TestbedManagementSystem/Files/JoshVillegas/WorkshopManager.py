from Workshop import Workshop
from WorkshopGroup import WorkshopGroup
from WorkshopUnit import WorkshopUnit
from lib2to3.pgen2.tokenize import group

class WorkshopManager:
    def __init__(self):
        print("Workshop Manager created")
        self.__groupSet = set() #not sure if used yet
        self.__unitSet = set() #not sure if used yet
        
    def __getWorkshop(self, workshopName):
        for workshop in self.__workshopSet:
            if workshopName == workshop.getName():
                return workshop
            return None
        
    def __getGroup(self, groupName):
        for group in self.__groupSet:
            if groupName == WorkshopGroup.getName():
                return WorkshopGroup
            return None
        
    def __getUnit(self, unitName):
        for unit in self.__unitSet:
            if unitName == WorkshopUnit.getName():
                return WorkshopUnit
            return None
        
    
    def getReferenceMaterial(self, workshopName):
         workshop = self.__getWorkshop(workshopName)
         return (workshop.getReferenceMaterial())
     
    def getGroupStatus(self, workshopName):
        workshop = self.__getWorkshop(workshopName)
        return(workshopGroup.getWorkshopStatus)
        
    def getAvailableWorkshops(self):
    
    def getUnitConnectionString(self, unitName):
        unit = self.__getUnit(unitName)
        return (unit.getConnectionString())
    
    def addWorkshopUnit(self, configurations):
        newUnit = workshopUnit(configurations)
        if(newUnit in self.__unitSet):  #unit already exists
            return False
        else:
            self.__unitSet.add(newUnit)
            return True
        
    def addWorkshopGroup(self, configurations):
        newGroup = WorkshopGroup(configurations)
        if(newGroup in self.__groupSet):
            return False
        else:
            self.__groupSet.add(newGroup)
            return True
        
    def addWorkshop(self, configurations):
        newWorkshop = Workshop(configurations)
        if(newWorkshop in self.__workshopSet):
            return False
        else:
            self.__workshopSet.add(newWorkshop)
            return True
    
    def createConfig(self):
        config = {}
        
        unitName = getFromGui
        config.update(unitName=unitName)
        
        vms = GetFromGui
        config.update(vms=vms)
        
        description = getFromGui
        config.update(description=description)
        
        referenceMaterial = GetFromGui
        config.update(referenceMaterial=referenceMaterial)
        
        connectionString = GetFromGui
        config.update(connectionString=connectionString)
        
        sessionType = GetFromGui
        config.update(sessionType=sessionType)
        
        endDate = GetFromGui
        config.update(endDate=endDate)
    
        return config
        
        
    def createUnit(self):
        configurations = createConfig()
        newUnit = WorkshopUnit(configurations)
        unitSet.add(newUnit)
        
    def createGroup(self):
        
        newGroup = WorkshopGroup(configurations)
        groupSet.add(newGroup)
        
    