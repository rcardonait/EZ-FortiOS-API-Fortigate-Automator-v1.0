from datetime import datetime
import requests
import string
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('fortigateinventory.txt') as devices_file:
    firewalls = devices_file.readlines()

with open('apicall.txt') as api_file:
    apiaction = api_file.readlines()

with open('apipushobject.json') as api_json:
    apiexecute=json.load(api_json)

date = datetime.now().strftime("%y-%m-%d-%M")
date1 = datetime.now().strftime("%B %d, %Y")

for line in firewalls:
    line = line.strip("\n")
    hostname = line.split(",")[0]
    ipaddr = line.split(",")[1]
    port = line.split(",")[2]
    token = line.split(",")[3]
    vdom = line.split(",")[4]

    for line in apiaction:
        line = line.strip("\n")
        context = line.split(",")[0]
        option = line.split(",")[1]

        api_url = r'https://'+ipaddr+':'+port+'/api/v2/cmdb/'+context+'/'+option+'/'+name+'/?access_token='+token
        print(api_url)
        r = requests.delete(api_url, data=json.dumps(apiexecute), verify=False)
        out_file = r.text
        save = open('result.json', 'w')
        print(out_file, file=save)
        save.close()
        print(out_file)
        print(apiexecute)

print('*' * 20)
print('Job Completed!!')
print('*' * 20)