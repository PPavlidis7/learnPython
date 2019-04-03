import multiprocessing as mp
import time
import numpy

import sys
sys.path.append('../')


import count_sort.number_generator as numbers_generator
from count_sort.serial import CountSortSequential

''' Try with multiprocess - SUCCESS'''


class CountSortParallel(CountSortSequential):
    def __init__(self, size_of_numbers):
        super().__init__(size_of_numbers)
        self.size_of_numbers = size_of_numbers
        self.total_process = 8
        self.processes = []
        self.sorted_numbers = mp.Array('i', size_of_numbers)

    def count_sort_process(self, process_id):
        start = int((self.size_of_numbers / self.total_process)) * process_id
        steps = int(self.size_of_numbers / self.total_process)

        if process_id == self.total_process - 1:
            steps += (self.size_of_numbers % self.total_process)

        print(process_id, "->", start, steps)
        st = time.time()
        numbers_len = len(self.numbers)
        for i in range(start, start + steps):
            count = 0
            for j in range(0, numbers_len):
                if self.numbers[j] < self.numbers[i]:
                    count += 1
                elif self.numbers[j] == self.numbers[i] and j < i:
                    count += 1

            # print(process_id, "--> did", count,  self.numbers[i] )
            self.sorted_numbers[count] = self.numbers[i]
        print(process_id, "-> did", (time.time() - st))

    def with_process(self):
        for i in range(self.total_process):
            p = mp.Process(target=self.count_sort_process, args=(i,))
            self.processes.append(p)
            p.start()

        for p in self.processes:
            p.join()

    def sort_validation(self):
        self.sorted_numbers = numpy.array(self.sorted_numbers)
        return super().sort_validation()


if __name__ == '__main__':
    # if len(sys.argv) != 5 or len(sys.argv) != 4:
    #     Usage(sys.argv[0])

    # call file generator
    numbers_generator.generate_numbers(900)
    numbers = CountSortParallel(900)
    start_time = time.time()
    numbers.with_process()
    print("Sorting finished. Start result's validation...")
    if numbers.sort_validation():
        print("--- Sorting succeeded ---")
        print("--- It took %s seconds to sort the numbers ---" % (time.time() - start_time))
    else:
        print("Sorting failed...")
