#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from star import Star

# Creo una instancia de estrella
altair = Star("Altair")

print("Nombre: ", altair.name)

altair.set_par(0.195)

altair.get_star_number()
