print("Asignaturas optativas - 2018/2")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

asignatura = raw_input("Escribe la asignatura elegida: ")
if asignatura.lower() in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura elegida no esta contemplada")