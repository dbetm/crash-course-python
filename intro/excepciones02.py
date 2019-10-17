# Capturar varias excepciones

def divide():
	try:
		op1 = float(input("Número 1: "))
		op2 = float(input("Número 2: "))

		print("La división es: " + str(op1/op2))
	except ValueError:
		print("El valor introducido es erróneo")
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
	# except:
		# print("Error genérico")

	finally: # Líneas para que se ejecute siempre, ocurra o no la excepción
		print("Hecho")

divide()