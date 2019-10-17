class Coche():
    largo_chasis = 250
    ancho_chasis = 250
    ruedas = 4
    en_marcha = False

    def arrancar(self):
        self.en_marcha = True

    def estado(self):
        ans = ""
        if(self.en_marcha):
            ans = "El coche está en marcha"
        else:
            ans = "El coche está detenido"
        return ans

mi_coche = Coche()
print("El largo del coche es: ", mi_coche.largo_chasis)
print("El coche tiene %d puertas" % (mi_coche.ruedas))
# Arrancamos el coche
mi_coche.arrancar()
# Mostramos el estado actual del coche
print(mi_coche.estado())
