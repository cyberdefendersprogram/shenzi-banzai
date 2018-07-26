from OTXv2 import OTXv2
from pandas.io.json import json_normalize
from datetime import datetime, timedelta
import getopt
import sys
from sendemail import sendemail
from otx_tool import otx

def tools():
    
    # Takes user input for search and removes 'newline' character.
    search = str(input('Please enter search: '))
    search.strip()

    pulses = otx.search_pulses(search, 40) # Retrieves json list of top 40 pulses with tag <search>

    pulsefile = open('pulseIds.txt', "w+") # Creates and opens file to write pulse ID #'s to.

    with open('pulseIds.txt', "r+") as pulsefile: # Opens PulseIds for reading.
            pulseIdList = pulsefile.read()

    for singularPulse in pulses["results"]: # 
        name = singularPulse.get('name')
        description = singularPulse.get('description')
        modified = singularPulse.get('modified') 
        pulseid = singularPulse.get('id')

        if pulseid in pulseIdList:
            print("Threat has already been alerted")

        else:
            pulsefile = open('pulseIds.txt', "a+")
            pulsefile.write(pulseid+"\n")
            email = open('email.txt', "a+")
            email.write("Name: "+name+"\n"+"\n"+"Description: "+description+ "\n"+"\n"+"Modified: "+modified+"\n"+"\n"+"\n")  
    
    if pulseid not in pulseIdList:
        sendemail()
        email.close()
