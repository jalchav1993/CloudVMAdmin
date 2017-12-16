from Workshop import Workshop
from WorkshopGroup import WorkshopGroup
from WorkshopUnit import WorkshopUnit
from lib2to3.pgen2.tokenize import group

class WorkshopManager:
    groupSet = set()
    unitSet = set()
    
    def __init__(self):
        print("Workshop Manager created")
        
    def __getGroup(self, groupName):
        for group in WorkshopManager.groupSet:
            if groupName == group.getGroupName():
                return group
        return None
        
    def __getUnit(self, unitName):
        for unit in WorkshopManager.unitSet:
            if unitName == unit.getUnitName():
                return unit
        return None
        
    
    def getReferenceMaterial(self, workshopName):
        if(workshopName in WorkshopManager.groupSet):
            workshop = self.__getGroup(workshopName)
        elif(workshopName in WorkshopManager.unitSet):
            workshop = self.getUnit(workshopName)
        else:
            return None
        return (workshop.getReferenceMaterial())
     
    def getGroupStatus(self, workshopName):
        group = self.__getGroup(workshopName)
        return(workshopGroup.getWorkshopStatus)
        
    def getAvailableWorkshops(self):
        availableUnits = set()
        for unit in WorkshopManager.getUnit():
            if(unit.isAvailable()):
                availableUnits.add(unit)
            
        return availableUnits
    
    
    def addWorkshopUnit(self, configurations):
        newUnit = WorkshopUnit(configurations)
        if(newUnit in WorkshopManager.unitSet):  #unit already exists
            return False
        else:
            WorkshopManager.unitSet.add(newUnit)
            return True
        
    def addWorkshopGroup(self, configurations):
        newGroup = WorkshopGroup(configurations)
        if(newGroup in WorkshopManager.groupSet):
            return False
        else:
            WorkshopManager.groupSet.add(newGroup)
            return True

    def startGroup(self, groupName):
        group = self.__getGroup(groupName)
        if(group is None):
            return False
        group.startAllUnits()

    def cloneUnit(self, unitName, numOfClones):
        unit = self.__getUnit(unitName)
        if(unit is None):
            return False
        newUnits = unit.cloneUnits(numOfClones)
        WorkshopManager.unitSet.union(newUnits)
        return(newUnits)

    def startUnit(self, unitName):
        unit = self.__getUnit(unitName)
        if(unit is None):
            return False
        unit.startAllVMs()
        
    def pauseUnit(self, unitName):
        unit = self.__getUnit(unitName)
        if(unit is None):
            return False
        unit.pauseAllVMs()
    
    def resumeUnit(self, unitName):
        unit = self.__getUnit(unitName)
        if(unit is None):
            return False
        unit.resumeAllVMs()    
        
    def power_downUnit(self, unitName):
        unit = self.__getUnit(unitName)
        if(unit is None):
            return False
        unit.power_downAllVMs()    