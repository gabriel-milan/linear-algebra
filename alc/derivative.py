__all__ = [
  'diff',
]

from sympy import *
from alc.constants import constants
from alc.exceptions import ExpressionError

def diff (function, x0, delta_x=constants.epsilon, method='center', p=2, q=2):
  x = Symbol('x')
  try:
    f = lambdify(x, eval(function))
  except:
    raise ExpressionError("Falhou ao executar a seguinte função: {}. Favor verificar a expressão.".format(function))
  if (method == 'step_back'):
    d1 = (f(x0)-f(x0-delta_x))/delta_x
    delta_x /= q
    d2 = (f(x0)-f(x0-delta_x))/delta_x
  elif (method == 'step_forward'):
    d1 = (f(x0+delta_x)-f(x0))/delta_x
    delta_x /= q
    d2 = (f(x0+delta_x)-f(x0))/delta_x
  elif (method == 'center'):
    d1 = (f(x0+delta_x)-f(x0-delta_x))/(2*delta_x)
    delta_x /= q
    d2 = (f(x0+delta_x)-f(x0-delta_x))/(2*delta_x)
  else:
    raise NameError ("Method {} not allowed".format(method))
  return d1 + ((d1-d2)/(q**(-p)-1))