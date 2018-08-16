import requests
import datetime
import getopt
import sys
from urllib.request import urlopen, base64
from requests.auth import HTTPBasicAuth
from pandas.io.json import json_normalize


try: # Handles user input options.
    opts = getopt.getopt(sys.argv[1:],"hdtmiavro")
    opts = opts[1][0:]
    options = []
    for opt in opts:
        if opt=='h':
            print("\n"+"AVAILABLE OPTIONS: h:help d:description t:risk level d:reported s: solution\n\ni.e: python3 xfo_tool.py d l r")
            print()
            sys.exit()
        elif opt=='d':
            options.append('description')
        elif opt=='l':
            options.append('risk_level')
        elif opt=='r':
            options.append('reported')
        elif opt=='s':
            options.append('remedy')
except getopt.GetoptError:
    print("\n"+"python3 xfo_tool.py h for help"+"\n")
    sys.exit()
 
def user_authentication():
    api_key = 'API KEy'
    auth_pass = 'Password'
    search = str(input('Please enter search: '))
    s = search.strip()
    response = requests.get('https://api.xforce.ibmcloud.com/vulnerabilities/fulltext?q='+str(s), auth=HTTPBasicAuth(api_key, auth_pass))
    data = response.json()

    for singleResponse in data["rows"]:
        print('[+] '+'Name: '+singleResponse.get('title')+'\n')

        for switch in options:
            try:
                print('[+] '+switch.title()+': '+singleResponse.get(switch)+'\n')
            except:
                print()
        print('-'*30)

user_authentication()
