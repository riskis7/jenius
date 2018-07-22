#!/data/data/com.termux/files/bin/python

#Importing Modules \(o,,,o)/

import argparse

import requests, json

import sys

from sys import argv

import os

#Arguments *_*

 

parser = argparse.ArgumentParser()

 

parser.add_argument("-t",help = "target ip address", type=str, dest = 'target', required=True)

 

args = parser.parse_args() 

 

#I love Colors !

lightblue='\033[94m'

lightgreen='\033[92m'

clear ='\033[0m'

boldblue='\033[01m''\033[94m'

cyan='\033[36m'

bold = '\033[01m'

red='\033[31m'

lightcyan='\033[96m'

yellow='\033[93m'

#Clear The Terminal

os.system('clear')

#Banner

print (bold+cyan+"""

[.. [....... [........ [.. [..[......

[.. [.. [.. [.. [.. [..[[[[[[[[........

[.. [.. [.. [.. [.. [..

[.. [....... [..... [...... [..

[.. [.. [.. [..

[.. [.. [.. [..

[.. [.. [.. [..

"""+clear)

print (lightcyan+bold+"[ Written By Riskis_7 ] | [Youtube:M Riski Akbar]\n"+clear)

 

ip = args.target

#Let's Begin

api = "https://api.ipdata.co/"

#Sending Requests And Getting Data

try :

	data = requests.get(api+ip).json()

	sys.stdout.flush()

	a = yellow+bold+"[~]"

	#Printing,Not Phising ; P

	#print(a,"Target:",data['ip'])

	print(a,"ISP:",data['organisation'])

	print(a,"City:",data['city'])

	print(a,"Region:",data['region'])

	print(a,"Latitude:",data['latitude'])

	print(a,"Longitude:",data['longitude'])

	print(a,"Tor:",data['threat']['is_tor'])

	print(a,"Proxy:",data['threat']['is_proxy'])

	print(a,"Calling Code:",data['calling_code'])

	print(a,"Currency:",data['currency']['name'])

	print(a,"Timezone:",data['time_zone']['offset'])

	print(a,"Continent Name :",data['continent_name'])

	print(" "+clear)

#Error Handling

except KeyboardInterrupt:

print ('Exiting,Good Bye'+clear)

sys.exit(0)

except requests.exceptions.ConnectionError as e:

print (red+bold+"[!]"+" Please Check Your Internet Connection!"+clear)

sys.exit(1)

#Done!

