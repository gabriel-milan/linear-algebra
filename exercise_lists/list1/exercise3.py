import alc

A = alc.Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
B = alc.Array([
  [-1],
  [2],
  [1],
  [3]
])
print ("A = {}".format(A))
print ("B = {}".format(B))
try:
  print ("==> Método de Jacobi")
  x = alc.systems.solve(A, B, method='jacobi')
  print ("x = {}".format(x))
except ValueError as e:
  print (e)

try:
  print ("==> Método de Gauss-Seidel")
  x = alc.systems.solve(A, B, method='gauss_seidel')
  print ("x = {}".format(x))
except ValueError as e:
  print (e)