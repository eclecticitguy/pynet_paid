import paramiko
from getpass import getpass
from time import sleep

ip_addr = '184.105.247.70'
username = 'pyclass'
password = getpass()
port = 22

remote_conn_pre = paramiko.SSHClient()

# Instruct Paramiko to ignore SSH invalid host keys and automatically add 
# any missing or incorrect keys, however, this is a security issue.
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Load system SSH known hosts file
# remote_conn_pre.load_system_host_keys()

# Load known hosts file from specific directory
# remote_conn_pre.load_host_keys("/home/wblack/.ssh/known_hosts")

remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

# Confirm SSH connection on server using Netstat
'''
(applied_python)[wblack@ip-172-30-0-10 ~]$ netstat -an | grep 184.105
tcp        0      0 172.30.0.10:54828           184.105.247.70:22           ESTABLISHED 
'''

remote_conn = remote_conn_pre.invoke_shell()

# Receive up to 5000 bytes of data from device using SSH connection
# outp = remote_conn.recv(5000)

# Maximum amount of data that can be read is 65535. If more than 65535 bytes of data, need to use while loop
# and recv_ready() method to continually read until method returns False.
# outp = remote_conn.recv(65535)

# Send command to SSH device and receive data back
remote_conn.send("show ip int brief\n")

# Must sleep for a second to give device time to respond
sleep(1)
outp = remote_conn.recv(5000)
print outp

# Good practice is to set timeout in case there is no data to receive
# remote_conn.settimeout(6.0)

# Determine if there is any data available to read. Returns True or False.
# remote_conn.recv_ready()
