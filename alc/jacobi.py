__all__ = [
  "jacobi"
]

from copy import deepcopy
from alc.constants import constants
from alc.utils import random_array, zeros, vector_norm, is_diagonally_dominant

def jacobi (A, B, threshold=constants.epsilon):
  if (not is_diagonally_dominant(A)):
    raise ValueError("A matriz \"A\" não é estritamente diagonal dominante e, portanto, o método de Jacobi não irá convergir!")
  prev_x = random_array(B.shape)
  r = 1000
  n = B.shape[0]
  while (r > threshold):
    x = zeros(B.shape)
    for i in range(x.shape[0]):
      x[i][0] = B[i][0]
      for j in range(0, n):
        if (i != j):
          x[i][0] -= A[i][j]*prev_x[j][0]
      x[i][0] /= A[i][i]
    r = vector_norm(x - prev_x, 2) / vector_norm(x, 2)
    prev_x = deepcopy(x)
  return x
