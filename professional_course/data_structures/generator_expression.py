
vals = [0, 1, 3, 4, 5, 9]

flo = [x*2 for x in vals] # list comprehension - saving in memory
ret = (x*2 for x in vals) # generator

print(flo)
print(next(ret))
print(next(ret))
print(next(ret))
