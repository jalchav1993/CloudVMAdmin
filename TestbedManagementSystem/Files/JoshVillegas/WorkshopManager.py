from Workshop import Workshop
from WorkshopGroup import WorkshopGroup
from WorkshopUnit import WorkshopUnit
from lib2to3.pgen2.tokenize import group

class WorkshopManager:
    def __init__(self):
        print("Workshop Manager created")
        self.__groupSet = set() #not sure if used yet
        self.__unitSet = set() #not sure if used yet
        
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
        if(workshopName in self.__groupSet):
            workshop = self.__getGroup(workshopName)
        elif(workshopName in self.__unitSet):
            workshop = self.__getUnit(workshopName)
        else:
            return None
        return (workshop.getReferenceMaterial())
     
    def getGroupStatus(self, workshopName):
        group = self.__getGroup(workshopName)
        return(workshopGroup.getWorkshopStatus)
        
    def getAvailableWorkshops(self):
        availableUnits = set()
        for unit in self.__getUnit():
            if(unit.isAvailable()):
                availableUnits.add(unit)
            
        return availableUnits
    
    
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

    def cloneUnit(self, unitName, numOfClones):
        unit = self.__getUnit(unitName)
        if(unit is None):
            return False
        newUnits = unit.cloneUnits(numOfClones)
        return(newUnits)
