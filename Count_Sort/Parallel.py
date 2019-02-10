import time

import NumberGenerator
import Serial


class CountSortParallel(Serial.CountSortSequential):
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
        print("asd")
        print("--- It took %s seconds to sort the numbers ---" % (time.time() - start_time))


if __name__ == '__main__':
    # if len(sys.argv) != 5 or len(sys.argv) != 4:
    #     Usage(sys.argv[0])

    NumberGenerator.generate_numbers(3)

    # TODO: implement parallel sort
    # TODO: remove main
    numbers = CountSortParallel("size_of_numbers")
    numbers.count_sort_ser()
    print(numbers.sorted_numbers)
