import multiprocessing as mp
import sys
import time
import numpy as np


def read_matrix():
    file_name = 'output' + sys.argv[1] + '.txt'
    # file_name = 'matrix.txt'
    with open(file_name, 'r') as f:
        A = [list(map(int, line.split())) for line in f]
    return A


def create_vectors():
    A = read_matrix()
    AR, IA, JA = [], [], []
    start_time = time.time()
    IA.append(1)
    ne_counter = 1
    for row, line in enumerate(A):
        for col, value in enumerate(line):
            if value != 0:
                AR.append(value)
                ne_counter += 1
                JA.append(col)
        IA.append(ne_counter)
    total_time = time.time() - start_time
    with open('time.txt', 'a') as f:
        f.write('%s\t%.5f\n' %(sys.argv[1], total_time))
    # print("AR = ", AR)
    # print("IA = ", IA)
    # print("JA = ", JA)

    return AR, IA, JA, A


def create_vectors_paral(line, AR, priv_IA, priv_JA):
    ne_coutner = 0
    for index, value in enumerate(line):
        if value != 0:
            ne_coutner += 1
            AR.append(value)
            priv_JA.append(index)

    priv_IA.value = ne_coutner


def initialize_paral():
    print("----------------------------------")
    A = read_matrix()
    IA, processes = [], []
    IA.append(1)
    ne_counter = 1

    manager = mp.Manager()
    AR = manager.list()
    JA = manager.list()
    for row, line in enumerate(A):
        last_IA = IA[len(IA) - 1]
        priv_IA = mp.Value('i', 0)
        proccess = mp.Process(target=create_vectors_paral, args=(line, AR, priv_IA, JA))
        proccess.start()
        proccess.join()

        IA = IA + [priv_IA.value + last_IA]
    print("AR = ", AR)
    print("IA = ", IA)
    print("JA = ", JA)


def take_it_back(AR,IA,JA):
    a = np.zeros(shape=(100, 100), dtype=np.int)
    temp=[]
    rows=[]
    for index,value in enumerate(IA):
        if index == len(IA) -1:
            break
        size = IA[index+1] - value
        for inner in range(value,value+ size):
            temp.append(AR[inner-1])
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
    AR, IA, JA, A = create_vectors()
    # second_a = take_it_back(AR, IA, JA)

