import multiprocessing as mp
import sys
import time
import numpy as np


def read_matrix():
    file_name = 'output' + sys.argv[1] + '.txt'
    #file_name = 'output15000.txt'
    start_time = time.time()
    with open(file_name, 'r') as f:
        A = tuple([tuple(map(int, line.split())) for line in f])
    total_time = time.time() - start_time
    # with open('read_time.txt', 'a') as f:
    #     f.write('%s\t%.5f\n' % (sys.argv[1], total_time))
    return A


def CSR(A):
    AR, IA, JA = [], [], []
    start_time = time.time()
    IA.append(0)
    ne_counter = 0
    for row, line in enumerate(A):
        for col, value in enumerate(line):
            if value != 0:
                AR.append(value)
                ne_counter += 1
                JA.append(col)
        IA.append(ne_counter)
    total_time = time.time() - start_time
    # with open('execution_time.txt', 'a') as f:
    #     f.write('%s\t%.5f\n' %(sys.argv[1], total_time))
    print("Time", total_time)
    # print("AR = ", AR)
    # print("IA = ", IA)
    # print("JA = ", JA)
    return AR, IA, JA

#
# def CSR(A):
#     AR, IA, JA = [], [], []
#     start_time = time.time()
#     it = np.nditer(A, flags=['multi_index'])
#     IA.append(0)
#     ne_counter = 0
#     while not it.finished:
#         if it[0] != 0:
#             AR.append(it[0])
#             ne_counter += 1
#             JA.append(it.multi_index[1])
#
#     for x in range(array_len):
#         for y in range(array_len):
#             if A[x, y] != 0:
#                 AR.append(A[x, y])
#                 ne_counter += 1
#                 JA.append(y)
#         IA.append(ne_counter)
#     total_time = time.time() - start_time
#     # with open('execution_time.txt', 'a') as f:
#     #     f.write('%s\t%.5f\n' %(sys.argv[1], total_time))
#     print("Time", total_time)
#     # print("AR = ", AR)
#     # print("IA = ", IA)
#     # print("JA = ", JA)
#     return AR, IA, JA


def COO(A):
    AR, IA, JA = [], [], []
    for row, line in enumerate(A):
        for col, value in enumerate(line):
            if value != 0:
                AR.append(value)
                IA.append(row)
                JA.append(col)
    return AR, IA, JA


def CSC(A):
    AR, IA, JA = [], [], []
    IA.append(0)
    ne_counter = 0
    for col, line in enumerate(A.T):
        for row, value in enumerate(line):
            if value != 0:
                AR.append(value)
                ne_counter += 1
                IA.append(row)
        JA.append(ne_counter)

    print("AR = ", AR)
    print("IA = ", IA)
    print("JA = ", JA)
    return AR, IA, JA


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
    # AR1, IA1, JA1 = CSR(np.array(A))
    # AR2, IA2, JA2 = COO(A)
    # AR3, IA3, JA3 = CSC(A)
    # AR4, IA4, JA4 = create_vectors()

    # second_a = take_it_back(AR3, IA3, JA3)

