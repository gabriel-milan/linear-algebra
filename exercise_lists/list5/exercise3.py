import alc

functions = [
  "(1/(sqrt( (1 - (x/1)**2)**2 + (2*0.05*x/1)**2 )))**2 * 2",
  "(x**2) * ((1/(sqrt( (1 - (x/1)**2)**2 + (2*0.05*x/1)**2 )))**2 * 2)"
]

interval = (0, 10)
a = interval[0]
b = interval[1]

for i in range(len(functions)):
  print ("==> Integral da função {} de {} a {}:".format(functions[i], a, b))
  for n_points in range(1, 11):
    print ("--> {} pontos: {}".format(n_points, alc.integrate(functions[i], a, b, n_points=n_points)))
