from OTXv2 import OTXv2
from pandas.io.json import json_normalize
from datetime import datetime, timedelta
import getopt
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from email import encoders


time = str(datetime.now() - timedelta()) # Time at which script was initiated.

'''
The following try/except block handles user input options.
'''
try:
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

if 's' in opts:
    x = userSearch
else:
    x = "crypto"

pulses = otx.search_pulses(x, 40) # Retrieves list (in json format) of top 40 pulses with tag "crypto"

'''
The pulse_print() function loops through each individual pulse retreived from OTX, and prints their names + the fields requested by the user through options.
'''
'''
reads the textfile pulseid to 
'''
with open('pulseid.txt', "r") as pulsefile:
    pulsesid = pulsefile.read()

'''
Function to send email with name, description, and when it was modified. 
as a text file 
'''
#def sendemail(name, description, modified):
def sendemail():
    gmail_user = '@gmail.com'
    gmail_pass = ''

    sent_from = gmail_user

    email_to = '@gmail.com'
    
    send_out = MIMEMultipart()
    send_out['Subject'] = 'Potentioal threats on Blockchain'
    send_out['To'] = email_to
    send_out['From'] = sent_from
    send_out.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    


    # List of attachments
    attachments = ['"ISERT PATH TO TEXT FILE"/email.txt']

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            send_out.attach(msg)
        except:
            print("Error: ", sys.exc_info()[0])
            raise
 
    comp = send_out.as_string()

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_pass)
        server.sendmail(sent_from, email_to, comp)
        server.close()

        print('Email sent!')
    except:  
        print('Error')   

def pulse_print():
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

print()
print("DATE AND TIME: " + time + "\n")
print('-'*30)
print()


        
try:
    pulse_print()
except TypeError:
    print("\n"+"python3 otx_blkchn.py h for help"+"\n")
    sys.exit()

