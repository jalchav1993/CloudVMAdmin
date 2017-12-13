from Admin import Admin
from GuestUser import QuestUser
from RegisteredUser import RefisteredUser
from WorkshopManager import WorkshopManager

class UserInteractionManager: 
    def __init__(self):
        print("User Interaction Manager Created")
        self.__wsName = set()
    
    def __getWorkshop(self, wsName):
        for ws in self.__wsName:
            if wsName == ws.getName():
                return ws
            return None
        
    def __getMaterial(self, wsName):
        for ws in self.__wsName:
            if wsName == ws.getName():
                return ws
            return None
       
    def getWorkShop(self, wsName):
        ws = WorkshopManager.Instace()
        return (ws.getWorkshop())
    
    def getMaterial(self, wsName):
        ws = self.__getWorkshop(wsName)
        return (ws.getReferenceMaterial())
    
    def createWorkshop(self):
        
        return

    def deleteWorkshop(self):
        return
    
    def updateWorkshop(self):
        return
    
    def participateInSurvey(self):
        return
    
    def getConnectString(self):
        return
    
    
    
    
