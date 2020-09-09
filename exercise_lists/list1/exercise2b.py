import alc
from alc.systems import solve

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
x = solve(A, B, method='lu')
print ("x = {}".format(x))
