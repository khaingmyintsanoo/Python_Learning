import email
import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login("gmail", 'password')
M.list()
M.select('INBOX')[0]
typ, data = M.search(None, 'SUBJECT "Hello"')
email_id = data[0]
# print(email_id)
result, email_data = M.fetch(email_id, '(RFC822)')
# print(email_data)
raw_email = email_data[0][1]
print(raw_email)
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
