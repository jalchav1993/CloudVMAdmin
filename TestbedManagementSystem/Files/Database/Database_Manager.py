from TestbedManagementSystem.Files.Database.UserDatabase import UserDatabase
from TestbedManagementSystem.Files.Database.AdminDatabase import AdminDatabase




class Database_Manager:
    dict = {'Uemail': 'test@test.com','Ufname': '', 
            'Ulname': '','Upassword':''}
    user = UserDatabase(dict)
    print(user.selectUser(dict))
    
    dict2 = {'Uemail': 'test@test.com','Ufname': 'testName', 
             'Ulname': 'testLastName','Upassword':'testPass'}
    user = UserDatabase(dict2)
    print(user.updateUser(dict2))
    print(user.resetPassword(dict2['Uemail'],'testPass'))
    print(user.removeUser(dict2))
    dict3 = {'Uemail': 'test2@test.com','Ufname': '2testName2', 
             'Ulname': '2testLastName2','Upassword':'2testPass2'}
    user.printAllUsers();
    user = UserDatabase(dict3)
    print(user.insertUser(dict3))
    user.printAllUsers();
    print(user.removeUser(dict3))
    user.printAllUsers();

    adDict = []
    adDict.append({'Aemail':'admin@test.com','dict':dict2})
    admin = AdminDatabase(adDict)
    admin.insertAdmin(adDict)