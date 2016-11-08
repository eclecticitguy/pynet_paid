#!/usr/bin/env python

'''
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
'''

import pexpect
import sys
from getpass import getpass
import re

def main():

    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22
    # password = getpass()
    password = '88newclass'

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    ssh_conn.timeout = 3

    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('pynet-rtr2#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before

if __name__ == "__main__":
    main()