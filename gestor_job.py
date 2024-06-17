import os
from gestor_finviz import get_latest_insiders_trading_info
from gestor_email import send_email
from estado_compartido import estado_compartido

def do_job():
    print("Ejecutando gestor_job.do_job()")

    estado_compartido.actualizar_ultima_ejecucion()  # Actualizar la última ejecución
    print(f"Última ejecución: {estado_compartido.obtener_ultima_ejecucion()}")

    get_latest_insiders_trading_info()
    
    salidas_dir = './salidas'
    os.makedirs(salidas_dir, exist_ok=True)    
    attachment_paths = [os.path.join(salidas_dir, filename) for filename in os.listdir(salidas_dir)]

    send_email(attachment_paths)
