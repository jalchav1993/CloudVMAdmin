from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
from TestbedManagementSystem.Files.Database.UserTable import UserTable


class AdminTable:
    
    def __init__(self,configuration):
        self.__Aemail = configuration['Aemail']
        self.__dict = configuration['dict']
        self.__email = self.__dict['Uemail']
        self.__fname = self.__dict['Ufname']
        self.__lname = self.__dict['Ulname']
        self.__password = self.__dict['Upassword']
        
    def insertAdmin(self,configuration):
        UserTable.insertUser(self, configuration)    
        
    def selectAdmin(self,configuration):
        UserTable.selectUser(self, configuration)        
    
    def updateAdmin(self,configuration):
        UserTable.updateUser(self, configuration)
        
    def removeAdmin(self,configuration):
        UserTable.removeUser(self, configuration)

    def getAdminColums(self):
        colum = ['Aemail','Uemail','Ufname','Ulname','Upassword']
        return colum
    def __toDict(self):
        dict = {'Aemail':self.__Aemail,'Uemail': self.__email,'Ufname': self.__fname, 
                'Ulname': self.__lname,'Upassword':self.__password}
        return dict