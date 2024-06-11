import schedule
import time

import smtplib
from email.mime.multipart import MIMEMultipart

def send_email():
    from_email = 'jllmnchr@gmail.com'
    to_email = 'jllmnchr@gmail.com'
    subject = 'Informe de transacciones'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, 'kwjn kcsg bzlr xcpt')
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def job():
    print("Ejecutando Tarea")
    send_email()

#schedule.every().day.at("08:00").do(job)
schedule.every(15).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)