from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
class VirtualMachineTable:
    
    def __init__(self, configuration):
        self._vmName= configuration['VMname']
        self.__vmVRDP = configuration['VMvrdp']
        self.__vmSnapshopt= configuration['VMsnapshot']
        self.__vmhost = configuration['VMhost']
        self.__dictServer = configuration['dictS']

    def insertVirtualMachine(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO VIRTUAL_MACHINE (VMname,Vmvrdp,VMsnapshot,VMhost) VALUES ('" + configuration['VMname'] + "','" + configuration['VMvrdp'] + "','" + configuration['VMsnapshot'] + "','" + configuration['VMhost'] + "')"
        try:
            cur.execute(insert)
            conn.commit()
        except:
            conn.rollback()
            
        print('Add a New Virtual Machine\n')
        cur.close()
        conn.close()
       
    def selectVirtualMachine(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM VIRTUAL_MACHINE WHERE VMname = '" + configuration['VMname']+"'"
        try:
            cur.execute(select)     
            conn.commit()
        except:
            conn.rollback()
        
        print('Virtual Machine selected\n')
        cur.close()
        conn.close()
        
    
    def updateVirtualMachine(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE VIRTUAL_MACHINE SET VMname = %s , VMvrdp = %s ,VMsnapshot = %s ,VMhost= %s WHERE VMname = %s" 
        try:
            cur.execute(update,(configuration['VMname'], configuration['VMvrdp'],configuration['VMsnapshot'],configuration['VMhost'], configuration['VMname']))
            conn.commit()
        except:
            conn.rollback()
        print('Virtual Machine Updated\n')
        cur.close()
        conn.close()
    
       
    def removeVirtualMachine(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove = "DELETE FROM VIRTUAL_MACHINE WHERE WHERE VMname= '"+configuration['VMname']+"'"
        try:
            cur.execute(remove) 
            conn.commit()
        except:
            conn.rollback()
        print('Virtual Machine deleted\n')
    
    def __toDict(self):
        dict = {'VMname':self._vmName,
                'VMvrdp':self.__vmVRDP, 
                'VMsnapshot':self.__vmSnapshopt,
                'VMhost':self.__vmhost,
                'dictS':self.__dictServer }
        return dict