#!/usr/bin/python3
#-*- coding: utf-8 -*-

""" Programa de cálculo del cubo de un número """

__autor__ = "David"
__copyright__ = "curso_python3"
__credits__ = ["David", "Betancourt", "Montellano"]
__license__ = "GPL"
__version__ = "1.0"
__email__ = "davbetm@gmail.com"
__status__ = "Development"

def cubo(x):
    """Calcula el cubo de un número"""
    y = x**3
    return y

if __name__ == "__main__":
    x = int(input("Escribe el número: "))
    y = cubo(x)
    print("El cubo de %.2f es %.2f" % (x, y))
