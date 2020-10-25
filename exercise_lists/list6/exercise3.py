import alc
from math import sqrt
import matplotlib.pyplot as plt

def function (t, y, z):
  g = 9.81 # m*s^(-2)
  return - g - z * sqrt(z ** 2)

ts, xs = alc.solve_second_order_ode(function, 0, 20, 0.1, 0, 0, method='taylor_series')

plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,20))
plt.title ("Método: expansão em série de Taylor")
plt.plot (ts, xs, color='red')
plt.ylabel("y''(t)")
plt.xlabel("t")
plt.show()

ts, xs = alc.solve_second_order_ode(function, 0, 20, 0.1, 0, 0, method='runge_kutta_nystron')

plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,20))
plt.title ("Método: Runge-Kutta-Nystron")
plt.plot (ts, xs, color='red')
plt.ylabel("y''(t)")
plt.xlabel("t")
plt.show()