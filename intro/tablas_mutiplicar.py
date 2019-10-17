print("Programa que muestra las tablas de mutiplicar del 1 al 10")

for i in range(1,11):
	j = 1
	while j < 11:
		result = i * j
		print(str(i) + "x" + str(j) + " = " + str(result))
		j = j + 1
	print("\n")