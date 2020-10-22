import alc

func = "log(cosh(x*sqrt(9.806*0.00341)))-50"

print ("==> Função f(x) = {}".format(func))
print ("- Raiz pelo método da bisseção: {}".format(alc.bisection(func, 0, 300)))
print ("- Raiz pelo método de Newton: {}".format(alc.newton(func, 1)))
print ("- Raiz pelo método de Newton secante: {}".format(alc.newton_secant(func, 1)))
print ("- Raiz pelo método da interpolação inversa: {}".format(alc.inverse_interpolation(func, 0, 100, 200)))