import numpy as np
import math 
import matplotlib.pyplot as plt

def f(x0):
    return math.erf(x0)

def lagrangeInterpolationGen(xr,fxr,deg,x):
    ans = 0
    for i in range(deg+1):
        val = fxr[i]
        l = 1
        for j in range(deg+1):
            if i != j:
                l *= (x - xr[j])/(xr[i] - xr[j])
        ans += val*l
    return ans

def MonomialMat(xr):
    n = len(xr)
    mat = []
    for i in range(n):
        hor = []
        for j in range(n):
            val = pow(xr[i],j)
            hor.append(val)
        mat.append(hor)
    return mat

def MonomialInterpolation(xr,fxr,deg,x):
    mat = MonomialMat(xr)
    mat = np.array(mat)
    A = np.linalg.solve(mat,fxr)

    ans = 0
    for i, fi in enumerate(A):
        ans += fi*pow(x,i)
    return ans

def NewtonPoly(xr,j,x):
    ans = 1
    for i in range(j):
        ans*=(x-xr[i])
    return ans 

def NewtonMat(xr):
    n = len(xr)
    mat = []
    for i in range(n):
        hor = []
        for j in range(n):
            val = NewtonPoly(xr,j,xr[i])
            hor.append(val)
        mat.append(hor)
    return mat

def NewtonInterpolation(xr,fxr,deg,x):
    mat = NewtonMat(xr)
    mat = np.array(mat)
    A = np.linalg.solve(mat,fxr)
    ans = 0
    for i, fi in enumerate(A):
        ans += fi*NewtonPoly(xr,i,x)
    return ans

def Q5():
    print("-------------------Q5-------------------")
    print("")
    xr = []
    it = 1
    while it<=3.2:
        xr.append(it)
        it += 0.2
    deg = len(xr)-1
    fxr = []
    for x in xr:
        fxr.append(f(x))

    z = []
    it = 0
    while it<=4:
        z.append(it)
        it += 0.01
    
    errorMon = []
    errorLang = []
    errorNew = []
    errorMonNew = []
    errorlangNew = []

    for it in z:
        exact = f(it)
        Lang = lagrangeInterpolationGen(xr,fxr,deg,it)
        Mon = MonomialInterpolation(xr,fxr,deg,it)
        New = NewtonInterpolation(xr,fxr,deg,it)
        err_Lang = abs(exact-Lang)
        errorLang.append(err_Lang)
        err_Mon = abs(exact-Mon)
        errorMon.append(err_Mon)
        err_New = abs(exact-New)
        errorNew.append(err_New)
        error_MonNew = abs(Mon-New)
        errorMonNew.append(error_MonNew)
        error_LangNew = abs(Lang-New)
        errorlangNew.append(error_LangNew)
        print("Actaul Value for z = %0.2f is %0.2f ,Lagrange : %0.2f ,Monomial : %0.2f ,Newton : %0.2f"%(it,exact,Lang,Mon,New))
    
    plt.plot(z,errorLang)
    plt.title("Error for LagrangeInterpolation")
    plt.xlabel("Value of z")
    plt.ylabel("Lagrange Error")
    plt.show()
    plt.clf()
    plt.plot(z,errorMon)
    plt.title("Error for MonomialInterpolation")
    plt.xlabel("Value of z")
    plt.ylabel("Monomial Error")
    plt.show()
    plt.clf()
    plt.plot(z,errorNew)
    plt.title("Error for NewtonInterpolation")
    plt.xlabel("Value of z")
    plt.ylabel("Newton Error")
    plt.show()
    plt.clf()
    plt.plot(z,errorMonNew)
    plt.title("Error between MonomialInterpolation && NewtonInterpolation")
    plt.xlabel("Value of z")
    plt.ylabel("Error difference")
    plt.show()
    plt.clf()
    plt.plot(z,errorlangNew)
    plt.title("Error between LagrangeInterpolation && NewtonInterpolation")
    plt.xlabel("Value of z")
    plt.ylabel("Error difference")
    plt.show()
    plt.clf()
    print("-------------------------------------------------------")

Q5()
