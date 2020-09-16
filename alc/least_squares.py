__all__ = [
  'least_squares'
]

from alc.utils import zeros, ones

def least_squares (x, y):
  # Length of X and Y samples must be the same
  try:
    if (len(x) != len(y)):
      raise ValueError ("Length of X and Y samples must be the same!")
  except Exception as e:
    print ("Failure while comparing X and Y length")
    raise e
  # Start with ones matrix and then just replace with X values on first column
  P = ones((len(x), 2))
  for i, val in enumerate(x):
    P[i][0] = val
  # Then, turn y samples into an array
  Y = zeros((len(y), 1))
  for i, val in enumerate(y):
    Y[i][0] = val
  # Next, do A = P^T * P, C = P^T * Y
  A = P.t * P
  C = P.t * Y
  # Finally, find B = A^(-1) * C
  B = ~A * C
  # a, b are first and second values of B
  return B[0][0], B[1][0]