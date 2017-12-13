from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
from TestbedManagementSystem.Files.Database.UserDatabase import UserDatabase


class RegUserDatabase:
    
    def __init__(self,configuration):
        self.__RUemail = configuration['RUemail']
        self.__org = configuration['RUorganizaition']
        self.__RUskillLevel = configuration['RUorganization']
        self.__dict = configuration['dict']
        self.__email = self.__dict['Uemail']
        self.__fname = self.__dict['Ufname']
        self.__lname = self.__dict['Ulname']
        self.__password = self.__dict['Upassword']
        
    def insertRegUser(self,configuration):
        UserDatabase.insertUser(self, configuration)    
        
             
    def selectRegUser(self,configuration):
        UserDatabase.selectUser(self, configuration)        
    
    def updateRegUser(self,configuration):
        UserDatabase.updateUser(self, configuration)
        
        
    def removeUser(self,configuration):
        UserDatabase.removeUser(self, configuration)

    def __toDict(self):
        dict = {'RUemail':self.__RUemail, 'RUorganizaition' : self.__org,
                'RUorganization':self.__RUskillLevel ,'Uemail': self.__email,
                'Ufname': self.__fname, 'Ulname': self.__lname,'Upassword':self.__password}
        return dict