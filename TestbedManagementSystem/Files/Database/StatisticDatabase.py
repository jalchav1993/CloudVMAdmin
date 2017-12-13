from TestbedManagementSystem.Files.Database.configurationDB import configurationDB

class StatisticDatabase:
    def __init__(self, configuration):
        self.__dateCreated= configuration['SdateCreated']
        self.__availConn = configuration['SavailableConn']
        self.__unsusedConn = configuration['SunusedConn']
        self.__usedConn = configuration['SusedConn']
        self.__cpuUsage = configuration['ScpuUsage']
        self.__memUsage = configuration['SmemUsage']
#     SdateCreated,SavailableConn,SunusedConn,SusedConn,ScpuUsag,SmemUsage
#    configuration['SdatedCreated'], configuration['SavailableConn'],
#    configuration['SunusedConn'], configuration['SusedConn'],
#    configuration['ScpuUsage'], configuration['SmemUsage']
    def insertStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO STATISTICS (SavailableConn,SunusedConn,SusedConn,ScpuUsag,SmemUsage) VALUES ('" 
        + configuration['SdateCreated'] + "','" + configuration['SavailableConn'] + "','" 
        + configuration['SunusedConn'] + "','" + configuration['SusedConn'] + "','"
        + configuration['ScpuUsage'] + "','" + configuration['SmemUsage'] + "')"
        
        cur.execute(insert)
        print('Add a New Clone\n')
        cur.close()
        conn.close()
       
    def selectStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM STATISTICS WHERE SdateCreated = '" + configuration['SdateCreated']+"'"
        cur.execute(select)     
        
        for row in cur:
            print()
            print (row)
        print('Statistic selected\n')
        cur.close()
        conn.close()
        
    
    def updateStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE STATISTICS SET"
        +" Uemail = '" + configuration['SdateCreated'] 
        + "', SavailableConn = '" + configuration['SavailableConn'] 
        + "',SunusedConn = '" + configuration['SunusedConn'] 
        + "',SusedCon = '" + configuration['SusedConn'] 
        + "',ScpuUsage = '" + configuration['ScpuUsage'] 
        + "',SmemUsage = '" + configuration['SmemUsage'] 
        + "' WHERE SdateCreated = '" + configuration['SdateCreated'] + "'"
        cur.execute(update)

        print('Statistics Updated\n')
        cur.close()
        conn.close()
    
       
    def removeStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()    
        cur.execute("DELETE FROM STATISTICS WHERE SdateCreated = '" + configuration['SdateCreated']+"'") 
        print('Statistic deleted\n')
    
    def __toDict(self):
        dict = {'SdateCreated': self.__dateCreated,
                'SavailableConn':self.__availConn,
                'SunusedConn':self.__unsusedConn,
                'SusedConn':self.__usedConn,
                'ScpuUsage':self.__cpuUsage ,
                'SmemUsage':self.__memUsage}
        return dict