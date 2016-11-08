#!/usr/bin/env python

import pexpect
import sys
from getpass import getpass
import re

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    port = 22
    # password = getpass()
    password = '88newclass'

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout

    ssh_conn.timeout = 3
    
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
   
    ssh_conn.expect('pynet-rtr1#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('pynet-rtr1#')
    print ssh_conn.before
    
    # ssh_conn.sendline('terminal length 0')
    # ssh_conn.expect('pynet-rtr1#')

    '''
    You can catch errors using Try/Expect:

    try:
        ssh_conn.sendline('show version')
        ssh_conn.expect('zzzz')
    except pexpect.TIMEOUT:
        print "Found timeout"
    '''

    '''
    Pattern matching with regular expressions:

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)
    '''

if __name__ == "__main__":
    main()
