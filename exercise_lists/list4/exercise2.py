import alc

func = "4*cos(x)-exp(2*x)"

print ("==> Função f(x) = {}".format(func))
print ("- Raiz pelo método da bisseção: {}".format(alc.bisection(func, -5, 5)))
print ("- Raiz pelo método de Newton: {}".format(alc.newton(func, -5)))
print ("- Raiz pelo método de Newton secante: {}".format(alc.newton_secant(func, -5)))
print ("- Raiz pelo método da interpolação inversa: {}".format(alc.inverse_interpolation(func, 0, 0.5, 1)))