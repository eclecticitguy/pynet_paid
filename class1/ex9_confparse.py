'''
9. Find all of the crypto map entries that are using PFS group2
'''

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco_ipsec.txt')
pfs_group2 = config.find_objects_w_child(parentspec=r"^crypto map CRYPTO",
                                         childspec=r"pfs group2")

for entry in pfs_group2:
    print entry.text