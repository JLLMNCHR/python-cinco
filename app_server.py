from flask import Flask, render_template
from random import uniform
from estado_compartido import estado_compartido
from gestor_job import do_job

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route("/")
def home():
    print("Ejecutando app_server.home()")    
    return "<h1>Estación de Monitoreo de Datos</h1>"

# /api/planificador/latest_insiders_trading
@app.route("/api/planificador/<id_planificador>")
def api_planificador(id_planificador):
    print("Ejecutando app_server.api_planificador()")    

    do_job()

    estado_compartido.actualizar_ultima_ejecucion()
    ultima_ejecucion = estado_compartido.obtener_ultima_ejecucion()
    print(f"(api_planificador) Última ejecución: {ultima_ejecucion}")

    ultima_actualizacion = estado_compartido.obtener_ultima_actualizacion()
    print(f"(api_planificador) Última actualización: {ultima_actualizacion}")

    return {
        "id_planificador": id_planificador,
        "ultima_ejecucion": ultima_ejecucion,
        "ultima_actualizacion": ultima_actualizacion
    }

# /view/planificador/latest_insiders_trading
@app.route("/view/planificador/<id_planificador>")
def view_planificador(id_planificador):
    print("Ejecutando app_server.view_planificador()")   
    return render_template("index.html")

if __name__ == '__main__':
    app.run()