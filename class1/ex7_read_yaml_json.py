'''
7. Write a Python program that reads both the YAML file and the JSON file created in
exercise6 and pretty prints the data structure that is returned.
'''

import yaml
import json
from pprint import pprint as pp

with open("my_file.yml") as f_yaml:
    yaml_list = yaml.load(f_yaml)

with open("my_file.json") as f_json:
    json_list = json.load(f_json)

pp(yaml_list)
print
pp(json_list)
