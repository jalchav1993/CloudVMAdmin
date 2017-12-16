from TestbedManagementSystem.Files.Database.configurationDB import configurationDB

class StatisticTable:
    def __init__(self, configuration):
        self.__dateCreated= configuration['SdateCreated']
        self.__availConn = configuration['SavailableConn']
        self.__unsusedConn = configuration['SunusedConn']
        self.__usedConn = configuration['SusedConn']
        self.__cpuUsage = configuration['ScpuUsage']
        self.__memUsage = configuration['SmemUsage']


    def insertStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO STATISTICS (SavailableConn,SunusedConn,SusedConn,ScpuUsag,SmemUsage) VALUES ('" + configuration['SdateCreated'] + "','" + configuration['SavailableConn'] + "','" + configuration['SunusedConn'] + "','" + configuration['SusedConn'] + "','"+ configuration['ScpuUsage'] + "','" + configuration['SmemUsage'] + "')"
        try:
            cur.execute(insert)
            conn.commit()
        except:
            conn.rollback()
            
        print('Add a New Clone\n')
        cur.close()
        conn.close()
       
    def selectStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM STATISTICS WHERE SdateCreated = '" + configuration['SdateCreated']+"'"
        try:
            cur.execute(select)     
            conn.commit()
        except:
            conn.rollback()
        
        print('Statistic selected\n')
        cur.close()
        conn.close()
        
    
    def updateStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE STATISTICS SET Sdatecreated = %s , SavailableConn = %s ,SunusedConn = %s ,SusedCon = %s,ScpuUsage = %s ,SmemUsage = %s WHERE SdateCreated = %s" 
        try:
            cur.execute(update,(configuration['SdateCreated'],configuration['SavailableConn'],configuration['SunusedConn'],configuration['SusedConn'],configuration['ScpuUsage'],configuration['SmemUsage'],configuration['SdateCreated']))
            conn.commit()
        except:
            conn.rollback()
        print('Statistics Updated\n')
        cur.close()
        conn.close()
    
       
    def removeStat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove = "DELETE FROM STATISTICS WHERE SdateCreated = '" + configuration['SdateCreated']+"'"     
        try:
            cur.execute(remove) 
            conn.commit()
        except:
            conn.rollback()
        print('Statistic deleted\n')
    
    def __toDict(self):
        dict = {'SdateCreated': self.__dateCreated,
                'SavailableConn':self.__availConn,
                'SunusedConn':self.__unsusedConn,
                'SusedConn':self.__usedConn,
                'ScpuUsage':self.__cpuUsage ,
                'SmemUsage':self.__memUsage}
        return dict