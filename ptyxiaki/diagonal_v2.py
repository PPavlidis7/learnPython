import time


def read_matrix():
    # file_name = 'output' + sys.argv[1] + '.txt'
    file_name = 'output.txt'
    start_time = time.time()
    with open(file_name, 'r') as f:
        A = tuple([tuple(map(int, line.split())) for line in f])
    total_time = time.time() - start_time
    # with open('read_time.txt', 'a') as f:
    #     f.write('%s\t%.5f\n' % (sys.argv[1], total_time))
    return A


def diagonal():
    LA, AD = [], [[]]
    a_length = len(A)
    start_time = time.time()

    # main diagonal
    main_diagonal = get_main_diagonal(a_length)

    # upper diagonal
    upper_diagonals = []
    for index in range(1, a_length):
        AD.append([])  # start initializing AD array
        upper_inner_diagonal = get_upper_inner_diagonal(index, a_length)
        if upper_inner_diagonal:
            LA.append(index)
            upper_diagonals.append(upper_inner_diagonal)

    # lower diagonal
    lower_diagonals = []
    for index in range(a_length - 1, 0, -1):
        lower_inner_diagonal = get_lower_inner_diagonal(index, a_length)
        if lower_inner_diagonal:
            LA.append(-1 * index)
            lower_diagonals.append(lower_inner_diagonal)

    # create AD array
    AD = tuple(AD)  # tuple or list or numpy
    if main_diagonal:
        create_ad_with_main_diagonal(AD, main_diagonal, upper_diagonals, lower_diagonals, a_length)
    else:
        create_ad_without_main_diagonal(AD, upper_diagonals, lower_diagonals, a_length)

    print("total time : ", time.time() - start_time)
    # print(AD)
    print(LA)


def create_ad_with_main_diagonal(AD, main_diagonal, upper_diagonals, lower_diagonals, a_length):
    row = 0
    uppers_number = len(upper_diagonals)
    lowers_number = len(lower_diagonals)

    while row < a_length:
        AD[row].append(main_diagonal[row])
        for index in range(uppers_number):
            AD[row].append(upper_diagonals[index][row])

        for index in range(lowers_number):
            AD[row].append(lower_diagonals[index][row])

        row += 1
    return AD


def create_ad_without_main_diagonal(AD, upper_diagonals, lower_diagonals, a_length):
    row = 0
    uppers_number = len(upper_diagonals)
    lowers_number = len(lower_diagonals)

    while row < a_length:
        for index in range(uppers_number):
            AD[row].append(upper_diagonals[index][row])

        for index in range(lowers_number):
            AD[row].append(lower_diagonals[index][row])

        row += 1
    return AD


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


A = read_matrix()

if __name__ == '__main__':
    diagonal()
