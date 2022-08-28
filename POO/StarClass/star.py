class Star:
    """ Clase para estrellas
    Ejemplo de clases con Python
    Fichero: star.py
    """

    # Número total de estrellas
    num_stars = 0

    def __init__(self, name):
        self.name = name
        Star.num_stars += 1

    def set_mag(self, mag):
        self.mag = mag

    def set_par(self, par):
        """Asigna paralaje en segundos de arco"""
        self.par = par

    def get_mag(self):
        print("La magnitud de {} es de {}".format(self.name, self.mag))

    def get_dist(self):
        """Calcula la distancia en parsec a partir de la paralaje"""
        print("La distancia de {} es {:.2f}".format(self.name, 1/self.par))

    def get_star_number(self):
        print("Número total de estrella: {}".format(Star.num_stars))
