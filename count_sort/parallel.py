import time

import count_sort.serial.CountSortSequential as CountSortSequential

import count_sort.number_generator as numbers_generator


class CountSortParallel(CountSortSequential):
    def count_sort_parallel(self):
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
        print("asd")
        print("--- It took %s seconds to sort the numbers ---" % (time.time() - start_time))


if __name__ == '__main__':
    # if len(sys.argv) != 5 or len(sys.argv) != 4:
    #     Usage(sys.argv[0])

    numbers_generator(3)

    # TODO: implement parallel sort
    # TODO: remove main
    numbers = CountSortParallel("size_of_numbers")
    numbers.count_sort_parallel()
    print(numbers.sorted_numbers)
