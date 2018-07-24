import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from email import encoders

#def sendemail(name, description, modified):

def sendemail():

    gmail_user = 'mufasacyberdefenders2018@gmail.com'
    gmail_pass = 'Cyberdefenders_2018'

    sent_from = gmail_user

    sendto = str(input('Please enter email: '))
    sendto.strip()
    
    email_to = sendto

    send_out = MIMEMultipart()
    send_out['Subject'] = 'Potentioal threats on Blockchain'
    send_out['To'] = email_to
    send_out['From'] = sent_from
    send_out.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    


    # List of attachments
    attachments = ['Your Path /email.txt']

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
