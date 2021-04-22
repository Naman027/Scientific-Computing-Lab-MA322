#Scientific Computing Lab 3 Question 2
def Delta(diff):
    temp = []
    for i in range(1, len(diff)):
        temp.append(diff[i]-diff[i-1])
    return temp

def backward_interpolation(nodes, val, x0):
    n = len(nodes)
    diff = val
    fac = 1
    h = nodes[1]-nodes[0]
    sol = 0
    for i in range(n):
        if i == 0:
            sol += diff[n-1]
        else:
            fac *= i
            prod = 1
            for j in range(i):
                prod *= (x0-nodes[n-1-j])
            prod /= h**i
            prod /= fac
            prod *= diff[len(diff)-1]
            sol += prod
        diff = Delta(diff)
    return sol

nodes = [-0.75, -0.5, -0.25, 0]
val = [-0.0718125, -0.02475, 0.3349375, 1.101]
x0 = -1/3
print('Nodes\t Value of function')
for i in range(len(nodes)):
    print(nodes[i], '\t', val[i])
print('Using Backward Interpolation For Degree 1:')
print('Estimate for x =', round(x0, 4), 'rounded to 6 decimal places is', round(backward_interpolation(nodes[1:3], val[1:3], x0), 6))
print('Using Backward Interpolation For Degree 2:')
print('Estimate for x =', round(x0, 4), 'rounded to 6 decimal places is', round(backward_interpolation(nodes[:3], val[:3], x0), 6))
print('Using Backward Interpolation For Degree 3:')
print('Estimate for x =', round(x0, 4), 'rounded to 6 decimal places is', round(backward_interpolation(nodes, val, x0), 6))
print()

nodes = [0.1, 0.2, 0.3, 0.4]
val = [-0.62049958, -0.28398668, 0.00660095, 0.2484244]
x0 = 0.25
print('Nodes\t Value of function')
for i in range(len(nodes)):
    print(nodes[i], '\t', val[i])
print('Using Backward Interpolation For Degree 1:')
print('Estimate for x =', round(x0, 4), 'rounded to 6 decimal places is', round(backward_interpolation(nodes[1:3], val[1:3], x0), 6))
print('Using Backward Interpolation For Degree 2:')
print('Estimate for x =', round(x0, 4), 'rounded to 6 decimal places is', round(backward_interpolation(nodes[:3], val[:3], x0), 6))
print('Using Backward Interpolation For Degree 3:')
print('Estimate for x =', round(x0, 4), 'rounded to 6 decimal places is', round(backward_interpolation(nodes, val, x0), 6))