#!/usr/bin/env python

'''
Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
Verify this change by examining the output of 'show run'.
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

    ssh_conn.sendline('show run | inc logging')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('configure term')
    ssh_conn.expect('pynet-rtr2')
    print ssh_conn.before

    ssh_conn.sendline('logging buffered 20000')
    ssh_conn.expect('pynet-rtr2')
    print ssh_conn.before

    ssh_conn.sendline('end')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before

    ssh_conn.sendline('show run | inc logging')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before


if __name__ == "__main__":
    main()