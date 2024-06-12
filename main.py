import schedule
import time
import os

from latest_insiders_trading import get_info
from gestor_email import send_email


def job():
    print("Ejecutando main.job()")
    
    get_info()

    salidas_dir = './salidas'
    attachment_paths = [os.path.join(salidas_dir, filename) for filename in os.listdir(salidas_dir)]

    send_email(attachment_paths)

#schedule.every().day.at("08:00").do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

