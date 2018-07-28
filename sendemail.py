import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from email import encoders

#def sendemail(name, description, modified):

def sendemail():

    hostEmail = '@gmail.com'
    hostPass = ''

    sendTo = str(input('Please enter email: '))
    sendTo.strip()

    send_out = MIMEMultipart()
    send_out['Subject'] = 'Potentioal threats on Blockchain'
    send_out['To'] = sendTo
    send_out['From'] = hostEmail
    send_out.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    
    attachment = [FULL PATH TO ATTACHMENTS HERE]

# Add the attachment to the message
    for file in attachments:

    try:
        with open(attachment, 'rb') as fp:
            msg = MIMEBase('application', "octet-stream")
            msg.set_payload(fp.read())
        encoders.encode_base64(msg)
        msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment)
        send_out.attach(msg)
    except:
        print("Error: ", sys.exc_info()[0])
        raise
 
    comp = send_out.as_string()

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(hostEmail, hostPass)
        server.sendmail(hostEmail, sendTo, comp)
        server.close()
        print('Email sent!')
    except:  
        print('Error')   
