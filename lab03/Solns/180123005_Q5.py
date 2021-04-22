#Scientific Computing Lab 3 Question 5
def func_P(x):
    return (3 - 2*(x+1) + (x+1)*x*(x-1))

def func_Q(x):
    return (-1 + 4*(x+2) - 3*(x+2)*(x+1) + (x+2)*(x+1)*x)

nodes = [-2, -1, 0, 1, 2]
val = [-1, 3, 1, -1, 3]

for i in range(len(nodes)):
    if func_P(nodes[i]) != val[i]:
        print('Polynomial P does NOT interpolate the given data.')
        break
    if func_Q(nodes[i]) != val[i]:
        print('Polynomial Q does NOT interpolate the given data.')
        break
    if i == len(nodes)-1:
        print('Both polynoials, P and Q, succesfully interpolate the given data.')