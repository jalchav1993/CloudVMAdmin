from TestbedManagementSystem.Files.Database.configurationDB import configurationDB

class ReferenceMaterialTable:
    def __init__(self, configuration):
        self.__rmFileName= configuration['RMfileName']
        self.__rmWname = configuration['RMwname']
        self.__dictWU = configuration['dictWu']
        

    def insertRefeMat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO REFERENCE_MATERIAL (RMfileName,RMwname) VALUES ('" + configuration['RMfileName'] + "','" + configuration['RMwname'] + "')"
        try:
            cur.execute(insert)
            conn.commit()
        except:
            conn.rollback
        print('Add a Reference Material\n')
        cur.close()
        conn.close()
       
    def selectRefeMaterial(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM REFERENCE_MATERIAL WHERE RMfileName = '" + configuration['RMfileName']+"', RMwname = '" + configuration['RMwname']+"'"
        try:
            cur.execute(select)     
            conn.commit()
        except:
            conn.rollback()
            
        for row in cur:
            print()
            print (row)
        print('Reference Material\n')
        cur.close()
        conn.close()
        
    
    def updateRefeMat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE REFERENCE_MATERIAL SET RMfileName = $s , RMwname = $s WHERE RMfileName = $s, RMwname = $s "
        try:
            cur.execute(update,(configuration['RMfileName'], configuration['RMwname'],configuration['RMfileName'],configuration['RMwname']))
            conn.commit()
        except:
            conn.rollback
        print('Reference Material Updated\n')
        cur.close()
        conn.close()
    
       
    def removeRefeMat(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove ="DELETE FROM REFERENCE_MATERIAL WHERE RMfileName = '" + configuration['RMfileName']+"', RMwname = '" + configuration['RMwname']+"'"    
        try:
            cur.execute(remove)
            conn.commit()
        except:
            conn.rollback()
        print('Reference Material deleted\n')
    
    def __toDict(self):
        dict = {'RMfileName': self.__dateCreated,'RMwname':self.__availConn}
        return dict