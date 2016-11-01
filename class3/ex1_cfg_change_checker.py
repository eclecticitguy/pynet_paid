#!/usr/bin/env python

from snmp_helper import snmp_get_oid_v3,snmp_extract
from time import localtime, asctime

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_UPTIME = '1.3.6.1.2.1.1.3.0'
RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
SYS_TIME_SEC = 100
DEBUG = True

class NetworkDevice(object):

    def __init__(self, device_name, uptime, last_changed, config_changed=False):

        self.device_name = device_name
        self.uptime = uptime
        self.last_changed = last_changed
        self.config_changed = config_changed

def main():
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'

    pynet_rtr1 = ('184.105.247.70', SNMP_PORT)
    pynet_rtr2 = ('184.105.247.71', SNMP_PORT)

    snmp_user = (a_user, auth_key, encrypt_key)

    for a_device in (pynet_rtr1, pynet_rtr2):
        snmp_results = []
        for oid in (SYS_NAME, SYS_UPTIME, RUN_LAST_CHANGED):
            try:
                value = snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=oid))
                snmp_results.append(int(value))
            except ValueError:
                snmp_results.append(value)

        device_name, uptime, last_changed = snmp_results

        if DEBUG:
            print "\nConnected to device = {0}".format(device_name)
            print "Last changed timestamp = {0}".format(last_changed)
            print "Uptime = {0}".format(uptime)



if __name__ == "__main__":
   main()



