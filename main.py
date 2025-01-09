import os
import smtplib
import mimetypes
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['programmingcaleb@gmail.com, calebdubuzz@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'In few days my Birthday'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Image attached...')
print(msg)

files = ['birthday.jpg', 'birthday2.jpg']
for file in files:

    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        print(file_name)
        file_type = mimetypes.guess_type(f.name)[0].split('/')[1]
        print(file_type) 
   
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    
pdf_files = ['Glossary_Cybersecurity_Terms(v.2.0).pdf']

with open(pdf_files[0], 'rb') as f:
    file_data = f.read()
    file_name = f.name
    print(file_name)
    file_type = mimetypes.guess_type(f.name)[0].split('/')[1]
    print(file_type)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
