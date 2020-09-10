__all__ = [
  'power_method'
]

from alc.utils import random_array
from alc.constants import constants

def power_method (arr, threshold=1e-3):
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
