import smtplib

from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Daniel Daréus'
email['to'] = '123@hotmail.com'   
email['subject'] = 'You are on the way of becoming one of the greatest AI engineer of all time'  

email.set_content(html.substitute({'name': 'Pè Da'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('123@gmail.com', '123@2021')
    smtp.send_message(email)
    print('It is all good!')
    
    # if you're sending mail from Google Server you need to enable "Less secure app access" feature in your security setting.
