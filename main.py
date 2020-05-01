from scipy.integrate import quad
from math import pi, cos, log
from decimal import *

def f(alpha):
    return ((3*pi)/2)*quad(lambda x: cos((3*pi*x)/2)/((3*pi*x)/2)**(alpha),0,1)[0]

def df(alpha):
    return (-(3*pi)/2)*quad(lambda x: cos((3*pi*x)/2)*log((3*pi*x)/2)*((3*pi*x)/2)**(-alpha),0,1)[0]

def newton(p0, TOL, Nmax):
    for i in range(Nmax):
        p=p0-f(p0)/df(p0)
        #getcontext().prec = 5
        print(str(i)+"\t"+str(p0)+"\t"+str(p)+"\t"+str(abs(p0-p)))
        if abs(p-p0) < TOL:
            break
        p0 = p

newton(pi/4, 10**-15, 40)