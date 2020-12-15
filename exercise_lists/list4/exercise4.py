import alc

for (delta1, delta2) in [(0, 3), (0.75, 6.5), (0, 11.667)]:
  print ("******* delta1 = {}, delta2 = {}".format(delta1, delta2))
  print ("==> Sistema de equações:")
  f1 = "2*c**2 + b**2 + 6*d**4 - 1"
  f2 = "8*c**3 + 6*c*b**2 + 36*c*b*d + 108*c*d**2 - {}".format(delta1)
  f3 = "60*(c**4) + 60*(c**2)*(b**2) + 576*(c**2)*b*d + 2232*(c**2)*(d**2) + 252*(d**2)*(b**2) + 1296*(d**3)*b + 3348*(d**4) + 24*(b**3)*d + 3*b - {}".format(delta2)

  print ("- Equação #1: {} = 0".format(f1))
  print ("- Equação #2: {} = 0".format(f2))
  print ("- Equação #3: {} = 0".format(f3))

  print ("-> Método de Newton: {}".format(alc.equations([f1, f2, f3], ['b', 'c', 'd'], [1, 0, 0])))
  print ("-> Método de Broyden: {}".format(alc.equations([f1, f2, f3], ['b', 'c', 'd'], [1, 0, 0], method='broyden')))