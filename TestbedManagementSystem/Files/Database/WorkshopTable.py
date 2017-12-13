from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
class WorkshopTable:
    
    def __init__(self, configuration):
        self._groupName= configuration['WGname']
        self.__unitName = configuration['WUname']
        self.__description = configuration['Wdescription']
        self.__wType = configuration['Wtype']
        self.__wHost= configuration['Whost']
        self.__wStatus = configuration['Wstatus']
        self.__publishDate = configuration['WpublishDate']
        self.__dictServer = configuration['dictS']

    def insertWorkshop(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO WORKSHOP (WGname ,WUname,Wdescription,Wtype,Whost,Wstatus,WpublishDate) VALUES ('" + configuration['WGname'] + "','" + configuration['WUname'] + "','" + configuration['Wdescription'] + "','" + configuration['Wtype'] + "','" + configuration['Whost'] + "','" + configuration['Wstatus'] + "NOW()"
        try:
            cur.execute(insert)
            conn.commit()
        except:
            conn.rollback()
            
        print('Add a New Workshop\n')
        cur.close()
        conn.close()
       
    def selectWorkshop(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM WORKSHOP WHERE WGname = '" + configuration['WGname']+"', WUname = '"+ configuration['WUname']
        try:
            cur.execute(select)     
            conn.commit()
        except:
            conn.rollback()
        
        print('Workshop selected\n')
        cur.close()
        conn.close()
        
    
    def updateWorkshop(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE WORKSHOP SET WGname = %s , WUname= %s ,Wdescription = %s ,Wtype= %s,Whost= %s ,Wstatus= %s, WpublishDate  = NOW() WHERE WGname= %s, WUname = %s" 
        try:
            cur.execute(update,(configuration['WGname'], configuration['WUname'], configuration['Wdescription'],configuration['Wtype'],configuration['Whost'], configuration['Wstatus'],"NOW()",configuration['WGname'], configuration['WUname']))
            conn.commit()
        except:
            conn.rollback()
        print('Workshop Updated\n')
        cur.close()
        conn.close()
    
       
    def removeWorkshop(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove = "DELETE FROM WORKSHOP WHERE WHERE WGname= '"+configuration['WGname']+"', WUname = '" + configuration['WUname']+"'"     
        try:
            cur.execute(remove) 
            conn.commit()
        except:
            conn.rollback()
        print('Worshop deleted\n')
    
    def __toDict(self):
        dict = {'WGname':self._groupName,
                'WUname':self.__unitName, 
                'Wdescription':self.__description,
                'Wtype':self.__wType,
                'Whost':self.__wHost,
                'Wstatus':self.__wStatus,
                'WpublishDate':self.__publishDate,
                'dictS':self.__dictServer }
        return dict