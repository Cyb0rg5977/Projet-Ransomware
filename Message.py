from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart('alternative')
message['Subject'] = 'Test'
message['From'] = 'chupacabrac@yopmail.com'
message['To'] = 'chupacabrac@yopmail.com'

message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain')

server = smtplib.SMTP('smtp.yopmail.com', 587)
server.starttls()
server.login('chupacabrac@yopmail.com', '')
server.sendmail('chupacabrac@yopmail.com', 'chupacabrac@yopmail.com', message.as_string())
server.quit()
