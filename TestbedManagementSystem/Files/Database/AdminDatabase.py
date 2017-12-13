from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
from TestbedManagementSystem.Files.Database.UserDatabase import UserDatabase

class AdminDatabase:
    
    def __init__(self,configuration):
        self.__Aemail = configuration['Aemail']
        self.__dict = configuration['dict']
        self.__email = self.__dict['Uemail']
        self.__fname = self.__dict['Ufname']
        self.__lname = self.__dict['Ulname']
        self.__password = self.__dict['Upassword']
        
    def insertAdmin(self,configuration):
        UserDatabase.insertUser(self, configuration)    
        
             
    def selectAdmin(self,configuration):
        UserDatabase.selectUser(self, configuration)        
    
    def updateAdmin(self,configuration):
        UserDatabase.updateUser(self, configuration)

    def __toDict(self):
        dict = {'Aemail':self.__Aemail,'Uemail': self.__email,'Ufname': self.__fname, 
                'Ulname': self.__lname,'Upassword':self.__password}
        return dict