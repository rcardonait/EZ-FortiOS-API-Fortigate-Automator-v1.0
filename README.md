# EZ-FortiOS-API-Fortigate-Automator
By Rene Cardona www.rcitnet.com
#
A Fortigate FortiOS API Automation-Script. 
Easy to use! - Automate bulk configs in seconds reading excel files.
#
Very simple yet powerful! It uses FortiOS API to perform the instructions
over HTTPS. Make sure your fortigate interface is admin enabled over https.
#
First you need to generate an API token for your appliance.
On your fortigate create an API Admin
once configured it will generate a token and display it
save it, you will need it for this automator to work.

#
1- Setup Environment

Download all files in this git then execute :modules-install.sh
 Allow this to run on your linux box:
 #
   chmod 755 modules-install.sh
 #
 then run script:
#
 ./modules-install.sh
#
It will install the following pre-requesites:
![Modules](/images/API-Modules-FortiOS-1.JPG)
#
2- Run the FortiOS Automator Module.
The Automator is composed of 3 items.
#
- An inventory file : fortigateinventory.txt
#
 You can list endless Fortigates to configure
 on one shot.
 if you need to add fortigates to the file,
 please follow this syntax, everything separated with ","
 #
 hostname,IPADDRESS,PORT,API-TOKEN,vDOM
#
 Example:
 #
 Firewall1,10.10.20.49,8443,95x7srqd0djHsGd2d345f8wr8yy,root
 #
- An API Action file : api-call.txt
!
This file will contain the respective section in the Fortigate
database. Depending on what you need to autoconfigure, you'll
need the right location in hardware to push the configuration.
(Refer to the Fortinet's API documentation for location specifics.)

#
Example if I need to configure address objects:
 firewall,address

- Use one of the scripts to perform the each API function:

GET -- PUT -- POST -- DELETE
#
GET :  FortigateAPI-GET-Module-to-EXCEL.py

- This module reads an API location and extracts its data, it then
parses out into an excel file that will be stored on the same working directory.
#
PUT : FortigateAPI-PUT-Module-from-EXCEL.py

- This module updates an existing object on the fortigate via API.
it will use an excel spreadsheet populated with all objects.
the column name will be called in a for loop to perform the update
for each data row. XLS file must be in script's working directory.




Example:





