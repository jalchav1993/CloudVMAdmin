from AdminDB import AdminDB
from RegUserDB import RegUserDB
from ServerDB import ServerDB
from VirtualMachineDB import VirtualMachineDB
from WorkshopDB import WorkshopDB
from WorkshopGroupDB import WorkshopGroupDB
from WorkshopUnitDB import WorkshopUnitDB

class DatabaseManager:
    def __init__(self):
        print("Database Manager Created")
		self.__adminDB = configurations['adminDB']
		self.__regUserDB = configurations['regUserDB']
		self.__serverDB = configurations['serverDB']
		self.__virtualMachineDB = configurations['virtualMachineDB']
		self.__workshopDB = configurations['workshopDB']
		self.__workshopGroupDB = configurations['workshopGroupDB']
		self.__workshopUnitDB = configurations['workshopUnitDB']

    def __getAdminDB(self)
        return self.__adminDB

    def __getRegUserDB(self)
        return self.__regUserDB

    def __getServerDB(self)
        return self.__serverDB

    def __getVirtualMachineDB(self)
        return self.__virtualMachineDB

    def __getWorkshopDB(self)
        return self.__workshopDB

    def __getWorkshopGroupDB(self)
        return self.__workshopGroupDB

    def __getWorkshopUnitDB(self)
        return self.__workshopUnitDB
