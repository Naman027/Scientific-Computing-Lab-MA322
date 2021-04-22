import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Q1_P(x):
    return 0

def Q1_Q(x):
    return 1

def Q1_R(x):
    return 1+x

def Q1_y(x):
    return 1 + x - np.cos(x) - (1+np.pi/2)*np.sin(x)

def MatGenerat_Q1(h, x0, xn):
    L = []
    xi = x0+h
    n = int((xn-x0)/h)-1
    for i in range(1, n+1):
        L1 = [0]*n
        if i-2 >= 0:
            L1[i-2] = 1 - h*Q1_P(xi)/2
        L1[i-1] = -2 + h*h*Q1_Q(xi)
        if i < n:
            L1[i] = 1+h*Q1_P(xi)/2
        L.append(L1)
        xi += h
    return np.array(L)

def VectGenerat_Q1(h, x0, xn, alpha, beta):
    F = []
    xi = x0+h
    n = int((xn-x0)/h)-1
    for i in range(1, n+1):
        f = h*h*Q1_R(xi)
        if i == 1:
            f -= alpha*(1 - h*Q1_P(xi)/2)
        if i == n:
            f -= beta*(1 + h*Q1_P(xi)/2)
        F.append(f)
        xi += h
    return np.array(F)

def Q1():
    print("-------------------Q1-------------------")
    print("")
    h_list = [1/4, 1/8, 1/16, 1/32, 1/64]
    x0 = 0
    xn = np.pi/2
    alpha = 0
    beta = 0
    sol = []
    act = [Q1_y(1/2)]*5
    df = pd.DataFrame()

    for h in h_list:
        L = MatGenerat_Q1(h, x0, xn)
        F = VectGenerat_Q1(h, x0, xn, alpha, beta)
        U = np.linalg.inv(L).dot(F)
        sol.append(U[int(1/(2*h))-1])

    df['y(1/2)'] = pd.Series(act)
    df['fd sol (1/2)'] = pd.Series(sol)
    df['Error'] = pd.Series(np.array(act)-np.array(sol))
    r = df['Error']/df['fd sol (1/2)']
    df['Err Ratio'] = r
    df.set_index(pd.Series(['1/4', '1/8', '1/16', '1/32', '1/64']), inplace = True)
    print(df)
    X = np.linspace(x0, xn, 500)
    Y = [Q1_y(x) for x in X]
    X1 = [x0+i*h for i in range(len(U)+2)]
    Y1 = [0]
    for u in U:
        Y1.append(u)
    Y1.append(0)
    plt.title('Approximation vs Actual')
    plt.plot(X, Y, label='Actual')
    plt.plot(X1, Y1, label='Approximation with h = 1/64')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.show()
    print("-------------------------------------------------------")
    print("")

def Q2_f(x):
    return np.sin(x)

def MatGenerat_Q2(h, x0, xn):
    L = []
    xi = x0+h
    n = int((xn-x0)/h)
    for i in range(1, n+1):
        L1 = [0]*n
        if i-2 >= 0:
            L1[i-2] = -1
        L1[i-1] = 2
        if i < n:
            L1[i] = -1
        L.append(L1)
        xi += h
    return np.array(L)

def VectGenerat_Q2(h, x0, xn):
    F = []
    xi = x0+h
    n = int((xn-x0)/h)
    for i in range(1, n+1):
        fi = h*h*(Q2_f(xi) + (Q2_f(xi-h) - 2*Q2_f(xi) + Q2_f(xi+h))/12)
        F.append(fi)
        xi += h
    return np.array(F)

def Q2():
    print("-------------------Q2-------------------")
    print("")
    x0 = 0
    xn = 2*np.pi
    alpha = 0
    beta = 0
    N_list = [10, 20, 40, 80, 160, 320]
    err = []
    l2 = []
    print("The Plots for Q2:")
    for N in N_list:
        h = (xn-x0)/(N-2)
        L = MatGenerat_Q2(h, x0, xn)
        F = VectGenerat_Q2(h, x0, xn)
        U = np.linalg.inv(L).dot(F)
        Y = [alpha]
        for u in U:
            Y.append(u)
        Y.append(beta)
        X = np.linspace(x0, xn, N)
        Y1 = [Q2_f(x) for x in X]
        plt.show()
        error = np.array([abs(Y1[i]-Y[i]) for i in range(len(Y))])
        err.append(max(error))
        l2.append(np.sum(error*error))

    plt.title('Max Err vs Grid Points')
    plt.plot(N_list, err)
    plt.xlabel('No of Grid Points')
    plt.ylabel('Max Error')
    plt.show()

    plt.title('Max Err vs Grid Points')
    plt.loglog()
    plt.plot(N_list, err)
    plt.xlabel('Log No of Grid Points')
    plt.ylabel('Log Max Error')
    plt.show()

    plt.title('L2 Err vs Grid Points')
    plt.plot(N_list, l2)
    plt.xlabel('No of Grid Points')
    plt.ylabel('L2 Error')
    plt.show()

    plt.title('L2 Err vs Grid Points')
    plt.loglog()
    plt.plot(N_list, l2)
    plt.xlabel('Log No of Grid Points')
    plt.ylabel('Log L2 Error')
    plt.show()
    print("-------------------------------------------------------")
    print("")

def Q3_P(x):
    return -1

def Q3_Q(x):
    return 0

def Q3_R(x):
    return 1

def Q3_y(x):
    return 2*np.exp(x) - x - 1

def MatGenerat_Q3(h, x0, xn):
    L = []
    xi = x0+h
    n = int((xn-x0)/h) - 1
    for i in range(1, n+1):
        L1 = [0]*n
        if i-2 >= 0:
            L1[i-2] = 1 - h*Q3_P(xi)/2
        L1[i-1] = -2 + h*h*Q3_Q(xi)
        if i < n:
            L1[i] = 1+h*Q3_P(xi)/2
        L.append(L1)
        xi += h
    return np.array(L)

def VectGenerat_Q3(h, x0, xn, alpha, beta):
    F = []
    xi = x0+h
    n = int((xn-x0)/h) - 1
    for i in range(1, n+1):
        f = h*h*Q3_R(xi)
        if i == 1:
            f -= alpha*(1 - h*Q3_P(xi)/2)
        if i == n:
            f -= beta*(1 + h*Q3_P(xi)/2)
        F.append(f)
        xi += h
    return np.array(F)

def Q3():
    print("-------------------Q3-------------------")
    print("")
    x0 = 0
    xn = 1
    h = 1/3
    alpha = 1
    beta = 2*(np.e-1)
    L = MatGenerat_Q3(h, x0, xn)
    F = VectGenerat_Q3(h, x0, xn, alpha, beta)
    U = np.linalg.inv(L).dot(F)
    Y = [alpha]
    for u in U:
        Y.append(u)
    Y.append(beta)
    Y1 = [Q3_y(x0+i*h) for i in range(len(Y))]
    df = pd.DataFrame()
    df['Actual'] = pd.Series(Y1)
    df['Approx'] = pd.Series(Y)
    df['Err'] = pd.Series(np.array(Y1)-np.array(Y))
    df.set_index(pd.Series(['0', '1/3', '2/3', '1']), inplace=True)
    print(df)
    print("-------------------------------------------------------")
    print("")

def Q4_f(x):
    return (math.exp(10*x)-1)/(math.exp(10)-1)

def P(x):
    return -10

def Q(x):
    return 0

def R(x):
    return 0

def alpha():
    return 0

def beta():
    return 1

def A_c(xi, h):
    return 1 - h*P(xi)/2

def B_c(xi, h):
    return -2 + h*h*Q(xi)

def C_c(xi, h):
    return 1 + h*P(xi)/2

def A_f(xi, h):
    return 1 

def B_f(xi, h):
    return -2 - h*P(xi) + h*h*Q(xi)

def C_f(xi, h):
    return 1 + h*P(xi)

def A_b(xi, h):
    return 1 - h*P(xi)

def B_b(xi, h):
    return -2 + h*P(xi) + h*h*Q(xi)

def C_b(xi, h):
    return 1 


def fun_Q4_compL(x, h, A, B, C):
    n = len(x)-1
    L = []
    for i in range(1, n):
        temp = [0]*(n-1)
        if i == 1:
            temp[i] = C(x[i], h)
            temp[i-1] = B(x[i], h)
        elif i < n-1:
            temp[i] = C(x[i], h)
            temp[i-1] = B(x[i], h)
            temp[i-2] = A(x[i], h)
        else:
            temp[i-1] = B(x[i], h)
            temp[i-2] = A(x[i], h)
        L.append(temp)
    return L

def fun_Q4_compF(x, h, A, C):
    n = len(x)-1
    F = []
    for i in range(1, n):
        if i == 1:
            term = h*h*R(x[i]) - alpha()*A(x[i],h)
        elif i < n-1:
            term = h*h*R(x[i])
        else:
            term = h*h*R(x[i]) - beta()*C(x[i], h)
        F.append(term)
    return  F

def arrayDiv(x0, xn, h):
    return np.arange(x0, xn+h/2, h)

def Q4():
    print("-------------------Q4-------------------")
    print("")
    ferr, berr, cerr = [], [], []
    x0, xn = 0, 1
    h = 0.25
    x = arrayDiv(x0, xn, h)
    U = [Q4_f(xi) for xi in x]
    U = np.array(U)
    #-------------central scheme----------------
    L = fun_Q4_compL(x, h, A_c, B_c, C_c)
    F = fun_Q4_compF(x, h, A_c, C_c)
    V = np.linalg.inv(L).dot(F)
    V = np.append(alpha(), V)
    V = np.append(V, beta())
    cerr = abs(U-V)
    #-------------forward scheme----------------
    L = fun_Q4_compL(x, h, A_f, B_f, C_f)
    F = fun_Q4_compF(x, h, A_f, C_f)
    V = np.linalg.inv(L).dot(F)
    V = np.append(alpha(), V)
    V = np.append(V, beta())
    ferr = abs(U-V)
    #-------------backward scheme----------------
    L = fun_Q4_compL(x, h, A_b, B_b, C_b)
    F = fun_Q4_compF(x, h, A_b, C_b)
    V = np.linalg.inv(L).dot(F)
    V = np.append(alpha(), V)
    V = np.append(V, beta())
    berr = abs(U-V)
    df = pd.DataFrame({'Central': cerr, 'Backward': berr, 'Forward': ferr}, index = np.arange(0, 1.1, 0.25))
    print('Errors for following Schemes:')
    print(df)
    print()
    plt.figure()
    plt.plot(x, cerr, label = "Central")
    plt.plot(x, berr, label = "Backward")
    plt.plot(x, ferr, label = "Forward")
    plt.xlabel('Nodal Points')
    plt.ylabel('Error')
    plt.title(r'Errors for Schemes for $\frac{dy}{dx}$')
    plt.legend()
    plt.savefig('4.png')
    plt.show()
    print("-------------------------------------------------------")
    print("")

Q1()
Q2()
Q3()
Q4() 