import sys

N = 7


def usage(prog_name):
    sys.exit('usage:' + prog_name + '<files name> <thread_count>')


def readfile():
    # file = sys.argv[1];
    file = '../numbers.txt'
    files_numbers = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for item in lines:
            files_numbers.append(int(item.split()[0]))
        return files_numbers


def count_sort_ser(numbers):
    numbers_len = len(numbers)
    temp = [0] * numbers_len
    for i in range(0, numbers_len):
        count = 0
        for j in range(0, numbers_len):
            if numbers[j] < numbers[i]:
                count += 1
            elif numbers[j] == numbers[i] & j < i:
                count += 1
        temp[count] = numbers[i]
    return temp


if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     Usage(sys.argv[0])

    numbers = readfile()
    final = count_sort_ser(numbers)
    print(final)
