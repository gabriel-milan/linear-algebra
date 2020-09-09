import alc

A = alc.Array([
    [5, -4, 1, 0],
    [-4, 6, -4, 1],
    [1, -4, 6, -4],
    [0, 1, -4, 5],
])

L, U = alc.decomposition.lu_decomposition(A)
L, LT = alc.decomposition.cholesky_decomposition(A)

print ("==> LU decomposition")
print ("A = {}".format(A))
print ("L = {}".format(L))
print ("U = {}".format(U))

print ("==> Cholesky decomposition")
print ("A = {}".format(A))
print ("L = {}".format(L))
print ("LT = {}".format(LT))
