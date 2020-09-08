__all__ = [
  "eye",
  "zeros",
  "ones",
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
