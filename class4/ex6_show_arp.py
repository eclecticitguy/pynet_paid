#!/usr/bin/env python

'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
'''

from netmiko import ConnectHandler
from getpass import getpass


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

    print

    for device in device_list:

        prompt = device.find_prompt()
        outp = device.send_command("show arp")

        print "Device name: %s" % prompt
        print
        print outp
        print

if __name__ == "__main__":
    main()
