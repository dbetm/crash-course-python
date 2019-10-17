import math

def calculaRaiz(num):
	if num<0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num)

opt1 = int(input("Número: "))
try:
	print(calculaRaiz(opt1))
except ValueError as ErrorNumeroNegativo:
	print(ErrorNumeroNegativo)

print("Programa terminó con éxito")