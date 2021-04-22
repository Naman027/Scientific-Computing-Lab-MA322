#Scientific Computing Lab 3 Question 1
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

nodes = [0, 0.25, 0.5, 0.75]
val = [1, 1.64872, 2.71828, 4.48169]
x0 = 0.43
print('Nodes\t Value of function')
for i in range(len(nodes)):
    print(nodes[i], '\t', val[i])
print('Using Forward Interpolation For Degree 1:')
print('Estimate for x =', x0, 'rounded to 6 decimal places is', round(forward_interpolation(nodes[1:3], val[1:3], x0), 6))
print('Using Forward Interpolation For Degree 2:')
print('Estimate for x =', x0, 'rounded to 6 decimal places is', round(forward_interpolation(nodes[1:], val[1:], x0), 6))
print('Using Forward Interpolation For Degree 3:')
print('Estimate for x =', x0, 'rounded to 6 decimal places is', round(forward_interpolation(nodes, val, x0), 6))
print()


nodes = [0.1, 0.2, 0.3, 0.4]
val = [-0.29004986, -0.56079734, -0.81401972, -1.0526302]
x0 = 0.18
print('Nodes\t Value of function')
for i in range(len(nodes)):
    print(nodes[i], '\t', val[i])
print('Using Forward Interpolation For Degree 1:')
print('Estimate for x =', x0, 'rounded to 6 decimal places is', round(forward_interpolation(nodes[:2], val[:2], x0), 6))
print('Using Forward Interpolation For Degree 2:')
print('Estimate for x =', x0, 'rounded to 6 decimal places is', round(forward_interpolation(nodes[:3], val[:3], x0), 6))
print('Using Forward Interpolation For Degree 3:')
print('Estimate for x =', x0, 'rounded to 6 decimal places is', round(forward_interpolation(nodes, val, x0), 6))