import alc

def function (t, y):
  return -2*t*(y**2)

ts, xs = alc.solve_first_order_ode(function, 0, 10, 0.1, 1, method='euler')

for i in range(len(ts)):
  print("t={:.3f}\t\tx={:.5f}".format(ts[i], xs[i]))
