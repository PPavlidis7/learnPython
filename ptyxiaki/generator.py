import numpy as np
import scipy.sparse as sp

np.random.seed(2)
con = 'y'

while con == 'y':
    will = int(input('Do you want to give the bounds for the matrix? If yes press 0 else press 1\n'))
    if not will:
        lb = (input('Give the lower bounds\n'))
        ub = (input('Give the upper bounds\n'))
        Alu = [lb, ub]
        Al = Alu[0], Au = Alu[1]
        m, n = 10, 10
        A = np.round((int(Au) - int(Al) + 1) * sp.random(m, n, density=0.1))
        print(A)
        con = input('Do you want to continue with another matrix? y or n\n')
    else:
        lb = -1000
        ub = 1000
        Alu = [lb, ub]
        print(Alu[0])
        print(Alu[1])
        Al = Alu[0]
        Au = Alu[1]
        m, n = 10, 10
        A = np.round((Au - Al + 1) * sp.random(m, n, density=0.1))
        print(A)
        con = input('Do you want to continue with another matrix? y or n\n')
