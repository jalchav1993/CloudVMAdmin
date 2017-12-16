
import virtualbox
from time import sleep
from VirtualMachine import VirtualMachine

vmname = "vmTest"
vrdp = {'ip': "172.19.156.75", 'port': 8000}
networkAdapter = "testAdapter"
host = "172.19.156.75"

config = {"vmname": vmname, "vrdp": vrdp, "networkAdapter": networkAdapter, "host":host}

vm = VirtualMachine(config)
#sleep(5)
#vm.startVM()
sleep(5)
#vm.pauseVM()
#sleep(5)
newClones = vm.clone(3)