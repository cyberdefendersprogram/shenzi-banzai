import os
import sys
import requests
import datetime
from urllib.request import urlopen, base64
from requests.auth import HTTPBasicAuth
import json
import csv
import xconfig
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
from sendemail import sendemail 
from IPython.display import HTML


class xForce:
    # x = key # y = pass z = path
    def user_authentication(self, x, y, interest):
        #Currently search works for ethereum, crypto, bitcoin 
        valid_words = ['ethereum', 'crypto', 'bitcoin']
        #self.search = str(input('Please enter search: '))
        self.s = interest
        
        if self.s not in valid_words:
            print("Not a Key Word")
        else:
        
            self.api_key = x
            self.auth_pass = y
            self.response = requests.get('https://api.xforce.ibmcloud.com/vulnerabilities/fulltext?q='+str(self.s), auth=HTTPBasicAuth(self.api_key, self.auth_pass))
            self.data = self.response.json()
            
            #response message 
            #<200> = Proper authentication
            #<400> = Invalid API key format
            #<401> = Unauthorized
            #<404> = Not found

            print(self.response)
    def xforce_csv(self, z):
        for singleResponse in self.data["rows"]:
            self.id = singleResponse.get("updateid")
            self.title = singleResponse.get("title")
            self.desc = singleResponse.get("description")
            self.risk = singleResponse.get("risk_level") 
            self.solution = singleResponse.get("remedy") 
            self.reported = singleResponse.get("reported") 
            
            self.date = datetime.datetime.strptime(self.reported,"%Y-%m-%dT%H:%M:%SZ").strftime('%m/%d/%Y')
            
            self.raw_data = [{'Title':self.title,'Risk level':self.risk, 'Reported':self.date, 'Description':self.desc, 'Solution': self.solution}]

            #the path to the file
            self.filename = z
            #use to check for the file
            self.file_exists = os.path.isfile(self.filename)
            #opens the file to append ID, Name, Modified, Description
            with open(self.filename, "a") as self.csv_file:
                self.csv_columns_headers = ['Title','Risk level','Reported', 'Description','Solution'] #headers
                self.writer = csv.DictWriter(self.csv_file, delimiter=',',lineterminator='\n', fieldnames=self.csv_columns_headers)
                    #if file does not exist write the headers
                if not self.file_exists:
                    self.writer.writeheader()
                    #write the information from raw_data by rows
                else:
                    for info in self.raw_data:
                        self.writer.writerow(info)
                
        print("File formatted to CSV") 
    
    def write_xF_html(self, h, z):
        pd.set_option('display.max_colwidth', 1000, 'display.colheader_justify', 'left')
        #Link to an external style sheet:
        self.html_string = h
        df = pd.read_csv('x-force-vulnerability.csv')
        #start index at 1
        df.index = np.arange(1,len(df)+1)
        #create html file as table with css class style
        with open('xforcereport.html', 'w') as self.f:
            self.f.write(self.html_string.format(table=df.to_html()))

        print("File formatted to HTML")
        os.remove(z) 

# x = key # y = pass z = path
    
