import numpy as np
import math

def f1(x0):
    return np.exp(x0)

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

def Q2():
    print("-------------------Q2-------------------")
    print("")
    # Part I
    print("Part I --->")
    x1 = 8.3
    x2 = 8.6
    xr = np.array([x1, x2])
    y1 = 17.56492
    y2 = 18.50515
    fxr = np.array([y1, y2])
    x = 8.4
    ans = lagrangeInterpolationOne(xr,fxr,x)
    print("Choosen Interval = [8.3, 8.6]")
    print("The Approximate value of f(8.4) with degree 1 Lagrange Interpolation is %.10f"%(ans))
    print("")
    x0 = 8.1
    xr = np.array([x0,x1,x2])
    y0 = 16.94410
    fxr = np.array([y0,y1,y2])
    x = 8.4
    ans = lagrangeInterpolationTwo(xr,fxr,x)
    print("Choosen Interval = [8.1, 8.3, 8.6]")
    print("The Approximate value of f(8.4) with degree 2 Lagrange Interpolation is %.10f"%(ans))
    print("")
    x3 = 8.7
    y3 = 18.82091
    xr = np.array([x0,x1,x2,x3])
    fxr = np.array([y0,y1,y2,y3])
    x = 8.4
    ans = lagrangeInterpolationThree(xr,fxr,x)
    print("Choosen Interval = [8.1, 8.3, 8.6, 8.7]")
    print("The Approximate value of f(8.4) with degree 3 Lagrange Interpolation is %.10f"%(ans))
    print("")
    print("Part II --->")
    x1 = -0.5
    x2 = -0.25
    y1 = -0.02475000
    y2 = 0.33493750
    xr = np.array([x1,x2])
    fxr = np.array([y1,y2])
    x = -1/3
    ans = lagrangeInterpolationOne(xr,fxr,x)
    print("Choosen Interval = [-0.5, -0.25")
    print("The Approximate value of f(-1/3) with degree 1 Lagrange Interpolation is %.10f"%(ans))
    print("")
    x3 = 0 
    y3 = 1.10100000
    xr = np.array([x1,x2,x3])
    fxr = np.array([y1,y2,y3])
    x = -1/3
    ans = lagrangeInterpolationTwo(xr,fxr,x)
    print("Choosen Interval = [-0.5, -0.25, 0]")
    print("The Approximate value of f(-1/3) with degree 2 Lagrange Interpolation is %.10f"%(ans))
    print("")
    x0 = -0.75
    y0 = -0.07181250
    xr = np.array([x0,x1,x2,x3])
    fxr = np.array([y0,y1,y2,y3])
    x = -1/3
    ans = lagrangeInterpolationThree(xr,fxr,x)
    print("Choosen Interval = [-0.75, -0.5, -0.25, 0]")
    print("The Approximate value of f(-1/3) with degree 3 Lagrange Interpolation is %.10f"%(ans))
    print("")
    print("-------------------------------------------------------")
    
Q2()