import  numpy as np


def read_matrix():
    # A = []
    with open('output.txt', 'r') as f:
        A = [list(map(int, line.split())) for line in f]
    return A


def create_vectors():
    A = read_matrix()
    AR, IA, JA = [], [], []
    IA.append(1)
    ne_counter = 1
    for row, line in enumerate(A):
        for col, value in enumerate(line):
            if value != 0:
                AR.append(value)
                ne_counter += 1
                JA.append(col)
        IA.append(ne_counter)
    print("AR = ", AR)
    print("IA = ", IA)
    print("JA = ", JA)

    return AR,IA,JA


def take_it_back(AR,IA,JA):
    a = np.zeros(shape=(10,10), dtype=np.int)
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
    print(a)


if __name__ == '__main__':
    AR,IA,JA=create_vectors()
    take_it_back(AR,IA,JA)