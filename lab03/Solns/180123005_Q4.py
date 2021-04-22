#Scientific Computing Lab 3 Question 4
import numpy as np

def Delta(diff):
    temp = []
    for i in range(1, len(diff)):
        temp.append(diff[i]-diff[i-1])
    return temp

def forward_interpolation(nodes, val, x0):
    n = len(nodes)
    diff = val
    fac = 1
    h = nodes[1]-nodes[0]
    sol = 0
    for i in range(n):
        if i == 0:
            sol += diff[0]
        else:
            fac *= i
            prod = 1
            for j in range(i):
                prod *= (x0-nodes[j])
            prod /= h**i
            prod /= fac
            prod *= diff[0]
            sol += prod
        diff = Delta(diff)
    return sol

nodes = [0.1, 0.2, 0.3, 0.4, 0.5]
val = [9.9833, 4.9667, 3.2836, 2.4339, 1.9177]
x_val = []
for i in range(len(val)):
    x_val.append(val[i]*nodes[i])
x0 = 0.25
print('Directly using forward interpolation on g(x) provides', round(forward_interpolation(nodes, val, x0), 8), 'as the estimate of g(0.25)')
print('Using forward interpolation on x*g(x) provides', round(4*forward_interpolation(nodes, x_val, x0), 8), 'as the estimate of g(0.25)')
print('The actual value of g(0.25) is', round((np.sin(x0)/(x0**2)), 8))