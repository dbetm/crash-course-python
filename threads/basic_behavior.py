import threading
import time
import datetime
import logging

# Para simular que hay que hacer dos tareas 'pesadas'.

def consultar(id_persona):
    time.sleep(2)
    return

def guardar(id_persona, data):
    time.sleep(5)
    return

tiempo_0 = datetime.datetime.now();

# Instanciamos los hilos
t1 = threading.Thread(name="hilo_1", target=consultar, args=(1, ))
t2 = threading.Thread(name="hilo_2", target=guardar, args=(1, "hola mundo"))

# Iniciamos los hilos
t1.start()
t2.start()

# Comportamiento normal
#consultar(1)
#guardar(1, "bla")

# Comportamiento sincrono
t1.join()
t2.join()

# Las siguientes líneas no se ejecutan hasta terminar los
# hilos (Comportamiento sincrono)

tiempo_1 = datetime.datetime.now()
print("Tiempo transcurrido " + str(tiempo_1.second - tiempo_0.second))
