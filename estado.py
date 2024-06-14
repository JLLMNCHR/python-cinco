from datetime import datetime

class Estado:
    def __init__(self):
        self.ultima_ejecucion = None

    def actualizar_ultima_ejecucion(self):
        self.ultima_ejecucion = datetime.now()

    def obtener_ultima_ejecucion(self):
        return self.ultima_ejecucion
        '''
        if self.ultima_ejecucion:
            return self.ultima_ejecucion.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return "No disponible"
        '''