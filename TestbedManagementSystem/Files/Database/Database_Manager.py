from TestbedManagementSystem.Files.Database.UserDatabase import UserDatabase
UserDatabase

class Database_Manager:
    dict = {'Uemail': 'test@test.com','Ufname': '', 
            'Ulname': '','Upassword':''}
    user = UserDatabase(dict)
    print(user.selectUser(dict))