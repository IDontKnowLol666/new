import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = 'test'

#The mail addresses and password
sender_address = 'spinoshit@gmail.com'
sender_pass = 'B00fu123'
receiver_address = 'jolene5652@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an a2ttachment!!'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))


def countdownN(t):
    t = t
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        name = 'Jolene'
def countdown(t):
    t = t
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


#for i in range(100000):
    #countdown(20)
    #name = "Jolene"
    #if name=='Jolene':
        #session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        #session.starttls()  # enable security
        #session.login(sender_address, sender_pass)  # login with mail_id and password
        #text = message.as_string()
        #session.sendmail(sender_address, receiver_address, text)
        #session.quit()
    #countdownN(20)
