import scipy as sp  #.integrate.solve_ivp for diff. equ
import numpy as np  #numeric stuff
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
    xc = x[1]
    dxc = x[2]
    xb = x[3]
    dxb = x[4]
    alpha = x[5]
    dalpha = x[6]

    dx = np.array([u(t)/L - R*i/L,
                   dxc,
                   dc/mc*(dxc-dxb) - cc/mc*(xc-xb) + np.sin(alpha)*mp*g/mc - i*36,69/mc,
                   dxb,
                   -dc/mb*(dxc-dxb) - cc/mb*(xc-xb) + db/mb*dxb + cb/mb*xb,
                   dalpha,
                   np.sin(alpha)*g/l**2 + drot*dalpha]).T


    return dx


#test solve
