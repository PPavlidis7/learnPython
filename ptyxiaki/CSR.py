def read_matrix():
    # A = []
    with open('matrix.txt', 'r') as f:
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
    print(AR)
    print(IA)
    print(JA)


if __name__ == '__main__':
    create_vectors()
