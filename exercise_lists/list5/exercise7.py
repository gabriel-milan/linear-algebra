import alc

function = "(1 / sqrt(2*pi))*exp((-1/2)*(x**2))"

intervals = [
  (float("-inf"), 1),
  (float("-inf"), float("inf")),
]

for i in range(len(intervals)):
  a = intervals[i][0]
  b = intervals[i][1]
  print ("==> Integral da função {} de {} a {}:".format(function, a, b))
  print ("Resultado: {}".format(alc.integrate(function, a, b)))
