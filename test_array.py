from alc import Array, ones, zeros, eye, gauss_elimination, lu_decomposition, solve, det, vector_norm, gauss_jordan_elimination
from alc import cholesky_decomposition, is_definite_positive

print ("==> Column vector test")
arr = Array([
  [1,],
  [2,],
  [3,]
])
assert arr.shape == [3, 1]
print (arr)

print ("==> Row vector test")
arr = Array(
  [1, 2, 3]
)
assert arr.shape == [1, 3]
print (arr)

print ("==> 3x3 array test")
arr = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
assert arr.shape == [3, 3]
print (arr)

print ("==> Get item test [0]")
print (arr[0])

print ("==> Get item test [0, 1]")
print (arr[0, 1])

print ("==> Get item test [0][1]")
print (arr[0][1])

print ("==> Set item test [0][1]=99")
print ("Before: {}".format(arr))
arr[0][1] = 99
print ("After: {}".format(arr))

print ("==> Scalar multiplication test")
arr = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
arr = 2*arr
assert arr.shape == [3, 3]
print (arr)

print ("==> Scalar multiplication with attrib test")
arr = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
arr *= 2
assert arr.shape == [3, 3]
print (arr)

print ("==> Matrix multiplication (3x3) x (3x3)")
arr1 = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
arr2 = Array([
  [9, 8, 7],
  [6, 5, 4],
  [3, 2, 1]
])
res1 = arr1 * arr2
assert res1.shape == [arr1.shape[1], arr2.shape[0]]
res2 = arr2 * arr1
assert res2.shape == [arr2.shape[1], arr1.shape[0]]
print ("A x B: {}".format(res1))
print ("B x A: {}".format(res2))

print ("==> Matrix multiplication with attrib")
arr1 = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
arr2 = Array([
  [9, 8, 7],
  [6, 5, 4],
  [3, 2, 1]
])
arr1 *= arr2
print ("A x B: {}".format(arr1))

print ("==> Matrix adding with attrib")
arr1 = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
arr2 = Array([
  [9, 8, 7],
  [6, 5, 4],
  [3, 2, 1]
])
arr1 += arr2
print ("A + B: {}".format(arr1))

print ("==> Matrix subtraction with attrib")
arr1 = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
arr2 = Array([
  [9, 8, 7],
  [6, 5, 4],
  [3, 2, 1]
])
arr1 -= arr2
print ("A - B: {}".format(arr1))

print ("==> Getting negative matrix")
arr1 = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
print ("-A: {}".format(-arr1))

print ("==> Getting absolute values of matrix")
arr1 = Array([
  [-1, 2, -3],
  [4, -5, -6],
  [-7, 8, -9]
])
print ("abs(A): {}".format(abs(arr1)))

print ("==> Identity test (3x3)")
print (eye(3))

print ("==> Zeros test (3x4)")
print (zeros((3, 4)))

print ("==> Ones test (4x3)")
print (ones((4, 3)))

print ("==> Transpose test")
arr1 = Array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
print (arr1.t)

print ("==> Trace test")
print (arr1.trace())

print ("==> Gauss elimination")
arr = Array([
  [1, 2, 2],
  [4, 4, 2],
  [4, 6, 4]
])
gauss_elimination(arr)

print ("==> Gauss elimination w/ pivot")
arr = Array([
  [0, 1, 1],
  [1, 2, 1],
  [1, 1, -1]
])
arr, intermediates = gauss_elimination(arr, show_steps=False, return_intermediates=True)
print ("Intermediates: {}".format(intermediates))
print ("Final result: {}".format(arr))

print ("==> LU decomposition")
arr = Array([
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
])
print ("Original: {}".format(arr))
l, u = lu_decomposition(arr)
print ("L: {}".format(l))
print ("U: {}".format(u))
print ("L * U : {}".format(l*u))

print ("==> Solve Ax=B system")
A = Array([
  [1, 2, 2],
  [4, 4, 2],
  [4, 6, 4],
])
B = Array([
  [3],
  [6],
  [10],
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B)
print ("x = {}".format(x))

print ("==> Solve Ax=B system (exercise 4)")
A = Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
B = Array([
  [-1],
  [2],
  [1],
  [3]
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B)
print ("x = {}".format(x))

print ("==> Determinant test")
arr = Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
print ("A={}".format(arr))
print ("det(A)={}".format(det(arr)))

print ("==> Solve Ax=B system (exercise 5)")
A = Array([
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
B = Array([
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
x = solve(A, B)
print ("x = {}".format(x))

print ("==> Determinant (exercise 6)")
A = Array([
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
print ("A={}".format(A))
print ("det(A)={}".format(det(A)))

print ("==> p-norm test")
v = Array([
  [1],
  [2],
  [3],
])
print ("v = {}".format(v))
print ("p-norm (p=1) = {}".format(vector_norm(v, 1)))
print ("p-norm (p=2) = {}".format(vector_norm(v, 2)))
print ("p-norm (p=3) = {}".format(vector_norm(v, 3)))

print ("==> Solve Ax=B system (jacobi)")
A = Array([
  [3, -1, -1],
  [-1, 3, -1],
  [-1, -1, 3],
])
B = Array([
  [1],
  [2],
  [1],
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B, method="jacobi")
print ("x = {}".format(x))

print ("==> Solve Ax=B system (gauss-seidel)")
A = Array([
  [3, -1, -1],
  [-1, 3, -1],
  [-1, -1, 3],
])
B = Array([
  [1],
  [2],
  [1],
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B, method="gauss_seidel")
print ("x = {}".format(x))

print ("==> Solve exercise 4 w/ gauss only")
A = Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
B = Array([
  [-1],
  [2],
  [1],
  [3]
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B, method='gauss')
print ("x = {}".format(x))

print ("==> Solve exercise 4 w/ gauss-jordan")
A = Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
B = Array([
  [-1],
  [2],
  [1],
  [3]
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B, method='gauss_jordan')
print ("x = {}".format(x))

print ("==> Inversion test")
A = Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
print ("A = {}".format(A))
print ("A^(-1) = {}".format(~A))
print ("A * (A^-1) = {}".format(A*(~A)))
print ("(A^-1) * A = {}".format((~A)*A))

print ("==> Cholesky decomposition")
A = Array([
  [ 1,  0.2, 0.4],
  [0.2,  1 , 0.5],
  [0.4, 0.5,  1 ],
])
print ("A = {}".format(A))
l, lt = cholesky_decomposition(A)
print ("L = {}".format(l))
print ("L.t = {}".format(lt))

print ("==> is_definite_positive")
A = Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
print ("A = {}".format(A))
print ("Definite positive? {}".format(is_definite_positive(A)))

print ("==> Solve exercise 4 w/ LU")
A = Array([
  [5, -4, 1, 0],
  [-4, 6, -4, 1],
  [1, -4, 6, -4],
  [0, 1, -4, 5],
])
B = Array([
  [-1],
  [2],
  [1],
  [3]
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B, method='lu')
print ("x = {}".format(x))

print ("==> Solve Ax=B w/ Cholesky")
A = Array([
  [ 1,  0.2, 0.4],
  [0.2,  1 , 0.5],
  [0.4, 0.5,  1 ],
])
B = Array([
  [ 0.6],
  [-0.3],
  [-0.6],
])
print ("A = {}".format(A))
print ("B = {}".format(B))
x = solve(A, B, method='cholesky')
print ("x = {}".format(x))
