import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def send_email(attachment_paths):
    print("Ejecutando gestor_email.send_email()")

    from_email = 'jllmnchr@gmail.com'
    to_email = 'jllmnchr@gmail.com'
    subject = 'Informe de transacciones main'
    body = 'Adjunto encontrarás el informe de las nuevas transacciones.'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    for attachment_path in attachment_paths:
        filename = os.path.basename(attachment_path)
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    gmail_app_key = os.getenv("GMAIL_APP_KEY")
    if gmail_app_key is None:
        print("Error: La variable de entorno GMAIL_APP_KEY no está configurada.")
        return
    else:
        server.login(from_email, gmail_app_key)

    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    salidas_dir = './salidas'
    os.makedirs(salidas_dir, exist_ok=True)
    attachment_paths = [os.path.join(salidas_dir, filename) for filename in os.listdir(salidas_dir)]

    send_email(attachment_paths)

if __name__ == '__main__':
    main()
