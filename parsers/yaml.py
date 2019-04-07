import yaml

def Get_config(ConfigFile):
 d={}
 document = open(ConfigFile, 'r')
 parsed = yaml.load(document, Loader=yaml.FullLoader)

# print("--------Load-Config---------")
# print(yaml.dump(parsed))

# load external config at file "config.yaml"
 for key,value in parsed.items():
  if key == "namevar1":
   d['namevar1']=value
  if key == "namevar2":
   d['namevar2']=value
 return d
