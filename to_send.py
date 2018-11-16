from OTXv2 import OTXv2
from pandas.io.json import json_normalize
from datetime import datetime, timedelta
import getopt
import sys
from sendemail import sendemail
from main import otx
import csv
import pandas as pd
from pandas import read_csv
import os.path

def tools():

    search = str(input('Please enter search: '))
    search.strip()
    pulsesJSON = otx.search_pulses(search, 40) # Retrieves list (in json format) of top 40 pulses with tag "crypto"

 # Loops through each individual pulse retrieved from OTX, and prints name & requested fields.

    for aPulse in pulsesJSON["results"]:
         
        name = aPulse.get('name')
        description = aPulse.get('description')
        modified = aPulse.get('modified') 
        pulseid = aPulse.get('id')

        '''
        If needed, add more categories to pull for each pulse here.
        '''
        
        #list with data to add to csv file
        raw_data = [{'Pulse ID': pulseid, 'Name': name, 'Description': description, 'Modified': modified}]

        #the path to the file
        filename = 'shenzi_pulses.csv'
        
        #use to check for the file
        #file_exists = os.path.isfile(filename)
        
        #opens the file to append ID, Name, Modified, Description
        with open(filename, "w") as csv_file:
            csv_columns_headers = ['Pulse ID','Name','Description','Modified']
            writer = csv.DictWriter(csv_file, delimiter=',',lineterminator='\n', fieldnames=csv_columns_headers)
            #if file does not exist write the headers
            if not file_exists:
                writer.writeheader()
            #write the information from raw_data by rows
            else:
                for data in raw_data:
                    writer.writerow(data)

        #simple option to email or quit 
    option = input('1: To Email 2: To quit : ')
    
    option = int(option)
    
    if option == 1:
        #uses the email function to send email
        sendemail()
        #delete file once email has sent
        os.remove('pulseIdsList.csv')
    elif option == 2:
        #option to quit
        SystemExit()      
