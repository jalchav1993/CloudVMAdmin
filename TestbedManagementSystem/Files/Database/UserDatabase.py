from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
configurationDB

import pymysql
class UserDatabase:
    
    def __init__(self,configuration):
        self.__uemail = configuration['Uemail']
        self.__ufname = configuration['Ufname']
        self.__ulname = configuration['Ulname']
        self.__upassword = configuration['Upassword']
        
        
    def insertUser(self,db,configuration):
        configuration['Uemail'] = db.escape(configuration['Uemail'])
        configuration['Upassword'] = db.escape(configuration['Upassword'])
        
        return db.insert("INSERT INTO USERS (Uemail, Ufname, Ulname, Upassword) VALUES ('"
                         , configuration["Uemail"] , "','" , configuration["Ufname"] , "','" 
                         , configuration["Ulname"] ,"','" , configuration["Upassword"] , "')")
        
     #the only one that works   
    def selectUser(self,configuration):
        conn = pymysql.connect(host="earth.cs.utep.edu", user = "aquiroz10", passwd="cs4311", db="aquiroz10")
        db = conn.cursor()         

        db.execute("SELECT * FROM USER WHERE Uemail = 'test@test.com'")     
        
        for row in db:
            print (row)  
        print(row[0])
        db.close()
        
    
    def updateUser(self,configuration):
        db = configurationDB(configuration)
        e = db.getError
        if e is True:
            print ("Unable to fetch parts: ",e)
        
        db.update("UPDATE USER SET Uemail = '",configuration['Uemail'],
                  "Ufname = '",configuration['Ufname'],
                  "Ulname = '",configuration['Ulanme'],
                  ", WHERE Uemail = '",configuration['Uemail'],"'")
    
    def resetPassword(self,configuration):
        db = configurationDB(configuration)
        e = db.getError
        if e is True:
            print ("Unable to fetch parts: ",e)
            
        db.update("UPDATE USER SET Upassword = '",configuration['Uemail'],
                  ", WHERE Uemail = '",configuration['Uemail'],"'") 
        
    def removeUser(self,configuration):
        db = configurationDB(configuration)
        e = db.getError
        if e is True:
            print ("Unable to fetch parts: ",e)
            
        db.delete("DELETE FROM USER WHERE Uemail = '",configuration['Uemail'],"'") 
        
    
    
    def __toDict(self):
        dict = {'Uemail': self.__uemail,'Ufname': self.__ufname, 
                'Ulname': self.__ulname,'Upassword':self.__upassword}
        return dict