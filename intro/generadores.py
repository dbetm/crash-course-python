def generaPares(limite):
	num = 1
	miLista = []
	while num < limite:
		miLista.append(num*2)
		num += 1

	return miLista

# Entre llamada y llamada entra en estado suspensión
def generadorPares(limite):
	num = 1
	while num < limite:
		yield num*2
		num += 1


print(generaPares(10))
devuelvePares = generadorPares(10)
print(next(devuelvePares))
print("Aquí podría ir más código")
print(next(devuelvePares))
print("Aquí podría ir más código")
print(next(devuelvePares))

