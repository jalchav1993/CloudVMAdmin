from WorkshopManager import WorkshopManager
from HardwareManager import HardwareManager
from time import sleep

vm1 = {"vmname": "vmTest", "vrdp": {'ip': "172.19.156.75", 'port': 8000}, "networkAdapter": "testAdapter", "host":"172.19.156.75"}
vm2 = {"vmname": "vmUnitTest", "vrdp": {'ip': "172.19.156.75", 'port': 4000}, "networkAdapter": "testAdapter", "host":"172.19.156.75"}

vms = {vm1['vmname'], vm2['vmname']}

unit1 = {"unitName": "unit1", "vms": vms, "description": "fuck", "referenceMaterial": "fuck.txt",
         "connectionString": "something", "sessionType": "persistent", "status": "available"}

hwmgr = HardwareManager()
wsmgr = WorkshopManager()

hwmgr.addVirtualMachine(vm1)
hwmgr.addVirtualMachine(vm2)

wsmgr.addWorkshopUnit(unit1)

#wsmgr.startUnit( "unit1")
#sleep(5)
#wsmgr.pauseUnit("unit1")
#sleep(5)
#wsmgr.resumeUnit("unit1")
#sleep(5)
#wsmgr.power_downUnit("unit1")

newUnits = wsmgr.cloneUnit("unit1", 2)
print( len(newUnits) )

ws1 = {"groupName": "group1", "associatedUnits": newUnits, "description": "fuck", "referenceMaterial": "fuck.txt",
       "sessionType": "persistent", "endDate": "12/15/2017", "status": "okayFam"}

wsmgr.addWorkshopGroup(ws1)

sleep(5)

wsmgr.startGroup("group1")