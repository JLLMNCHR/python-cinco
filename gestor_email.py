import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def send_email():
    from_email = 'jllmnchr@gmail.com'
    to_email = 'jllmnchr@gmail.com'
    subject = 'Informe de transacciones main'
    body = 'Adjunto encontrarás el informe de las nuevas transacciones.'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, 'kwjn kcsg bzlr xcpt')
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
