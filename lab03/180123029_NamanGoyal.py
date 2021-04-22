import numpy as np
import math

def DiffArray(A):
    ans = []
    for i in range(1, len(A)):
        ans.append(A[i]-A[i-1])
    return ans

def NewtonForwardDiffMethod(X,fX,x):
    A = fX
    factorial = 1
    ans = 0
    for i in range(len(X)):
        if i == 0:
            ans += A[0]
        else:
            factorial *= i
            cur = 1
            for j in range(i):
                cur *= (x-X[j])
            cur /= pow(X[1]-X[0],i)
            cur /= factorial
            cur *= A[0]
            ans += cur
        A = DiffArray(A)
    return ans

def Q1():
    print("-------------------Q1-------------------")
    print("")
    # Use Newton forward-difference
    print("Part I --->")
    x = 0.43
    X = [0.25,0.5]
    fX = [1.64872,2.71828]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.43) using degree 1 Interpolating polynomials is %0.10f"%(ans))
    X = [0.25,0.5,0.75]
    fX = [1.64872,2.71828,4.48169]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.43) using degree 2 Interpolating polynomials is %0.10f"%(ans))
    X = [0,0.25,0.5,0.75]
    fX = [1,1.64872,2.71828,4.48169]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.43) using degree 3 Interpolating polynomials is %0.10f"%(ans))

    print("")
    print("Part II --->")
    x = 0.18
    X = [0.1, 0.2]
    fX = [-0.29004986, -0.56079734]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.18) using degree 1 Interpolating polynomials is %0.10f"%(ans))
    X = [0.1, 0.2, 0.3]
    fX = [-0.29004986, -0.56079734, -0.81401972]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.18) using degree 2 Interpolating polynomials is %0.10f"%(ans))
    X = [0.1, 0.2, 0.3, 0.4]
    fX = [-0.29004986, -0.56079734, -0.81401972, -1.0526302]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.18) using degree 3 Interpolating polynomials is %0.10f"%(ans))
    print("-------------------------------------------------------")
    print("")

def NewtonBackwardDiffMethod(X,fX,x):
    A = fX
    factorial = 1
    ans = 0
    n = len(X)
    for i in range(len(X)):
        if i == 0:
            ans += A[n-1]
        else:
            factorial *= i
            cur = 1
            for j in range(i):
                cur *= (x-X[n-1-j])
            cur /= pow(X[1]-X[0],i)
            cur /= factorial
            cur *= A[len(A)-1]
            ans += cur
        A = DiffArray(A)
    return ans

def Q2():
    print("-------------------Q2-------------------")
    print("")
    # Use Newton backward-difference
    print("Part I --->")
    x = -0.33333
    X = [-0.5, -0.25]
    fX = [-0.02475, 0.3349375]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(-1/3) using degree 1 Interpolating polynomials is %0.10f"%(ans))
    X = [-0.75, -0.5, -0.25]
    fX = [-0.0718125, -0.02475, 0.3349375]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(-1/3) using degree 2 Interpolating polynomials is %0.10f"%(ans))
    X = [-0.75, -0.5, -0.25, 0]
    fX = [-0.0718125, -0.02475, 0.3349375, 1.101]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(-1/3) using degree 3 Interpolating polynomials is %0.10f"%(ans))

    print("")
    print("Part II --->")
    x = 0.25
    X = [0.2, 0.3]
    fX = [-0.28398668, 0.00660095]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.25) using degree 1 Interpolating polynomials is %0.10f"%(ans))
    X = [0.1, 0.2, 0.3]
    fX = [-0.62049958, -0.28398668, 0.00660095]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.25) using degree 2 Interpolating polynomials is %0.10f"%(ans))
    X = [0.1, 0.2, 0.3, 0.4]
    fX = [-0.62049958, -0.28398668, 0.00660095, 0.2484244]
    ans = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of f(0.25) using degree 3 Interpolating polynomials is %0.10f"%(ans))
    print("-------------------------------------------------------")
    print("")

def Q3():
    print("-------------------Q3-------------------")
    print("")
    D2 = [0]
    D3 = [6]
    D4 = [24]*11

    for j in range(1,11):
        D3.append(D4[j-1]+D3[j-1])
        D2.append(D3[j-1]+D2[j-1])
    print("The Value of Del2P(10) is %0.10f"%(D2[10]))
    print("-------------------------------------------------------")
    print("")

def Q4():
    print("-------------------Q4-------------------")
    print("")
    x = 0.25
    X = [0.1, 0.2, 0.3, 0.4, 0.5]
    fX = [9.9833, 4.9667, 3.2836, 2.4339, 1.9177]
    XgX = []
    for i in range(5):
        XgX.append(X[i]*fX[i])
    actual = round((np.sin(x)/(x*x)), 10)
    print("The Actual Value of g(0.25) is %0.10f"%(actual))
    forwardInterofg = NewtonForwardDiffMethod(X,fX,x)
    print("Approx Value of g(0.25) using Forward Interpolating of g(x) is %0.10f"%(forwardInterofg))
    forwardInterofg_mul_x = 4*NewtonForwardDiffMethod(X,XgX,x)
    print("Approx Value of g(0.25) using Forward Interpolating of x*g(x) is %0.10f"%(forwardInterofg_mul_x))
    print("-------------------------------------------------------")
    print("")

def P(x):
    return (3 - 2*(x+1) + 0 + (x+1)*x*(x-1))

def Q(x):
    return (-1 + 4*(x+2) - 3*(x+2)*(x+1) + (x+2)*(x+1)*x)

def Q5():
    print("-------------------Q5-------------------")
    print("")
    X = [-2, -1, 0, 1, 2]
    fX = [-1, 3, 1, -1, 3]
    for i in range(5):
        valP = P(X[i])
        valQ = Q(X[i])

        if(valP!=fX[i]):
            print("The Polynomial P don't intrerpolate the given data correctly")
            break
        if(valQ!=fX[i]):
            print("The Polynomial Q don't intrerpolate the given data correctly")
            break
        if i == 4:
            print("Both Polynomials P && Q successfully interpolated all the data correctly")

    print("-------------------------------------------------------")
    print("")

def f6(X,fX):
    ans = []
    n = len(X)
    for i in range(n):
        ans.append(fX[i]-pow(X[i],4)/24)
    return ans

def Q6():
    print("-------------------Q6-------------------")
    print("")
    X = [0, 1, 2, 3]
    fX = [4, 9, 15, 18]
    CubicPolyCoeff = f6(X,fX)
    Coeffx3 = DiffArray(DiffArray(DiffArray(CubicPolyCoeff)))
    print("The coefficient of x3 in P(x) is "+str(int(Coeffx3[0]*2))+'/12')
    print("-------------------------------------------------------")
    print("")

def f7(x):
    return (1 + 4*x + 4*x*(x-0.25) + 16/3*x*(x-0.25)*(x-0.5))

def Q7():
    print("-------------------Q7-------------------")
    print("")
    x = 0.75
    ans = f7(x)
    print("The Value of f(0.75) is %0.10f"%(ans))
    print("-------------------------------------------------------")
    print("")

Q1()
Q2()
Q3()
Q4()
Q5()
Q6()
Q7()
