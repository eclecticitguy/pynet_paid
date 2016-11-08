#!/usr/bin/env python

import paramiko
from getpass import getpass
from time import sleep

ip_addr = '184.105.247.71'
username = 'pyclass'
#password = getpass()
password = '88newclass'
port = 22

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip_addr, username=username, password=password,
                        look_for_keys=False, allow_agent=False, port=port)

remote_conn = remote_conn_pre.invoke_shell()

remote_conn.send("terminal length 0\n")
remote_conn.send("show version\n")
sleep(2)
outp = remote_conn.recv(65535)

print outp