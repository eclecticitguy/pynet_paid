#!/usr/bin/env python

'''
Bonus Question - Redo exercise6 but have the SSH connections happen concurrently using
either threads or processes
'''

from netmiko import ConnectHandler
from getpass import getpass
from multiprocessing import Pool

def send_command(command):
    #router = ConnectHandler(**device)
    output = router.send_command(command)
    prompt = router.find_prompt()

    print "Device name: %s" % prompt
    print
    print output
    print


def main():

    password = getpass()

    pynet1 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.70',
        'username': 'pyclass',
        'password': password,
    }

    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': 'pyclass',
        'password': password,
    }

    juniper_srx = {
        'device_type': 'juniper',
        'ip': '184.105.247.76',
        'username': 'pyclass',
        'password': password,
        'secret': '',
    }

    pynet_rtr1 = ConnectHandler(**pynet1)
    pynet_rtr2 = ConnectHandler(**pynet2)
    srx = ConnectHandler(**juniper_srx)

    device_list = [pynet_rtr1, pynet_rtr2, srx]

    pool = Pool()

    pool.map(send_command, device_list)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
