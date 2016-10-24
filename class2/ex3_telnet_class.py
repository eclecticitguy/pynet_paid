#!/usr/bin/env python
import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class TelnetConn(object):

    def __init__(self, ip_addr, username, password):

        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        try:
            self.remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

    def login(self):
        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        return output

    def send_command(self, cmd='\n', sleep_time=1):
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(sleep_time)
        return self.remote_conn.read_very_eager()

    def disable_paging(self, paging_cmd="terminal length 0"):
        return self.send_command(paging_cmd)

    def close_conn(self):
        return self.remote_conn.close()


def main():

    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    rtr1 = TelnetConn(ip_addr, username, password)
    rtr1.login()
    rtr1.send_command()
    rtr1.disable_paging()
    output = rtr1.send_command("show ip int brief")
    print output

    rtr1.close_conn()


if __name__ == "__main__":
    main()