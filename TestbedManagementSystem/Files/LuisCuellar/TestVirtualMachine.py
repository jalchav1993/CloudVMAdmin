<<<<<<< HEAD
import virtualbox
from VirtualMachine import VirtualMachine

vmname = "test2"
vrdp = {'ip': "172.19.156.75", 'port': 8000}
networkAdapter = "testAdapter"
host = "172.19.156.75"

config = {"vmname": vmname, "vrdp": vrdp, "networkAdapter": networkAdapter, "host":host}

vm = VirtualMachine(config)
vm.startVM()
newClones = vm.clone(3)
=======
import virtualbox
from VirtualMachine import VirtualMachine

vmname = "test1"
vrdp = {'ip': "172.19.156.75", 'port': 8000}
networkAdapter = "testAdapter"
host = "172.19.156.75"

config = {"vmname": vmname, "vrdp": vrdp, "networkAdapter": networkAdapter, "host":host}

vm = VirtualMachine(config)
vm.startVM()
newClones = vm.clone(3)
>>>>>>> 60c5cc35dc452055da630d513ef02cf6a512d26d
