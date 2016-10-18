'''
6. Write a Python program that creates a list.
One of the elements of the list should be a dictionary with at least two keys.
Write this list out to a file using both YAML and JSON formats.
The YAML file should be in the expanded form.
'''

import yaml
import json

my_list = range(8)
my_list.append({})
my_list[-1]['ip_addr'] = '192.168.1.1'
my_list[-1]['attribs'] = range(6)

with open("my_file.yml", "w") as f_yaml:
    f_yaml.write(yaml.dump(my_list, default_flow_style=False))

with open("my_file.json", "w") as f_json:
    json.dump(my_list, f_json)
