from datetime import datetime

class Estado:
    def __init__(self):
        self.ultima_ejecucion = None
        self.ultima_actualizacion = None

    def actualizar_ultima_ejecucion(self):
        self.ultima_ejecucion = datetime.now()

    def actualizar_ultima_actualizacion(self):
        self.ultima_actualizacion = datetime.now()

    def obtener_ultima_ejecucion(self):
        if self.ultima_ejecucion:
            return self.ultima_ejecucion.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return "No disponible"
        
    def obtener_ultima_actualizacion(self):
        if self.ultima_actualizacion:
            return self.ultima_actualizacion.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return "No disponible"

