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
		self.__adminDB = set()
		self.__regUserDB = set()
		self.__serverDB = set()
		self.__virtualMachineDB = set()
		self.__workshopDB = set()
		self.__workshopGroupDB = set()
		self.__workshopUnitDB = set()

    def __getAdminDB(self, adminDBName)
		for adminDB in self.__adminDBSet
			if adminDBName == adminDB.getName()
				return adminDB
			return None

    def __getRegUserDB(self, regUserDBName)
		for regUserDB in self.__regUserDBSet
			if regUserDBName == regUserDB.getName()
				return regUserDB
			return None

    def __getServerDB(self, serverDBName)
		for serverDB in self.__serverDBSet
			if serverDBName == serverDB.getName()
				return serverDB
			return None

    def __getVirtualMachineDB(self, virtualMachineDBName)
		for getVirtualMachineDB in self.__virtualMachineDBSet
			if virtualMachineDBName == virtualMachineDB.getName()
				return virtualMachineDB
			return None

    def __getWorkshopDB(self, workshopDBName)
		for workshopDB in self.__workshopDBSet
			if workshopDBName == workshopDB.getName()
				return workshopDB
			return None

    def __getWorkshopGroupDB(self, workshopGroupDB)
		for workshopGroupDB in self.__workshopGroupDBSet
			if workshopGroupDBName == workshopGroupDB.getName()
				return workshopGroupDB
			return None

    def __getWorkshopUnitDB(self, workshopUnitDB)
		for workshopUnitDB in self.__workshopUnitDBSet
			if workshopUnitDBName == workshopUnitDB.getName()
				return workshopUnitDB
			return None
