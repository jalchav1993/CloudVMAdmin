import configurationDB
class UserDatabase:
    
    def __init__(self,configuration):
        self.__uemail = configuration['Uemail']
        self.__ufname = configuration['Ufname']
        self.__ulname = configuration['Ulname']
        self.__upassword = configuration['Upassword']
        
        
        def insertUser(db,userData):
            userData['username'] = db.escape(userData['username'])
            userData['password'] = db.escape(userData['password'])
            
            return db.insert("INSERT INTO USERS (Uemail, Ufname, Ulname, Upassword) VALUES ('"
                             , userData["email"] , "','" , userData["fname"] , "','" 
                             , userData["lname"] ,"','" , userData["password"] , "')")
            
            