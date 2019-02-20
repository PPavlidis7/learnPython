import sys
import time

import numpy as np

from count_sort import number_generator as numbers_generator


class CountSortSequential:
    def __init__(self, size_of_numbers):
        file = '../numbers' + str(size_of_numbers) + '.txt'
        # file = '../numbers100000.txt'
        self.numbers = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for item in lines:
                self.numbers.append(int(item.split()[0]))
        self.sorted_numbers = np.zeros(shape=(len(self.numbers)), dtype=np.int64)

    def count_sort_ser(self):
        numbers_len = len(self.numbers)
        for i in range(0, numbers_len):
            count = 0
            for j in range(0, numbers_len):
                if self.numbers[j] < self.numbers[i]:
                    count += 1
                elif self.numbers[j] == self.numbers[i] and j < i:
                    count += 1
            self.sorted_numbers[count] = self.numbers[i]
        print("Sorting finished. Start result's validation...")

    def sort_validation(self):
        for index, number in enumerate(self.sorted_numbers):
            if number == 0:
                break
                return False
            elif index + 1 < len(self.sorted_numbers) and \
                    self.sorted_numbers[index] < self.sorted_numbers[index + 1]:
                continue
            else:
                break
                return False
        return True


def usage(program_name):
    sys.exit('usage:' + program_name + '<files name> < serial | parallel> <numbers> <threads>')


if __name__ == '__main__':
    # if len(sys.argv) != 5 or len(sys.argv) != 4:
    #     Usage(sys.argv[0])

    numbers_generator.generate_numbers(900)

    # TODO: take from sys.argv the size of numbers and
    # TODO: if asked file doesn't exist call generator , otherwise use the existing file
    # TODO: remove main
    numbers = CountSortSequential(900)
    print("Start sorting...")
    start_time = time.time()
    numbers.count_sort_ser()
    if numbers.sort_validation():
        print("--- Sorting succeeded ---")
        print("--- It took %s seconds to sort the numbers ---" % (time.time() - start_time))
        # print(self.sorted_numbers)
    else:
        print("Sorting failed...")
