from WorkshopManager import WorkshopManager
from HardwareManager import HardwareManager
from time import sleep
import sys

vm1 = {"vmname": "vmTest", "vrdp": {'ip': "172.19.156.75", 'port': 8000}, "networkAdapter": "testAdapter", "host":"172.19.156.75"}
vm2 = {"vmname": "vmUnitTest", "vrdp": {'ip': "172.19.156.75", 'port': 4000}, "networkAdapter": "testAdapter", "host":"172.19.156.75"}

vms = {vm1['vmname'], vm2['vmname']}

unit1 = {"unitName": "unit1", "vms": vms, "description": "desc", "referenceMaterial": "filename.txt",
         "connectionString": "172.19.156.75", "sessionType": "persistent", "status": "available"}



hwmgr = HardwareManager()
wsmgr = WorkshopManager()

line = ""

while( line != "EXIT"):
    line = input()
    if(line == "Add VMs"):
        hwmgr.addVirtualMachine(vm1)
        hwmgr.addVirtualMachine(vm2)
        
    elif(line == "Add Unit"):
        wsmgr.addWorkshopUnit(unit1)
    elif(line == "Start Unit"):
        wsmgr.startUnit( "unit1")
    elif(line == "Pause Unit"):
        wsmgr.pauseUnit("unit1")
    elif(line == "Resume Unit"):
        wsmgr.resumeUnit("unit1")
    elif(line == "Power Down Unit"):
        wsmgr.power_downUnit("unit1")
        
        
    elif(line == "Add Group"):
        newUnits = wsmgr.cloneUnit("unit1", 2)
        ws1 = {"groupName": "group1", "associatedUnits": newUnits, "description": "desc", "referenceMaterial": "filename.txt",
               "sessionType": "persistent", "endDate": "12/15/2017", "status": "available"}        
        wsmgr.addWorkshopGroup(ws1)
        
    elif(line == "Start Group"):
        wsmgr.startGroup( "group1")
    elif(line == "Pause Group"):
        wsmgr.pauseGroup("group1")
    elif(line == "Resume Group"):
        wsmgr.resumeGroup("group1")
    elif(line == "Power Down Unit"):
        wsmgr.power_downGroup("group1")
    else:
        break