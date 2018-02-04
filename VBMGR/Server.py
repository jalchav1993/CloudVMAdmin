class Server:
    def __init__(self, configuartions):
        print("Server Created")
        self.__ipAddress = configurations['ipAddress']
        self.__username = configurations['username']
        self.__password = configurations['password']
        self.__status = "Something???"
        
        self.__createServerRecord()
        
    def getIP(self):
        return self__.ipAddress
    
    def __createServerRecord(self):
        dbMgr = DatabaseManager.Instance()
        dbMgr.addRecord( dbMgr.getServerID(), self.__toDict() )
        
    def __toDict(self):
        dict = {'ipAddress': self.__ipAddress, 'username': self.__username, 'password': self.__password, 'status': self.__status}
        return dict    
    