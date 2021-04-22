import math
import numpy as np
import matplotlib.pyplot as plt

def Q1a(t,x):
    return math.exp(t-x)

def Q1b(t,x):
    return (1+t)/(1+x)

def Q1c(t,x):
    return -x + t*math.sqrt(x)

def Q1d(t,x):
    return (math.sin(2*t) - 2*t*x)/(t*t)

def Q2a(t):
    return math.log(math.exp(t) + math.e - 1)

def Q2b(t):
    return math.sqrt(t**2 + 2*t + 6) - 1

def Q2c(t):
    return (t - 2 + (math.sqrt(2))*(math.e)*(math.exp(-t/2)))**2

def Q2d(t):
    return (4 + math.cos(2) - math.cos(2*t))/(2*t*t)

def eulerMethod(fx, A0, start, end, h):
    divisons = int((end - start)/h)
    A = []
    A.append(A0);
    for i in range(divisons):
        An = A[-1]
        xn = start + i*h
        An1 = An + fx(xn,An)*h
        A.append(An1)
    return A

def Q1and2():
    print("-------------------Q1 && Q2-------------------")
    print("")

    print("Part A ------------>")
    ti = 0
    tf = 1
    A0 = 1
    h = 0.5
    A = eulerMethod(Q1a,A0,ti,tf,h)
    x = ti
    n = len(A)-1
    for i in range(n+1):
        print("y(%0.2f) = %.9f"%(x, A[i]))
        A_actual = Q2a(x);
        print("y(%0.2f) (Actual) = %.9f"%(x, A_actual))
        abs_err = abs(A_actual - A[i])
        rel_err = 100*abs(abs_err/A_actual)
        print("Absolute Error = %.6f"%(abs_err))
        print("Relative Error = %.6f%%"%(rel_err))
        print("")
        x+=h

    print("Part B ------------>")
    ti = 1
    tf = 2
    A0 = 2
    h = 0.5
    x = ti
    A = eulerMethod(Q1b,A0,ti,tf,h)
    n = len(A)-1
    for i in range(n+1):
        print("y(%0.2f) = %.9f"%(x, A[i]))
        A_actual = Q2b(x);
        print("y(%0.2f) (Actual) = %.9f"%(x, A_actual))
        abs_err = abs(A_actual - A[i])
        rel_err = 100*abs(abs_err/A_actual)
        print("Absolute Error = %.6f"%(abs_err))
        print("Relative Error = %.6f%%"%(rel_err))
        print("")
        x+=h

    print("Part C ------------>")
    ti = 2
    tf = 3
    A0 = 2
    h = 0.25
    x = ti
    A = eulerMethod(Q1c,A0,ti,tf,h)
    n = len(A)-1
    for i in range(n+1):
        print("y(%0.2f) = %.9f"%(x, A[i]))
        A_actual = Q2c(x);
        print("y(%0.2f) (Actual) = %.9f"%(x, A_actual))
        abs_err = abs(A_actual - A[i])
        rel_err = 100*abs(abs_err/A_actual)
        print("Absolute Error = %.6f"%(abs_err))
        print("Relative Error = %.6f%%"%(rel_err))
        print("")
        x+=h

    print("Part D ------------>")
    ti = 1
    tf = 2
    A0 = 2
    h = 0.25
    x = ti
    A = eulerMethod(Q1d,A0,ti,tf,h)
    n = len(A)-1
    for i in range(n+1):
        print("y(%0.2f) = %.9f"%(x, A[i]))
        A_actual = Q2d(x);
        print("y(%0.2f) (Actual) = %.9f"%(x, A_actual))
        abs_err = abs(A_actual - A[i])
        rel_err = 100*abs(abs_err/A_actual)
        print("Absolute Error = %.6f"%(abs_err))
        print("Relative Error = %.6f%%"%(rel_err))
        print("")
        x+=h

    print("-------------------------------------------------------")
    print("")

def Q3a(t,x):
    return 1/t**2 - x/t - x**2

def Q3b(t):
    return -1/t

def linearInterpolate(Comp, Actual, start, end, h, x):
    n = len(Comp) - 1
    for i in range(n+1):
        x1 = start + i*h
        if x1 <= x and x < x1+h:
            x2 = x1+h
            y1 = Comp[i]
            y2 = Comp[i+1]
            y0 = y1 + (x-x1)*((y2-y1)/(x2-x1))
            break

    Act_value = Actual(x)
    abs_err = abs(Act_value - y0)
    rel_err = 100*abs(abs_err/Act_value)
    print("For X = %0.3f"%(x))
    print("Actual Value = %.9f"%( Act_value))
    print("Estimated Value = %.9f"%( y0))
    print("Absolute Error = %.6f"%(abs_err))
    print("Relative Error = %.6f%%"%(rel_err))
    print("")

def Q3():
    print("-------------------Q3-------------------")
    print("")

    print("Part A ------------>")
    ti = 1
    tf = 2
    A0 = -1
    h = 0.05
    x = ti
    A = eulerMethod(Q3a,A0,ti,tf,h)
    n = len(A)-1
    for i in range(n+1):
        print("y(%0.3f) = %.9f"%(x, A[i]))
        A_actual = Q3b(x);
        print("y(%0.3f) (Actual) = %.9f"%(x, A_actual))
        abs_err = abs(A_actual - A[i])
        rel_err = 100*abs(abs_err/A_actual)
        print("Absolute Error = %.6f"%(abs_err))
        print("Relative Error = %.6f%%"%(rel_err))
        print("")
        x+=h

    print("Part B ------------>")
    X = [1.052, 1.555,1.978]
    for x in X:
        linearInterpolate(A, Q3b, ti, tf, h, x)

    print("-------------------------------------------------------")
    print("")

def Q5f(x, y, lamb = -20):
    return lamb*y + math.cos(x) - lamb*math.sin(x)

def Q5y1(x):
    return math.sin(x)

def Q5y2(x):
        return -math.cos(x)

def Q5y3(x):
    return math.sin(x)

def errBound(n,h):
    y = 0.5
    # because max value of sinx = 1
    return n*h*h*y
    
def Q5():
    print("-------------------Q5-------------------")
    print("")

    ti = 0
    tf = 3
    A0 = 0
    h = 0.5
    A = eulerMethod(Q5f,A0,ti,tf,h)[6]
    A_actual = Q5y1(3)
    abs_err = abs(A_actual - A)
    ErrBound = errBound(6,h)
    print("Actual Value = %0.9f"%(A_actual))
    print("Computed value = %0.9f"%(A))
    print("Absolute Error = %.9f"%(abs_err))
    print("Error Bound = %0.9f"%(ErrBound))
    print("-------------------------------------------------------")
    print("")

Q1and2()
Q3()
Q5()