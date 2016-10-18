'''
8. Write a Python program using ciscoconfparse that parses this config file. Note, this config file is not
fully valid (i.e. parts of the configuration are missing). The script should find all of the crypto map entries
in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print
out its children.
'''

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco_ipsec.txt')
crypto_map = config.find_objects(r"^crypto map CRYPTO")

for crypto in crypto_map:

    print crypto.text

    for child in crypto.children:
        print child.text

    print "!"

