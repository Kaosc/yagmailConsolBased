from re import sub
from smtplib import SMTPAuthenticationError
import yagmail

sender = input("Sender mail: ")
senderPassword = input("Sender password: ")
receiver = input("Receiver mail: ")
subject = input("Subject of the mail: ")
textFile = input("Text file name: ")

with open(f"texts/{textFile}.txt","r") as f:
    content = f.read()

try:
    yag = yagmail.SMTP(user=sender,password=senderPassword)
    yag.send(to=receiver,subject=subject,contents=content)
    print("The email sended Successfully!")
except SMTPAuthenticationError:
    print("ERROR --> Turn on 'Less secure app access' from your Google account")