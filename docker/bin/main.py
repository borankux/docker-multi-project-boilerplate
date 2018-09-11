import yaml
import json
import re
import os
from dotenv import load_dotenv


docker = yaml.load(open('../docker-compose.yml', 'r'))
services=docker['services']
json_config = json.dumps(docker, indent=4)
#open('docker-compose.json', 'w').write(json_config)

env_path = '../.env'
env = load_dotenv(dotenv_path=env_path)


def clear_env(key):
	return key[2:len(key)-1]

def env(key):
	return os.getenv(key)

#\${[A-Z_]{1,60}\}
keys = re.findall(r'\${[A-Z_]{1,60}\}', json_config)
for k in keys:
	val = env(clear_env(k))
	json_config = json_config.replace(k,val)

print(json_config)