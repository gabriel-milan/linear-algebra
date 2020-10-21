__all__ = [
  'least_squares',
  'nl_least_squares',
]

from sympy import *
from alc.constants import constants
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

def nl_least_squares (fit_function, symbols, xs, ys, start_values, threshold=constants.epsilon, max_iter=constants.max_iter):
  try:
    if (len(xs) != len(ys)):
      raise ValueError ("Length of X and Y samples must be the same!")
    if (len(symbols) != len(start_values)):
      raise ValueError ("Length of SYMBOLS mus match length of START_VALUES!")
  except Exception as e:
    print ("Failure while comparing X and Y length")
    raise e
  func_vars = []
  for symbol in symbols:
    exec("{0} = Symbol('{0}')".format(symbol))
    exec("func_vars.append({})".format(symbol))
  x = Symbol('x')
  y = Symbol('y')
  eqs = []
  for i in range(len(xs)):
    eqs.append(eval(fit_function).limit(x, xs[i]).limit(y, ys[i]))
  F = Matrix(eqs)
  Y = Matrix(func_vars)
  J = F.jacobian(Y)
  xk1 = Matrix(start_values)
  for k in range(max_iter):
    j = J
    f = F
    for i, var in enumerate(func_vars):
      j = j.limit(var, xk1[i])
      f = f.limit(var, xk1[i])
    delta_x = (j.transpose().n() * j.n()).inv() * (- j.transpose().n() * f.n())
    xk = xk1 + delta_x
    xk1 = xk
    tol = delta_x.norm().n() / xk.norm().n()
    # print ("Iter #{} => j={}, f={}, delta_x={}, xk={}, tol={}".format(k, j, f, delta_x, xk.n(), tol))
    if tol <= threshold:
      ret_arr = []
      for w in range(len(func_vars)):
        ret_arr.append(float(xk.n()[w]))
      return Array(ret_arr)
  raise ValueError("Método de Newton não convergiu (threshold={:e}, max_iter={}).".format(threshold, max_iter))
