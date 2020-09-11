import alc

A = alc.Array([
  [3, 2, 0],
  [2, 3, -1],
  [0, -1, 3],
])

print ("A = {}".format(A))

eigenvalues, eigenvectors = alc.jacobi_eigen(A)
print ("autovalores = {}".format(eigenvalues))
print ("autovetores = {}".format(eigenvectors))