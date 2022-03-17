import numpy as np
# a*b = sum(d = (1, D) : a_d * b_d)
# alternativa: |a| |b| cos(theta)_ab

a = np.array([1,2])
b = np.array([2,1])

# Primer manera, es lento
dot = 0
for e, f in zip(a, b):
    dot += e*f

print("Primer manera", dot)

# Segunda manera
print("Segunda manera", np.sum(a*b))

# Tercer forma
print("Tercer manera", (a*b).sum())

# Cuarta forma, recomendada
print("Cuarta manera", np.dot(a, b))

# Quinta forma
print("Quinta manera", a.dot(b))

# Calculando el ángulo
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cosangle)

print("ángulo: ", angle)
