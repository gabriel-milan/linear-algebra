import alc

A = alc.Array([
  [16,  9,  8,  7,  6,  5,  4,  3,  2,  1],
  [ 9, 17,  9,  8,  7,  6,  5,  4,  3,  2],
  [ 8,  9, 18,  9,  8,  7,  6,  5,  4,  3],
  [ 7,  8,  9, 19,  9,  8,  7,  6,  5,  4],
  [ 6,  7,  8,  9, 18,  9,  8,  7,  6,  5],
  [ 5,  6,  7,  8,  9, 17,  9,  8,  7,  6],
  [ 4,  5,  6,  7,  8,  9, 16,  9,  8,  7],
  [ 3,  4,  5,  6,  7,  8,  9, 15,  9,  8],
  [ 2,  3,  4,  5,  6,  7,  8,  9, 14,  9],
  [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 13],
])
B = alc.Array([
  [4],
  [0],
  [8],
  [0],
  [12],
  [0],
  [8],
  [0],
  [4],
  [0],
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x_lu = alc.systems.solve(A, B, method='lu')
x_cholesky = alc.systems.solve(A, B, method='cholesky')
print ("x (LU) = {}".format(x_lu))
print ("x (Cholesky) = {}".format(x_cholesky))
