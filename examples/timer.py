import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = 'Hello'
sender_address = 'spinoshit@gmail.com'
sender_pass = 'B00fu123'
receiver_address = 'jolene5652@gmail.com'
# import the time module
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'

message.attach(MIMEText(mail_content, 'plain'))
name = 'Jolene'

if name=="Jolene":
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    var = 'un'
    # define the countdown func.
if var == 'un':
    def countdown(t):
        t = 30
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            name = 'Not Jolene'
            countdown(15)
            def countdownN(t):
                t = 30
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    t -= 1
                    name = 'Jolene'
                    countdownN(15)

            if name == "Jolene":
                session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                session.starttls()  # enable security
                session.login(sender_address, sender_pass)  # login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                var = 'un'


if name=='Jolene':
    for i in range(100):
        countdown(0)






