#Scientific Computing Lab 3 Question 3
Delta4 = [24]*10
Delta3 = [6]
Delta2 = [0]
for i in range(1, 10):
    Delta3.append(Delta4[i-1]+Delta3[i-1])
for i in range(1, 10):
    Delta2.append(Delta3[i-1]+Delta2[i-1])
print('The value of Delta2(10) =', Delta2[9])