__all__ = [
  'power_method',
  'jacobi_eigen'
]

from alc.utils import random_array, is_symmetric, eye, generate_p_matrix, get_greater_value_outside_diagonal
from alc.constants import constants

def power_method (arr, threshold=constants.epsilon):
  # Start with random array
  x = random_array((arr.shape[0], 1))
  # First element equals 1
  x[0][0] = 1
  # Iterations
  r = 1000
  lambda_i = constants.epsilon
  while (r > threshold):
    y = arr * x
    new_lambda_i = y[0][0]
    x = y / new_lambda_i
    r = abs(new_lambda_i - lambda_i) / abs(new_lambda_i)
    lambda_i = new_lambda_i
  return lambda_i, x


def jacobi_eigen (arr, threshold=constants.epsilon):
  if not is_symmetric(arr):
    raise ValueError ("Input matrices for Jacobi method must be symmetric.")
  A = arr
  X = eye(arr.shape[0])
  greater, i, j = get_greater_value_outside_diagonal(A)
  while (greater > threshold):
    P = generate_p_matrix(A, i, j)
    A = P.t * A * P
    X = X * P
    greater, i, j = get_greater_value_outside_diagonal(A)
  return A, X