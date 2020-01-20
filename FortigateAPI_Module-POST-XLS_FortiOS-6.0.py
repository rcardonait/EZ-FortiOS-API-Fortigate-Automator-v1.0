from datetime import datetime
import requests
import string
import urllib3
import json
import xlrd
import pandas as pd
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('fortigateinventory.txt') as devices_file:
    firewalls = devices_file.readlines()

with open('api-call.txt') as api_file:
    apiaction = api_file.readlines()

df = pd.read_excel('addresses.xls', sheet_name='Sheet1')

name = df['name'].values.tolist()
start = df['start-ip'].values.tolist()
end = df['end-ip'].values.tolist()

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
        i = 0
        for i, (a, b, c) in enumerate(zip(name, start, end)):
            namevar = a
            startvar = b
            endvar = c
            data1 = {"name": namevar, "type": "ipmask", "start-ip": startvar, "end-ip": endvar}
            i += 1
            api_url = r'https://'+ipaddr+':'+port+'/api/v2/cmdb/'+context+'/'+option+'/?access_token='+token
            print('Performing API Request to '+ hostname)
            r = requests.post(api_url, data=json.dumps(data1), verify=False)

print('*' * 20)
print('Job Completed!!')
print('*' * 20)