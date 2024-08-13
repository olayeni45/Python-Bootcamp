import imaplib, getpass, email

M = imaplib.IMAP4_SSL("outlook.office365.com", 993)

email = getpass.getpass("Email: ")
password = getpass.getpass("Password please: ")

M.login(email, password)
print(M.list())

typ, data = M.search(None, "SUBJECT ""Testing Python SMTP""")
print(typ)
print(data)

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')

raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")

#email_message = email.m
