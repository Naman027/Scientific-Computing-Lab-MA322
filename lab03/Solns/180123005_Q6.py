#Scientific Computing Lab 3 Question 6
def Delta(diff):
    temp = []
    for i in range(1, len(diff)):
        temp.append(diff[i]-diff[i-1])
    return temp

def func_Q(nodes, P_val):
    Q_val = []
    for i in range(len(nodes)):
        Q_val.append(P_val[i] - (nodes[i]**4)/24)
    return Q_val

nodes = [0, 1, 2, 3]
P_val = [4, 9, 15, 18]
Q_val = func_Q(nodes, P_val)
D3 = Delta(Delta(Delta(Q_val)))
print(str(int(D3[0]*2))+'/12')