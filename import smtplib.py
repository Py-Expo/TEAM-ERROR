import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



sender_email = "aj3681528@gmail.com"
receiver_email = "vinuthiyagaran@gmail.com"
subject = "Subject of the email"
body = "Body of the email." 
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Use 465 for SSL
username = "kokilavanitamilarasu@gmail.com"
password = "wfkmbovtnxgipoxs"
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()

