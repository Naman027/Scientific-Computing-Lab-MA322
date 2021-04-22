import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f1(x, y):
    n1 = 2e3
    n2 = 2e3
    n3 = 3e3
    k = 6.22e-19
    return k*((n1-y/2)**2)*((n2 - y/2)**2)*((n3 - 3*y/4)**3)

def RangeKuttafun4(f, y0, start, end, h):
    n = int((end - start)/h)
    y = [y0]
    for i in range(n):
        yn = y[-1]
        xn = start + i*h
        k1 = f(xn, yn)
        k2 = f(xn + h/2, yn + (k1*h)/2)
        k3 = f(xn + h/2, yn + (k2*h)/2)
        k4 = f(xn + h, yn + h*k3)
        yn1 = yn + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        y.append(yn1)
    return y

def Q1():
    print("-------------------Q1-------------------")
    print("")
    start = 0
    end = 0.2
    h = 0.005
    y0 = 0
    y = RangeKuttafun4(f1, y0, start, end, h)[-1]
    print("Units of KOH at t = 0.2s is %.4f" % y)
    print("-------------------------------------------------------")
    print("")

def EulerModification(f, y0, start, end, h):
    n = int((end - start)/h)
    y = [y0]
    for i in range(n):
        yn = y[-1]
        xn = start + i*h
        xn1 = xn + h
        yn1 = yn + (h/2)*(f(xn, yn) + f(xn1, yn + h*f(xn, yn)))
        y.append(yn1)
    return y

def RangeKuttafun2(f, y0, start, end, h):
    n = int((end - start)/h)

    y = [y0]
    alpha = 0.5
    beta = alpha
    a = 1 - 1/(2*alpha)
    b = 1/(2*alpha)

    for i in range(n):
        yn = y[-1]
        xn = start + i*h
        k1 = f(xn, yn)
        k2 = f(xn + alpha*h, yn + beta*h*k1)
        yn1 = yn + h*(a*k1 + b*k2)
        y.append(yn1)
    return y

def f2(t, y):
    return -y + t + 1

def Q2():
    print("-------------------Q2-------------------")
    print("")

    start = 0
    end = 1
    y0 = 1

    H = [0.1, 0.2, 0.25]

    for h in H:
        y_rk = RangeKuttafun2(f2,  y0, start, end, h)
        y_me = EulerModification(f2,  y0, start, end, h)
        print("h = %.2f" % h)
        for i in range(len(y_rk)):
            print("Runge-Kutta Method: y(%.2f) = %.6f " %(start + i*h, y_rk[i]))
            print("Modified Euler Method: y(%.2f) = %.6f " %(start + i*h, y_me[i]))
            print("")
    print("-------------------------------------------------------")
    print("")

def ErrorFun(y_comp, y_actual, start, end, h):
    n = len(y_comp) - 1

    for i in range(n+1):
        x = start + i*h
        actual = y_actual(x)
        comp = y_comp[i]
        abs_err = abs(actual - comp)
        rel_err = 100*abs(abs_err/actual)

        print("Actual: y(%.3f) = %.6f"%(x, actual))
        print("Calculated; y(%.3f) = %.6f"%(x, comp))
        print("Absolute Error = %.6f"%(abs_err))
        print("Relative Error = %.6f %%"%(rel_err))
        print("")

def f31(t, y):
        return (1+t)/(1+y)

def f33(t, y):
    return (math.sin(2*t) - 2*t*y)/(t**2)

def f32(t):
    return math.sqrt(t**2 + 2*t + 6) - 1

def f34(t):
    return (4 + math.cos(2) - math.cos(2*t))/(2*t*t)

def Q3():
    print("-------------------Q3-------------------")
    print("")

    print("Part A ------------>")
    y0 = 2
    start = 1
    end = 2 
    h = 0.5
    y_comp = EulerModification(f31, y0, start, end, h)
    ErrorFun(y_comp, f32, start, end, h)

    print("Part B ------------>")
    y0 = 2
    start = 1
    end = 2 
    h = 0.25
    y_comp = EulerModification(f33, y0, start, end, h)
    ErrorFun(y_comp, f34, start, end, h)

    print("-------------------------------------------------------")
    print("")

def Euler(f, y0, start, end, h):
    n = int((end - start)/h)

    y = [y0]

    for i in range(n):
        yn = y[-1]
        xn = start + i*h
        yn1 = yn + f(xn,yn)*h
        y.append(yn1)

    return y

def findX(y, start, end, h, val):
    n = int((end - start)/h)
    eps = 1e-5

    for i in range(n+1):
        x = start + i*h
        if abs(x - val) < eps:
            return y[i]

    return -1

def f4(t, y):
    return y - t*t + 1

def Q4():
    print("-------------------Q4-------------------")
    print("")

    start = 0 
    end = 2
    y0 = 0.5
    y_euler = Euler(f4, y0, start, end, 0.025)
    y_rk2 = RangeKuttafun2(f4, y0, start, end, 0.05)
    y_rk4 = RangeKuttafun4(f4, y0, start, end, 0.1)
    vals = [0.1, 0.2, 0.3, 0.4, 0.5]
    for val in vals:
        euler = findX(y_euler, start, end, 0.025, val)  
        rk2 = findX(y_rk2, start, end, 0.05, val)
        rk4 = findX(y_rk4, start, end, 0.1, val)
        print("Euler Method: y(%.1f) = %.6f"%(val, euler))
        print("Runge-Kutta Order 2: y(%.1f) = %.6f "%(val, rk2))
        print("Runge-Kutta Order 4: y(%.1f) = %.6f "%(val, rk4))
        print("")
    print("-------------------------------------------------------")
    print("")

def adamBashforth(f, x, y_initial, h):
    n = len(x) - 1
    m = len(y_initial) - 1
    y = [y1 for y1 in y_initial]
    for i in range(m, n):
        yn = y[i]
        fn = f(x[i], y[i])
        fn1 = f(x[i-1], y[i-1])
        fn2 = f(x[i-2], y[i-2])
        fn3 = f(x[i-3], y[i-3])
        yn1 = yn + (h/24)*(55*fn -59*fn1 + 37*fn2 -9*fn3)
        y.append(yn1)
    return y

def adamMolton(f, x, y_initial, h):
    n = len(x) - 1
    m = len(y_initial) - 1
    y = [y1 for y1 in y_initial]
    for i in range(m, n):
        yn = y[i]
        fn = f(x[i], y[i])
        fn1 = f(x[i-1], y[i-1])
        fn2 = f(x[i-2], y[i-2])
        fn3 = f(x[i-3], y[i-3])
        y_next = yn + (h/24)*(55*fn -59*fn1 + 37*fn2 -9*fn3)
        f_next = f(x[i+1], y_next)
        yn1 = yn + (h/24)*(9*f_next + 19*fn - 5*fn1 + fn2)

        y.append(yn1)
    return y

def f51(t, y):
        return y - t**2 + 1

def f52(t):
    return (t+1)**2 - 0.5*math.exp(t)

def f5init(f, y, h, start, end):
    n = int((end - start)/h)
    x = []
    for i in range(n+1):
        x.append(start + i*h)

    y_in = []
    for i in range(4):
        yn = y(x[i]) 
        y_in.append(yn)
    return x, y_in

def Q5():
    print("-------------------Q5-------------------")
    print("")

    start = 0
    end = 2
    y0 = 0.5
    h = 0.2
    x,y_initial = f5init(f51, f52, h, start, end)
    y_bash = adamBashforth(f51, x, y_initial, h)
    y_molton = adamMolton(f51, x, y_initial, h)
    for x1, y1_b, y1_m in zip(x, y_bash, y_molton):
        print("Actual: y(%.1f) = %.6f "%(x1, f52(x1)))
        print("Bashforth: y(%.1f) = %.6f "%(x1, y1_b))
        print("Molton: y(%.1f) = %.6f "%(x1, y1_m))
        print("")
    print("-------------------------------------------------------")
    print("")

def f6init(f, y0, h, start, end):
    n = int((end - start)/h)
    y = RangeKuttafun4(f, y0, start, start + 3*h, h)
    x = []
    for i in range(n+1):
        x.append(start + i*h)
    return x, y

def f61(t, y):
        return (2 - 2*t*y)/(t**2 + 1)

def f63(t, y):
    return (y**2)/(t + 1)

def f65(t, y):
    return (y**2 + y)/t

def f62(t):
    return (2*t + 1)/(t**2 + 1)

def f64(t):
    return -1/math.log(t+1)

def f66(t):
    return (2*t)/(1-2*t)

def Q6():
    print("-------------------Q6-------------------")
    print("")

    print("Part A ------------>")
    start = 0
    end = 1
    y0 = 1
    h = 0.1
    x,y_inital = f6init(f61, y0, h, start, end)
    y_comp = adamBashforth(f61, x, y_inital, h)
    ErrorFun(y_comp, f62, start, end, h)

    print("Part B ------------>")
    start = 1
    end = 2
    y0 = -1/math.log(2)
    h = 0.1
    x,y_inital = f6init(f63, y0, h, start, end)
    y_comp = adamBashforth(f63, x, y_inital, h)
    ErrorFun(y_comp, f64, start, end, h)

    print("Part C ------------>")
    start = 1
    end = 3
    y0 = -2
    h = 0.2
    x,y_inital = f6init(f63, y0, h, start, end)
    y_comp = adamBashforth(f63, x, y_inital, h)
    ErrorFun(y_comp, f66, start, end, h)

    print("-------------------------------------------------------")
    print("")

def f7init(f, y0, h, start, end):
    n = int((end - start)/h)
    y = RangeKuttafun4(f, y0, start, start + 3*h, h)
    x = []
    for i in range(n+1):
        x.append(start + i*h)
    return x, y

def f7(t, y):
    return y - t*t + 1

def Q7():
    print("-------------------Q7-------------------")
    print("")

    start = 0
    end = 2
    y0 = 0.5
    h = 0.2
    x,y_inital =f7init(f7, y0, h, start, end)
    y_comp = adamMolton(f7, x, y_inital, h)

    print("Adam Predictor Corrector Method")
    for x1, y1 in zip(x, y_comp):
        print("y(%.1f) = %.6f"%(x1, y1))    

    print("-------------------------------------------------------")
    print("")

Q1()
Q2()
Q3()
Q4()
Q5()
Q6()
Q7()

