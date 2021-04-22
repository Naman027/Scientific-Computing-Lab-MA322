import numpy as np
import math

def f1(x0):
    return np.exp(-x0*x0)

def lagrangeInterpolationOne(xr,fxr,x):
    ans = 0
    for i in range(2):
        val = fxr[i]
        l = 1
        for j in range(2):
            if i != j:
                l *= (x - xr[j])/(xr[i] - xr[j])
        ans += val*l
    return ans

def lagrangeInterpolationTwo(xr,fxr,x):
    ans = 0
    for i in range(3):
        val = fxr[i]
        l = 1
        for j in range(3):
            if i != j:
                l *= (x - xr[j])/(xr[i] - xr[j])
        ans += val*l
    return ans


def Q3():
    print("-------------------Q3-------------------")
    print("")
    x0 = -1
    x1 = 0
    x2 = 1
    xr = np.array([x0,x1,x2])
    fxr = f1(xr)
    x = 0.9
    actual = f1(0.9)
    print("The Actual Value of f(0.9) is %.6f"%(actual))
    expected = lagrangeInterpolationTwo(xr,fxr,x)
    print("The Expected value of f(0.9) using degree 2 Lagrange Interpolation is %.6f"%(expected))
    abserr = abs(expected-actual)
    print("The Max Absolute Error is %.6f"%(abserr))
    relerr = (abserr/actual)*100
    print("The Max Relative Error is %.6f%%"%(relerr))
    print("-------------------------------------------------------")

Q3()
