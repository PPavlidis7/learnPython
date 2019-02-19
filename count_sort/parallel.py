import threading
import time

import count_sort.number_generator as numbers_generator
from count_sort.serial import CountSortSequential


# try with threading
class CountSortParallel(CountSortSequential):
    def __init__(self, size_of_numbers):
        super().__init__(size_of_numbers)
        self.size_of_numbers = size_of_numbers
        self.total_threads = 10
        self.threads = []
        self.main_thread = threading.currentThread()

    def count_sort_thread(self, threadID):
        start = int((self.size_of_numbers / self.total_threads)) * threadID
        steps = int(self.size_of_numbers / self.total_threads)
        print(threadID, "->", start, steps)
        if threadID == self.total_threads - 1:
            steps += (self.size_of_numbers % self.total_threads)

        numbers_len = len(self.numbers)
        for i in range(start, start + steps):
            count = 0
            for j in range(0, numbers_len):
                if self.numbers[j] < self.numbers[i]:
                    count += 1
                elif self.numbers[j] == self.numbers[i] and j < i:
                    count += 1
            self.sorted_numbers[count] = self.numbers[i]

    def __call__(self):
        for i in range(self.total_threads):
            t = threading.Thread(target=self.count_sort_thread, args=(i,))
            self.threads.append(t)
            t.start()

        for t in threading.enumerate():
            if t is self.main_thread:
                continue
            t.join()


if __name__ == '__main__':
    # if len(sys.argv) != 5 or len(sys.argv) != 4:
    #     Usage(sys.argv[0])

    # call file generator
    numbers_generator.generate_numbers(20000)

    # TODO: implement parallel sort
    # TODO: remove main
    numbers = CountSortParallel(20000)
    start_time = time.time()
    numbers()
    print("Sorting finished. Start result's validation...")
    if numbers.sort_validation():
        print("--- Sorting succeeded ---")
        print("--- It took %s seconds to sort the numbers ---" % (time.time() - start_time))
        # print(numbers.sorted_numbers)
    else:
        print("Sorting failed...")
