#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

#password = getpass()
password = '88newclass'

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
#pynet_rtr2 = ConnectHandler(**pynet2)
#srx = ConnectHandler(**juniper_srx)

# Print router prompt
print pynet_rtr1.find_prompt()

# Enter configuration mode
pynet_rtr1.config_mode()

# Check that router is in configuration mode
print pynet_rtr1.check_config_mode()
print pynet_rtr1.find_prompt()

# Exit out of config mode and confirm
pynet_rtr1.exit_config_mode()
print pynet_rtr1.find_prompt()

# Send various commands to routers. Disable paging enabled by default
outp = pynet_rtr1.send_command('show ip int brief')
print outp

outp = pynet_rtr1.send_command('show version')
print outp

outp = pynet_rtr1.send_command('show run | inc logging')
print outp

# Change configuration must use list
config_commands = ['logging buffered 19999']
output = pynet_rtr1.send_config_set(config_commands)
print output

# Check that the commands were changed
outp = pynet_rtr1.send_command('show run | inc logging')
print outp
