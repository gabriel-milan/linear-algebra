from alc import Array, ones, zeros, eye

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