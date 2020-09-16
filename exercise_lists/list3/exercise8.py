import alc

x = [1, 2, 3, 4]
y = [1, 2.5, 3.5, 4.3]

print ("==> Pontos (x,y):")
for i in range(len(x)):
  print ("-- (%3.3s, %3.3s)" % (x[i], y[i]))
print ("")
print ("Ajustando uma função y = ax + b")
a, b = alc.least_squares(x, y)
print ("a = {:.4f}".format(a))
print ("b = {:.4f}".format(b))