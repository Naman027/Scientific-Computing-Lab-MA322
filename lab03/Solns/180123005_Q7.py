#Scientific Computing Lab 3 Question 7
def func_P(x):
    return (1 + 4*x + 4*x*(x-0.25) + 16*x*(x-0.25)*(x-0.5)/3)

print('The value of f(0.75) is', func_P(0.75))