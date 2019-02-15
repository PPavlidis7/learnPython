import sys
import time

import numpy as np

from count_sort import number_generator as numbers_generator


# import count_sort.number_generator as numbers_generator


class CountSortSequential:
    def __init__(self, size_of_numbers):
        #  file = '../numbers' + str(size_of_numbers) + '.txt'
        file = '../numbers3.txt'
        self.numbers = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for item in lines:
                self.numbers.append(int(item.split()[0]))
        self.sorted_numbers = np.ndarray(shape=(len(self.numbers)), dtype=int)

    def count_sort_ser(self):
        start_time = time.time()
        numbers_len = len(self.numbers)
        for i in range(0, numbers_len):
            count = 0
            for j in range(0, numbers_len):
                if self.numbers[j] < self.numbers[i]:
                    count += 1
                elif self.numbers[j] == self.numbers[i] & j < i:
                    count += 1
            self.sorted_numbers[count] = self.numbers[i]
        print("--- It took %s seconds to sort the numbers ---" % (time.time() - start_time))


def usage(program_name):
    sys.exit('usage:' + program_name + '<files name> < serial | parallel> <numbers> <threads>')


def readfile():
    # file = sys.argv[1];
    file = '../numbers.txt'
    files_numbers = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for item in lines:
            files_numbers.append(int(item.split()[0]))
        return files_numbers


if __name__ == '__main__':
    # if len(sys.argv) != 5 or len(sys.argv) != 4:
    #     Usage(sys.argv[0])

    numbers_generator(3)

    # TODO: take from sys.argv the size of numbers and
    # TODO: if asked file doesn't exist call generator , otherwise use the existing file
    # TODO: remove main
    numbers = CountSortSequential("size_of_numbers")
    numbers.count_sort_ser()
