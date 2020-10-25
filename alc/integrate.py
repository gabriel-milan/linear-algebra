__all__ = [
  'integrate',
]

import math
from sympy import *
from alc.Array import Array
from alc.utils import zeros
from alc.systems import solve
from alc.constants import constants
from alc.exceptions import ExpressionError

def integrate (function, a, b, n_points = 10, method='polynomial'):

  if ((n_points < 1) or (n_points > 10)):
    raise ValueError("n_points must be between 1 and 10")
  x = Symbol('x')
  try:
    f = lambdify(x, eval(function))
  except:
    raise ExpressionError("Falhou ao executar a seguinte função: {}. Favor verificar a expressão.".format(function))
  if (n_points == 1):
    return f(abs(a+b)/2)*(abs(b-a))
  
  def laguerre_function (x):
    return f(x)/math.exp(-x)

  def hermite_function (x):
    return f(x)/math.exp(-x**2)

  # Getting hermite sum
  sum_hermite = 0
  points = constants.hermite[n_points]['points']
  weights = constants.hermite[n_points]['weights']
  for i in range(n_points):
    sum_hermite += hermite_function(points[i]) * weights[i]

  # Getting laguerre sum
  sum_laguerre = 0
  points = constants.laguerre[n_points]['points']
  weights = constants.laguerre[n_points]['weights']
  for i in range(n_points):
    sum_laguerre += laguerre_function(points[i]) * weights[i]

  if (a == float("-inf")):
    
    # B is positive infinite
    if (b == float("inf")):
      return sum_hermite

    # B is positive
    elif (b >= 0):
      return sum_hermite - sum_laguerre + integrate(function, 0, b, n_points, method='gauss_quadrature')

    # B is negative
    else:
      return sum_hermite - sum_laguerre - integrate(function, b, 0, n_points, method='gauss_quadrature')

  elif (b == float("inf")):

    if (a == 0):
      return sum_laguerre

    elif (a > 0):
      return sum_laguerre - integrate(function, 0, a, n_points, method='gauss_quadrature')

    else:
      return sum_hermite - sum_laguerre - integrate(function, a, 0, n_points, method='gauss_quadrature')

  if (method == 'polynomial'):
    delta_x = abs(b - a) / (n_points - 1)
    B = []
    integration_points = []
    res = 0

    for i in range(1, n_points + 1):
      integration_points.append(a+(i-1)*delta_x)
      B.append((b**i - a**i) / i)

    vandermonde = zeros((n_points, n_points))
    B = Array([
      [b] for b in B
    ])

    for i in range(n_points):
      for j in range(n_points):
        vandermonde[i][j] = integration_points[j]**i

    x = solve(vandermonde, B)

    for i in range(n_points):
      res += x[i][0]*f(integration_points[i])
    
    return res

  elif (method == 'gauss_quadrature'):
    weights = constants.legendre[n_points]['weights']
    points = constants.legendre[n_points]['points']
    L = b - a
    res = 0
    integration_points = []
    
    for i in range(n_points):
      integration_points.append((a + b + points[i] * L) / 2)
    
    for i in range(n_points):
      res += f(integration_points[i])*weights[i]
    
    return res * L / 2

  else:
    raise NameError("Method {} not allowed.".format(method))