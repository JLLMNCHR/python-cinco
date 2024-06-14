import schedule
import time
from gestor_job import do_job

def job():
    print("Ejecutando main.job()")

    do_job()


# schedule.every().day.at("08:00").do(job)
schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
