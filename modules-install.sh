#!/bin/bash
#packages

apt-get install python-pip
echo "Hi, $USER !"
echo "Installing Python Modules..."
echo "Installing datetime"
python -m pip install datetime
echo "Installing requests"
python -m pip install requests
echo "Installing urllib3"
python -m pip install urllib3
echo "Installing xlrd"
python -m pip install xlrd
echo "Installing pandas"
python -m pip install pandas
echo "Installing xlwt"
python -m pip install xlwt
echo "**********************"
echo "Auto-Install Completed"
echo "**********************"
