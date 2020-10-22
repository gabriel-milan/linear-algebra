__all__ = [
  'bisection',
  'newton',
  'newton_secant',
  'inverse_interpolation',
]

from sympy import *
from alc.constants import constants
from alc.exceptions import ExpressionError

def bisection (function, a, b, threshold=constants.epsilon):
  x = Symbol('x')
  try:
    f = lambdify(x, eval(function))
  except:
    raise ExpressionError("Falhou ao executar a seguinte função: {}. Favor verificar a expressão.".format(function))
  while (abs(b - a) >= threshold):
    xi = (a + b) / 2
    fi = f(xi)
    if (fi > 0):
      b = xi
    else:
      a = xi
  return xi

def newton (function, x0, threshold=constants.epsilon, max_iter=constants.max_iter):
  x = Symbol('x')
  try:
    func = eval(function)
    f = lambdify(x, func)
    f_prime = func.diff(x)
    f_prime = lambdify(x, f_prime)
  except:
    raise ExpressionError("Falhou ao executar a seguinte função: {}. Favor verificar a expressão.".format(function))
  xk1 = x0
  for k in range(max_iter):
    xk = xk1 - f(xk1) / f_prime(xk1)
    if (abs(xk-xk1) <= threshold):
      return xk
    xk1 = xk
  raise ValueError("Método de Newton não convergiu (threshold={:e}, max_iter={}).".format(threshold, max_iter))

def newton_secant (function, x0, threshold=constants.epsilon, max_iter=constants.max_iter):
  x = Symbol('x')
  try:
    f = lambdify(x, eval(function))
  except:
    raise ExpressionError("Falhou ao executar a seguinte função: {}. Favor verificar a expressão.".format(function))
  delta_x = 1e-3
  xk1 = x0
  xk = xk1 + delta_x
  fa = f(xk1)
  for k in range(max_iter):
    fi = f(xk)
    new_xk = xk - fi*(xk-xk1)/(fi-fa)
    # print ("Iter {} => x(k-1) = {}, x(k) = {}, x(k+1) = {}, |x(k+1)-x(k)|={}".format(k, xk1, xk, new_xk, abs(new_xk-xk)))
    if (abs(new_xk-xk) <= threshold):
      return xk
    fa = fi
    xk1 = xk
    xk = new_xk
  raise ValueError("Método de Newton secante não convergiu (threshold={:e}, max_iter={}).".format(threshold, max_iter))

def inverse_interpolation (function, x1, x2, x3, threshold=constants.epsilon, max_iter=constants.max_iter):
  
  def sort_pairs (x1, x2, x3, y1, y2, y3):
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    for passnum in range(len(y)-1, 0, -1):
      for i in range(passnum):
        if y[i] > y[i+1]:
          tmp_x = x[i]
          tmp_y = y[i]
          x[i] = x[i+1]
          y[i] = y[i+1]
          x[i+1] = tmp_x
          y[i+1] = tmp_y
    return x[0], x[1], x[2], y[0], y[1], y[2]

  def replace_greater (x1, x2, x3, y1, y2, y3, new_x, new_y):
    greater = max([y1, y2, y3])
    if y1 == greater:
      x1 = new_x
      y1 = new_y
    elif y2 == greater:
      x2 = new_x
      y2 = new_y
    elif y3 == greater:
      x3 = new_x
      y3 = new_y
    return sort_pairs(x1, x2, x3, y1, y2, y3)

  x = Symbol('x')
  try:
    f = lambdify(x, eval(function))
  except:
    raise ExpressionError("Falhou ao executar a seguinte função: {}. Favor verificar a expressão.".format(function))
  xk1 = float('inf')
  for k in range(max_iter):
    y1 = f(x1)
    y2 = f(x2)
    y3 = f(x3)
    xk = (y2*y3*x1) / ((y1-y2)*(y1-y3)) + (y1*y3*x2) / ((y2-y1)*(y2-y3)) + (y1*y2*x3) / ((y3-y1)*(y3-y2))
    # print ("Iter {} => x1={:.3f}, x2={:.3f}, x3={:.3f}, y1={:.3f}, y2={:.3f}, y3={:.3f}, x*={:.3f}, |x(k) - x(k-1)|={:.3f}".format(k, x1, x2, x3, y1, y2, y3, xk, abs(xk-xk1)))
    if (abs(xk-xk1) <= threshold):
      return xk
    x1, x2, x3, y1, y2, y3 = replace_greater(x1, x2, x3, y1, y2, y3, xk, f(xk))
    xk1 = xk
  raise ValueError("Método da interpolação inversa não convergiu (threshold={:e}, max_iter={}).".format(threshold, max_iter))
