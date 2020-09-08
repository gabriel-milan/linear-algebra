__all__ = [
  "eye",
  "zeros",
  "ones",
  "det",
  "vector_norm"
]

from alc.Array import Array

def eye (shape):
  if not issubclass(int, shape.__class__):
    raise TypeError("Shape of identity must be an integer")
  res = []
  for i in range(shape):
    res.append([])
    for j in range(shape):
      if i == j:
        res[i].append(1)
      else:
        res[i].append(0)
  return Array(res)

def zeros (shape):
  if len(shape) != 2:
    raise ValueError("Shape must have two values!")
  res = []
  for i in range(shape[0]):
    res.append([])
    for j in range(shape[1]):
      res[i].append(0)
  return Array(res)

def ones (shape):
  if len(shape) != 2:
    raise ValueError("Shape must have two values!")
  res = []
  for i in range(shape[0]):
    res.append([])
    for j in range(shape[1]):
      res[i].append(1)
  return Array(res)

def random_array (shape):
  import random
  random.seed()
  if len(shape) != 2:
    raise ValueError("Shape must have two values!")
  res = []
  for i in range(shape[0]):
    res.append([])
    for j in range(shape[1]):
      res[i].append(random.random())
  return Array(res)

def det (arr):
  from alc.decomposition import lu_decomposition
  _, _, det = lu_decomposition(arr, return_det=True)
  return det

def vector_norm (vec, p=2):
  if ((vec.shape[0] != 1) and (vec.shape[1] != 1)):
    raise ValueError("Input for vector_norm must be a vector (first or second dimension equals 1)")
  p_sum = 0
  for i in range(vec.shape[0]):
    for j in range(vec.shape[1]):
      p_sum += vec[i][j] ** p
  return p_sum ** (1./p)

def is_square (arr):
  """
  Checks whether a matrix is square
  """
  return arr.shape[0] == arr.shape[1]

def is_diagonally_dominant (arr):
  """
  Checks whether a matrix is diagonally dominant
  """
  dom = zeros((arr.shape[0], 1))
  for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
      if (i != j):
        dom[i][0] += abs(arr[i][j])
  for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
      if (i == j):
        if (abs(arr[i][j]) < dom[i][0]):
          return False
  return True

def is_symmetric (arr):
  """
  Checks whether a matrix is symmetric
  """
  if not is_square(arr):
    raise ValueError("Matrix must be a square before checking whether it's symmetric")
  for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
      if (arr[i][j] != arr[j][i]):
        return False
  return True

def is_definite_positive (arr):
  """
  Checks whether a matrix is definite positive
  """
  # TODO: Implement
  return False