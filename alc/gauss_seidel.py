__all__ = [
  "gauss_seidel"
]

from copy import deepcopy
from alc.utils import random_array, zeros, vector_norm, is_diagonally_dominant, is_definite_positive

def gauss_seidel (A, B, threshold=1e-3):
  if (not is_diagonally_dominant(A)):
    if (not is_definite_positive(A)):
      raise ValueError("A matriz \"A\" não é estritamente diagonal dominante nem positiva definida e, portanto, o método de Gauss-Seidel não irá convergir!")
  prev_x = random_array(B.shape)
  r = 1000
  n = B.shape[0]
  while (r > threshold):
    x = zeros(B.shape)
    for i in range(x.shape[0]):
      x[i][0] = B[i][0]
      for j in range(0, i):
        x[i][0] -= A[i][j]*x[j][0]
      for j in range(i+1, n):
        x[i][0] -= A[i][j]*prev_x[j][0]
      x[i][0] /= A[i][i]
    r = vector_norm(x - prev_x, 2) / vector_norm(x, 2)
    prev_x = deepcopy(x)
  return x