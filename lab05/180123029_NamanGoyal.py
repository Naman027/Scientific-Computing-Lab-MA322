import math
import random
import numpy as np
import matplotlib.pyplot as plt

def f11(x0):
    return x0*x0*np.log(x0)

def f12(x0):
    return 2/(x0*x0 - 4)

def f13(x0):
    return x0*x0*np.sin(x0)

def gaussQuadratureforn2(f,a,b):
    x = [-1/np.sqrt(3), 1/np.sqrt(3)]
    for i in range(len(x)):
        x[i] = (a+b)/2 + (x[i] * (b-a)/2)
    w = [1,1]
    ans = 0 
    for i in range(2):
        ans +=  w[i]*f(x[i])
    ans *= (b-a)/2
    return ans

def Q1():
    print("-------------------Q1-------------------")
    print("")

    print("Part I -------->")
    actualIntegral = 0.192259357
    a = 1
    b = 1.5
    calcIntegral = gaussQuadratureforn2(f11,a,b)
    absError = abs(calcIntegral-actualIntegral)
    percentageError = abs(absError/actualIntegral)*100
    print("Actual Integral    : %.9f"%(actualIntegral))
    print("Calculated Integral: %.9f"%(calcIntegral))
    print("Error              : %.9f"%(absError))
    print("Percent Error      : %.9f%%"%(percentageError))
    print("")

    print("Part II -------->")
    actualIntegral = -0.17682002
    a = 0
    b = 0.35
    calcIntegral = gaussQuadratureforn2(f12,a,b)
    absError = abs(calcIntegral-actualIntegral)
    percentageError = abs(absError/actualIntegral)*100
    print("Actual Integral    : %.9f"%(actualIntegral))
    print("Calculated Integral: %.9f"%(calcIntegral))
    print("Error              : %.9f"%(absError))
    print("Percent Error      : %.9f%%"%(percentageError))
    print("")

    print("Part III -------->")
    actualIntegral = 0.088755283
    a = 0
    b = np.pi/4
    calcIntegral = gaussQuadratureforn2(f13,a,b)
    absError = abs(calcIntegral-actualIntegral)
    percentageError = abs(absError/actualIntegral)*100
    print("Actual Integral    : %.9f"%(actualIntegral))
    print("Calculated Integral: %.9f"%(calcIntegral))
    print("Error              : %.9f"%(absError))
    print("Percent Error      : %.9f%%"%(percentageError))
    print("-------------------------------------------------------")
    print("")

def f3(x0): 
    return 1/(x0+2)

def Trapezoidal(f,a,b):
    T = ((b-a)/2)*(f(a) + f(b))
    return T

def Simpson(f,a,b):
    S = ((b-a)/6) * (f(a) + 4*f((a+b)/2) + f(b))
    return S

def Q3():
    print("-------------------Q3-------------------")
    print("")

    actualIntegral = 1.098612289
    a = -1
    b = 1
    gaussQuadrature = gaussQuadratureforn2(f3,a,b)
    T = Trapezoidal(f3,a,b)
    S = Simpson(f3,a,b)

    print("Actual Integral     : %0.9f"%(actualIntegral))
    print("Gaussian Integral   : %0.9f"%(gaussQuadrature))
    print("Trapezoidal Integral: %.9f"%(T))
    print("Simpson Integral    : %.9f"%(S))

    print("-------------------------------------------------------")
    print("")

def f4(x0):
    return 1/(1+x0)

def gaussQuadratureforn3(f,a,b):
    x = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
    for i in range(len(x)):
        x[i] = (a+b)/2 + (x[i] * (b-a)/2)
    w = [5/9, 8/9, 5/9]
    ans = 0 
    for i in range(3):
        ans +=  w[i]*f(x[i])
    ans *= (b-a)/2
    return ans

def CompSimpson(f,a,b,h):
    x = np.arange(a,b+h,h)
    n = len(x)-1
    ans = f(x[0])
    for i in range(1,n,2):
	    ans += 4*f(x[i])
    for i in range(2,n,2):
	    ans += 2*f(x[i])
    ans += f(x[n])
    ans *= h/3
    return ans

def Q4(): 
    print("-------------------Q4-------------------")
    print("")

    actualIntegral = 0.69314718
    a = 0
    b = 1
    gaussQuadrature = gaussQuadratureforn3(f4,a,b)
    h = 0.125
    compSimpson = CompSimpson(f4,a,b,h)

    print("Actual Integral     : %0.9f"%(actualIntegral))
    print("Gaussian Integral   : %0.9f"%(gaussQuadrature))
    print("CompSimpson Integral: %.9f"%(compSimpson))

    print("-------------------------------------------------------")
    print("")

def f6(x0):
    return (np.cos(x0)*np.log(np.sin(x0)))/(1 + (np.sin(x0)*(np.sin(x0))))

def gaussQuadratureforn1(f,a,b):
    x = [0]
    for i in range(len(x)):
        x[i] = (a+b)/2 + (x[i] * (b-a)/2)
    w = [2]
    ans = 0 
    for i in range(1):
        ans +=  w[i]*f(x[i])
    ans *= (b-a)/2
    return ans

def gaussQuadratureforn4(f,a,b):
    x = [-np.sqrt(3/7 + (2/7 * np.sqrt(6/5))), -np.sqrt(3/7 - (2/7 * np.sqrt(6/5))), np.sqrt(3/7 - (2/7 * np.sqrt(6/5))), np.sqrt(3/7 + (2/7 * np.sqrt(6/5)))]
    for i in range(len(x)):
        x[i] = (a+b)/2 + (x[i] * (b-a)/2)
    w = [(18 - np.sqrt(30))/36, (18 + np.sqrt(30))/36, (18 + np.sqrt(30))/36, (18 - np.sqrt(30))/36]
    ans = 0 
    for i in range(4):
        ans +=  w[i]*f(x[i])
    ans *= (b-a)/2
    return ans

def gaussQuadratureforn5(f,a,b):
    x = [-1/3 * np.sqrt(5 + 2*np.sqrt(10/7)), -1/3 * np.sqrt(5 - 2*np.sqrt(10/7)), 0, 1/3 * np.sqrt(5 - 2*np.sqrt(10/7)), 1/3 * np.sqrt(5 + 2*np.sqrt(10/7))]            
    for i in range(len(x)):
        x[i] = (a+b)/2 + (x[i] * (b-a)/2)
    w = [(322-13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, 128/225, (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900]  
    ans = 0 
    for i in range(5):
        ans +=  w[i]*f(x[i])
    ans *= (b-a)/2
    return ans

def Q6():
    print("-------------------Q6-------------------")
    print("")

    actualIntegral = -0.915966
    print("Actual Integral: %0.9f"%(actualIntegral))
    a = 0
    b = np.pi/2

    gaussQuadrature1 = gaussQuadratureforn1(f6,a,b)
    gaussQuadrature2 = gaussQuadratureforn2(f6,a,b)
    gaussQuadrature3 = gaussQuadratureforn3(f6,a,b)
    gaussQuadrature4 = gaussQuadratureforn4(f6,a,b)
    gaussQuadrature5 = gaussQuadratureforn5(f6,a,b)

    print("Gaussian Integral for N = 1 : %0.2f"%(gaussQuadrature1))
    print("Gaussian Integral for N = 2 : %0.2f"%(gaussQuadrature2))
    print("Gaussian Integral for N = 3 : %0.2f"%(gaussQuadrature3))
    print("Gaussian Integral for N = 4 : %0.2f"%(gaussQuadrature4))
    print("Gaussian Integral for N = 5 : %0.2f"%(gaussQuadrature5))
    print("-------------------------------------------------------")
    print("")

Q1()
Q3()
Q4()
Q6()

