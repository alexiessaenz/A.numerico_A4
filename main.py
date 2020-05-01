from scipy.integrate import quad
from math import pi, cos, log
import decimal 

def f(alpha):
    return ((3*pi)/2)*quad(lambda x: cos((3*pi*x)/2)/((3*pi*x)/2)**(alpha),0,1)[0]

def df(alpha):
    return (-(3*pi)/2)*quad(lambda x: cos((3*pi*x)/2)*log((3*pi*x)/2)*((3*pi*x)/2)**(-alpha),0,1)[0]

def newton(p0, TOL, Nmax):
    for i in range(Nmax):
        p=p0-f(p0)/df(p0)
        decimal.getcontext().prec = 15
        print ( i , "\t"  ,  p0 , "\t"  , p , "\t"  , abs(p0-p) )
        if abs(p-p0) < TOL:
            break
        p0 = p

newton(pi/4, 10**-15, 40)