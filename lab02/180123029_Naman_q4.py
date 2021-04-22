import numpy as np
import math

def f1(x0):
    return np.log10(np.tan(x0))

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

def lagrangeInterpolationThree(xr,fxr,x):
    ans = 0
    for i in range(4):
        val = fxr[i]
        l = 1
        for j in range(4):
            if i != j:
                l *= (x - xr[j])/(xr[i] - xr[j])
        ans += val*l
    return ans

def Q4():
    print("-------------------Q4-------------------")
    print("")
    x0 = 1.00
    x1 = 1.05
    x2 = 1.10
    x3 = 1.15
    xr = np.array([x0,x1,x2,x3])
    fxr = np.array([0.1924,0.2414,0.2933,0.3492])
    x = 1.09
    actual = f1(1.09)
    print("The Actual Value of f(1.09) is %.4f"%(actual))
    expected = lagrangeInterpolationThree(xr,fxr,x)
    print("The Expected value of f(1.09) using degree 3 Lagrange Interpolation is %.4f"%(expected))
    abserr = abs(expected-actual)
    print("The Max Absolute Error is %.4f"%(abserr))
    relerr = (abserr/actual)*100
    print("The Max Relative Error is %.4f%%"%(relerr))
    print("-------------------------------------------------------")

Q4()
