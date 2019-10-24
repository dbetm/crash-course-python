import numpy as np

# Convertir lista en arreglo
L = [1, 2, 3]
A = np.array(L)

# Iterar lista y array
print("Lista")
for e in L:
    print(e)

print("Arreglo")
for e in A:
    print(e)

# Agregando un elemento a lista
L.append(4)
L = L + [5]
print(L)

# Suma de vectores, en arreglo
print(A + A)

# Multiplicación por un escalar, en array
print(2*A)

# Lo anterior en la lista funciona como concatenación
print(2*L)

# Más operaciones en arreglo
print("Elevar al cuadrado ", A**2)

print("Obtener raíz cuadrada ", np.sqrt(A))

print("Logaritmo natural ", np.log(A))

print("Exponencial a cada elemento ", np.exp(A))
