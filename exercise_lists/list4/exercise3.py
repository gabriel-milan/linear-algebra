import alc

f1 = "16*a**4 + 16*b**4 + c**4"
f2 = "a**2 + b**2 + c**2 - 3"
f3 = "a**3 - b + c - 1"

print ("==> Sistema de equações:")
print (f1)
print (f2)
print (f3)

print (alc.equations([f1, f2, f3], [1, 1, 1]))