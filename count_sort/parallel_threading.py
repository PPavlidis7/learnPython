import threading
import time
import sys
sys.path.append('../')
import count_sort.number_generator as numbers_generator
from count_sort.serial import CountSortSequential


# try with threading - SUCCESS
class CountSortParallel(CountSortSequential):
    def __init__(self, size_of_numbers):
        super().__init__(size_of_numbers)
        self.size_of_numbers = size_of_numbers
        self.total_threads = 11
        self.threads = []
        self.main_thread = threading.currentThread()

    def count_sort_thread(self, thread_id):
        start = int((self.size_of_numbers / self.total_threads)) * thread_id
        steps = int(self.size_of_numbers / self.total_threads)

        if thread_id == self.total_threads - 1:
            steps += (self.size_of_numbers % self.total_threads)

        print(thread_id, "->", start, steps)
        # time.sleep(random.uniform(0, 4))
        st = time.time()
        numbers_len = len(self.numbers)
        for i in range(start, start + steps):
            count = 0
            for j in range(0, numbers_len):
                if self.numbers[j] < self.numbers[i]:
                    count += 1
                elif self.numbers[j] == self.numbers[i] and j < i:
                    count += 1
            # print(threadID, "-", i, "-> did", (time.time() - st))
            self.sorted_numbers[count] = self.numbers[i]
        print(thread_id, "-> did", (time.time() - st))

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
    numbers_generator.generate_numbers(900)

    numbers = CountSortParallel(900)
    start_time = time.time()
    numbers()
    print("Sorting finished. Start result's validation...")
    if numbers.sort_validation():
        print("--- Sorting succeeded ---")
        print("--- It took %s seconds to sort the numbers ---" % (time.time() - start_time))
        # print(numbers.sorted_numbers)
    else:
        print("Sorting failed...")
