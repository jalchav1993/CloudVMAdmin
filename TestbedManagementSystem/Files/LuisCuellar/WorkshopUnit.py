from HardwareManager import HardwareManager
from time import sleep

class WorkshopUnit():
    def __init__(self, configurations):
        print("Workshop Unit created")
        self.__unitName = configurations['unitName']
        self.__vms = configurations['vms']
        self.__description = configurations['description']
        self.__referenceMaterial = configurations['referenceMaterial']
        self.__connectionString = configurations['connectionString']
        self.__sessionType = configurations['sessionType']
        self.__status = configurations['status']
        self.__hwmgr = HardwareManager()
        #self.__createUnitRecord()
    
    def getName(self):
        return self.__unitName
        
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
    
    def startAllVMs(self):
        for vmname in self.__vms:
            self.startVM(vmname)
            
    def startVM(self, vmname):
        if vmname in self.__vms:
            self.__hwmgr.startVM(vmname)
            
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
        if vmname in self.__vms:
            vms.remove(vmname)
        
    def removeAllVMs(self):
        self.__vms.clear()
        
    #def createUnit(self, configurations):
        #newUnit = WorkshopUnit(configurations)
        #new = set()
        #for vm in vms:
            #set.add(HardwareManager.clone(vm))
            
    def cloneUnits(self, numUnits):
        newUnits = set()
        
        vmList = []
        for vm in self.__vms:
            newVMs = self.__hwmgr.cloneVM(vm, numUnits)
            print(newVMs)
            vmList.append( list(newVMs) )
        
        print(vmList)
        
        for i in range(0, numUnits):
            uName = self.__unitName + str(i)
            uPort = self.__connectionString
            
            vmSet = set()
            for j in range(0, len(vmList)):
                vmSet.add( vmList[j][i])
            
            print(vmSet)
            
            unitConfig = {"unitName" : uName, "vms" : vmSet, "description" : self.__description, "referenceMaterial" : self.__referenceMaterial, "connectionString" : uPort, "sessionType" : self.__sessionType, "status" : self.__status} 
            newUnit = WorkshopUnit(unitConfig)
            newUnits.add(newUnit)
            
        return newUnits
     
    def unitDetailView(self):
        return configurations
                
            
    
     
    