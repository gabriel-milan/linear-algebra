import alc

function = "1 / (1 + x**2)"

a = 0
b = 3

names = [
  'ponto médio',
  'trapézio',
  'simpson'
]

print ("==> Integral da função {} de {} a {}:".format(function, a, b))
for n_points in range(1, 4):
  print ("{} pontos ({}): {}".format(n_points, names[n_points-1], alc.integrate(function, a, b, n_points=n_points)))

# 2 pontos por quadratura, 3 por polinomial