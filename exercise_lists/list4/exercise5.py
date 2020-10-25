import alc
import random

f = "a + b*(x**c) - y"
xs = [1, 2, 3]
ys = [1, 2, 9]

print ("==> Função para ajustar:")
print (f)
print ("-> Pontos (x,y): {}".format([(xs[i], ys[i]) for i in range(len(xs))]))


print (alc.nl_least_squares(f, ['a', 'b', 'c'], xs, ys, [0, 1, 2], threshold=1e-4))
