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

 # Loops through each individual pulse retrieved from OTX, and prints name & requested fields.
    '''
    pulls information from the results of the otx api
    writes to a txt file and checks to see if the threat
    has already been sent. By checking the pulseid in pulsesid
    '''
    with open('pulseIds.txt', "r+") as pulsefile: # Reads text file pulse id 
            pulseIdList = pulsefile.read()  
    for singularPulse in pulses["results"]:
         
        name = singularPulse.get('name')
        description = singularPulse.get('description')
        modified = singularPulse.get('modified') 
        pulseid = singularPulse.get('id')
        if pulseid in pulseIdList:
            print("Threat has already been alerted")
        else:
            pulsefile = open('pulseIds.txt', "a+")
            pulsefile.write(pulseid + "\n")
            pulsefile2 = open('email.txt', "a+")
            pulsefile2.write("Name: " +name+ "\n"+"\n" +"Description: " +description+ "\n"+"\n" +"Modified: " +modified+ "\n"+"\n"+"\n")  
    
    
    
    if pulseid not in pulseIdList:
        sendemail()
        open('email.txt', "w").close()
