import scipy as sp  #.integrate.solve_ivp for diff. equ
import numpy as np  #numeric stuff
import scipy.integrate
from matplotlib import pyplot as plt    #plotting
from param import *

def u(t):
#input function
    if t==0:
        return 1
    else:
        return 0

def kran_nonlin(t, x):
    i = x[0]
    xc = np.clip(x[1], 0, 6)
    dxc = x[2]
    xb = np.clip(x[3], 0, 1)
    dxb = x[4]
    alpha = x[5]
    dalpha = x[6]

    dx = np.array([u(t)/L - R*i/L,
                   dxc,
                   dc/mc*(dxc-dxb) - cc/mc*(xc-xb) + np.sin(alpha)*mp*g/mc - i*36.69/mc,
                   dxb,
                   -dc/mb*(dxc-dxb) - cc/mb*(xc-xb) + db/mb*dxb + cb/mb*xb,
                   dalpha,
                   np.sin(alpha)*g/l**2 + drot*dalpha]).T


    return dx


#test solve
t = [0, 10]
x0 = np.array([0, 0, 0, 0, 0, 0, 0])
sol = scipy.integrate.solve_ivp(kran_nonlin, t, x0)


plt.plot(sol.t, sol.y[1], label='xc')
plt.plot(sol.t, sol.y[3], label='xb')

plt.grid()
plt.legend()
plt.show()