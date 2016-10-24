#!/usr/bin/env python

'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and 
prints out both the MIB2 sysName and sysDescr.
'''

from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161

routers = {'pynet-rtr1': '184.105.247.70',
           'pynet-rtr2': '184.105.247.71'}

OID_list = ('1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0')


def get_snmp_data(input_OID, device):

    snmp_data = snmp_get_oid(device, oid=input_OID)
    output = snmp_extract(snmp_data)

    return output


def main():

    for item in routers.items():

        hostname, ip_addr = item
        print "Hostname: %s" % hostname

        a_device = (ip_addr, COMMUNITY_STRING, SNMP_PORT)

        for oid_item in OID_list:

            print "OID: %s" % oid_item
            data = get_snmp_data(oid_item, a_device)
            print "Output is: \n\n%s" % data
            print

        print "---------------\n"


if __name__ == "__main__":
    main()