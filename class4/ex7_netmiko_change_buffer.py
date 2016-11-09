#!/usr/bin/env python

'''
Use Netmiko to enter into configuration mode on pynet-rtr2.
Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).
'''

from netmiko import ConnectHandler
from getpass import getpass


def main():

    #password = getpass()
    password = '88newclass'

    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': 'pyclass',
        'password': password,
    }

    pynet_rtr2 = ConnectHandler(**pynet2)

    # Confirm current buffering
    log_buffer = pynet_rtr2.send_command("show run | inc logging")
    print log_buffer

    # Enter configuration mode
    pynet_rtr2.config_mode()

    # Change buffering
    pynet_rtr2.send_command("logging buffered 30000")

    # Exit out of config mode
    pynet_rtr2.exit_config_mode()

    # Confirm buffering has changed
    log_buffer = pynet_rtr2.send_command("show run | inc logging")
    print log_buffer

if __name__ == "__main__":
    main()