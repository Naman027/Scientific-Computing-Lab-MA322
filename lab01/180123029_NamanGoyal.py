import math

def Ques1():
    a = 2
    x0 = 5
    x1 = x0
    n = 0
    e = 1.0/100000
    f = []
    while 1:
        f.append(x0)
        n = n+1
        x = ((x0*1.00)*((x0*x0*1.00)+(3*a*1.00)))/((3*x0*x0*1.00)+a)
        if abs(x-x0)<=e:
            f.append(x)
            break
        else:
            x0 = x
    print("No. of iterations = %d" %n)
	
    p= []
    lenth = len(f) 
    for i in range(1, lenth-2):
        p.append(math.log((x-f[i+1])/(x-f[i]))/math.log((x-f[i])/(x-f[i-1])))   
    print("Order of Convergence(p) = 2, Calculated Value = %f"%(p[0]))

def Ques2():
    n = 1000000
    a = 1.6
    b = 3.0
    h = (b-a)/n
    p = []
    x0 = 1.6
    for i in range(0, n+1):
        x = x0+i*h
        ans = math.tan(math.pi - x) - x
        p.append([abs(ans),x])
    p.sort()    
    print("Value of x = %f Value of f(x) = %f"%(p[0][1],p[0][0]))

def sgn(a):
    if(a>0): return 1
    elif(a==0): return 0
    return -1

def f3(x0):
    return x0/2.0-math.sin(x0)

def Ques3():
    a = math.pi/2.00
    b = math.pi*1.00
    e = 1.0/10000000
    n = (math.log(b-a)-math.log(e))/math.log(2)
    n = math.ceil(n)
    for i in range(0, int(n)):
        c= (a+b)/2.0
        sgna = sgn(f3(a))
        sgnb = sgn(f3(b))
        sgnc = sgn(f3(c))
        if(sgna*sgnc < 0):
            b = c
        else: 
            a = c

    print("Approximate root using Bisection method = %0.15f" %c)

    b = math.pi*1.00
    while 1:
        valb = f3(b)
        f_dash_b = 1/2.0 - math.cos(b)
        c = b - (valb/f_dash_b)
        h = valb/f_dash_b
        if(abs(h)<e):
            break
        b = c
    print("Approximate root using Newton method = %0.7f" %c)

def f4(x0):
    return x0/2.0 + math.sin(x0)

def Ques4():
    a = math.pi/2.00
    b = math.pi*1.00
    e = 1.0/10000000
    n = (math.log(b-a)-math.log(e))/math.log(2)
    n = math.ceil(n)
    for i in range(0, int(n)):
        c= (a+b)/2.0
        sgna = sgn(f3(a))
        sgnb = sgn(f3(b))
        sgnc = sgn(f3(c))
        if(sgna*sgnc < 0):
            b = c
        else: 
            a = c
    print("Approximate root using Bisection method = %0.15f" %c)

    x0 = math.pi*1.00
    f = []
    while 1:
        x = f4(x0)
        f.append(x)
        if(abs(x-x0)<=e):
            break
        x0= x
    print("Approximate root using Fix Point method = %0.15f" %x)
    lenth = len(f) 
    for i in range(1, lenth-2):
        if(abs(f[i+1]-f[i])<0.0001):
            print("Order of Convergence(p) = 1, Calculated Value = %f"%(math.log((x-f[i+1])/(x-f[i]))/math.log((x-f[i])/(x-f[i-1]))))
            break

def f5(x0):
    return (math.exp(-1*x0)*(x0*x0+5*x0+2))+1

def Ques5():
    x0 = -1
    x1 = 1
    e = 1.0/100000
    while 1:
        f_at_x0 = f5(x0)
        f_at_x1 = f5(x1)
        x = x1 - (f_at_x1 * ((x1-x0)/(f_at_x1-f_at_x0)))
        x0 = x1
        x1 = x
        if(abs(x1-x0)<=e):
            break
    print("Approximate root using Secant method = %0.15f" %x1)

def f6(x0):
    return (math.exp(-1*x0)*(x0*x0+5*x0+2))+1

def Ques6():
    a= -1.00
    b= 1.00
    e= 1.0/10000000
    n = (math.log(b-a)-math.log(e*100.00))/math.log(2)
    n = math.ceil(n)
    for i in range(0, int(n)):
        c= (a+b)/2.0
        vala= f6(a)
        vala = sgn(vala)
        valb= f6(b)
        valb = sgn(valb)
        valc= f6(c)
        valc = sgn(valc)
        if(vala*valc < 0):
            b= c
        else: 
            a= c
    print("Approximate root using Bisection method = %0.15f"%c)
    x = -0.50
    x0 = -1
    f= []
    while 1:
        f_at_x= f6(x)
        f_at_x0= f6(x0)
        f.append(x)
        e = 1.0/100000
        x1= (x0*f_at_x-x*f_at_x0)/(f_at_x-f_at_x0)
        if(abs(x1-x)<e):
            break
        x = x1
    print("Approximate root using Iterative scheme = %0.15f"%x)
    lenth = len(f) 
    for i in range(1, lenth-1):
        if(abs(f[i+1]-f[i])<0.0001):
            print("Order of Convergence(p) = 1, Calculated Value = %0.15f"%(math.log((x-f[i+1])/(x-f[i]))/math.log((x-f[i])/(x-f[i-1]))))
            break    

def f7(x0):
    return x0/2.0 - math.sin(x0);

def Ques7(): 
    a = math.pi/2.00
    b = math.pi*1.00
    e = 1.0/10000000
    n = (math.log(b-a)-math.log(0.00001))/math.log(2)
    n = math.ceil(n)
    for i in range(0, int(n)):
        c = (a+b)/2.0
        vala = f7(a)
        vala = sgn(vala)
        valb = f7(b)
        valb = sgn(valb)
        valc = f7(c)
        valc = sgn(valc)
        if(vala*valc < 0):
            b = c
        else: 
            a = c
    print("Approximate root using biesction method = %0.15f"%c)
    x = 1.90
    x0 = math.pi/2.00
    f = []
    while 1:
        f_at_x = f7(x)
        f_at_x0 = f7(x0)
        f.append(x)
        x1 = (x0*f_at_x-x*f_at_x0)/(f_at_x-f_at_x0)
        if(abs(x1-x)<e):
            break
        x = x1
    print("Approximate root using iterative scheme = %0.15f"%x)
    lenth = len(f) 
    for i in range(1, lenth-2):
        if(abs(f[i+1]-f[i])<0.0001):
            print("Order of Convergence(p) = 1, Calculated Value = %f"%(math.log(abs((x-f[i+1])/(x-f[i])))/math.log(abs((x-f[i])/(x-f[i-1])))))
            break  

def f8(x0):
    return (math.exp(-1*x0)*(x0*x0+5*x0+2))+1

def Ques8():
    a = -1.00
    b = 1.00
    e = 1.0/10000000
    n = (math.log(b-a)-math.log(0.00001))/math.log(2)
    n = math.ceil(n)
    for i in range(0, int(n)):
        c = (a+b)/2.0
        vala = f8(a)
        vala = sgn(vala)
        valb = f8(b)
        valb = sgn(valb)
        valc = f8(c)
        valc = sgn(valc)
        if(vala*valc < 0):
            b= c
        else: 
            a= c
    print("Approximate root using biesction method = %0.15f"%c)
    x0 = -0.75
    f = []
    while 1:
        f_at_x0= f8(x0)
        x1= x0-f_at_x0
        f_at_x1= f8(x1)
        x= x0 - (f_at_x0*f_at_x0)/(f_at_x0-f_at_x1)
        f.append(x0)
        if(abs(x-x0)<=e):
            break
        x0= x   
    print("Approximate root using Iterative scheme = %0.15f"%x)
    lenth = len(f)
    for i in range(1, lenth-2):
        if(abs(f[i+1]-f[i])<0.0001 or i==len(f)-3):
            print("Order of Convergence(p) = 2, Calculated Value = %f"%(math.log(abs((x-f[i+1])/(x-f[i])))/math.log(abs((x-f[i])/(x-f[i-1])))))
            break  

print("Solution 1 --->")
Ques1()
print("")
print("Solution 2 --->")
Ques2()
print("")
print("Solution 3 --->")
Ques3()
print("")
print("Solution 4 --->")
Ques4()
print("")
print("Solution 5 --->")
Ques5()
print("")
print("Solution 6 --->")
Ques6()
print("")
print("Solution 7 --->")
Ques7()
print("")
print("Solution 8 --->")
Ques8()








