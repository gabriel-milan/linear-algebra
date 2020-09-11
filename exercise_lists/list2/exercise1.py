import alc

A = alc.Array([
  [3, 2, 0],
  [2, 3, -1],
  [0, -1, 3],
])

print ("A = {}".format(A))

eigenvalue, eigenvector = alc.power_method(A)
print ("autovalor = {}".format(eigenvalue))
print ("autovetor = {}".format(eigenvector))
