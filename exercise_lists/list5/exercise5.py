import alc

function = "2 + 2*x - x**2 + 3*x**3"

a = 0
b = 4

print ("==> Integral da função {} de {} a {}:".format(function, a, b))
for n_points in range(1, 11):
  print ("{} pontos (polinomial): {}".format(n_points, alc.integrate(function, a, b, n_points=n_points)))
  print ("{} pontos (quadratura): {}".format(n_points, alc.integrate(function, a, b, n_points=n_points, method='gauss_quadrature')))

# 2 pontos por quadratura, 3 por polinomial