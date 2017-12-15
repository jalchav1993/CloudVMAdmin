from TestbedManagementSystem.Files.Database.configurationDB import configurationDB


class UserTable:
    
    def __init__(self,configuration):
        self.__email = configuration['Uemail']
        self.__fname = configuration['Ufname']
        self.__lname = configuration['Ulname']
        self.__password = configuration['Upassword']
        
        
    def insertUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO USER (Uemail, Ufname, Ulname, Upassword) VALUES ('" + configuration["Uemail"] + "','" + configuration["Ufname"] + "','" + configuration["Ulname"] +"','" + configuration["Upassword"] + "')"
        try:
            cur.execute(insert)
            conn.commit()
        except:
            conn.rollback()
            
        print('Add a New User\n')
        cur.close()
        conn.close()
     
       
    def selectUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM USER WHERE Uemail = '"+configuration['Uemail']+"'"
        cur.execute(select)     
        
        print('User elected\n')
        cur.close()
        conn.close()
        
    
    def updateUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        try:
            cur.execute("UPDATE USER SET Upassword = %s WHERE Uemail = $s",(configuration['Upassword'], self.__email))
            conn.commit()
        except:
            conn.rollback()
        
        print('User Updated\n')
        cur.close()
        conn.close()
    
    def resetPassword(self,email,password):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
#             
        update = "UPDATE USER SET Upassword = '"+password+"' WHERE Uemail = '"+email+"'"
        cur.execute("UPDATE USER SET Upassword = %s WHERE Uemail = $s",(password, email))     
         
        cur.close()
        conn.close()
        return self.__password
        
    def removeUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        remove = "DELETE FROM USER WHERE Uemail = '"+configuration['Uemail']+"'"     
        cur.execute(remove) 
        print('User deleted\n')
    
    def printAllUsers(self):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        select = "SELECT * FROM USER "
        try:
            cur.execute(select) 
            conn.commit()
        except:
            conn.rollback()
            
        results = cur.fetchall()
        for row in results:
            for i in range(0,len(row)):
                print("%s" % row[i])
        print("List all users\n") 

    def __toDict(self):
        dict = {'Uemail': self.__email,'Ufname': self.__fname, 'Ulname': self.__lname,'Upassword':self.__password}
        return dict