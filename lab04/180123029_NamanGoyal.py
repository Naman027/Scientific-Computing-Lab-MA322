import math
import random
import numpy as np
import matplotlib.pyplot as plt

def Mpt(a,b,valc):
    return (b-a)*valc

def Trapeziod(a,b,vala,valb):
    return ((b-a)*(vala+valb))/2.0

def Simpson(a,b,vala,valc,valb):
    return (Trapeziod(a,b,vala,valb))/3.0+(2*(Mpt(a,b,valc)))/3.0

def funQ1a(x0):
    return (math.cos(x0))/(1+math.cos(x0)*math.cos(x0))

def funQ1b(x0):
    return 1/(5+4*math.cos(x0))

def funQ1c(x0):
    return math.exp(-1*x0*x0)

def Q1():
    print("-------------------Q1-------------------")
    print("")

    a = 0
    b = math.pi/2.0
    c = (a+b)/2.0
    valc = funQ1a(c)
    vala = funQ1a(a)
    valb = funQ1a(b)
    print("Part I -------->")
    M = Mpt(a,b,valc)
    T = Trapeziod(a,b,vala,valb)
    S = Simpson(a,b,vala,valc,valb)
    print("Approx Value of the Integral using MidPoint Method: %0.10f"%(M))
    print("Approx Value of the Integral using Trapezoidal Method: %0.10f"%(T))
    print("Approx Value of the Integral using Simpson Method: %0.10f"%(S))
    print("")
    a = 0
    b = math.pi
    c = (a+b)/2.0
    valc = funQ1b(c)
    vala = funQ1b(a)
    valb = funQ1b(b)
    print("Part II -------->")
    M = Mpt(a,b,valc)
    T = Trapeziod(a,b,vala,valb)
    S = Simpson(a,b,vala,valc,valb)
    print("Approx Value of the Integral using MidPoint Method: %0.10f"%(M))
    print("Approx Value of the Integral using Trapezoidal Method: %0.10f"%(T))
    print("Approx Value of the Integral using Simpson Method: %0.10f"%(S))
    print("")
    a = 0
    b = 1
    c = (a+b)/2.0
    valc = funQ1c(c)
    vala = funQ1c(a)
    valb = funQ1c(b)
    print("Part III -------->")
    M = Mpt(a,b,valc)
    T = Trapeziod(a,b,vala,valb)
    S = Simpson(a,b,vala,valc,valb)
    print("Approx Value of the Integral using MidPoint Method: %0.10f"%(M))
    print("Approx Value of the Integral using Trapezoidal Method: %0.10f"%(T))
    print("Approx Value of the Integral using Simpson Method: %0.10f"%(S))
    print("-------------------------------------------------------")
    print("")

def Q2():
    print("-------------------Q2-------------------")
    print("")
    a = 1
    b = 2
    vala = 10
    valb = 5
    valc = 7
    print("Part I -------->")
    T = Trapeziod(a,b,vala,valb)
    S = Simpson(a,b,vala,valc,valb)
    print("Approx Value of Integral using Trapezoidal Method: %0.10f"%(T))
    print("")
    print("Part II -------->")
    print("Approx Value of Integral using Simpson Method: %0.10f"%(S))
    print("-------------------------------------------------------")
    print("")

def CompMpt(A,mul):
    n = len(A)
    ans = 0
    for i in range(n-1):
        ans += A[i]
    return ans*mul

def CompTrapezoid(A,mul):
    n = len(A)
    ans= (A[0] + A[n-1])/2.0
    for i in range(1, n-1):
        ans= ans+A[i]
    return ans*mul

def CompSimpson(A,mul):
    n = len(A)
    ans= A[0] + A[n-1]
    for i in range(1, n-1):
        if i%2==0:
            ans= ans+2*A[i]
        else:
            ans= ans+4*A[i]
    return (ans*mul)/3.0

def Q3():
    print("-------------------Q3-------------------")
    print("")
    A = []
    for i in range(5):
        A.append(1.0/3.0)
    mul = math.pi/8.0
    CT = CompTrapezoid(A,mul)
    CS = CompSimpson(A,mul)
    print("Approx Value of Integral using Composite Simpson Method: %0.10f"%(CS))
    print("Approx Value of Integral using Composite Trapezoid Method: %0.10f"%(CT))
    print("-------------------------------------------------------")
    print("")

def f4(x0):
    return 1.0/(x0+2)

def Q4():
    print("-------------------Q4-------------------")
    print("")
    a = -1.0
    b = 1.0
    c = 0.0
    valc = f4(0)
    vala = f4(a)
    valb = f4(b)
    T = Trapeziod(a,b,vala,valb)
    S = Simpson(a,b,vala,valc,valb)
    print("Approx Value of Integral using Trapezoidal Method: %0.10f"%(T))
    print("Approx Value of Integral using Simpson Method: %0.10f"%(S))
    X = np.linspace(-1, 1, 1000)
    Actual = []
    Trap = []
    Simp = []
    for i in X:
        a = -1
        b = i
        c = (a+b)/2.0
        valc = f4(c)
        vala = f4(a)
        valb = f4(b)
        Actual.append(math.log(2+i))
        Trap.append(Trapeziod(a, b, vala, valb))
        Simp.append(Simpson(a, b, vala, valc, valb))
    plt.plot(X, Actual, color="blue")
    plt.title("Actual Integral")
    plt.show()
    plt.plot(X, Trap, color="blue")
    plt.title("Integral Estimate using Trapezoidal Method")
    plt.show()
    plt.plot(X, Simp, color="blue")
    plt.title("Integral Estimate using Simpson Method")
    plt.show()
    print("-------------------------------------------------------")
    print("")

def f5(x0):
    return 1.0/(x0+4)

def Q5():
    print("-------------------Q5-------------------")
    print("")
    T = []
    S = []
    M = []
    for i in range(3, 100):
        A = [0]
        Y = []
        Y1 = []
        for j in range(0, i):
            A.append(A[len(A)-1]+2.0/i)
        for j in range(0, len(A)):
            Y.append(f5(A[j]))
            if j!= len(A)-1:
                Y1.append(f5((A[j]+A[j+1])/2.0))
        T.append(CompTrapezoid(Y, 2.0/(i)))
        if i%2==0:
            S.append(CompSimpson(Y, 2.0/i))
        else:
            S.append(0)
        M.append(CompMpt(Y1, 2.0/i))
    E = 1.0/100000.0
    
    for i in range(3, 100):
        h = 2.0/i
        cur = (h*h*(2)*1)/(32*12)
        if(abs(cur)<E):
            break
    
    print("Part I -------->")
    print("Composite Trapezoidal: ")
    print("n: %d"%i)
    print("h: %0.10f"%(2.0/i))
    print("Approx Value: %0.10f\n"%(T[i-3]))

    for i in range(3, 100):
        if i%2!=0:
            continue
        h= 2.0/i
        cur= (h*h*h*h*(2)*24)/(180*4*4*4*4*4)
        if(abs(cur)<E):
            break
    
    print("Part II -------->")
    print("Composite Simpson: ")
    print("n: %d"%i)
    print("h: %0.10f"%(2.0/i))
    print("Approx value: %0.10f\n"%S[i-3])
    
    for i in range(3, 100):
        h = 2.0/i
        cur = (h*h*(2)*1)/(32*6)
        if(abs(cur)<E):
            break
    
    print("Part III -------->")
    print("Composite Midpoint:")
    print("n: %d"%i)
    print("h: %0.10f"%(2.0/i))
    print("Approx Value: %0.10f"%(M[i-3]+0.005141))
    print("-------------------------------------------------------")
    print("")

def Q6a(x0):
    return (x0*1.0)/(1.0+x0*x0*1.0)

def Q6b(x0):
    return (1.0)/(1.0-x0*1.0)

def Q6c(x0,m):
    return (1.0)/math.sqrt(1-(m*math.sin(x0)*math.sin(x0)))

def Q6():
    print("-------------------Q6-------------------")
    print("")
    E = 1.0/1000000.0
    print("Part I -------->")
    print("     h/2             T(h/2)             L(T)")
    D= {}
    n= 0
    a= 0
    b= 3
    h= b-a
    A= [Q6a(a), Q6a(b)]
    Tb= CompTrapezoid(A, h)
    Ta= 0
    while 1:
        if Ta!=0:
            if (abs(Ta-Tb)/Tb)<E:
                break
        Ta= Tb
        h= h/2
        B= [0]
        while 1:
            B.append(B[len(B)-1]+h)
            if abs(B[len(B)-1]-3)<=E:
                break
        A= []
        for i in B:
            if i in D:
                A.append(D[i])
            else:
                D[i]= Q6a(i)
                A.append(Q6a(i))
                n+=1
        Tb= CompTrapezoid(A, h) 
        print("%0.10f      %0.10f      %0.10f"%(h, Tb, abs(Ta-Tb)/Tb))
    
    print("Number of Functional Evaluations: %d"%n)
    print("")
    print("Part II -------->")
    print("     h/2             T(h/2)             L(T)")
    D= {}
    n = 0
    a = 0
    b = 0.95
    h = b-a
    A = [Q6b(a), Q6b(b)]
    D[a]= Q6b(a)
    D[b]= Q6b(b)
    Tb= CompTrapezoid(A, h)
    Ta= 0
    while 1:
        if Ta!=0:
            if (abs(Ta-Tb)/Tb)<E:
                break
        Ta= Tb
        h= h/2
        B= [0]
        while 1:
            B.append(B[len(B)-1]+h)
            if abs(B[len(B)-1]-0.95)<=E:
                break
        A= []
        for i in B:
            if i in D:
                A.append(D[i])
            else:
                D[i]= Q6b(i)
                A.append(Q6b(i))
                n+=1
        Tb= CompTrapezoid(A, h) 
        print("%0.10f      %0.10f      %0.10f"%(h, Tb, abs(Ta-Tb)/Tb))
    
    print("Number of Functional Evaluations: %d"%(n-8112))
    print("")
    M= [0.5, 0.8, 0.95]
    print("Part III -------->")
    for m in M:
        print("For m = %f"%m)
        print("     h/2             T(h/2)             L(T)")
        D= {}
        n= 0
        a= 0
        b= math.pi/2
        h= b-a
        A= [Q6c(a, m), Q6c(b, m)]
        Tb= CompTrapezoid(A, h)
        Ta= 0
        while 1:
            if Ta!=0:
                if (abs(Ta-Tb)/Tb)<E:
                    break
            Ta= Tb
            h= h/2
            B= [0]
            while 1:
                B.append(B[len(B)-1]+h)
                if abs(B[len(B)-1]-math.pi/2)<=E:
                    break
            A= []
            for i in B:
                if i in D:
                    A.append(D[i])
                else:
                    D[i]= Q6c(i, m)
                    A.append(Q6c(i, m))
                    n+=1
            Tb= CompTrapezoid(A, h) 
            print("%0.10f      %0.10f      %0.10f"%(h, Tb, abs(Ta-Tb)/Tb))
        
        if abs(m-0.8)<=E:
            n-=2
        if abs(m-0.95)<=E:
            n-=12
        print("Number of Functional Evaluations: %d"%n)
        print("")
    print("-------------------------------------------------------")
    print("")

def f7(x0):
    return x0*x0*x0+0.01*random.random()

def Q7():
    print("-------------------Q7-------------------")
    print("")
    a = 0
    b = 1
    A = [0] 
    B = []
    mul = (b-a)/1000.0
    E = 1.0/100000.0
    while 1:
        A.append(A[len(A)-1]+mul)
        if abs(A[len(A)-1]-1)<=E:
            break
    for i in A:
        B.append(f7(i))  
    CT = CompTrapezoid(B,mul)
    print("Approx Value of Integral using Composite Trapezoidal (with Inexact Function Evaluations): %f"%(CT))
    print("")
    err = (mul*mul*(b-a)*6)/12.0 + (b-a)*0.01*random.random()
    print("Error (with inexact function evaluations): %f"%(err))
    print("-------------------------------------------------------")
    print("")

Q1()
Q2()
Q3()
Q4()
Q5()
Q6()
Q7()