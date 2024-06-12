import schedule
import time

from gestor_email import send_email

def job():
    print("Ejecutando Tarea")
    send_email()

#schedule.every().day.at("08:00").do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

