import time


def read_matrix(file):
    # line = ([tuple(map(int, data.split())) for data in file])
    while True:
        data = file.readline()
        if not data:
            break
        line = tuple(map(int, data.split()))
        yield line


def CSR():
    AR, IA, JA = [], [], []
    IA.append(0)
    ne_counter = 0
    file_name = 'output.txt'
    with open(file_name, 'r') as f:
        for line in read_matrix(f):
            for col, value in enumerate(line):
                if value != 0:
                    AR.append(value)
                    ne_counter += 1
                    JA.append(col)
            IA.append(ne_counter)

    print("AR = ", AR)
    print("IA = ", IA)
    print("JA = ", JA)
    return AR, IA, JA


def COO(A):
    AR, IA, JA = [], [], []
    for row, line in enumerate(A):
        for col, value in enumerate(line):
            if value != 0:
                AR.append(value)
                IA.append(row)
                JA.append(col)
    return AR, IA, JA


if __name__ == '__main__':
    start_time = time.time()
    AR1, IA1, JA1 = CSR()
    print("total time : ", time.time() - start_time)
    # AR2, IA2, JA2 = COO(A)
