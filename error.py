import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

str_date=input("enter your date:")
str_destination=input("enter your destination:")
str_email=input("enter your emailid:")

df= pd.read_excel("error_uipath.xlsx")

for i in df['PLACES']:
    if i== str_destination:

            
            sender_email = 'kokilavanitamilarasu@gmail.com'
            receiver_email = str_email
            password = 'wfkmbovtnxgipoxs'
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  


            subject = 'Subject of the email'
            body = i

            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
  
                server.starttls()

  
                server.login(sender_email, password)

    
                server.sendmail(sender_email, receiver_email, message.as_string())

            print('Email sent successfully!')


