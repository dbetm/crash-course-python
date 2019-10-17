a = ["Daniel","David","Daniela"]
print(a[:])
print(a[-3])
print(a[0:2]) #el 0 es inclusivo, el 2 es exclusivo
print(a[:2]) # no importa si no se pone el 0
print(a[1:])

a.append("Sandra") # lo agrega al final

print(a[:])

a.insert(1,"Miguel")

print(a[:])

a.extend(["Ruby","Diana"])

a.append(True)

print(a[:])

print(a.index("David"))

print("Karen" in a)

a.remove("Diana")

print(a[:])

a.pop()

print(a[:])

b = ["Luis","Andrea"]

b *= 3

c = a + b

print(c[:])