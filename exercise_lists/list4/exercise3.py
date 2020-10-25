import alc

f1 = "16*(a**4) + 16*(b**4) + c**4 - 16"
f2 = "a**2 + b**2 + c**2 - 3"
f3 = "a**3 - b + c - 1"

print ("==> Sistema de equações:")
print ("- Equação #1: {} = 0".format(f1))
print ("- Equação #2: {} = 0".format(f2))
print ("- Equação #3: {} = 0".format(f3))

print ("-> Método de Newton: {}".format(alc.equations([f1, f2, f3], ['a', 'b', 'c'], [1, 1, 1])))
print ("-> Método de Broyden: {}".format(alc.equations([f1, f2, f3], ['a', 'b', 'c'], [1, 1, 1], method='broyden')))