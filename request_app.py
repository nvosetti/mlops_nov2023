import requests
import json
import yaml

def read_params(config_path) :
    with open(config_path) as yaml_file :
        config = yaml.safe_load(yaml_file)
    return config

if __name__ == "__main__" :
    config = read_params("params.yaml")
    json_file = open(config["request_param_file"])
    url = config["url"]
    myobj = json.load(json_file)
    x = requests.post(url, json = myobj)

    print(x.text)

