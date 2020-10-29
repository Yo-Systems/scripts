import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'username', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.72')
iosvl2.load_merge_candidate(filename='ACL1.cfg')
iosvl2.commit_config()
iosvl2.close()