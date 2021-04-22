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

def Q1():
    print("-------------------Q1-------------------")
    print("")
    ans1 = f1(0.25)
    ans2 = f1(0.75)
    print("The Actual Value for x = 0.25 is %.10f"%(ans1))
    print("The Actual Value for x = 0.75 is %.10f"%(ans2))
    print("")
    # Part 1
    x0 = 0.0
    x1 = 0.5
    print("Part I --->")
    xr = np.array([x0,x1])
    fxr = f1(xr)
    x = 0.25
    ans = lagrangeInterpolationOne(xr,fxr,x)
    print("The Approx Value of f(0.25) using Lagrange Interpolation is %.10f"%(ans))
    print("")
    # Part 2
    x0 = 0.5
    x1 = 1.0
    print("Part II --->")
    xr = np.array([x0,x1])
    fxr = f1(xr)
    x = 0.75
    ans = lagrangeInterpolationOne(xr,fxr,x)
    print("The Approx Value of f(0.75) using Lagrange Interpolation is %.10f"%(ans))
    print("")
    #Part 3
    x0 = 0
    x1 = 1
    x2 = 2
    print("Part III --->")
    xr = np.array([x0,x1,x2])
    fxr = f1(xr)
    x = 0.25
    ans = lagrangeInterpolationTwo(xr,fxr,x)
    print("The Approx Value of f(0.25) using Lagrange Interpolation is %0.10f"%(ans))
    x = 0.75
    ans = lagrangeInterpolationTwo(xr,fxr,x)
    print("The Approx Value of f(0.75) using Lagrange Interpolation is %.10f"%(ans))
    print("")
    print("By observations we can see that I and II approximations are better as compared to III")
    print("-------------------------------------------------------")

Q1()



