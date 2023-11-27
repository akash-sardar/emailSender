import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path, PurePath
#pyemail
#fvxm csmj ktcb ulyz
infp = 'C:\\Akash\\LearningDocuments\\Python\\Projects\\emails\\input files'
p = PurePath(infp).joinpath('index.html')
html = Path(p).read_text()
html = Template(html)
html = html.substitute(name = 'Akash')
email = EmailMessage()
email['from'] = 'Akash Sardar'
email['to'] = 'lordakashjoy@gmail.com'
email['Subject'] = 'Test Email - Python'
app_password = 'fvxm csmj ktcb ulyz'

email.set_content(html,'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('akashjoy2023@gmail.com',app_password)
    smtp.send_message(email)
    print('email sent')

