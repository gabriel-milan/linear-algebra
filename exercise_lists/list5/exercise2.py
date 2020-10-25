import alc

function = "(1 / sqrt(2*pi))*exp((-1/2)*(x**2))"

intervals = [
  (0, 1),
  (0, 5),
]

for i in range(len(intervals)):
  a = intervals[i][0]
  b = intervals[i][1]
  print ("==> Integral da função {} de {} a {}:".format(function, a, b))
  print ("Numérico: {}".format(alc.integrate(function, a, b)))
