import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

def g1(x0):
    return 1.21

def Q1():
    print("-------------------Q1-------------------")
    print("")
    print("Part A ------>")
    a = 0
    b = 2
    Ep = 1.0/100000000
    n1 = (math.log(b-a)-math.log(Ep))/math.log(2)
    n1 = math.ceil(n1)
    for i in range(0, 1000):
        c= (a+b)/2.0
        vala = math.sqrt(a) - 1.1
        valb = math.sqrt(b) - 1.1
        valc = math.sqrt(c) - 1.1
        if(vala*valc < 0):
            b = c
        else: 
            a = c    
        if(abs(valc)<Ep):
            break
    n2 = i
    print("Using Bisection Method:")
    print("Number of iteration required: %d"%n2)
    print("Expected number of iteration required (Convergence Analysis): %d"%n1)
    print("Approximate root of given equation: %f"%c)
    print("f(%f): %0.15f"%(c, valc))

    print("")
    print("Part B ------>")
    print("Fixed Point Iteration")
    tol = 0.00000001
    err = 1
    r = 0
    n = 0
    while err > tol:
        n += 1
        r = g1(r)
        err = abs(r - g1(r))

    print('The root of the equation comes out to be', round(r, 6))
    print('Number of iterations required are', n)

    print("-------------------------------------------------------")
    print("")

def f2(x):
    return np.tan(x*np.pi)-6

def Q2():
    print("-------------------Q2-------------------")
    print("")
    x0 = 0
    x1 = 0.48
    root = 0.447431543
    for i in range(10):
        if f2((x0+x1)/2)*f2(x1) < 0:
            x0 = (x0+x1)/2
        else:
            x1 = (x0+x1)/2
    r = (x0+x1)/2
    print("Bisection Method ---->")
    print('The root obtained: ', r)
    print('Error in approximation:', round(abs(r-root), 10))

    x0 = 0
    x1 = 0.48
    for i in range(10):
        x0 = x1 - f2(x1)*((x1-x0)/(f2(x1)-f2(x0)))
        x0, x1 = x1, x0
    print("Secant Method ---->")
    print('The root obtained: ', x1)
    print('Error in approximation: ', round(abs(x1-root), 10))
    print("-------------------------------------------------------")
    print("")

def f3(x):
    return x*x

def Q3():
    print("-------------------Q3-------------------")
    print("")
    Cong_X = [0.25]
    Diverg_X = [4]
    for i in range(2):
        x1 = f3(0.25)
        Cong_X.append(x1)
        y1 = f3(4)
        Diverg_X.append(y1)
    X = np.linspace(0, 20, 500)
    Y = [f3(x) for x in X]
    fx_Cong = [f3(x) for x in Cong_X]
    fx_Diverg = [f3(y) for y in Diverg_X]
    plt.title('Function with 2 fixed points Function = x*x')
    plt.plot(X, Y, label='Function f(x) = x-square')
    plt.scatter(Cong_X, fx_Cong, label='Converging Sequence with x0 = 0.25')
    plt.scatter(Diverg_X, fx_Diverg, label='Diverging Sequence with y0 = 4')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()
    print("-------------------------------------------------------")
    print("")

def EulerMethod(x0,x1,y0,h,f):
    y=[y0]
    x=[x0]
    j=x0
    while (j<x1):
        x.append(j+h)
        j=j+h

    for i in range(len(x)):
        y.append(y[i]+f(x[i],y[i])*h)
    x.append(j+h)
    return x[:-1:],y[:-1:]

def EulerModified(t1,t2,y0,h,f):
    ans=[y0]
    x=[t1]
    y=y0
    t=t1
    i=0
    while(t<t2):
        y=y+h*(f(t,y)+f(t+h,y+h*f(t,y)))/2
        t=t+h
        x.append(t)
        ans.append(y)
        i+=1
    return x, ans  

def RungeKuttafun4(x0,x1,y0,h,f):
    x=x0
    y=y0
    res=[y0]
    xp=[x0]
    while(x<x1):
        k1=f(x,y)
        k2=f(x+h/2,y+h*k1/2)
        k3=f(x+h/2,y+h*k2/2)
        k4=f(x+h,y+h*k3)
        y=y+h*(k1+2*k2+2*k3+k4)/6
        x=x+h
        xp.append(x)
        res.append(y)
    return xp, res

def RungeKuttafun2(x0,x1,y0,h,f):
    x=x0
    y=y0
    res=[y0]
    xp=[x0]
    alpha=1/2
    beta=alpha
    a=1-1/(2*alpha)
    b=1/(2*alpha)
    while(x<x1):
        k1=f(x,y)
        k2=f(x+alpha*h,y+h*k1*beta)
        y=y+h*(a*k1+b*k2)
        x=x+h
        xp.append(x)
        res.append(y)
    return xp, res

def f4(x,y):
  return 0.5*(x-y)

def yx(x0):
  return 3*math.exp(-x0/2)+x0-2

def Q4():
    print("-------------------Q4-------------------")
    print("")

    H=[1,1/2,1/4,1/8]
    x0=0
    x1=3
    y0=1
    print("Euler Method ---->")
    print("")
    for h in H:
        table=[]
        x,eu=EulerMethod(x0,x1,y0,h,f4)
        for i in range(len(x)):
            table.append([i,h,x[i],eu[i],yx(x[i]),abs(eu[i]-yx(x[i]))])
        print(tabulate(table, headers=["Iter","h","Xi","Yi","Actual Y","Err"]))
        print("")

    print("Modified Euler Method ---->")
    print("")
    i = 0
    for h in H:
        table=[]
        x,eu=EulerModified(x0,x1,y0,h,f4)
        for i in range(len(x)):
            table.append([i,h,x[i],eu[i],yx(x[i]),abs(eu[i]-yx(x[i]))])
        print(tabulate(table, headers=["Iter","h","Xi","Yi","Actual Y","Err"]))
        print("")

    print("Runge Kutta Order 4 Method ---->")
    print("")
    for h in H:
        i=0
        table=[]
        x,eu=RungeKuttafun4(x0,x1,y0,h,f4)
        for i in range(len(x)):
            table.append([i,h,x[i],eu[i],yx(x[i]),abs(eu[i]-yx(x[i]))])
        print(tabulate(table, headers=["Iter","h","Xi","Yi","Actual Y","Err"]))
        print("")

    print("Runge Kutta Order 2 Method ---->")
    print("")
    for h in H:
        i=0
        table=[]
        x,eu=RungeKuttafun2(x0,x1,y0,h,f4)
        for i in range(len(x)):
            table.append([i,h,x[i],eu[i],yx(x[i]),abs(eu[i]-yx(x[i]))])
        print(tabulate(table, headers=["Iter","h","Xi","Yi","Actual Y","Err"]))
        print("")

    print("-------------------------------------------------------")
    print("")

Q1()
Q2()
Q3()
Q4()

