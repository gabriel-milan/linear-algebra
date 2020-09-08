__all__ = [
  'Array'
]

from copy import deepcopy

class Array (object):

  def __init__ (self, iterable, *args, **kwargs):
    self.__iterable = iterable
    self.__shape = []
    self.__shape.append(len(iterable))
    shape2 = None
    for row in iterable:
      try:
        if not shape2:
          shape2 = len(row)
          self.__shape.append(shape2)
        elif shape2 != len(row):
          raise ValueError("Shape mismatch")
      except TypeError:
        self.__shape.append(1)
        self.__shape.reverse()
        break
  
  @property
  def shape (self):
    return self.__shape

  @property
  def iterable (self):
    return self.__iterable

  # Pretty printer
  def __repr__ (self):
    ret = "alc.Array(\n"
    if self.shape[0] == 1:
      ret += "{},\n".format(self.__iterable)
    else:
      for i in range(self.shape[0]):
        ret += "{},\n".format(self.__iterable[i])
    return ret + ")"

  def __str__ (self):
    return self.__repr__()

  # Overrides multiplication
  def __rmul__ (self, other):
    return self.__mul__(other)

  # Overrides multiplication
  def __mul__ (self, other):
    if issubclass(self.__class__, other.__class__):
      return self.__matmul(self, other)
    else:
      it = deepcopy(self.__iterable)
      for i in range(self.shape[0]):
        for j in range(self.shape[1]):
          it[i][j] *= other
      return Array(it)

  # Item getter
  def __getitem__ (self, key):
    if issubclass(tuple, key.__class__):
      return self.__iterable[key[0]][key[1]]
    return self.__iterable[key]

  # Item setter
  def __setitem__ (self, key, val):
    self.__iterable[key] = val

  # Matrix multiplication implementation
  def __matmul (self, mat1, mat2):
    try:
      assert mat1.shape[1] == mat2.shape[0]
    except AssertionError:
      raise AssertionError("Matrices can't be multiplied with shapes {} and {}".format(mat1.shape, mat2.shape))
    result = []
    for i in range(mat1.shape[1]):
      result.append([])
      for j in range(mat2.shape[0]):
        result[i].append(0)
    result = Array(result)
    for i in range(mat1.shape[1]):
      for j in range(mat2.shape[0]):
        for k in range(mat2.shape[1]):
          result[i][j] += mat1[i][k] * mat2[k][j]
    return result

  # Matrix comparison
  def __eq__ (self, other):
    if issubclass(self.__class__, key.__class__):
      return self.__iterable == other.iterable
    else:
      raise TypeError("Always compare alc.Array objects instead of anything else")
  
  def __ne__ (self, other):
    return not self.__eq__(other)

  # Matrix adding
  def __add__ (self, other):
    if issubclass(self.__class__, other.__class__):
      try:
        assert self.shape == other.shape
      except AssertionError:
        raise AssertionError("Shape mismatch ({} and {})".format(self.shape, other.shape))
      it = deepcopy(self.__iterable)
      for i in range(self.shape[0]):
        for j in range(self.shape[1]):
          it[i][j] += other[i][j]
      return Array(it)
    else:
      raise TypeError("Always compare alc.Array objects instead of anything else")
    return self
  
  def __radd__ (self, other):
    return self.__add__(other)
  
  # Matrix subtraction
  def __sub__ (self, other):
    if issubclass(self.__class__, other.__class__):
      try:
        assert self.shape == other.shape
      except AssertionError:
        raise AssertionError("Shape mismatch ({} and {})".format(self.shape, other.shape))
      it = deepcopy(self.__iterable)
      for i in range(self.shape[0]):
        for j in range(self.shape[1]):
          it[i][j] -= other[i][j]
      return Array(it)
    else:
      raise TypeError("Always compare alc.Array objects instead of anything else")
    return self

  def __rsub__ (self, other):
    return self.__sub__(other)

  # Matrix division
  def __truediv__ (self, other):
    raise NotImplementedError("Hey! This is not implemented yet!")

  def __rtruediv__ (self, other):
    return self.__truediv__(other)

  # Getting negative of matrix
  def __neg__ (self):
    it = deepcopy(self.__iterable)
    for i in range(self.shape[0]):
      for j in range(self.shape[1]):
        it[i][j] = -it[i][j]
    return Array(it)

  # Getting absolute values of matrix
  def __abs__ (self):
    it = deepcopy(self.__iterable)
    for i in range(self.shape[0]):
      for j in range(self.shape[1]):
        it[i][j] = abs(it[i][j])
    return Array(it)

  # Inverting matrix
  def __invert__ (self):
    raise NotImplementedError("Hey! This is not implemented yet!")

  