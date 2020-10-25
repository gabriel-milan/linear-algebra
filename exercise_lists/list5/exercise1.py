import alc
import random

functions = [
  "x**3 + 1/exp(x)",
  "x**(1/3) + ln(x)",
  "1-exp(-(x/5)**2)"
]

xs = [
  3,
  2,
  6
]

num = [
  "(27 - 1/e^3) ~ 26.95021293",
  "(1/6*(3+2^(1/3))) ~ 0.7099868",
  "12/25(e^(36/25)) ~ 0.113725324167",
]

for i in range(len(functions)):
  f = functions[i]
  x = xs[i]
  print ("==> Derivada da função {} no ponto {}:".format(f, x))
  print ("Numérico: {}, Analítico: {}".format(alc.diff(f, x), num[i]))