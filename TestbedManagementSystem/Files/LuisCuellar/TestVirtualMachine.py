import virtualbox
from VirtualMachine import VirtualMachine

d = {"vmname": "testVM", "vrdp":"172.19.156.75:3389", "networkAdapter": "test", "host": "172.19.156.75"}
vm = VirtualMachine(d)
vm.startVM()