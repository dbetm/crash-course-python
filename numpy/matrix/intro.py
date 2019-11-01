import numpy as np
# Arreglos
M = np.array([[1,2], [3,4]])
L = [[1,2], [3,4]] # Lista de listas

print(L[0])
print(L[0][0]) # -> 1
print(M[0][0])  # -> 1
print(M[0,0]) # -> 1

# Matrices
M2 = np.matrix([[1,2], [3,4]])
print(M2)

# Convertir matriz a arreglo
A = np.array(M2)
print(A)

# Transpuesta
print("Matriz transpuesta", A.T)
