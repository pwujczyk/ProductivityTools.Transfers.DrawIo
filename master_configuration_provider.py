import json
import os

def get_master_configuration_value(key):
    masterconfiguration_path = os.getenv('MasterConfigurationPath')
    print(masterconfiguration_path)
    filepath = masterconfiguration_path + "ProductivityTools.MasterConfiguration.json"
    with open(filepath, encoding="utf-8-sig") as myfile:
        data = myfile.read()
        parsed_json = json.loads(data)
        x = parsed_json[key]
        return x