import scipy as sp  #.integrate.solve_ivp for diff. equ
import numpy as np  #numeric stuff
import scipy.integrate
from matplotlib import pyplot as plt    #plotting
from param import *

def u(t):
#input function
    if t < 5:
        return 0
    elif 5 <= t < 10:
        return 50
    elif 10 <= t < 20:
        return -25
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

    Fg = mp*g
    J = mp*l**2

    ddxc = dc/mc*(dxb-dxc) + cc/mc*(xb-xc) - np.sin(alpha)*mp*g/mc - i*36.69/mc
    dx = np.array([u(t)/L - R*i/L - kt/L*(dxb-dxc),
                   dxc,
                   ddxc,
                   dxb,
                   -dc/mb*(dxb-dxc) - cc/mb*(xb-xc) + db/mb*dxb + cb/mb*xb + i*36.69/mb,
                   dalpha,
                    -Fg*np.sin(alpha)*l/J - drot*dalpha/J + mp*ddxc*l*np.cos(alpha)/J]).T

    return dx


#test solve#
t_span = [0, 50]
x0 = np.array([0, 0, 0, 0, 0, 0, 0])
sol = scipy.integrate.solve_ivp(kran_nonlin, t_span, x0)

plt.plot(sol.t, sol.y[0], label='i')
plt.plot(sol.t, sol.y[1], label='xc')
plt.plot(sol.t, sol.y[3], label='xb')

plt.plot(sol.t, sol.y[2], label='dxc')
plt.plot(sol.t, sol.y[4], label='dxb')
plt.plot(sol.t, sol.y[5], label='alpha')
#plt.plot(sol.t, sol.y[6], label='dalpha')
plt.grid()
plt.legend()
plt.show()