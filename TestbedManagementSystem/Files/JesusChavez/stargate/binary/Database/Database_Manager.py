from TestbedManagementSystem.Files.Database.AdminTable import AdminTable
from TestbedManagementSystem.Files.Database.CloneTable import CloneTable
from TestbedManagementSystem.Files.Database.NetworkAdapterTable import NetworkAdapterTable
from TestbedManagementSystem.Files.Database.ReferenceMaterialTable import ReferenceMaterialTable
from TestbedManagementSystem.Files.Database.RegUserTable import RegUserTable
from TestbedManagementSystem.Files.Database.ServerTable import ServerTable
from TestbedManagementSystem.Files.Database.StatisticTable import StatisticTable
from TestbedManagementSystem.Files.Database.UserTable import UserTable
from TestbedManagementSystem.Files.Database.VirtualMachineTable import VirtualMachineTable
from TestbedManagementSystem.Files.Database.WorkshopHistoryTable import WorkshopHistoryTable
from TestbedManagementSystem.Files.Database.WorkshopTable import WorkshopTable

class Database_Manager:  
#     
#     def createConfigList(self,colum,values):
#         config = dict(zip(colum, values))
#         return config
#       
#         
#     
#     values = ["Admin1","Admin@Email.com","AdminName","AdminLast","AdminPass"]   
#     colum = AdminTable.getAdminColums(None)
#     config = createConfigList(None,colum,values)
#       
#     print (config) 
#     print(config['Aemail'])   