from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
class ServerTable:
    
    def __init__(self, configuration):
        self._vmName= configuration['SipAddress']
        self.__vmVRDP = configuration['Susername']
        self.__vmSnapshopt= configuration['Spassword']
        self.__vmhost = configuration['Sstatus']
        self.__dictServer = configuration['dictS']

    def insertServer(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO SERVER (SipAddress,Vmvrdp,Spassword,Sstatus) VALUES ('" + configuration['SipAddress'] + "','" + configuration['Susername'] + "','" + configuration['Spassword'] + "','" + configuration['Sstatus'] + "')"
        try:
            cur.execute(insert)
            conn.commit()
        except:
            conn.rollback()
            
        print('Add a New Server\n')
        cur.close()
        conn.close()
       
    def selectServer(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM SERVER WHERE SipAddress = '" + configuration['SipAddress']+"'"
        try:
            cur.execute(select)     
            conn.commit()
        except:
            conn.rollback()
        
        print('Server selected\n')
        cur.close()
        conn.close()
        
    
    def updateServer(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE SERVER SET SipAddress = %s , Susername = %s ,Spassword = %s ,Sstatus= %s WHERE SipAddress = %s" 
        try:
            cur.execute(update,(configuration['SipAddress'], configuration['Susername'], configuration['Spassword'],configuration['Sstatus'], configuration['SipAddress']))
            conn.commit()
        except:
            conn.rollback()
        print('Server Updated\n')
        cur.close()
        conn.close()
    
       
    def removeServer(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove = "DELETE FROM SERVER WHERE WHERE SipAddress= '"+configuration['SipAddress']+"'"
        try:
            cur.execute(remove) 
            conn.commit()
        except:
            conn.rollback()
        print('Server deleted\n')
    
    def __toDict(self):
        dict = {'SipAddress':self._vmName,
                'Susername':self.__vmVRDP, 
                'Spassword':self.__vmSnapshopt,
                'Sstatus':self.__vmhost }
        return dict