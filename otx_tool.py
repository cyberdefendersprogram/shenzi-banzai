from OTXv2 import OTXv2
from pandas.io.json import json_normalize
from datetime import datetime, timedelta
import getopt
import sys
from sendemail import sendemail

time = str(datetime.now() - timedelta()) # Time at which script was initiated.

try: # Handles user input options.
    opts = getopt.getopt(sys.argv[1:],"hdtmiavro")
    opts = opts[1][0:]
    options = []
    for opt in opts:
        if opt=='h':
            print("\n"+"AVAILABLE OPTIONS: s:search h:help d:description t:tags m:modified i:id a:author_name \nv:adversary r:references o:revisions\n\ni.e: python3 otx_blkchn.py d n r")
            print()
            sys.exit()
        elif opt=='d':
            options.append('description')
        elif opt=='s':
            userSearch = str(input('Please enter search query: '))
            userSearch.strip()
        elif opt=='t':
            options.append('tags')
        elif opt=='m':
            options.append('modified')
        elif opt=='i':
            options.append('id')
        elif opt=='a':
            options.append('author_name')
        elif opt=='v':
            options.append('adversary')
        elif opt=='r':
            options.append('references')
        elif opt=='o':
            options.append('revisions')
except getopt.GetoptError:
    print("\n"+"python3 otx_blkchn.py h for help"+"\n")
    sys.exit()

otx = OTXv2("e89676d6a1d9333168218175d7576abc24d33c0a1d20504e56a1151497146d14") # Initializes session with OTXv2 API using API key

if 's' in opts: # Handles 'search' option, with 'crypto' as the default search query
    x = userSearch
else:
    x = "crypto"

pulses = otx.search_pulses(x, 40) # Retrieves list (in json format) of top 40 pulses with tag "crypto"

with open('pulseid.txt', "r") as pulsefile: # Reads text file pulse id 
    pulsesid = pulsefile.read()

def pulse_print(): # Loops through each individual pulse retrieved from OTX, and prints name & requested fields.
    for singularPulse in pulses["results"]:
        print('[+] '+'Pulse Name: '+singularPulse.get('name')+'\n')
        for switch in options:
            try:
                print('[+] '+switch.title()+': '+singularPulse.get(switch)+'\n')
            except:
                print()
        print('-'*30)

    print()
    print("\n"+"AVAILABLE OPTIONS: s:search h:help d:description t:tags m:modified i:id a:author_name \nv:adversary r:references o:revisions\n\ni.e: python3 otx_blkchn.py d n r")
    print()
   
    '''
    pulls information from the results of the otx api
    writes to a txt file and checks to see if the threat
    has already been sent. By checking the pulseid in pulsesid
    '''  
    for singularPulse in pulses["results"]:

        name = singularPulse.get('name')
        description = singularPulse.get('description')
        modified = singularPulse.get('modified') 
        pulseid = singularPulse.get('id')
        if pulseid in pulsesid:
            print("Threat has already been alerted")
        else:
            with open('pulseid.txt', "a") as pulsefile:
                pulsefile.write(pulseid + "\n")
            with open('email.txt', "a") as pulsefile:
                pulsefile.write("Name: " +name+ "\n"+"\n" +"Description: " +description+ "\n"+"\n" +"Modified: " +modified+ "\n"+"\n"+"\n")  
   
    if pulseid not in pulsesid:
        sendemail()
        open('email.txt', "w").close()

print()
print("DATE AND TIME: " + time + "\n")
print('-'*30)
print()


'''       
try:
    pulse_print()
except TypeError:
    print("\n"+"python3 otx_blkchn.py h for help"+"\n")
    sys.exit()
'''
