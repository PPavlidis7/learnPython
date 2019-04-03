import numpy as np
from scipy.sparse import random
from datetime import datetime


# while True:
#     will = int(input('Do you want to give the bounds for the matrix? If yes press 0 else press 1\n'))
#     if not will:
#         lb = input('Give the lower bounds\n')
#         ub = int(input('Give the upper bounds\n'))
#         Alu = [lb, ub]
#         Al = int(Alu[0])
#         Au = int(Alu[1])
#         m, n = 10, 10
#         spare_matrix = random(m, m, format='csr', density=0.25)
#         A = np.round((int(Au) - int(Al)) + int(Al)* spare_matrix.ceil())
#         print(A)
#         con = input('Do you want to continue with another matrix? y or n\n')
#         if con == 'y':
#             break
#     else:
#         lb = -1000
#         ub = 1000
#         Alu = [lb, ub]
#         print(Alu[0])
#         print(Alu[1])
#         Al = Alu[0]
#         Au = Alu[1]
#         m, n = 10, 10
#         A = np.round((Au - Al + 1) * sp.random(m, n, density=0.1))
#         print(A)
#         con = input('Do you want to continue with another matrix? y or n\n')


def get_user_input():
    will_bounds = input('Do you want to give the bounds for the matrix? Y/n \n')
    if will_bounds.lower() == 'y':
        while True:
            lb = input('Give the lower bounds\n')
            ub = input('Give the upper bounds\n')
            if not lb.isnumeric() or not ub.isnumeric():
                print("Wrong input. Bounds must be numeric. Please try again")
                continue
            else:
                lb = int(lb)
                ub = int(ub)
                break
    else:
        lb = -1000
        ub = 1000

    will_size = input('Do you want to give matrix\'s number of rows and columns? Y/n \n')
    if will_size.lower() == 'y':
        while True:
            m = input('Give the number of rows\n')
            n = input('Give the number of columns\n')
            if not m.isnumeric() or not n.isnumeric():
                print("Wrong input. Rows and columns must be numeric. Please try again")
                continue
            else:
                m = int(m)
                n = int(n)
                break
    else:
        m = 100
        n = 100

    will_density = input('Do you want to give matrix\'s density? Y/n \n')
    if will_density.lower() == 'y':
        while True:
            dens = input('Give the density\n')
            if not dens.isnumeric():
                print("Wrong input. Density must be numeric. Please try again")
                continue
            else:
                dens = int(dens)
                break
    else:
        dens = 0.1

    return lb, ub, m, n, dens


def generate_sparse_matrix(lb, ub, m, n, dens):
    # np.random.seed(2)
    np.random.seed(datetime.now())
    temp_matrix = random(m, n, format='csr', density=dens)
    generated_matrix = np.round((ub-lb + 1)*temp_matrix + lb*temp_matrix.ceil())
    return generated_matrix


def write_matrix_to_file(lb, ub, m, n, matrix):
    file_name = 'output' + lb + "_" + ub + "_" + m + "_" + n + ".txt"
    with open(file_name,'w') as f:
        for item in matrix:
            for index,inner in enumerate(item):
                if index == len(item)-1:
                    f.write("%s" % str(inner), )
                else:
                    f.write("%s\t" % str(inner), )
            f.write("\n")


def main():
    lb, ub, m, n, dens = get_user_input()
    generated_matrix = get_user_input(lb, ub, m, n, dens)
    print(generated_matrix.A)


if __name__ == '__main__':
    main()
