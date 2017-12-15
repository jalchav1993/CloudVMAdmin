from TestbedManagementSystem.Files.Database.configurationDB import configurationDB

class NetworkAdapterTable:
    def __init__(self, configuration):
        self.__NAstring = configuration['NAstring']
        self.__NAvmName= configuration['NAvmName']
        self.__dictVm = configuration['dictVM']
        

    def insertNetAdapt(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO NETWORK_ADAPTER (NAstring,NAvmName) VALUES ('" + configuration['NAstring'] + "','" + configuration['NAstring'] + "')"
        try:
            cur.execute(insert)
            conn.commit()
            print('Add Network Adapter\n')
        except:
            conn.rollback
        cur.close()
        conn.close()
       
    def selectRefeNetAdapt(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM NETWORK_ADAPTER WHERE NAstring= '" + configuration['NAstring'] +"', NAvmName = '" + configuration['NAvmName']+"'"
        try:
            cur.execute(select)     
            conn.commit()
            print('Selected Network Adapter\n')
        except:
            conn.rollback()
            
        for row in cur:
            print()
            print (row)
        cur.close()
        conn.close()
        
    
    def updateNetAdapt(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE NETORK_ADAPTER SET NAstring= $s ,  NAvmName= $s WHERE NAString= $s, NAvmName= $s "
        try:
            cur.execute(update,(configuration['NAstring'], configuration['NAvmName'],configuration['NAstring'],configuration['NAvmName']))
            conn.commit()
        except:
            conn.rollback
        print('Network AdapterS Updated\n')
        cur.close()
        conn.close()
    
       
    def removeNetAdapt(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove ="DELETE FROM NETORK_ADAPTER WHERE NAstring= '" + configuration['NAstring'] +"', NAvmName = '" + configuration['NAvmName']+"'"
        try:
            cur.execute(remove)
            conn.commit()
        except:
            conn.rollback()
        print('Workshop History deleted\n')
        
        def __toDict(self):
            dict = {'NAstring':self.__NAstring,
                    'NAvmName':self.__NAvmName, 
                    'dictVM':self.__dictVm}
            return dict