import multiprocessing as mp
import time

import count_sort.number_generator as numbers_generator
from count_sort.serial import CountSortSequential

''' Try with multiprocess'''


class CountSortParallel(CountSortSequential):
    def __init__(self, size_of_numbers):
        super().__init__(size_of_numbers)
        self.size_of_numbers = size_of_numbers
        self.total_process = 11
        self.processes = []

    def count_sort_process(self):
        print("")
        # nothing

    def __call__(self):
        for i in range(self.total_process):
            p = mp.Process(target=self.count_sort_process, args=(i,))
            self.processes.append(p)
            p.start()
        # for p in self.processes:



if __name__ == '__main__':
    # if len(sys.argv) != 5 or len(sys.argv) != 4:
    #     Usage(sys.argv[0])

    # call file generator
    numbers_generator.generate_numbers(900)
    # TODO: remove main
    numbers = CountSortParallel(900)
    start_time = time.time()
