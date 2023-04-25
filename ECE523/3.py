# from sympy.core import S
# from sympy import  Symbol,nsolve, Eq,cos,pi
# import mpmath
# mpmath.mp.dps = 15
# x = Symbol('x')
# # solve_poly_inequality( Poly((10000 / x) - 1 ), '<')
# a=Eq(2 - 1.5*10**(-6), cos(pi/8*x) + cos(1/5*x) )
# nsolve(cos(pi/8*x) + cos(1/5*x),2 - 1.5*10**(-6))
import math

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
def Fcn(T):
    return np.cos(math.pi/8*T) + np.cos(1/5*T)-1.9999985
def Fcn3(T):
    return np.cos(2*T) + 2*np.cos(math.sqrt(2)*T) - 2.996
def Fcn2(T):
    return np.cos(2*T) + 2*np.cos(math.sqrt(2)*T) + 2*np.cos(2*np.cos(np.pi/8)*T) + 2*np.cos(2*np.sin(np.pi/8)*T) - 6.992
# sol = fsolve(Fcn2, 0)

for i in range(1000000000):
    a = i/10 + 10
    c1 = Fcn3(a)
    if c1>0:
        break

for i in range(1000000000):
    a = i/10 + 10
    c2 = Fcn2(a)
    if c2>0:
        break
