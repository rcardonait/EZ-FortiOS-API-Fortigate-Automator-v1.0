# EZ-FortiOS-API-Fortigate-Automator
A Fortigate FortiOS API Automation-Script. Easy to use! - Automate bulk configs in seconds reading excel files.

Very simple yet powerful!
#
1- Setup Environment

On this git download the file :modules-install.sh
Allow this to run on your linux box:
chmod 755 modules-install.sh
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
!
 You can list endless Fortigates to configure
 on one shot.
 if you need to add fortigates to the file,
 please follow this syntax, everything separated with ","
 hostname,IPADDRESS,PORT,API-TOKEN,vDOM
 Example:
 Firewall1,10.10.20.49,8443,95x7srqd0djHsGd2d345f8wr8yy,root
 
- An API Action file : api-call.txt
!
This file will contain the respective section in the Fortigate
database. Depending on what you need to autoconfigure, you'll
need the right location in hardware to push the configuration.
(Refer to the Fortinet's API documentation for location specifics.)


Example if I need to configure address objects:
firewall,address







