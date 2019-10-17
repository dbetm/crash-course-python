from sys import argv

# Los parámetros pasados están en una lista de strings en argv,
# en la que el primer elemento es el nombre del programa y el
# segundo el primer parámetroself.

x = argv[1]

x = float(x)

print(x ** 3)
