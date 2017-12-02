from AdminDB import AdminDB
from RegUserDB import RegUserDB
from ServerDB import ServerDB
from VirtualMachineDB import VirtualMachineDB
from WorkshopDB import WorkshopDB
from WorkshopGroupDB import WorkshopGroupDB
from WorkshopUnitDB import WorkshopUnitDB

class DatabaseManager:
	class __DatabaseManager
		def __init__(self):
			print("Database Manager Created")
			__adminDB = AdminDB.__init__(self)
			__regUserDB = RegUserDB.__init__(self)
			__serverDB = ServerDB.__init__(self)
			__virtualMachineDB = VirtualMachineDB.__init__(self)
			__workshopDB = WorkshopDB.__init__(self)
			__workshopGroupDB = WorkshopGroupDB.__init__(self)
			__workshopUnitDB = WorkshopUnitDB.__init__(self)
	instance = None
	def __init__(self):
		if not Database.instance:
			Database.instance = Database.__Database(self)
	
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
