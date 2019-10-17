import threading
import time
import logging # para hacer debug de una mejor forma

# Configuración básica
# Que muestre el nivel de logging, el nombre del hilo y el mensaje
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] ($(threadName)-s) %(message)s')

class Hilo2(threading.Thread): # Hilo1 hereda de Thread
    def __init__(self, nombre_hilo, id_persona, data):
        threading.Thread.__init__(self, name=nombre_hilo, target=Hilo2.run)
        self.nombre_hilo = nombre_hilo
        self.id_persona = id_persona
        self.data = data

    # Método que se sobreescribe de la clase padre
    def run(self):
        self.guardar(self.id_persona, self.data)

    def guardar(self, id_persona, data):
        logging.info("Consultando para el id " + str(id_persona) + " la data " + data)
        time.sleep(5)
        return
