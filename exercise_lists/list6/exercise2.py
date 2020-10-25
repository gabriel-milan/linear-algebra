import alc
from math import sin, cos
import matplotlib.pyplot as plt

def function (t, y, z):
  return -z/5 -y + 2 * sin(t/2) + sin(t) + cos(3*t/2)

for delta in [10, 5, 1, 0.5, 0.1, 0.05, 0.01]:
  ts, xs = alc.solve_second_order_ode(function, 0, 100, delta, 0, 0, method='taylor_series')

  plt.style.use('fivethirtyeight')
  plt.figure(figsize=(20,20))
  plt.title (r"Método: Expansão em Série de Taylor $\Delta={}$".format(delta))
  plt.plot (ts, xs, color='red')
  plt.ylabel("y''(t)")
  plt.xlabel("t")
  plt.show()

  ts, xs = alc.solve_second_order_ode(function, 0, 100, delta, 0, 0, method='runge_kutta_nystron')

  plt.style.use('fivethirtyeight')
  plt.figure(figsize=(20,20))
  plt.title (r"Método: Runge-Kutta-Nystron $\Delta={}$".format(delta))
  plt.plot (ts, xs, color='red')
  plt.ylabel("y''(t)")
  plt.xlabel("t")
  plt.show()