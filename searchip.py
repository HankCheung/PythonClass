import ssl
import  json
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
ip = "124.127.207.144"
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query="+ip+"&co=&resource_id=6006&t=1500565564095&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110209007437794934958_1500565535745&_=1500565535753"
print(url)
get_data = urllib.request.urlopen(url)
answer_data ='{'+ get_data.read().decode("gbk").split("({")[1].split(');')[0]
json_data = json.loads(answer_data)["data"][0]['location']

print(json_data)