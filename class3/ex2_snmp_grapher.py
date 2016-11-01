#!/usr/bin/env python

from snmp_helper import snmp_get_oid_v3,snmp_extract
from time import sleep
import pygal

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
SYS_DESC = '1.3.6.1.2.1.2.2.1.2.5'
IN_OCTETS = '1.3.6.1.2.1.2.2.1.10.5'
IN_PACKETS = '1.3.6.1.2.1.2.2.1.11.5'
OUT_OCTETS = '1.3.6.1.2.1.2.2.1.16.5'
OUT_PACKETS = '1.3.6.1.2.1.2.2.1.17.5'

DEBUG = False

def pull_data():

    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = ('184.105.247.70', SNMP_PORT)
    snmp_results = []

    for oid in (SYS_DESC, IN_OCTETS, IN_PACKETS, OUT_OCTETS, OUT_PACKETS):
        try:
            value = snmp_extract(snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=oid))
            snmp_results.append(int(value))
        except ValueError:
            snmp_results.append(value)

    return snmp_results

def pull_intf_data(input_type, input_stat):

    '''
    :param input_type: in_octet, in_packet, out_octet, out_packet
    :param input_stat: Input interface data used to compare against pulled SNMP data
    :return: Return the difference between the input_stat and the polled SNMP data (based on input_type)
    '''

    if input_type is "in_octet":
        return_stat = pull_data()[1]
        calc_stat = return_stat - input_stat
        return return_stat, calc_stat
    elif input_type is "in_packet":
        return_stat = pull_data()[2]
        calc_stat = return_stat - input_stat
        return return_stat, calc_stat
    elif input_type is "out_octet":
        return_stat = pull_data()[3]
        calc_stat = return_stat - input_stat
        return return_stat, calc_stat
    elif input_type is "out_packet":
        return_stat = pull_data()[4]
        calc_stat = return_stat - input_stat
        return return_stat, calc_stat
    else:
        return None, None

def main():

    input_octets = []
    input_packets = []
    output_octets = []
    output_packets = []

    # Initial pull of data used to calculate subsequent statistics
    int_name, in_octets_tmp, in_packets_tmp, out_octets_tmp, out_packets_tmp = pull_data()

    input_in_octets, calc_in_octets = pull_intf_data("in_octet", in_octets_tmp)
    input_in_packets, calc_in_packets = pull_intf_data("in_packet", in_packets_tmp)
    input_out_octets, calc_out_octets = pull_intf_data("out_octet", out_octets_tmp)
    input_out_packets, calc_out_packets = pull_intf_data("out_packet", out_packets_tmp)

    if DEBUG:
        print "\nInterface Stats = {0}".format(int_name)
        print "Input Octets = {0}".format(in_octets_tmp)
        print "Input Packets = {0}".format(in_packets_tmp)
        print "Output Octets = {0}".format(out_octets_tmp)
        print "Output Packets = {0}".format(out_packets_tmp)

    # Wait 10 seconds before pulling data again
    sleep(10)

    # Set initial time interval to 1
    interval = 1

    while interval <= 12:

        # Using previous interval data as input, pull data from SNMP
        input_in_octets, calc_in_octets = pull_intf_data("in_octet", input_in_octets)
        input_in_packets, calc_in_packets = pull_intf_data("in_packet", input_in_packets)
        input_out_octets, calc_out_octets = pull_intf_data("out_octet", input_out_octets)
        input_out_packets, calc_out_packets = pull_intf_data("out_packet", input_out_packets)

        # Store difference between previous internal and current interval into octet lists
        if (calc_in_octets is not None) \
                or (calc_in_packets is not None) \
                or (calc_out_octets is not None) \
                or (calc_out_packets is not None):

            input_octets.append(calc_in_octets)
            input_packets.append(calc_in_packets)
            output_octets.append(calc_out_octets)
            output_packets.append(calc_out_packets)

        print "Input Octets: %s" % input_octets
        print "Input Packets: %s" % input_packets
        print "Output Octets: %s" % output_octets
        print "Output Packets: %s" % output_packets
        print

        # Increment polling interval by 1
        interval += 1

        # Wait 5 minutes before polling data again
        sleep(300)

    # Create packet chart
    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Packets'
    line_chart.x_labels = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
    line_chart.add('InPackets', input_packets)
    line_chart.add('OutPackets', output_packets)
    line_chart.render_to_file('packets.svg')

    # Create octet chart
    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Octets'
    line_chart.x_labels = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
    line_chart.add('InOctets', input_octets)
    line_chart.add('OutOctets', output_octets)
    line_chart.render_to_file('octets.svg')


if __name__ == "__main__":
   main()