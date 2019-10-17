miDiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres"}
print(miDiccionario["Francia"])
print(miDiccionario)
# Agregando mas elementos
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
miDiccionario["Italia"]="Roma"
print(miDiccionario)
# Eliminar un par
del miDiccionario["Reino Unido"]
print(miDiccionario)

#DICCIONARIO MIXTO

diccionario = {23:"Jordan", "Mosqueteros":3, "Alemania":"Berlin"}


miTupla = ("Espania", "Francia", "Alemania")
dic = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Berlin"}
print(dic)


dic2 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1996, 1997, 1998]}
print(dic2)
print(dic2["Equipo"])


# Guardando un diccionario dentro de otro
dic3 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991, 1992, 1996, 1997, 1998]}}
print(dic3["Anillos"])
print(dic3.keys())
print(dic3.values())
print(len(dic3))