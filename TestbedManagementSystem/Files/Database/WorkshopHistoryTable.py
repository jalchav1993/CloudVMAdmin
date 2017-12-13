from TestbedManagementSystem.Files.Database.configurationDB import configurationDB

class WorkshopHistoryTable:
    def __init__(self, configuration):
        self.__wuName= configuration['WHwuName']
        self.__ruEmail= configuration['WHruName']
        self.__dictWU = configuration['dictWu']
        self.__dictRU = configuration['dictRu']
        

    def insertWShistory(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO WORKSHOP_HISTORY (WHwuName,WHruName) VALUES ('" + configuration['WHwuName'] + "','" + configuration['WHruname'] + "')"
        try:
            cur.execute(insert)
            conn.commit()
            print('Add Workshop Unit\n')
        except:
            conn.rollback
        cur.close()
        conn.close()
       
    def selectRefeWShistory(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM WORKSHOP_HISTORY WHERE WHwuName = '" + configuration['WHwuName'] +"', WHruName = '" + configuration['WHruname']+"'"
        try:
            cur.execute(select)     
            conn.commit()
            print('Selected Workshop History\n')
        except:
            conn.rollback()
            
        for row in cur:
            print()
            print (row)
        cur.close()
        conn.close()
        
    
    def updateWShistory(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE WORKSHOP_HISTORY SET WHwuName = $s ,  WHruName = $s WHERE WHwuName = $s, WHruName = $s "
        try:
            cur.execute(update,(configuration['RMfileName'], configuration['RMwname'],configuration['RMfileName'],configuration['RMwname']))
            conn.commit()
        except:
            conn.rollback
        print('Workshop History Updated\n')
        cur.close()
        conn.close()
    
       
    def removeWShistory(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove ="DELETE FROM WORKSHOP_HISTORY WHERE WHwuName = '" + configuration['WHwuName'] +"', WHruName = '" + configuration['WHruname']+"'"
        try:
            cur.execute(remove)
            conn.commit()
        except:
            conn.rollback()
        print('Workshop History deleted\n')
        
    def __toDict(self):
        dict = {'WHwuName':self.__wuName,
                'WHruName':self.__ruEmail, 
                'dictWu':self.__dictWU,
                'dictRu':self.__dictRU}
        return dict