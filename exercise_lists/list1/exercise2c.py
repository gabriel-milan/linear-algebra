import alc

A = alc.Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
print ("A = {}".format(A))
det = alc.utils.det(A)
print ("det(A) = {}".format(det))
