import yaml,json,re,os
from dotenv import load_dotenv


docker = yaml.load(open('original-compose.yml', 'r'))
services=docker['services']
json_conf= json.dumps(docker, indent=4)

env_path = '../.env'
env = load_dotenv(dotenv_path=env_path)
mustach_pattern = r'\${[A-Z_]{1,60}\}'

def clear_env(key):
	return key[2:len(key)-1]

def env(key):
	return os.getenv(key)

#\${[A-Z_]{1,60}\}
keys = re.findall(mustach_pattern, json_conf)
for k in keys:
	val = env(clear_env(k))
	json_conf = json_conf.replace(k,val)

# save the json format file
open('docker-compose.json', 'w').write(json_conf)

yaml_file = open('../docker-compose.yml', 'w')
yaml.dump(json.loads(json_conf), yaml_file)
yaml_file.close()


# for service in docker['services']:
# 	if (docker['services'][service]['image'] == 'mirzatsoft/nginx'):
# 		s = docker['services'][service]
		

nginx_conf_file = open('./nginx.template','r').read()
nginx_conf_json = json.loads(nginx_conf_file)
nginx_keys = re.findall(mustach_pattern, nginx_conf_file)
# for nk in nginx_keys:
print(os.getenv())