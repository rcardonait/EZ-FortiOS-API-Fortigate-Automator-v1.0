from datetime import datetime
import requests
import string
import pandas as pd
import csv
import json
import xlwt
import time
from pandas.io.json import json_normalize
from pandas import np
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('fortigateinventory.txt') as devices_file:
    firewalls = devices_file.readlines()

with open('api-call.txt') as api_file:
    apiaction = api_file.readlines()

date = datetime.now().strftime("%m-%d-%y")
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

        api_url = r'https://'+ipaddr+':'+port+'/api/v2/cmdb/'+context+'/'+option
        headers = {'Authorization': 'Bearer'+ token}
        print("!" * 32)
        time.sleep(3)
        print('Performing API Request to: ')
        print(hostname+' Address: '+ipaddr)
        print('Port: '+port)
        print("#" * 32)
        print('')
        print("Extracting "+option+ ' objects...')
        print('')
        time.sleep(4)
        r = requests.get(api_url, verify=False, headers=headers)
        out_file = r.text
        save = open('working.json', 'w')
        print(out_file, file=save)
        save.close()
        # Convert JSON RAW TO CSV

        with open('working.json') as data_file:
            data = json.load(data_file)

        df = json_normalize(data, 'results')
        df2 = pd.DataFrame(df, columns=['name', 'subnet', 'start-ip', 'end-ip'])
        df2.to_excel(hostname+"_"+option+"_"+date+".xls", index=False, encoding="utf-8")
print('*' * 32)
print('Task Completed Successfully')
print('*' * 32)
print('Please find output excel file:')
print(hostname+"_"+option+"_"+date+".xls")
print('on current working folder')
print('*' * 32)