import time
import sys
import numpy as np


def read_matrix():
    file_name = 'output' + sys.argv[1] + '.txt'
    # file_name = 'output.txt'
    start_time = time.time()
    with open(file_name, 'r') as f:
        A = tuple([tuple(map(int, line.split())) for line in f])
    total_time = time.time() - start_time
    with open('read_time.txt', 'a') as f:
        f.write('comprese_v2 %s\t%.5f\n' % (sys.argv[1], total_time))
    return A


def CSR(A):
    AR, IA, JA = [], [], []
    ne_counter = 0
    start_time = time.time()
    IA.append(0)
    for row, line in enumerate(A):
        for col, value in enumerate(line):
            if value != 0:
                AR.append(value)
                ne_counter += 1
                JA.append(col)
        IA.append(ne_counter)
    total_time = time.time() - start_time
    with open('execution_time.txt', 'a') as f:
        f.write('CSR %s\t%.5f\n' % (sys.argv[1], total_time))
    return AR, IA, JA


def COO(A):
    AR, IA, JA = [], [], []
    start_time = time.time()
    for row, line in enumerate(A):
        for col, value in enumerate(line):
            if value != 0:
                AR.append(value)
                IA.append(row)
                JA.append(col)
    total_time = time.time() - start_time
    with open('execution_time.txt', 'a') as f:
        f.write('COO %s\t%.5f\n' % (sys.argv[1], total_time))
    return AR, IA, JA


def CSC(A):
    AR, IA, JA = [], [], []
    ne_counter = 0
    start_time = time.time()
    for col, line in enumerate(A.T):
        for row, value in enumerate(line):
            if value != 0:
                AR.append(value)
                ne_counter += 1
                IA.append(row)

                if len(JA) == 0:
                    JA.append(col)
        JA.append(ne_counter)
    total_time = time.time() - start_time
    with open('execution_time.txt', 'a') as f:
        f.write('CSC %s\t%.5f\n' % (sys.argv[1], total_time))
    return AR, IA, JA


def diagonal(A):
    LA, AD = [], []
    a_length = len(A)
    start_time = time.time()

    # main diagonal
    main_diagonal = get_main_diagonal(a_length)
    if main_diagonal != []:
        LA.append(0)
        AD = np.array((main_diagonal))

    # upper diagonal
    for index in range(a_length - 1, 0, -1):
        upper_inner_diagonal = get_upper_inner_diagonal(index, a_length)
        if upper_inner_diagonal:
            LA.append(index)
            if len(AD) == 0:
                AD = np.array((upper_inner_diagonal))
            else:
                AD = np.column_stack((AD, (upper_inner_diagonal)))

    # lower diagonal
    for index in range(a_length - 1, 0, -1):
        lower_inner_diagonal = get_lower_inner_diagonal(index, a_length)
        if lower_inner_diagonal:
            LA.append(-1 * index)
            if len(AD) == 0:
                AD = np.array((lower_inner_diagonal))
            else:
                AD = np.column_stack((AD, (lower_inner_diagonal)))

    print(AD)
    print(LA)


def get_upper_inner_diagonal(col, a_length):
    found_nv = False
    temp_diagonal = []
    mine_row_index = 0
    for index in range(col, a_length):  # 0,5 1,6
        value = A[mine_row_index][index]
        if value != 0:
            found_nv = True
        temp_diagonal.append(value)
        mine_row_index += 1
        if mine_row_index == a_length:
            break

    if found_nv:
        left_zeros = a_length - len(temp_diagonal)
        for index in range(0, left_zeros):
            temp_diagonal.append(0)
        return temp_diagonal
    else:
        return []


def get_lower_inner_diagonal(row, a_length):
    found_nv = False
    temp_diagonal = []
    mine_col_index = 0
    for index in range(row, a_length):  # 6,1 5,2
        value = A[index][mine_col_index]
        if value != 0:
            found_nv = True
        temp_diagonal.append(value)
        mine_col_index += 1
        if mine_col_index == a_length:
            break

    if found_nv:
        left_zeros = a_length - len(temp_diagonal)
        for index in range(0, left_zeros):
            temp_diagonal.insert(0, 0)
        return temp_diagonal
    else:
        return []


def get_main_diagonal(a_length):
    main_diagonal = []
    found_nv = False
    for index in range(a_length):
        value = A[index][index]
        if value != 0:
            found_nv = True
        main_diagonal.append(value)
    if found_nv:
        return main_diagonal
    else:
        return []


def take_it_back(AR, IA, JA):
    a = np.zeros(shape=(10,10), dtype=np.int)
    temp=[]
    rows=[]
    for index,value in enumerate(IA):
        if index == len(IA) -1:
            break
        size = IA[index+1] - value
        for inner in range(value,value+ size):
            temp.append(AR[inner])
        rows.append(temp)
        temp = []

    index_counter = 0
    for index,inner_1 in enumerate(rows):
        for inner_2 in inner_1:
            a[index][JA[index_counter]] = inner_2
            index_counter +=1
    print("------------------------------------------------------")
    print(a)
    return a


if __name__ == '__main__':
    A = read_matrix()
    AR1, IA1, JA1 = CSR(A)
    AR1, IA1, JA1 = CSC(np.array(A))
    AR2, IA2, JA2 = COO(A)
    # AR4, IA4, JA4 = create_vectors()

    # second_a = take_it_back(AR3, IA3, JA3)
