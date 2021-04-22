import math

class Helper:

    def forwardDiffTable(f,n):
        dF0 = []
       
        dF0.append(f[0])

        temp = [x for x in f]

        for i in range(n):
            diffs = []
            for j in range(1,len(temp)):
                diff = (temp[j] - temp[j-1])
                diffs.append(diff)

            dF0.append(diffs[0])
            temp = diffs

        return dF0


                    
    def forwardDifference(nodes, vals, x, n):
        h = nodes[1] - nodes[0]
        u = (x - nodes[0])/h

        Pnx = 0 
        
        dF0 = Helper.forwardDiffTable(vals,n)

        Pnx = 0

        for i in range(n+1):
            u_term = 1
            for j in range(i):
                u_term *= (u-j)
            u_term /= math.factorial(i)
            
            Pnx += u_term*dF0[i]

        return Pnx 

    def backwardDifference(nodes, vals, x, n):

        nodes.reverse()
        vals.reverse()

        return Helper.forwardDifference(nodes, vals, x, n)

class Q1:
    def solve():
        print("****** Q1 ******\n")

        print("Part-A\n")

        nodes = [0.25, 0.5]
        vals = [1.64872, 2.71828]
        x = 0.43
        n = 1
        Px = Helper.forwardDifference(nodes,vals,x,n)
        print("f(0.43) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [0.25, 0.5, 0.75]
        vals = [1.64872, 2.71828, 4.48169]
        x = 0.43
        n = 2
        Px = Helper.forwardDifference(nodes,vals,x,n)
        print("f(0.43) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [0, 0.25, 0.5, 0.75]
        vals = [1, 1.64872, 2.71828, 4.48169]
        x = 0.43
        n = 3
        Px = Helper.forwardDifference(nodes,vals,x,n)
        print("f(0.43) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        print("Part-B\n")

        nodes = [0.1, 0.2]
        vals = [-0.29004986, -0.56079734]
        x = 0.18
        n = 1
        Px = Helper.forwardDifference(nodes,vals,x,n)
        print("f(0.18) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [0.1, 0.2, 0.3]
        vals = [-0.29004986, -0.56079734, -0.81401972]
        x = 0.18
        n = 2
        Px = Helper.forwardDifference(nodes,vals,x,n)
        print("f(0.18) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [0.1, 0.2, 0.3, 0.4]
        vals = [-0.29004986, -0.56079734, -0.81401972, -1.0526302]
        x = 0.18
        n = 3
        Px = Helper.forwardDifference(nodes,vals,x,n)
        print("f(0.18) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

class Q2:
    def solve():
        print("\n****** Q2 ******\n")

        print("Part-A\n")

        nodes = [-0.5, -0.25]
        vals = [-0.02475000, 0.33493750]
        x = -1/3
        n = 1
        Px = Helper.backwardDifference(nodes,vals,x,n)
        print("f(-1/3) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [-0.5, -0.25, 0]
        vals = [-0.02475000, 0.33493750, 1.10100000]
        x = -1/3
        n = 2
        Px = Helper.backwardDifference(nodes,vals,x,n)
        print("f(-1/3) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [-0.75, -0.5, -0.25, 0]
        vals = [-0.07181250, -0.02475000, 0.33493750, 1.10100000]
        x = -1/3
        n = 3
        Px = Helper.backwardDifference(nodes,vals,x,n)
        print("f(-1/3) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        print("Part-B\n")

        nodes = [0.2, 0.3]
        vals = [-0.28398668, 0.00660095]
        x = 0.25
        n = 1
        Px = Helper.backwardDifference(nodes,vals,x,n)
        print("f(0.25) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [0.1, 0.2, 0.3]
        vals = [-0.62049958, -0.28398668, 0.00660095]
        x = 0.25
        n = 2
        Px = Helper.backwardDifference(nodes,vals,x,n)
        print("f(0.25) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

        nodes = [0.1, 0.2, 0.3, 0.4]
        vals = [-0.62049958, -0.28398668, 0.00660095, 0.24842440]
        x = 0.25
        n = 3
        Px = Helper.backwardDifference(nodes,vals,x,n)
        print("f(0.25) = %.10f using polynomial of degree %d"%(Px,n))
        print("Nodes taken = ", nodes)
        print("")

class Q3:
    def solve():
        print("\n****** Q3 ******\n")

        del4P0 = 24
        del3P0 = 6
        del2P0 = 0 

        del2P10 = 0 

        u = 10

        dF0 = [del2P0, del3P0, del4P0]

        for i in range(3):
            u_term = 1
            for j in range(i):
                u_term *= (u-j)
            u_term /= math.factorial(i)
            
            del2P10 += u_term*dF0[i]

        print("Value of Del2P(10) = %f"%del2P10)
        
class Q4:
    def solve():
        print("\n****** Q4 ******\n")

        x = [0.1, 0.2, 0.3, 0.4, 0.5]
        gx = [9.9833, 4.9667, 3.2836, 2.4339, 1.9177]
        z = 0.25

        actual = math.sin(z)/(z**2)

        print("Actual value of g(0.25) = %.10f\n"%actual)
        
        print("Part-A\n")

        Px = Helper.forwardDifference(x,gx,z,4)
        print("g(0.25) = %.10f by interpolating directly\n"%Px)

        print("Part-B\n")

        xgx = [X*Gx for X, Gx in zip(x,gx)]
        
        print("xg(x) is given as - \n")
        print("(x, xg(x))")
        for X, Xgx in zip(x, xgx):
            print("(%.1f, %f)"%(X, Xgx))

        xPx = Helper.forwardDifference(x,xgx,z,4)
        Px = xPx/z
        print("\ng(0.25) = %.10f by interpolating xg(x)\n"%Px)


class Q5:
    pass

class Q6:
    pass

class Q7:
    pass

def main():
    Q1.solve()
    Q2.solve()
    Q3.solve()
    Q4.solve()


if __name__ == '__main__':
    main()