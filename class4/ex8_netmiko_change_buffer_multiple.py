#!/usr/bin/env python

'''
Use Netmiko to enter into configuration mode on pynet-rtr2.
Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).
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

    pynet_rtr1 = ConnectHandler(**pynet1)
    pynet_rtr2 = ConnectHandler(**pynet2)

    device_list = [pynet_rtr1, pynet_rtr2]

    for device in device_list:

        prompt = device.find_prompt()
        logging = device.send_command("show run | inc logging")

        print
        print "Device name: %s" % prompt
        print "Before:"
        print logging
        print

        device.config_mode()
        device.send_config_from_file(config_file='ex8_config_file.txt')
        device.exit_config_mode()

        logging = device.send_command("show run | inc logging")
        print "After:"
        print logging
        print

if __name__ == "__main__":
    main()