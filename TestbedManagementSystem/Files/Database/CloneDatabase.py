from TestbedManagementSystem.Files.Database.configurationDB import configurationDB

class CloneDatabase:
    def __init__(self, configuration):
        self.__vmName = configuration['CvmName']
        self.__numClones = configuration['CnumOfClones']
        self.__vrdpSeed = configuration['CVRDPSeed']
        
    
    def insertClone(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO CLONE (CvmName, CnumOfClones, CVRDPSeed) VALUES ('" + configuration["CvmName"] + "','" + configuration["CnumOfClones"] + "','" + configuration["CVRDPSeed"] +"')"
        cur.execute(insert)
        print('Add a New Clone\n')
        cur.close()
        conn.close()
       
    def selectClone(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM CLONE WHERE CvmName = '"+configuration['CvmName']+"'"
        cur.execute(select)     
        
        for row in cur:
            print()
            print (row)
        print('Clone selected\n')
        cur.close()
        conn.close()
        
    
    def updateClone(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE CLONE SET CvmName = '"+configuration['CvmName']
        + "', CnumOfClones = '"+configuration['CnumOfClones']
        + "', CVRDPSeed = '" + configuration['CVRDPSeed']
        +"' WHERE Cvname = '" +configuration['CvmName']+"'"
        cur.execute(update)
        
        print('User Updated\n')
        cur.close()
        conn.close()
    
       
    def removeClone(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()    
        cur.execute("DELETE FROM CLONE WHERE CvmName= '"+configuration['CvmName']+"'") 
        print('Clone deleted\n')
    
    def printAllClone(self):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        select = "SELECT * FROM ClONE "
        cur.execute(select) 
        conn.commit()
        results = cur.fetchall()
        for row in results:
            for i in range(0,len(row)):
                print("%s" % row[i])
        print("List all CLONES\n") 
=
    def __toDict(self):
        dict = {'CvmName': self.__vmName,'CnumOfClones': self.__numClones, 
                'CVRDPSeed': self.__vrdpSeed}
        return dict