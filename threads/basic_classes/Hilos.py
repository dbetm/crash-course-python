import threading
import time
import datetime
import logging
from Hilo1 import Hilo1
from Hilo2 import Hilo2

tiempo_0 = datetime.datetime.now();

# Instanciamos las clases que representan nuestros hilos
t1 = Hilo1("Hilo 1", 1, " ")
t2 = Hilo2("Hilo 2", 1, "Hola mundo")

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
