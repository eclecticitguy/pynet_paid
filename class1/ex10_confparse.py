'''
10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
Print these entries and their corresponding transform set name.
'''

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco_ipsec.txt')
transform_name = config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO",
                                              childspec=r"set transform-set AES-SHA")

for entry in transform_name:
    print entry.text