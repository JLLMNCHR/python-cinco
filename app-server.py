from flask import Flask, render_template
from random import uniform

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Estación de Monitoreo de Datos</h1>"

# /api/sensor/temperatura
# /api/sensor/humedad
# /api/sensor/123
# /api/sensor/...
@app.route("/api/sensor/<id>")
def sensor(id):
    celsius = uniform(0, 90)
    return {
        "celsius": celsius,
        "id": id
    }

@app.route("/view/sensor/<id>")
def sensor_view(id):
    return render_template("sensor.html")

app.run()