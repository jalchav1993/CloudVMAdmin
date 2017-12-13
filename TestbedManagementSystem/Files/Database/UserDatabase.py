from TestbedManagementSystem.Files.Database.configurationDB import configurationDB
configurationDB

class UserDatabase:
    
    def __init__(self,configuration):
        self.__email = configuration['Uemail']
        self.__fname = configuration['Ufname']
        self.__lname = configuration['Ulname']
        self.__password = configuration['Upassword']
        
        
    def insertUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        insert = "INSERT INTO USER (Uemail, Ufname, Ulname, Upassword) VALUES ('" + configuration["Uemail"] + "','" + configuration["Ufname"] + "','" + configuration["Ulname"] +"','" + configuration["Upassword"] + "')"
        cur.execute(insert)
        print(self.__email,self.__fname,self.__lname,self.__password)
        print('Add a New User\n')
        cur.close()
        conn.close()
       
    def selectUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()       
        select = "SELECT * FROM USER WHERE Uemail = '"+configuration['Uemail']+"'"
        cur.execute(select)     
        
        for row in cur:
            print()
#             print (row)  
        print(row[0])
        print('User elected\n')
        cur.close()
        conn.close()
        
    
    def updateUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
        
        update = "UPDATE USER SET Uemail = '"+configuration['Uemail']+"', Ufname = '"
        +configuration['Ufname']+ "', Ulname = '"+configuration['Ulname']
        +"' WHERE Uemail = '"+configuration['Uemail']+"'"
        cur.execute(update)
        select = "SELECT * FROM USER WHERE Uemail = '"+configuration['Uemail']+"'"
        cur.execute(select)  

        for row in cur: 
            print(row)
        print('User Updated\n')
        cur.close()
        conn.close()
    
    def resetPassword(self,email,password):
        conn = configurationDB.connect(self)
        cur = conn.cursor()
#             
        update = "UPDATE USER SET Upassword = '"+password+"' WHERE Uemail = '"+email+"'"
        cur.execute(update)     
         
        cur.close()
        conn.close()
        return self.__password
        
    def removeUser(self,configuration):
        conn = configurationDB.connect(self)
        cur = conn.cursor()    
        cur.execute("DELETE FROM USER WHERE Uemail = '"+configuration['Uemail']+"'") 
        print('User deleted\n')
    
    def printAllUsers(self):
        conn = configurationDB.connect(self)
        cur = conn.cursor()  
        select = "SELECT * FROM USER "
        cur.execute(select) 
        conn.commit()
        results = cur.fetchall()
        for row in results:
            for i in range(0,len(row)):
                print("%s" % row[i])
        print("List all users\n") 

    def __toDict(self):
        dict = {'Uemail': self.__email,'Ufname': self.__fname, 
                'Ulname': self.__lname,'Upassword':self.__password}
        return dict