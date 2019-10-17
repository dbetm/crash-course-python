import threading
import time
import logging # para hacer debug de una mejor forma

# Configuración básica
# Que muestre el nivel de logging, el nombre del hilo y el mensaje
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] ($(threadName)-s) %(message)s')

class Hilo1(threading.Thread): # Hilo1 hereda de Thread
    def __init__(self, nombre_hilo, id_persona, data):
        threading.Thread.__init__(self, name=nombre_hilo, target=Hilo1.run)
        self.nombre_hilo = nombre_hilo
        self.id_persona = id_persona
        self.data = data

    # Método que se sobreescribe de la clase padre
    def run(self):
        self.consultar(self.id_persona)

    def consultar(self, id_persona):
        logging.debug("Consultando para el id " + str(id_persona))
        time.sleep(2)
        return
