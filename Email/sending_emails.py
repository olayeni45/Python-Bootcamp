import smtplib,getpass
from email.mime.text import MIMEText

smtp_object = smtplib.SMTP("smtp-mail.outlook.com", 587)
smtp_object.ehlo()
smtp_object.starttls()

email = getpass.getpass("Email: ")
password = getpass.getpass("Password please: ")

smtp_object.login(email, password)

from_address = email
to_address = email
msg = MIMEText("Hi! This is from VSCode")
msg['Subject'] = "Testing Python SMTP"
msg['From'] = email
msg['To'] = email

smtp_object.sendmail(from_address, to_address, msg.as_string())

smtp_object.quit()