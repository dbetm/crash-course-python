class User():
    def __init__(self):
        self.nombre = "desconocido"
        self.apellido = "desconocido"
        self.edad = -1
        self.isAdmin = False

    def __init__(self, nombre, apellido, edad, isAdmin):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.isAdmin = isAdmin

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def isAdmin(self):
        return self.isAdmin

    def setIsAdmin(self, isAdmin):
        self.isAdmin = isAdmin

    def toString(self):
        return self.nombre + " " + self.apellido + " " + str(self.edad) + " " + str(self.isAdmin)

usuario = User("David", "Betancourt", 20, True)
usuario.setNombre(input("Escribe el nombre: "))
usuario.setEdad(input("Escribe la edad: "))
print(usuario.toString())
